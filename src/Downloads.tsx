import { useEffect, useRef, useState } from 'react';
import { CheckCircle2, Download, HardDrive, Pause, Trash2 } from 'lucide-react';
import { useStore } from './context';
import { PageHeading } from './components';
import { deletePack, downloadPack, downloadedPacks } from './storage';
import type { PackMeta } from './types';

export default function Downloads() {
  const { catalog, refreshPacks, toast } = useStore();
  const [installed, setInstalled] = useState<Record<string, string>>({});
  const [progress, setProgress] = useState<Record<string, number>>({});
  const [status, setStatus] = useState<Record<string, string>>({});
  const [usage, setUsage] = useState<StorageEstimate>();
  const [subject, setSubject] = useState('all');
  const controllers = useRef<Record<string, AbortController>>({});
  const refresh = async () => { setInstalled(Object.fromEntries((await downloadedPacks()).map(p => [p.id, p.sha256]))); setUsage(await navigator.storage?.estimate()); await refreshPacks(); };
  useEffect(() => { refresh().catch(e => toast(e.message)); return () => Object.values(controllers.current).forEach(c => c.abort()); }, []);
  async function install(meta: PackMeta) {
    const controller = new AbortController(); controllers.current[meta.id] = controller; setStatus(s => ({ ...s, [meta.id]: 'Downloading' }));
    try { await downloadPack(meta, controller.signal, n => setProgress(s => ({ ...s, [meta.id]: n }))); setStatus(s => ({ ...s, [meta.id]: 'Integrity checked · available offline' })); await refresh(); }
    catch (e) { const error = e as Error; setStatus(s => ({ ...s, [meta.id]: error.name === 'AbortError' ? 'Paused. Resume when ready.' : error.message })); }
    finally { delete controllers.current[meta.id]; }
  }
  return <><PageHeading eyebrow="YOUR LIBRARY, WHEREVER YOU GO" title="Take knowledge with you.">Download only what you need. Question packs are hash-checked before they’re saved.</PageHeading><div className="storage-card card"><HardDrive size={30} /><div><h2>{usage ? `${((usage.usage || 0) / 1048576).toFixed(1)} MB used by this app` : 'Browser storage'}</h2><p>{usage?.quota ? `${Math.round(usage.quota / 1048576).toLocaleString()} MB estimated browser quota. ` : ''}Browser storage may be cleared by the device; export your progress in Settings.</p></div><button className="secondary" onClick={() => navigator.storage?.persist?.().then(ok => toast(ok ? 'Persistent storage granted.' : 'Your browser did not grant persistent storage. Export important progress.')).catch(e => toast(e.message))}>Keep downloads</button></div><div className="download-intro"><h2>Verified question packs</h2><label>Filter subject<select value={subject} onChange={e => setSubject(e.target.value)}><option value="all">All subjects</option>{catalog.subjects.filter(s => s.questionCount).map(s => <option key={s.id} value={s.id}>{s.shortTitle}</option>)}</select></label></div><div className="pack-list">{catalog.packs.filter(p => subject === 'all' || p.subjectId === subject).map(p => { const active = !!controllers.current[p.id]; const ready = installed[p.id] === p.sha256; return <section className="card pack-card" key={p.id}><div className="stat-icon mint">{ready ? <CheckCircle2 /> : <Download />}</div><div className="pack-info"><h3>{p.title}</h3><p>{p.questionCount} questions · {(p.size / 1024).toFixed(1)} KB · {p.chapterId ? 'Chapter pack' : 'Subject pack'}</p><p className="small muted" role="status">{status[p.id] || (ready ? 'Integrity checked · available offline' : installed[p.id] ? 'An updated version is available' : 'Ready to download')}</p>{active && <progress aria-label={`${p.title} download progress`} value={progress[p.id] || 0} max={100} />}</div><div className="actions">{active ? <button className="secondary" onClick={() => controllers.current[p.id]?.abort()}><Pause size={16} />Pause</button> : !ready && <button className="secondary" onClick={() => install(p)}><Download size={16} />{status[p.id] ? 'Resume / retry' : 'Download'}</button>}{installed[p.id] && <button className="icon-button" aria-label={`Delete ${p.title}`} onClick={() => deletePack(p.id).then(refresh).then(() => setStatus(s => ({ ...s, [p.id]: 'Removed from this device' }))).catch(e => toast(e.message))}><Trash2 size={19} /></button>}</div></section>; })}</div><section className="card topic-section"><h2>Selected video downloads</h2><p>When an approved video is available, its topic page offers an individual offline download. No video library is downloaded automatically. This checkpoint has 0 approved videos.</p><p className="small muted">The small starter pack and app shell are cached on first visit. Downloading a pack does not change the global unique-question count. Deleting a pack preserves answer history and bookmarks.</p></section></>;
}
