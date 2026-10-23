import { createHash } from 'node:crypto';
import { readdir, readFile, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve('dist');
async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  return (await Promise.all(entries.map(async entry => {
    const full = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(full) : [full];
  }))).flat();
}
const files = (await walk(root)).filter(file => !file.endsWith('/sw.js') && !file.endsWith('sw.js'));
const relative = files.map(file => `/${path.relative(root, file).split(path.sep).join('/')}`);
const core = relative.filter(url => url === '/index.html' || url === '/manifest.webmanifest' || url.startsWith('/assets/') || url.startsWith('/icons/') || ['/data/catalog.json', '/data/starter.json', '/data/exams.json', '/data/current-news.json'].includes(url));
const signature = createHash('sha256');
for (const file of files.sort()) { signature.update(path.relative(root, file)); signature.update(await readFile(file)); }
const cacheName = `crorepati-${signature.digest('hex').slice(0, 16)}`;
const script = `const CACHE=${JSON.stringify(cacheName)};\nconst PRECACHE=${JSON.stringify([...new Set(['/', ...core])])};\nself.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(PRECACHE)).then(()=>self.skipWaiting())));\nself.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim())));\nself.addEventListener('message',event=>{if(event.data?.type==='SKIP_WAITING')self.skipWaiting()});\nself.addEventListener('fetch',event=>{if(event.request.method!=='GET')return;const url=new URL(event.request.url);if(url.origin!==self.location.origin)return;if(event.request.mode==='navigate'){event.respondWith(fetch(event.request).then(response=>{const copy=response.clone();caches.open(CACHE).then(cache=>cache.put('/index.html',copy));return response}).catch(()=>caches.match('/index.html')));return}event.respondWith(caches.match(event.request).then(cached=>cached||fetch(event.request).then(response=>{if(response.ok){const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy))}return response}))) });\n`;
await writeFile(path.join(root, 'sw.js'), script);
const total = (await Promise.all(files.map(file => stat(file)))).reduce((sum, info) => sum + info.size, 0);
console.log(`Service worker ${cacheName}: ${core.length + 1} precached URLs; build ${total.toLocaleString()} bytes.`);
