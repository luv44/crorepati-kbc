import { lazy, Suspense, useEffect, useState } from 'react';
import { Link, NavLink, Navigate, Route, Routes, useLocation } from 'react-router-dom';
import { ArrowRight, BarChart3, BookOpen, Bookmark, Check, ChevronRight, Download, Flame, Home, LayoutGrid, Menu, Search, Settings, ShieldCheck, Sparkles, Target, Trophy, WifiOff, X } from 'lucide-react';
import { useStore } from './context';
import { PageHeading, SectionTitle, SubjectCard } from './components';
import { revisionQuestions } from './domain';
import Learn, { TopicPage } from './Learn';
const Practice = lazy(() => import('./Practice'));
const Library = lazy(() => import('./Library'));
const Downloads = lazy(() => import('./Downloads'));
const SettingsPage = lazy(() => import('./Settings'));

const translations = {
  en: ['Home', 'Learn', 'Practice', 'Smart revision', 'Challenge', 'Performance', 'Downloads', 'Settings'],
  hi: ['होम', 'सीखें', 'अभ्यास', 'स्मार्ट रिविज़न', 'चुनौती', 'प्रदर्शन', 'डाउनलोड', 'सेटिंग्स'],
  hinglish: ['Home', 'Seekhein', 'Practice', 'Revision', 'Challenge', 'Progress', 'Downloads', 'Settings'],
};
const navigation = [ ['/', Home], ['/learn', BookOpen], ['/practice', Target], ['/revision', Sparkles], ['/challenge', Trophy], ['/performance', BarChart3], ['/downloads', Download], ['/settings', Settings] ] as const;

export default function App() {
  const { state, toast } = useStore();
  const [menu, setMenu] = useState(false);
  const [offline, setOffline] = useState(!navigator.onLine);
  const [update, setUpdate] = useState<ServiceWorkerRegistration>();
  const location = useLocation();
  useEffect(() => { setMenu(false); window.scrollTo(0, 0); document.getElementById('main')?.focus(); }, [location.pathname]);
  useEffect(() => {
    const online = () => setOffline(!navigator.onLine);
    const swUpdate = (e: Event) => setUpdate((e as CustomEvent).detail);
    const swError = () => toast('Offline setup failed. You can keep learning online; retry by reloading.');
    window.addEventListener('online', online); window.addEventListener('offline', online); window.addEventListener('pwa-update', swUpdate); window.addEventListener('pwa-error', swError);
    navigator.serviceWorker?.getRegistration().then(r => { if (r?.waiting) setUpdate(r); });
    return () => { window.removeEventListener('online', online); window.removeEventListener('offline', online); window.removeEventListener('pwa-update', swUpdate); window.removeEventListener('pwa-error', swError); };
  }, [toast]);
  if (!state.profile.onboarded) return <Onboarding />;
  const labels = translations[state.profile.language];
  return <div className="app-shell"><a href="#main" className="skip-link">Skip to content</a>
    <aside className={`sidebar ${menu ? 'open' : ''}`}>
      <Link to="/" className="brand"><span className="brand-mark">c<span>r</span></span><span>Crorepati<small>REVISION</small></span></Link>
      <button className="icon-button close-menu" onClick={() => setMenu(false)} aria-label="Close navigation"><X /></button>
      <p className="nav-label">YOUR LEARNING SPACE</p>
      <nav aria-label="Primary navigation">{navigation.map(([to, Icon], i) => <NavLink key={to} to={to} end={to === '/'}><Icon size={20} /><span>{labels[i]}</span>{i === 3 && <span className="nav-dot" />}</NavLink>)}</nav>
      <div className="sidebar-bottom"><div className="guest-symbol">{state.profile.name.slice(0, 1).toUpperCase()}</div><div><strong>{state.profile.name}</strong><small>Guest · saved on this device</small></div><ShieldCheck size={18} /></div>
    </aside>
    {menu && <button className="menu-overlay" aria-label="Dismiss navigation" onClick={() => setMenu(false)} />}
    <div className="main-column"><header className="topbar"><button className="icon-button mobile-menu" aria-label="Open navigation" onClick={() => setMenu(true)}><Menu /></button><div className="topbar-breadcrumb">Your daily dose of discovery <span>✦</span></div><div className="topbar-actions"><Link to="/search" className="search-shortcut" aria-label="Search knowledge"><Search size={18} /><span>Search anything</span></Link><Link to="/settings" aria-label="Learning language" className="language-indicator">{state.profile.language === 'hi' ? 'हिंदी' : state.profile.language === 'hinglish' ? 'Hinglish' : 'EN'}</Link><Link to="/settings" className="avatar" aria-label="Profile settings">{state.profile.name.slice(0, 1).toUpperCase()}</Link></div></header>
      {offline && <div className="offline-banner" role="status"><WifiOff size={16} /> You’re offline. Downloaded questions and local progress are available.</div>}
      {update && <div className="update-banner">A new version is ready. Finish your current session, then <button onClick={() => { navigator.serviceWorker.addEventListener('controllerchange', () => window.location.reload(), { once: true }); update.waiting?.postMessage({ type: 'SKIP_WAITING' }); }}>update the app</button>.</div>}
      <main id="main" tabIndex={-1}><Suspense fallback={<p className="card">Opening your learning space…</p>}><Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/learn/:subjectId?" element={<Learn />} />
        <Route path="/topic/:topicId" element={<TopicPage />} />
        <Route path="/practice/*" element={<Practice key={location.search} />} />
        <Route path="/challenge" element={<Practice key="challenge" mode="challenge" />} />
        <Route path="/mocks" element={<Practice key="mock" mode="mock" />} />
        {['revision', 'notebook', 'bookmarks', 'search', 'performance', 'current-affairs', 'pyq'].map(page => <Route key={page} path={`/${page}`} element={<Library page={page} />} />)}
        <Route path="/downloads" element={<Downloads />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes></Suspense></main>
      <footer className="app-footer"><span>Curiosity today. Confidence tomorrow.</span><Link to="/settings#about">Build status & privacy</Link></footer>
    </div>
    <nav className="bottom-nav" aria-label="Mobile navigation">{navigation.slice(0, 4).map(([to, Icon], i) => <NavLink key={to} to={to} end={to === '/'}><Icon size={21} /><span>{labels[i]}</span></NavLink>)}<Link to="/search"><Search size={21} /><span>Search</span></Link></nav>
  </div>;
}

function Onboarding() {
  const { catalog, state, update } = useStore();
  const [interests, setInterests] = useState<string[]>([]);
  const [name, setName] = useState('');
  const [exam, setExam] = useState('General knowledge');
  return <main className="onboarding"><div className="onboarding-art"><Link to="/" className="brand light"><span className="brand-mark">c<span>r</span></span><span>Crorepati<small>REVISION</small></span></Link><span className="eyebrow">STAY CURIOUS. GROW EVERY DAY.</span><h1>A world of knowledge.<br /><em>Your own pace.</em></h1><p>Understand a little more. Remember a little longer. Build a learning habit that stays with you.</p><div className="orbit-art" aria-hidden="true"><div className="orbit o1" /><div className="orbit o2" /><div className="planet" /><span className="star star1">✦</span><span className="star star2">✦</span><div className="satellite" /></div><div className="onboarding-proof"><ShieldCheck /> Source-grounded learning <span>·</span> Guest-first <span>·</span> Offline-ready</div></div><section className="onboarding-form"><div className="chip">LET’S MAKE THIS YOURS</div><h2>Where will curiosity take you?</h2><p className="muted">Pick a few interests. You can explore all 26 subjects anytime.</p><label>Your name <span className="muted">(optional)</span><input maxLength={40} placeholder="What should we call you?" value={name} onChange={e => setName(e.target.value)} /></label><label>Learning goal<select value={exam} onChange={e => setExam(e.target.value)}>{['General knowledge', 'UPSC', 'SSC', 'Banking', 'Railways', 'State exams', 'Just curious'].map(x => <option key={x}>{x}</option>)}</select></label><div className="interest-grid">{catalog.subjects.filter(s => ['S01', 'S03', 'S05', 'S06', 'S08', 'S09', 'S12', 'S13'].includes(s.id)).map(s => <button key={s.id} className={interests.includes(s.id) ? 'selected' : ''} aria-pressed={interests.includes(s.id)} onClick={() => setInterests(old => old.includes(s.id) ? old.filter(x => x !== s.id) : [...old, s.id])}>{s.shortTitle}{interests.includes(s.id) && <Check size={15} />}</button>)}</div><button className="button full" onClick={() => update(s => ({ ...s, profile: { ...state.profile, onboarded: true, name: name.trim() || 'Learner', exam, interests } }))}>Continue as guest<ArrowRight size={18} /></button><p className="small muted center">No account needed. Your progress stays on this device.</p><p className="small build-note">Development checkpoint · {catalog.counts.questions} verified questions · Hindi video production pending</p></section></main>;
}

function HomePage() {
  const { state, questions, catalog } = useStore();
  const now = new Date();
  const today = state.attempts.filter(a => new Date(a.at).toDateString() === now.toDateString()).length;
  const accuracy = state.attempts.length ? Math.round(state.attempts.filter(a => a.correct).length / state.attempts.length * 100) : null;
  const due = revisionQuestions(questions, state).length;
  const availableTopics = catalog.subjects.flatMap(s => s.chapters.flatMap(c => c.topics)).filter(t => t.questionCount > 0);
  const firstTopic = availableTopics.find(t => t.subjectId === 'S09') || availableTopics[0];
  const chosen = [...catalog.subjects].sort((a, b) => Number(state.profile.interests.includes(b.id)) - Number(state.profile.interests.includes(a.id))).slice(0, 6);
  return <>
    <PageHeading eyebrow={now.toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'long' }).toUpperCase()} title={`A little wiser, every day.`}>Welcome back, {state.profile.name}. Make room for one new discovery.</PageHeading>
    <div className="home-hero"><div className="hero-copy"><span className="hero-kicker"><span /> YOUR NEXT SMALL STEP</span><h2>Big knowledge.<br /><em>Small, daily wins.</em></h2><p>Explore an idea, put it into practice, and make it yours. Your next discovery is just a question away.</p><Link to="/practice" className="button light-button">Start today’s practice<ArrowRight size={18} /></Link><div className="hero-meta"><ShieldCheck size={15} /> Verified sources <span>·</span> At your own pace</div></div><div className="hero-illustration" aria-hidden="true"><div className="orbit-art"><div className="orbit o1" /><div className="orbit o2" /><div className="planet" /><div className="satellite" /><span className="star star1">✦</span><span className="star star2">✦</span></div><div className="floating-note"><LightbulbIcon /> Stay curious.</div><div className="floating-mini">a little more, every day</div></div></div>
    <div className="stats-row"><div className="stat"><span className="stat-icon peach"><Flame /></span><div><strong>{today}<small> / {state.profile.dailyGoal}</small></strong><p>Today’s practice</p></div><div className="mini-progress"><span style={{ width: `${Math.min(100, today / state.profile.dailyGoal * 100)}%` }} /></div></div><div className="stat"><span className="stat-icon lavender"><Target /></span><div><strong>{accuracy === null ? '—' : `${accuracy}%`}</strong><p>Overall accuracy</p></div></div><Link to="/revision" className="stat"><span className="stat-icon mint"><Sparkles /></span><div><strong>{due}</strong><p>Questions due for revision</p></div><ChevronRight size={18} /></Link></div>
    <div className="home-columns"><section><SectionTitle title="Find your next discovery" link="/learn" label="All 26 subjects" /><div className="subject-grid">{chosen.map(s => <SubjectCard subject={s} key={s.id} />)}</div><SectionTitle title="A good place to begin" />{firstTopic && <Link to={`/topic/${firstTopic.id}`} className="feature-lesson card"><div className="lesson-art"><div className="tiny-planet" /><span>EXPLORE<br />THE EXTRAORDINARY</span></div><div><span className="eyebrow">SPACE & ASTRONOMY</span><h3>{firstTopic.title}</h3><p>Explore the concepts. Test what you know.</p><span className="text-link">Open topic<ArrowRight size={16} /></span></div></Link>}</section><aside className="home-right"><SectionTitle title="Your learning toolkit" /><div className="toolkit card">{[['/notebook', Bookmark, 'Turn mistakes into progress', `${state.wrongIds.length} questions in your notebook`], ['/mocks', Target, 'Make practice count', 'Build a timed or untimed mock'], ['/bookmarks', BookOpen, 'Keep the good discoveries', `${state.bookmarks.length} saved for later`]].map(([url, Icon, title, detail]) => { const ItemIcon = Icon as typeof Bookmark; return <Link to={url as string} key={url as string}><ItemIcon size={22} /><div><h3>{title as string}</h3><p>{detail as string}</p></div><ChevronRight size={17} /></Link>; })}</div><Link to="/challenge" className="challenge-card"><span className="chip"><Trophy size={14} /> THE CROREPATI CHALLENGE</span><h3>15 stages.<br />One curious mind.</h3><p>A fresh challenge. Virtual points.<br />How far can you go?</p><span className="text-link">Take the challenge<ArrowRight size={17} /></span><Trophy className="trophy-art" size={88} strokeWidth={1} /></Link><div className="honesty-note"><ShieldCheck size={19} /><p><strong>Knowledge you can trace.</strong><br />{catalog.counts.questions} verified questions in this checkpoint. Sources are linked to every answer. Video lessons are in preparation.</p></div></aside></div>
    <div className="explore-links"><Link to="/current-affairs">Current affairs<ArrowRight size={16} /></Link><Link to="/pyq">Previous year questions<ArrowRight size={16} /></Link><Link to="/downloads">Learn offline<Download size={16} /></Link></div>
  </>;
}
function LightbulbIcon() { return <LayoutGrid size={20} strokeWidth={1.5} />; }
