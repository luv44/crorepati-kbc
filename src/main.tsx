import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from './context';
import App from './App';
import './styles.css';

ReactDOM.createRoot(document.getElementById('root')!).render(<React.StrictMode><BrowserRouter><Provider><App /></Provider></BrowserRouter></React.StrictMode>);

if ('serviceWorker' in navigator && import.meta.env.PROD) {
  window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js').then(registration => {
    const notify = () => window.dispatchEvent(new CustomEvent('pwa-update', { detail: registration }));
    if (registration.waiting) notify();
    registration.addEventListener('updatefound', () => registration.installing?.addEventListener('statechange', () => {
      if (registration.waiting && navigator.serviceWorker.controller) notify();
    }));
  }).catch(error => window.dispatchEvent(new CustomEvent('pwa-error', { detail: String(error) }))));
}
