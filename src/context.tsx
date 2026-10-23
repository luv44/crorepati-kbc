import { createContext, useContext, useEffect, useRef, useState } from 'react';
import type { ReactNode } from 'react';
import type { Catalog, CurrentNewsFeed, ExamDefinition, FactCard, LearningState, Pack, Question, Source, Subject } from './types';
import { initialState, eligible, focusedPracticeQuestion } from './domain';
import { downloadedPacks, loadState, saveState } from './storage';

interface Store {
  catalog: Catalog;
  exams: ExamDefinition[];
  selectedExam: ExamDefinition;
  examSubjects: Subject[];
  state: LearningState;
  questions: Question[];
  examQuestions: Question[];
  facts: FactCard[];
  sources: Source[];
  currentNews: CurrentNewsFeed;
  update: (f: (s: LearningState) => LearningState) => void;
  refreshPacks: () => Promise<void>;
  toast: (text: string) => void;
}

const Context = createContext<Store | null>(null);
export function useStore() { const store = useContext(Context); if (!store) throw new Error('Store unavailable'); return store; }

const legacyExamIds: Record<string, string> = {
  'General knowledge': 'general-knowledge',
  UPSC: 'upsc-cse',
  SSC: 'ssc',
  Banking: 'banking',
  Railways: 'railways',
  'State exams': 'state-exams',
  'Just curious': 'just-curious',
};

function migrateExam(state: LearningState, exams: ExamDefinition[]) {
  const candidate = legacyExamIds[state.profile.exam] || state.profile.exam;
  const exam = exams.find(item => item.id === candidate) || exams.find(item => item.id === 'general-knowledge') || exams[0];
  return exam && state.profile.exam !== exam.id ? { ...state, profile: { ...state.profile, exam: exam.id } } : state;
}

export function Provider({ children }: { children: ReactNode }) {
  const [catalog, setCatalog] = useState<Catalog>();
  const [exams, setExams] = useState<ExamDefinition[]>([]);
  const [currentNews, setCurrentNews] = useState<CurrentNewsFeed>();
  const [state, setState] = useState(initialState);
  const [packs, setPacks] = useState<Pack[]>([]);
  const starter = useRef<Pack | null>(null);
  const [error, setError] = useState('');
  const [ready, setReady] = useState(false);
  const [message, setMessage] = useState('');
  const [storageAvailable, setStorageAvailable] = useState(true);
  const writes = useRef(Promise.resolve());

  const refreshPacks = async () => {
    try { setPacks([...(starter.current ? [starter.current] : []), ...await downloadedPacks()]); }
    catch (e) { setStorageAvailable(false); setError(`Browser storage unavailable: ${String(e)}. Downloaded packs and progress cannot be saved in this session.`); }
  };

  useEffect(() => {
    Promise.allSettled([
      fetch('/data/catalog.json').then(r => { if (!r.ok) throw new Error('Cannot load the catalogue. Connect once to download the learning shell.'); return r.json(); }),
      fetch('/data/starter.json').then(r => { if (!r.ok) throw new Error('Starter content unavailable.'); return r.json(); }),
      fetch('/data/exams.json').then(r => { if (!r.ok) throw new Error('Exam mappings unavailable.'); return r.json(); }),
      fetch('/data/current-news.json').then(r => { if (!r.ok) throw new Error('Current Live data unavailable.'); return r.json(); }),
      loadState(),
      downloadedPacks(),
    ]).then(([catalogResult, starterResult, examsResult, newsResult, stateResult, packsResult]) => {
      const required = [catalogResult, starterResult, examsResult, newsResult];
      const failed = required.find(result => result.status === 'rejected') as PromiseRejectedResult | undefined;
      if (failed) {
        setError(`Learning content could not load: ${String(failed.reason)}. Check the terminal and reload.`);
        return;
      }
      const loadedExams = (examsResult as PromiseFulfilledResult<{ exams: ExamDefinition[] }>).value.exams;
      const loadedStarter = (starterResult as PromiseFulfilledResult<Pack>).value;
      setCatalog((catalogResult as PromiseFulfilledResult<Catalog>).value);
      starter.current = loadedStarter;
      setExams(loadedExams);
      setCurrentNews((newsResult as PromiseFulfilledResult<CurrentNewsFeed>).value);
      setPacks([loadedStarter, ...(packsResult.status === 'fulfilled' ? packsResult.value : [])]);
      if (stateResult.status === 'fulfilled') setState(migrateExam(stateResult.value, loadedExams));
      if (stateResult.status === 'rejected' || packsResult.status === 'rejected') {
        setStorageAvailable(false);
        setError(`Browser storage unavailable (${String(stateResult.status === 'rejected' ? stateResult.reason : (packsResult as PromiseRejectedResult).reason)}). The app is open for viewing, but progress will not be saved. Existing stored data has not been deleted.`);
      }
      setReady(true);
    }).catch(e => setError(`Startup failed: ${String(e)}`));
  }, []);

  useEffect(() => {
    if (!ready || !storageAvailable) return;
    writes.current = writes.current.then(() => saveState(state)).catch(e => {
      setStorageAvailable(false);
      setError(`Progress could not be saved: ${String(e)}. Existing stored data has not been deleted.`);
    });
  }, [state, ready, storageAvailable]);

  useEffect(() => { if (!message) return; const id = setTimeout(() => setMessage(''), 5000); return () => clearTimeout(id); }, [message]);

  if (!ready || !catalog || !currentNews || !exams.length) return <main className="loading"><div className="brand-mark">c<span>r</span></div><h1>Crorepati Revision</h1><p role={error ? 'alert' : 'status'}>{error || 'Opening your learning space…'}</p>{error && <button onClick={() => location.reload()}>Try again</button>}</main>;

  const unique = <T extends { id: string },>(items: T[]) => [...new Map(items.map(x => [x.id, x])).values()];
  const questions = unique(packs.flatMap(p => p.questions)).filter(q => eligible(q));
  const focusedQuestions = questions.filter(question => focusedPracticeQuestion(question));
  const focusedCountByTopic = new Map<string, number>();
  focusedQuestions.forEach(question => focusedCountByTopic.set(question.topicId, (focusedCountByTopic.get(question.topicId) || 0) + 1));
  const selectedExam = exams.find(exam => exam.id === state.profile.exam) || exams.find(exam => exam.id === 'general-knowledge') || exams[0];
  const mappedSubjectIds = new Set(selectedExam.subjectIds);
  const examSubjects = catalog.subjects.filter(subject => mappedSubjectIds.has(subject.id)).map(subject => {
    const chapters = subject.chapters.map(chapter => ({ ...chapter, topics: chapter.topics.map(topic => ({ ...topic, questionCount: focusedCountByTopic.get(topic.id) || 0 })) }));
    return { ...subject, chapters, questionCount: chapters.reduce((total, chapter) => total + chapter.topics.reduce((count, topic) => count + topic.questionCount, 0), 0) };
  });
  const value: Store = {
    catalog,
    exams,
    selectedExam,
    examSubjects,
    state,
    questions,
    examQuestions: focusedQuestions.filter(question => mappedSubjectIds.has(question.subjectId)),
    facts: unique(packs.flatMap(p => p.factCards)),
    sources: unique(packs.flatMap(p => p.sources)),
    currentNews,
    update: setState,
    refreshPacks,
    toast: setMessage,
  };
  return <Context.Provider value={value}>{error && <div role="alert" className="error-banner">{error}</div>}{children}{message && <div className="toast" role="status">{message}</div>}</Context.Provider>;
}
