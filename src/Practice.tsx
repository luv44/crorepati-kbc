import { useEffect, useRef, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { ArrowRight, Bookmark, Check, CheckCircle2, Clock, Flag, Lightbulb, RotateCcw, ShieldCheck, Trophy, X } from 'lucide-react';
import { useStore } from './context';
import { DownloadLink, PageHeading, useText } from './components';
import { conciseOptionText, recordAnswer, revisionQuestions, scoreSession, toggleBookmark, sessionKey, usefulLearningNote } from './domain';
import type { Question, SessionResult } from './types';

type Mode = 'practice' | 'mock' | 'challenge';
interface Run { id: string; examId: string; ids: string[]; index: number; answers: Record<string, number>; started: number; deadline: number | null; mode: Mode; negative: number; finished: boolean; hintUsed: boolean; eliminateUsed: boolean; eliminated: number[]; hintFor: string | null }
const rank = { EASY: 0, MEDIUM: 1, HARD: 2, EXPERT: 3 };

export default function Practice({ mode = 'practice' }: { mode?: Mode }) {
  const { examQuestions: questions, state, examSubjects, selectedExam, update, toast } = useStore();
  const [params] = useSearchParams();
  const text = useText();
  const [subject, setSubject] = useState(params.get('subject') || 'all');
  const [chapter, setChapter] = useState('all');
  const [topic, setTopic] = useState(params.get('topic') || 'all');
  const [kind, setKind] = useState('all');
  const [count, setCount] = useState(Number(params.get('count')) || (mode === 'challenge' ? 15 : 10));
  const [minutes, setMinutes] = useState(mode === 'mock' ? 10 : 0);
  const [negative, setNegative] = useState(0);
  const [confidence, setConfidence] = useState(3);
  const [run, setRun] = useState<Run | null>(null);
  const [remaining, setRemaining] = useState(0);
  const questionStart = useRef(Date.now());
  const finishing = useRef(false);
  const locked = useRef(false);
  const persistedKey = `${sessionKey(mode, params.toString())}:exam=${selectedExam.id}`;
  // Session drafts are isolated by exam. Invalid or out-of-range drafts are removed instead of opening a blank question screen.
  useEffect(() => {
    setRun(null);
    try {
      const saved = sessionStorage.getItem(persistedKey);
      if (!saved) return;
      const parsed = JSON.parse(saved) as Run;
      const valid = parsed.examId === selectedExam.id
        && Array.isArray(parsed.ids) && parsed.ids.length > 0 && new Set(parsed.ids).size === parsed.ids.length
        && Number.isInteger(parsed.index) && parsed.index >= 0 && parsed.index < parsed.ids.length
        && parsed.ids.every(id => typeof id === 'string' && questions.some(question => question.id === id))
        && parsed.answers && typeof parsed.answers === 'object'
        && Object.entries(parsed.answers).every(([id, answer]) => parsed.ids.includes(id) && Number.isInteger(answer) && answer >= 0 && answer < 4)
        && parsed.mode === mode && !parsed.finished;
      if (valid) setRun(parsed);
      else sessionStorage.removeItem(persistedKey);
    } catch {
      sessionStorage.removeItem(persistedKey);
      toast('A previous session could not be restored. Start a fresh session.');
    }
  }, [persistedKey, mode, questions.length]);
  useEffect(() => { if (run?.examId === selectedExam.id) { try { sessionStorage.setItem(persistedKey, JSON.stringify(run)); } catch { toast('Session resume is unavailable in this browser. Progress is still saved locally.'); } } }, [run, persistedKey, selectedExam.id]);
  useEffect(() => { locked.current = false; questionStart.current = Date.now(); setConfidence(3); }, [run?.index]);
  const pool = questions.filter(q => (subject === 'all' || q.subjectId === subject) && (chapter === 'all' || q.chapterId === chapter) && (topic === 'all' || q.topicId === topic) && (kind === 'all' || q.kind === kind));
  const filter = params.get('filter');
  const candidates = filter === 'wrong' ? pool.filter(q => state.wrongIds.includes(q.id)) : filter === 'saved' ? pool.filter(q => state.bookmarks.includes(q.id)) : filter === 'due' ? revisionQuestions(pool, state) : filter === 'high-yield' ? pool.filter(q => q.difficulty !== 'EXPERT') : params.get('question') ? pool.filter(q => q.id === params.get('question')) : pool;
  const runQuestions = run ? run.ids.map(id => questions.find(q => q.id === id)!).filter(Boolean) : [];
  const q = runQuestions[run?.index || 0];
  const finish = (active: Run) => {
    if (finishing.current || active.finished) return; finishing.current = true;
    const selectedQuestions = active.ids.map(id => questions.find(q => q.id === id)!).filter(Boolean);
    const result = scoreSession(selectedQuestions, active.answers, active.negative);
    const entry: SessionResult = { id: active.id, mode: active.mode, at: Date.now(), questionIds: active.ids, answers: active.answers, correct: result.correct, total: active.ids.length, score: result.score, negativeMark: active.negative, elapsedMs: Date.now() - active.started };
    update(s => s.results.some(r => r.id === entry.id) ? s : { ...s, results: [...s.results, entry] });
    setRun({ ...active, finished: true });
  };
  useEffect(() => { if (!run?.deadline || run.finished) return; const tick = () => { const seconds = Math.max(0, Math.ceil((run.deadline! - Date.now()) / 1000)); setRemaining(seconds); if (!seconds) finish(run); }; tick(); const timer = setInterval(tick, 1000); return () => clearInterval(timer); }, [run]);
  function start() {
    const shuffled = [...candidates];
    for (let i = shuffled.length - 1; i > 0; i--) { const j = crypto.getRandomValues(new Uint32Array(1))[0] % (i + 1); [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]; }
    if (mode === 'challenge') shuffled.sort((a, b) => rank[a.difficulty] - rank[b.difficulty]);
    const ids = shuffled.slice(0, mode === 'challenge' ? 15 : count).map(q => q.id);
    if (!ids.length) { toast('No questions match this selection. Clear the filters and try again.'); return; }
    finishing.current = false; locked.current = false; questionStart.current = Date.now();
    const now = Date.now(); setRun({ id: crypto.randomUUID(), examId: selectedExam.id, ids, index: 0, answers: {}, started: now, deadline: minutes ? now + minutes * 60_000 : null, mode, negative, finished: false, hintUsed: false, eliminateUsed: false, eliminated: [], hintFor: null });
  }
  function answer(index: number) {
    if (!run || !q || locked.current || run.answers[q.id] !== undefined || run.finished) return;
    if (run.deadline && Date.now() >= run.deadline) { finish(run); return; }
    locked.current = true;
    const answers = { ...run.answers, [q.id]: index };
    update(s => recordAnswer(s, q, index, Date.now() - questionStart.current, confidence, mode));
    const next = { ...run, answers }; setRun(next);
    if (mode === 'challenge' && index !== q.correctIndex) finish(next);
  }
  const reset = () => { sessionStorage.removeItem(persistedKey); setRun(null); finishing.current = false; };
  const advance = () => {
    if (!run) return;
    if (run.index + 1 === run.ids.length) finish(run);
    else setRun({ ...run, index: run.index + 1, eliminated: [], hintFor: null });
  };
  const title = mode === 'challenge' ? 'The Crorepati Challenge' : mode === 'mock' ? 'Make practice feel like test day.' : 'A little practice. A stronger memory.';
  if (!run) return <><PageHeading eyebrow={mode === 'challenge' ? 'ORIGINAL KNOWLEDGE CHALLENGE · VIRTUAL POINTS ONLY' : 'RETRIEVE. UNDERSTAND. REMEMBER.'} title={title}>{mode === 'challenge' ? '15 unique questions, a rising challenge, and two thoughtful ways to get unstuck.' : `Practice questions mapped to ${selectedExam.name}. Evidence links appear when a reviewed source is attached.`}</PageHeading><div className="practice-setup"><section className="card setup-card">{mode === 'challenge' ? <><Trophy className="large-trophy" size={48} /><h2>How far will curiosity take you?</h2><p>Answer correctly to advance. One incorrect answer ends the run. Earn 100 × your stage in virtual points for each correct answer.</p><ul><li><strong>Recall cue:</strong> reveal a memory cue once.</li><li><strong>Narrow the field:</strong> remove one incorrect option once.</li><li>Difficulty follows the available question bank.</li></ul></> : <h2>Build your session</h2>}<div className="form-grid"><label>Subject<select value={subject} onChange={e => { setSubject(e.target.value); setChapter('all'); setTopic('all'); }}><option value="all">All available subjects</option>{examSubjects.map(s => <option value={s.id} key={s.id}>{s.shortTitle}</option>)}</select></label><label>Chapter<select value={chapter} onChange={e => { setChapter(e.target.value); setTopic('all'); }}><option value="all">All chapters</option>{examSubjects.filter(s => subject === 'all' || s.id === subject).flatMap(s => s.chapters).map(c => <option key={c.id} value={c.id}>{c.title}</option>)}</select></label><label>Topic<select value={topic} onChange={e => setTopic(e.target.value)}><option value="all">All topics</option>{examSubjects.filter(s => subject === 'all' || s.id === subject).flatMap(s => s.chapters.filter(c => chapter === 'all' || c.id === chapter).flatMap(c => c.topics)).filter(t => t.questionCount).map(t => <option key={t.id} value={t.id}>{t.title}</option>)}</select></label>{mode !== 'challenge' && <><label>Number of questions<select value={count} onChange={e => setCount(Number(e.target.value))}>{[1, 5, 10, 15, 20, 50, 100].map(n => <option key={n} value={n}>{n}</option>)}</select></label><label>Timer<select value={minutes} onChange={e => setMinutes(Number(e.target.value))}><option value={0}>Untimed</option>{[5, 10, 20, 30, 60].map(n => <option key={n} value={n}>{n} minutes</option>)}</select></label><label>Wrong-answer penalty<select value={negative} onChange={e => setNegative(Number(e.target.value))}><option value={0}>None</option><option value={0.25}>−0.25 points</option><option value={0.5}>−0.5 points</option><option value={1}>−1 point</option></select></label><label>Question type<select value={kind} onChange={e => setKind(e.target.value)}><option value="all">All available practice</option><option value="ACTUAL_PYQ">Legacy PYQ label (provenance pending)</option></select></label></>}</div><p className="availability" aria-live="polite">{candidates.length} focused questions available · {mode === 'challenge' ? '15 required' : `${Math.min(count, candidates.length)} will be used`}</p><p className="small muted">One concise canonical legacy question is published per topic; repetitive expansion drafts remain preserved in the audit corpus but are not served in practice.</p><button className="button full" disabled={!candidates.length || (mode === 'challenge' && candidates.length < 15)} onClick={start}>{mode === 'challenge' ? 'Begin challenge' : `Start ${Math.min(count, candidates.length)}-question session`}<ArrowRight size={18} /></button>{!candidates.length && <div className="empty-filter-message"><p>No available questions match this selection.</p><Link className="secondary" to="/practice">Clear all practice filters</Link></div>}<DownloadLink /></section><aside className="card setup-aside"><ShieldCheck size={30} /><h2>Understand the answer.<br />Not just the score.</h2><p>Review explanations, see why other options don’t fit, and build your own revision rhythm.</p><div className="shortcut-list"><Link to="/notebook">Wrong answer notebook →</Link><Link to="/revision">Smart revision →</Link><Link to="/practice?filter=high-yield">High-yield practice →</Link><Link to="/mocks">Timed mock tests →</Link></div><p className="small muted">High-yield prioritizes accessible foundational questions; no unsupported exam-frequency claim is made.</p></aside></div></>;
  if (run.finished) {
    const results = scoreSession(runQuestions, run.answers, run.negative);
    const points = runQuestions.reduce((n, q, i) => n + (run.answers[q.id] === q.correctIndex ? 100 * (i + 1) : 0), 0);
    return <><PageHeading eyebrow="EVERY ATTEMPT MOVES YOU FORWARD" title={mode === 'challenge' ? 'Your challenge, reflected.' : 'Here’s what you learned.'} /><section className="result-summary card"><Trophy size={42} /><h2>{mode === 'challenge' ? `${points.toLocaleString()} virtual points` : `${results.score} / ${run.ids.length} points`}</h2><div className="result-stats"><span><strong>{results.correct}</strong>correct</span><span><strong>{results.wrong}</strong>to revisit</span><span><strong>{results.unanswered}</strong>unanswered</span><span><strong>{results.accuracy}%</strong>accuracy</span></div><div className="actions"><button onClick={reset}><RotateCcw size={17} />New session</button><Link to="/notebook" className="secondary">Review mistakes</Link></div></section><h2>Question-by-question review</h2>{runQuestions.filter(q => run.answers[q.id] !== undefined).map(q => <article className="card review-card" key={q.id}><h3>{text(q.question)}</h3><p className={run.answers[q.id] === q.correctIndex ? 'correct-text' : 'wrong-text'}>{run.answers[q.id] === q.correctIndex ? 'Correct' : 'Revisit'} · Your answer: {conciseOptionText(text(q.options[run.answers[q.id]]))}</p><Explanation question={q} /><Link to={`/topic/${q.topicId}`} className="text-link">Review the concept<ArrowRight size={16} /></Link></article>)}</>;
  }
  if (!q) return <section className="empty card"><RotateCcw size={32} /><h2>Start a fresh practice session</h2><p>The saved question selection no longer matches the active exam. Your learning history is safe.</p><button className="button" onClick={reset}>Return to question selection<ArrowRight size={17} /></button></section>;
  const answered = run.answers[q.id] !== undefined;
  const memoryCue = text(q.memoryCue);
  const hasMemoryCue = usefulLearningNote(memoryCue);
  return <><div className="session-header"><Link to="/">← Home</Link><span className="chip">{mode.toUpperCase()}</span>{run.deadline && <span className="timer" role="timer"><Clock size={17} />{Math.floor(remaining / 60)}:{String(remaining % 60).padStart(2, '0')}</span>}<button className="secondary" onClick={() => finish(run)}><Flag size={16} />Finish session</button></div><div className="session-progress"><span style={{ width: `${run.index / run.ids.length * 100}%` }} /></div><section className="question-card card"><div className="question-meta"><span>QUESTION {run.index + 1} OF {run.ids.length}</span><span className="chip neutral">{q.difficulty.toLowerCase()}</span><button className="icon-button bookmark" aria-label={state.bookmarks.includes(q.id) ? 'Remove bookmark' : 'Bookmark question'} aria-pressed={state.bookmarks.includes(q.id)} onClick={() => update(s => toggleBookmark(s, q.id))}><Bookmark fill={state.bookmarks.includes(q.id) ? 'currentColor' : 'none'} size={21} /></button></div><h1 className="question-title" lang={state.profile.language === 'hi' ? 'hi' : 'en'}>{text(q.question)}</h1><div className="options" role="group" aria-label="Answer options">{q.options.map((option, index) => <button key={index} disabled={answered || run.eliminated.includes(index)} className={`answer-option ${answered && mode !== 'mock' && index === q.correctIndex ? 'correct' : ''} ${answered && run.answers[q.id] === index ? mode !== 'mock' && index !== q.correctIndex ? 'incorrect' : 'chosen' : ''}`} onClick={() => answer(index)}><span className="option-letter">{String.fromCharCode(65 + index)}</span><span title={text(option)}>{conciseOptionText(text(option))}</span>{answered && mode !== 'mock' && index === q.correctIndex && <Check size={20} />}{answered && mode !== 'mock' && run.answers[q.id] === index && index !== q.correctIndex && <X size={20} />}</button>)}</div>{!answered && <label className="confidence">How confident are you?<select value={confidence} onChange={e => setConfidence(Number(e.target.value))}><option value={1}>Taking a guess</option><option value={3}>Fairly sure</option><option value={5}>Very sure</option></select></label>}{mode === 'challenge' && !answered && <div className="actions">{hasMemoryCue && <button className="secondary" disabled={run.hintUsed} onClick={() => setRun({ ...run, hintUsed: true, hintFor: q.id })}><Lightbulb size={17} />Recall cue</button>}<button className="secondary" disabled={run.eliminateUsed} onClick={() => setRun({ ...run, eliminateUsed: true, eliminated: [q.options.findIndex((_, i) => i !== q.correctIndex)] })}>Narrow the field</button></div>}{run.hintFor === q.id && hasMemoryCue && <p className="memory-cue">{memoryCue}</p>}{!answered && <div className="question-forward"><button className="secondary" onClick={advance}>{run.index + 1 === run.ids.length ? 'See results' : 'Skip this one'}<ArrowRight size={18} /></button></div>}{answered && <div aria-live="polite" className="answer-feedback">{mode !== 'mock' ? <><h2 className={run.answers[q.id] === q.correctIndex ? 'correct-text' : 'wrong-text'}>{run.answers[q.id] === q.correctIndex ? 'Nicely recalled.' : 'A good moment to make a connection.'}</h2><Explanation question={q} /></> : <p><CheckCircle2 size={17} /> Answer saved. Explanations appear after you finish.</p>}<button className="button" onClick={advance}>{run.index + 1 === run.ids.length ? 'See results' : 'Next question'}<ArrowRight size={18} /></button></div>}</section></>;
}

export function Explanation({ question: q }: { question: Question }) {
  const { facts, sources } = useStore(); const text = useText();
  const evidence = facts.filter(fact => q.factCardIds.includes(fact.id)).flatMap(fact => Array.isArray(fact.evidence) ? fact.evidence : []);
  const linkedSources = sources.filter(source => q.sourceIds.includes(source.id));
  const explanation = text(q.explanation);
  const detailed = text(q.detailedExplanation);
  const cue = text(q.memoryCue);
  let distractor = -1;
  const usefulReasons = q.options.flatMap((option, index) => {
    if (index === q.correctIndex) return [];
    distractor += 1;
    const reason = q.wrongReasons.length === q.options.length ? q.wrongReasons[index] : q.wrongReasons[distractor];
    const localizedReason = reason ? text(reason) : '';
    return usefulLearningNote(localizedReason) ? [{ index, option: conciseOptionText(text(option)), reason: localizedReason }] : [];
  });
  const showDetailed = usefulLearningNote(detailed) && detailed.normalize('NFKC').trim() !== explanation.normalize('NFKC').trim();
  const showCue = usefulLearningNote(cue);
  return <div className="explanation"><p><strong>Answer: {conciseOptionText(text(q.options[q.correctIndex]))}</strong></p><p>{explanation}</p>{(showDetailed || usefulReasons.length > 0) && <details><summary>Go a little deeper</summary>{showDetailed && <p>{detailed}</p>}{usefulReasons.length > 0 && <ul>{usefulReasons.map(item => <li key={item.index}><strong>{item.option}:</strong> {item.reason}</li>)}</ul>}</details>}{showCue && <div className="memory-cue"><Lightbulb size={18} /><span>{cue}</span></div>}<details><summary>Evidence & sources</summary>{evidence.map((entry, index) => <blockquote key={index}>{entry.quote}<cite>{entry.locator}</cite></blockquote>)}{linkedSources.map(source => <a className="source-link" key={source.id} href={source.url} target="_blank" rel="noopener noreferrer">{source.publisher} · {source.title} ↗</a>)}{!evidence.length && !linkedSources.length && <p className="muted">This preserved question does not yet have a resolvable direct-source excerpt. Its source gap remains listed in the project audit.</p>}</details></div>;
}
