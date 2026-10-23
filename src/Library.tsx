import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Bookmark, CalendarDays, CheckCircle2, Clock3, ListChecks, Newspaper, RotateCcw, Search, Sparkles, Target } from 'lucide-react';
import { useStore } from './context';
import { DownloadLink, Empty, PageHeading, useText } from './components';
import { revisionQuestions, searchMatch, toggleBookmark } from './domain';
import type { CurrentNewsItem, CurrentNewsMcq } from './types';

export default function Library({ page }: { page: string }) {
  const { state, examQuestions: questions, facts, examSubjects, update } = useStore();
  const text = useText();
  const [query, setQuery] = useState('');
  const [limit, setLimit] = useState(30);
  const topics = examSubjects.flatMap(s => s.chapters.flatMap(c => c.topics));
  const topicIds = new Set(topics.map(topic => topic.id));
  const mappedSubjectIds = new Set(examSubjects.map(subject => subject.id));
  const mappedConceptIds = new Set(topics.flatMap(topic => topic.concepts.map(concept => concept.id)));
  const mappedAttempts = state.attempts.filter(attempt => mappedSubjectIds.has(attempt.subjectId));
  const mappedResults = state.results.filter(result => result.questionIds.some(id => questions.some(question => question.id === id)));
  if (page === 'current-affairs') return <CurrentLive />;
  if (page === 'pyq') return <><PageHeading eyebrow="EVIDENCE BEFORE PUBLICATION" title="Previous year questions">Actual exam papers, official answer keys, and clear provenance.</PageHeading><Empty title="Official papers are awaiting ingestion." link="/practice" label="Explore reviewed practice">This checkpoint contains no provenance-complete actual PYQs. Exam, stage, year, paper, shift and official answer provenance are required before publication. Practice questions are not presented as past-paper questions.</Empty><section className="card topic-section"><h2>How provenance is checked</h2><p>Official paper → question number → official answer key → evidence review → verified question. Missing or ambiguous records remain unavailable.</p></section></>;
  if (page === 'performance') {
    const correct = mappedAttempts.filter(attempt => attempt.correct).length;
    const accuracy = mappedAttempts.length ? Math.round(correct / mappedAttempts.length * 100) : 0;
    const avg = mappedAttempts.length ? Math.round(mappedAttempts.reduce((total, attempt) => total + attempt.elapsedMs, 0) / mappedAttempts.length / 1000) : 0;
    const last7 = Array.from({ length: 7 }, (_, i) => { const d = new Date(); d.setDate(d.getDate() - 6 + i); return { label: d.toLocaleDateString('en', { weekday: 'short' }), count: mappedAttempts.filter(attempt => new Date(attempt.at).toDateString() === d.toDateString()).length }; });
    const max = Math.max(1, ...last7.map(x => x.count));
    return <><PageHeading eyebrow="SMALL STEPS ADD UP" title="Your learning, in perspective.">A reflection of practice on this device. No comparison needed.</PageHeading><div className="metric-grid">{[[mappedAttempts.length, 'Questions attempted'], [`${accuracy}%`, 'Answer accuracy'], [`${avg}s`, 'Average answer time'], [Object.entries(state.progress).filter(([id, progress]) => mappedConceptIds.has(id) && progress.state === 'MASTERED').length, 'Concepts mastered']].map(([n, label]) => <div className="card metric" key={label}><strong>{n}</strong><span>{label}</span></div>)}</div><div className="two-column"><section className="card topic-section"><h2>A week of curiosity</h2><div className="bar-chart" aria-label="Practice activity over the last seven days">{last7.map((x, i) => <div key={i}><span>{x.count}</span><div className="bar-track"><div style={{ height: `${x.count / max * 100}%` }} /></div><span>{x.label}</span></div>)}</div></section><section className="card topic-section"><h2>Find your next focus</h2>{examSubjects.map(s => ({ s, attempts: mappedAttempts.filter(a => a.subjectId === s.id) })).filter(x => x.attempts.length).map(({ s, attempts }) => <div className="subject-performance" key={s.id}><span>{s.shortTitle}</span><strong>{Math.round(attempts.filter(a => a.correct).length / attempts.length * 100)}%</strong></div>)}{!mappedAttempts.length && <p>Your strengths and areas to revisit will appear after your first practice session for this exam map.</p>}<Link className="text-link" to="/notebook">Review weak concepts<ArrowRight size={16} /></Link></section></div><h2>Session history</h2>{mappedResults.length ? [...mappedResults].reverse().map(r => <details className="card history-row" key={r.id}><summary>{r.mode} · {r.correct}/{r.total} correct · {r.score} points · {new Date(r.at).toLocaleString()}</summary><p>{Math.round(r.elapsedMs / 1000)} seconds · penalty {r.negativeMark} per wrong answer</p>{r.questionIds.map(id => { const q = questions.find(q => q.id === id); return <p key={id}>{q ? text(q.question) : `Question ${id} (pack not downloaded)`} — {r.answers[id] === undefined ? 'Unanswered' : q ? text(q.options[r.answers[id]]) : `Option ${r.answers[id] + 1}`}</p>; })}</details>) : <Empty title="Your story starts with one question." link="/practice" label="Start practicing">Completed practice sessions, mocks and challenges will appear here.</Empty>}</>;
  }
  if (page === 'search') {
    const subjectMatches = query.trim() ? examSubjects.filter(s => searchMatch(query, s.title, s.titleHindi)) : [];
    const chapterMatches = query.trim() ? examSubjects.flatMap(s => s.chapters.map(c => ({ ...c, subjectId: s.id }))).filter(c => searchMatch(query, c.title)) : [];
    const topicMatches = query.trim() ? topics.filter(t => searchMatch(query, t.title, ...t.concepts.map(c => c.title))) : [];
    const questionMatches = query.trim() ? questions.filter(q => searchMatch(query, q.question.en, q.question.hi, q.explanation.en, q.explanation.hi)) : [];
    const factMatches = query.trim() ? facts.filter(f => topicIds.has(f.topicId) && searchMatch(query, f.canonicalStatement, f.canonicalStatementHindi)) : [];
    return <><PageHeading eyebrow="FOLLOW A THREAD" title="What are you curious about?">Search subjects, chapters, topics, concepts, downloaded questions and stored fact records.</PageHeading><label className="search-field"><Search size={20} /><span className="sr-only">Search knowledge</span><input autoFocus value={query} onChange={e => { setQuery(e.target.value); setLimit(30); }} placeholder="Try planets, Harappan, units, संयुक्त राष्ट्र…" /></label>{query.trim() ? <><p className="muted">{subjectMatches.length + chapterMatches.length + topicMatches.length + questionMatches.length + factMatches.length} results · Questions and facts are searched locally.</p>{subjectMatches.map(s => <Link className="card search-result" key={s.id} to={`/learn/${s.id}`}><span className="eyebrow">SUBJECT</span><h3>{s.title}</h3><ArrowRight size={18} /></Link>)}{chapterMatches.slice(0, limit).map(c => <Link className="card search-result" key={c.id} to={`/learn/${c.subjectId}`}><span className="eyebrow">CHAPTER</span><h3>{c.title}</h3></Link>)}{topicMatches.slice(0, limit).map(t => <Link className="card search-result" key={t.id} to={`/topic/${t.id}`}><span className="eyebrow">TOPIC</span><h3>{t.title}</h3><p>{t.questionCount} available questions</p></Link>)}{questionMatches.slice(0, limit).map(q => <Link className="card search-result" key={q.id} to={`/practice?question=${q.id}`}><span className="eyebrow">QUESTION</span><h3>{text(q.question)}</h3></Link>)}{factMatches.slice(0, limit).map(f => <Link className="card search-result" key={f.id} to={`/topic/${f.topicId}`}><span className="eyebrow">FACT RECORD</span><p>{state.profile.language === 'hi' ? f.canonicalStatementHindi : f.canonicalStatement}</p></Link>)}{Math.max(chapterMatches.length, topicMatches.length, questionMatches.length, factMatches.length) > limit && <button onClick={() => setLimit(n => n + 30)}>Show more results</button>}</> : <Empty title="Every discovery begins with a question.">People, places, books and events can be found through their mapped topics. Hindi scripts are represented where bilingual fact records are available.</Empty>}</>;
  }
  const due = revisionQuestions(questions, state);
  const list = page === 'notebook' ? questions.filter(q => state.wrongIds.includes(q.id)) : page === 'bookmarks' ? questions.filter(q => state.bookmarks.includes(q.id)) : due;
  const title = page === 'notebook' ? 'Make a friend of your mistakes.' : page === 'bookmarks' ? 'Keep a little curiosity for later.' : 'Remember what matters.';
  const savedTopics = page === 'bookmarks' ? topics.filter(t => state.bookmarks.includes(t.id)) : [];
  const nextDue = Object.values(state.progress).map(p => p.due).filter(t => t > Date.now()).sort((a, b) => a - b)[0];
  return <><PageHeading eyebrow={page === 'notebook' ? 'WRONG ANSWER NOTEBOOK' : page === 'bookmarks' ? 'YOUR BOOKMARKS' : 'SMART REVISION'} title={title}>{page === 'revision' ? 'Spaced recall, guided by accuracy, confidence and recency. Previously unseen angles come first.' : page === 'notebook' ? 'An incorrect answer is a starting point. Understand why, then give it another try.' : 'Questions and topics you want to return to.'}</PageHeading>{page === 'revision' && <div className="revision-banner"><Sparkles size={30} /><div><h2>{due.length ? `${due.length} questions are ready for recall.` : 'You’re all caught up for now.'}</h2><p>{nextDue ? `Next scheduled review: ${new Date(nextDue).toLocaleString()}` : 'Your first practice session starts a personal revision schedule.'}</p></div>{!!due.length && <Link to="/practice?filter=due" className="button">Begin revision<ArrowRight size={17} /></Link>}</div>}{!!list.length && <Link to={`/practice?filter=${page === 'notebook' ? 'wrong' : page === 'bookmarks' ? 'saved' : 'due'}`} className="button">Practice these questions<ArrowRight size={17} /></Link>}{savedTopics.map(t => <Link to={`/topic/${t.id}`} className="card search-result" key={t.id}><span className="eyebrow">SAVED TOPIC</span><h3>{t.title}</h3></Link>)}{list.slice(0, limit).map(q => <article className="card notebook-card" key={q.id}><div><span className="chip neutral">{q.difficulty}</span><button className="icon-button" aria-label="Toggle bookmark" aria-pressed={state.bookmarks.includes(q.id)} onClick={() => update(s => toggleBookmark(s, q.id))}><Bookmark size={19} /></button></div><h2>{text(q.question)}</h2><p>{text(q.memoryCue)}</p><div className="actions"><Link className="text-link" to={`/practice?question=${q.id}`}><Target size={16} />Try again</Link><Link className="text-link" to={`/topic/${q.topicId}`}>Review the concept<ArrowRight size={16} /></Link></div></article>)}{list.length > limit && <button onClick={() => setLimit(n => n + 30)}>Show more</button>}{!list.length && !savedTopics.length && <Empty title={page === 'notebook' ? 'A fresh page for your learning.' : page === 'bookmarks' ? 'Something worth remembering?' : 'Build your recall rhythm.'} link="/practice" label="Start practice">{page === 'notebook' ? 'Questions you get wrong are saved here automatically. A correct retry resolves the entry while keeping your answer history.' : page === 'bookmarks' ? 'Use the bookmark button on a question or topic to save it here.' : 'Correct recall spaces reviews at 1, 3, 7, 14, 30 and 60 days. A mistake returns in 10 minutes.'}</Empty>}{page === 'revision' && <div className="revision-legend"><span><CalendarDays size={17} />Scheduled from recall</span><span><CheckCircle2 size={17} />Confidence-aware</span><span><Sparkles size={17} />Alternative angles first</span></div>}<DownloadLink /></>;
}

function CurrentLive() {
  const { currentNews, state, update, toast } = useStore();
  const text = useText();
  const locale = state.profile.language === 'hi' ? 'hi-IN' : 'en-IN';
  const verifiedDates = [...new Set(currentNews.items.map(item => item.publicationDate))].sort().reverse();
  const newest = verifiedDates[0] || new Date().toISOString().slice(0, 10);
  const initial = newest.split('-').map(Number);
  const [year, setYear] = useState(initial[0]);
  const [month, setMonth] = useState(initial[1]);
  const [day, setDay] = useState(initial[2]);
  const [view, setView] = useState<'brief' | 'quiz'>('brief');
  const [selectedItemId, setSelectedItemId] = useState('');
  const years = [...new Set([new Date().getFullYear(), ...currentNews.items.map(item => Number(item.publicationDate.slice(0, 4)))])].sort((a, b) => b - a);
  const monthNames = Array.from({ length: 12 }, (_, index) => new Date(2024, index, 1).toLocaleDateString(locale, { month: 'long' }));
  const daysInMonth = new Date(year, month, 0).getDate();
  const safeDay = Math.min(day, daysInMonth);
  const selectedDate = `${year}-${String(month).padStart(2, '0')}-${String(safeDay).padStart(2, '0')}`;
  const items = currentNews.items.filter(item => item.publicationDate === selectedDate);
  const selectedItem = items.find(item => item.id === selectedItemId) || items[0];
  const dailyQuestions = items.flatMap(item => item.mcqs.map(question => ({ question, story: item })));
  const savedItems = currentNews.items.filter(item => state.bookmarks.includes(item.id));

  useEffect(() => {
    setSelectedItemId(current => items.some(item => item.id === current) ? current : items[0]?.id || '');
    setView('brief');
  }, [selectedDate]);

  const chooseDate = (date: string) => {
    const [nextYear, nextMonth, nextDay] = date.split('-').map(Number);
    setYear(nextYear);
    setMonth(nextMonth);
    setDay(nextDay);
  };

  return <>
    <PageHeading eyebrow="DAILY GENERAL CURRENT AFFAIRS · OFFICIAL SOURCES" title="Current Live">Read a one-minute bilingual analysis, then answer only the questions supported by that story. Recruitment and result updates stay outside this feed.</PageHeading>
    <section className="card current-date-panel" aria-label="Current news date selectors">
      <div className="current-date-heading">
        <div><span className="eyebrow">PUBLICATION DATE</span><h2>{new Date(`${selectedDate}T00:00:00`).toLocaleDateString(locale, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}</h2></div>
        <button className="secondary" onClick={() => chooseDate(newest)}>Latest verified date</button>
      </div>
      <div className="date-selectors">
        <label>Year<select aria-label="News year" value={year} onChange={event => { setYear(Number(event.target.value)); setDay(current => Math.min(current, new Date(Number(event.target.value), month, 0).getDate())); }}>{years.map(value => <option key={value} value={value}>{value}</option>)}</select></label>
        <label>Month<select aria-label="News month" value={month} onChange={event => { const value = Number(event.target.value); setMonth(value); setDay(current => Math.min(current, new Date(year, value, 0).getDate())); }}>{monthNames.map((name, index) => <option key={name} value={index + 1}>{name}</option>)}</select></label>
        <label>Day<select aria-label="News day" value={safeDay} onChange={event => setDay(Number(event.target.value))}>{Array.from({ length: daysInMonth }, (_, index) => index + 1).map(value => <option key={value} value={value}>{value}</option>)}</select></label>
      </div>
      <div className="verified-date-strip" aria-label="Available verified dates">
        <span>Verified days</span>
        {verifiedDates.slice(0, 7).map(date => <button aria-pressed={date === selectedDate} onClick={() => chooseDate(date)} key={date}>{new Date(`${date}T00:00:00`).toLocaleDateString(locale, { day: 'numeric', month: 'short' })}</button>)}
      </div>
      {!!savedItems.length && <div className="saved-news-strip" aria-label="Saved current affairs briefs"><span><Bookmark size={14} fill="currentColor" />Saved for review</span>{savedItems.map(item => <button onClick={() => { chooseDate(item.publicationDate); setSelectedItemId(item.id); setView('brief'); }} key={item.id}>{text(item.category)} · {new Date(`${item.publicationDate}T00:00:00`).toLocaleDateString(locale, { day: 'numeric', month: 'short' })}</button>)}</div>}
      <p className="small muted"><CheckCircle2 size={16} /> Feed checked {new Date(currentNews.builtAt).toLocaleDateString('en-IN')} · every story retains its publication date, excerpt and official link.</p>
    </section>

    {items.length ? <section className="current-live-workspace">
      <div className="current-live-overview card">
        <div><Newspaper size={22} /><strong>{items.length}</strong><span>{items.length === 1 ? 'checked story' : 'checked stories'}</span></div>
        <div><Clock3 size={22} /><strong>1 min</strong><span>bilingual brief</span></div>
        <div><ListChecks size={22} /><strong>{dailyQuestions.length}</strong><span>story-linked MCQs</span></div>
      </div>
      <div className="current-mode-row">
        <div className="current-view-tabs" role="tablist" aria-label="Current Live mode">
          <button role="tab" aria-selected={view === 'brief'} className={view === 'brief' ? 'active' : ''} onClick={() => setView('brief')}><Newspaper size={18} />1-minute brief</button>
          <button role="tab" aria-selected={view === 'quiz'} className={view === 'quiz' ? 'active' : ''} onClick={() => setView('quiz')}><ListChecks size={18} />Daily quiz <span>{dailyQuestions.length}</span></button>
        </div>
        <span className="offline-ready"><CheckCircle2 size={16} />Cached with the app for offline reading</span>
      </div>
      {view === 'brief' && selectedItem && <div className="current-story-layout">
        <nav className="current-story-list card" aria-label="Stories for selected date">
          <p className="eyebrow">TODAY'S VERIFIED STORIES</p>
          {items.map(item => <button className={item.id === selectedItem.id ? 'active' : ''} aria-current={item.id === selectedItem.id ? 'true' : undefined} onClick={() => setSelectedItemId(item.id)} key={item.id}><span>{text(item.category)}</span><strong>{text(item.title)}</strong><small>{item.mcqs.length} questions</small></button>)}
        </nav>
        <NewsBrief item={selectedItem} saved={state.bookmarks.includes(selectedItem.id)} onToggleSave={() => { update(current => toggleBookmark(current, selectedItem.id)); toast(state.bookmarks.includes(selectedItem.id) ? 'Brief removed from saved review.' : 'Brief saved for review.'); }} onStartQuiz={() => setView('quiz')} />
      </div>}
      {view === 'quiz' && <DailyNewsQuiz key={selectedDate} questions={dailyQuestions} onReview={() => setView('brief')} />}
    </section> : <Empty title="No verified news found">No checked general-current-affairs story is stored for {selectedDate}. Nothing has been generated or inferred for this date.</Empty>}

    <section className="card current-policy"><h2>Verification rule</h2><p>{currentNews.policy}</p></section>
  </>;
}

function NewsBrief({ item, saved, onToggleSave, onStartQuiz }: { item: CurrentNewsItem; saved: boolean; onToggleSave: () => void; onStartQuiz: () => void }) {
  const text = useText();
  return <article className="card current-news-card current-brief">
    <div className="news-meta"><span className="chip"><CalendarDays size={13} /> {text(item.category)} · Published {new Date(`${item.publicationDate}T00:00:00`).toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' })}</span><span>Verified {new Date(`${item.verifiedAt}T00:00:00`).toLocaleDateString('en-IN')}</span></div>
    <span className="reading-time"><Clock3 size={15} /> {item.analysis.readTimeMinutes}-minute analysis</span>
    <div className="current-story-title"><h2>{text(item.title)}</h2><button className="secondary" aria-pressed={saved} onClick={onToggleSave}><Bookmark size={17} fill={saved ? 'currentColor' : 'none'} />{saved ? 'Saved' : 'Save brief'}</button></div>
    <p className="news-lead">{text(item.summary)}</p>
    <div className="news-analysis-grid">
      <section><p className="eyebrow">KEY POINTS</p><ul>{item.analysis.keyPoints.map((point, index) => <li key={index}><span>{index + 1}</span><p>{text(point)}</p></li>)}</ul></section>
      <aside><p className="eyebrow">WHAT TO REMEMBER</p><LightbulbCard>{text(item.analysis.whatToRemember)}</LightbulbCard><button className="button full" onClick={onStartQuiz}>Start this story's quiz<ArrowRight size={17} /></button></aside>
    </div>
    <details className="news-evidence"><summary>See checked evidence</summary><blockquote>{item.evidenceQuote}<cite>{item.evidenceLocator}</cite></blockquote></details>
    <div className="source-list" aria-label="Verified news sources">{item.links.map(link => <a className="source-link" href={link.url} target="_blank" rel="noopener noreferrer" key={link.url}>{link.label} ↗</a>)}</div>
  </article>;
}

function LightbulbCard({ children }: { children: string }) {
  return <div className="remember-card"><Sparkles size={20} /><p>{children}</p></div>;
}

function DailyNewsQuiz({ questions, onReview }: { questions: { question: CurrentNewsMcq; story: CurrentNewsItem }[]; onReview: () => void }) {
  const text = useText();
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState<number>();
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [finished, setFinished] = useState(false);
  const current = questions[index];
  const answered = selected !== undefined;
  const score = questions.filter(({ question }) => answers[question.id] === question.correctIndex).length;
  const skipped = questions.filter(({ question }) => answers[question.id] === -1).length;

  const moveForward = () => {
    if (index + 1 >= questions.length) setFinished(true);
    else { setIndex(value => value + 1); setSelected(undefined); }
  };
  const answer = (option: number) => {
    if (!current || answered) return;
    setSelected(option);
    setAnswers(saved => ({ ...saved, [current.question.id]: option }));
  };
  const skip = () => {
    if (!current || answered) return;
    setAnswers(saved => ({ ...saved, [current.question.id]: -1 }));
    moveForward();
  };
  const reset = () => { setIndex(0); setSelected(undefined); setAnswers({}); setFinished(false); };

  if (!questions.length) return <Empty title="No quiz is available">No source-backed question is stored for this date.</Empty>;
  if (finished) return <section className="card daily-quiz-result"><CheckCircle2 size={42} /><p className="eyebrow">DAILY QUIZ COMPLETE</p><h2>{score} / {questions.length} correct</h2><p>{skipped ? `${skipped} skipped · ` : ''}Every answer came from the checked stories shown for this date.</p><div className="actions"><button onClick={reset}><RotateCcw size={17} />Try again</button><button className="secondary" onClick={onReview}><Newspaper size={17} />Review the briefs</button></div></section>;
  if (!current) return null;

  const { question, story } = current;
  return <section className="card daily-news-quiz">
    <div className="daily-quiz-header"><div><span className="chip">{text(story.category)}</span><p>{text(story.title)}</p></div><strong>{index + 1} / {questions.length}</strong></div>
    <div className="daily-quiz-progress" aria-label={`Question ${index + 1} of ${questions.length}`}><span style={{ width: `${(index + 1) / questions.length * 100}%` }} /></div>
    <p className="eyebrow">QUESTION {index + 1}</p>
    <h2>{text(question.question)}</h2>
    <div className="news-options" role="group" aria-label={`Current affairs question ${index + 1}`}>{question.options.map((option, optionIndex) => <button className={answered ? optionIndex === question.correctIndex ? 'correct' : selected === optionIndex ? 'incorrect' : '' : ''} disabled={answered} onClick={() => answer(optionIndex)} key={optionIndex}><span className="option-letter">{String.fromCharCode(65 + optionIndex)}</span><span>{text(option)}</span></button>)}</div>
    {!answered && <div className="question-forward"><button className="secondary" onClick={skip}>{index + 1 === questions.length ? 'Skip & see result' : 'Skip this one'}<ArrowRight size={18} /></button></div>}
    {answered && <div className="news-answer" role="status"><strong>{selected === question.correctIndex ? 'Correct' : 'Answer'}: {text(question.options[question.correctIndex])}</strong><p>{text(question.explanation)}</p><div className="quiz-source-row"><span>Supported by the story above</span>{story.links.map(link => <a href={link.url} target="_blank" rel="noopener noreferrer" key={link.url}>Open official source ↗</a>)}</div><button className="button" onClick={moveForward}>{index + 1 === questions.length ? 'See result' : 'Next question'}<ArrowRight size={18} /></button></div>}
  </section>;
}
