import type { ReactNode } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, BookOpen, Bookmark, CheckCircle2, ChevronRight, Compass, Download, Globe2, Landmark, Leaf, Lightbulb, Orbit, Palette, Scale, Trophy, Zap } from 'lucide-react';
import { useStore } from './context';
import type { Localized, Subject } from './types';

export const subjectIcons = [Globe2, Zap, Landmark, Landmark, Compass, Scale, Scale, Lightbulb, Orbit, Lightbulb, Leaf, Trophy, Palette, BookOpen, BookOpen, Palette, Trophy, Bookmark, Globe2, Compass, Leaf, Trophy, BookOpen, BookOpen, Palette, Lightbulb];
export function SubjectIcon({ id, size = 24 }: { id: string; size?: number }) { const Icon = subjectIcons[(Number(id.slice(1)) - 1) % subjectIcons.length] || BookOpen; return <Icon size={size} strokeWidth={1.7} aria-hidden="true" />; }
export function useText() { const { state } = useStore(); return (value: Localized) => value[state.profile.language] || value.en; }
export function ExamSelector({ compact = false }: { compact?: boolean }) {
  const { exams, selectedExam, state, update } = useStore();
  const groups = [...new Set(exams.map(exam => exam.group))];
  const label = state.profile.language === 'hi' ? 'परीक्षा चुनें' : 'Choose exam';
  return <label className={compact ? 'exam-selector compact' : 'exam-selector'}><span>{label}</span><select aria-label={label} value={selectedExam.id} onChange={event => update(current => ({ ...current, profile: { ...current.profile, exam: event.target.value } }))}>{groups.map(group => <optgroup key={group} label={group}>{exams.filter(exam => exam.group === group).map(exam => <option key={exam.id} value={exam.id}>{state.profile.language === 'hi' ? exam.nameHindi : exam.name}{exam.legacy ? '' : ' · NEW'}</option>)}</optgroup>)}</select></label>;
}
export function PageHeading({ eyebrow, title, children, action }: { eyebrow?: string; title: string; children?: ReactNode; action?: ReactNode }) { return <header className="page-heading"><div>{eyebrow && <p className="eyebrow">{eyebrow}</p>}<h1>{title}</h1>{children && <p className="muted">{children}</p>}</div>{action}</header>; }
export function Empty({ title, children, link, label }: { title: string; children: ReactNode; link?: string; label?: string }) { return <section className="empty card"><BookOpen size={32} aria-hidden="true" /><h2>{title}</h2><p>{children}</p>{link && <Link className="button" to={link}>{label || 'Explore learning'}<ArrowRight size={17} /></Link>}</section>; }
export function SectionTitle({ title, link, label = 'View all' }: { title: string; link?: string; label?: string }) { return <div className="section-title"><h2>{title}</h2>{link && <Link className="text-link" to={link}>{label}<ArrowRight size={16} /></Link>}</div>; }
export function SubjectCard({ subject }: { subject: Subject }) { return <Link to={`/learn/${subject.id}`} className="subject-card card"><div className="subject-icon" style={{ background: subject.color }}><SubjectIcon id={subject.id} /></div><div><h3>{subject.shortTitle}</h3><p>{subject.chapters.length} chapters · {subject.chapters.reduce((n, c) => n + c.topics.length, 0)} topics</p><span className={subject.questionCount ? 'availability' : 'muted small'}>{subject.questionCount ? `${subject.questionCount} available questions` : 'Question build pending'}</span></div><ChevronRight className="card-arrow" size={18} /></Link>; }
export function SourceBadge() { return <span className="chip"><CheckCircle2 size={13} /> Source-grounded</span>; }
export function DownloadLink() { return <Link className="text-link" to="/downloads"><Download size={16} /> Download available packs</Link>; }
