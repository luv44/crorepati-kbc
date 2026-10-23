# Deployment state

Updated: **23 October 2026 (Asia/Calcutta)**

- Local production build: **PASS** (`npm run build`).
- Production-bundle browser scenarios: **PASS, 9/9** across Chromium desktop/mobile/tablet viewports.
- Current sandbox production preview: `0.0.0.0:4173` (available through Arena's live preview while this workspace is running).
- Public HTTPS deployment: **NOT DEPLOYED**.
- Production URL: **NONE**.
- Hosting project/account: not supplied or authorized.
- Production deploy configuration, backend/admin authorization, and live-host QA remain pending.
- `FINAL_ELIGIBLE=false` because strict focused/source-complete content gates remain open.

For a local preview use:

```bash
npm run preview -- --host 0.0.0.0 --port 4173
```

A localhost or sandbox preview is not a public production deployment. See `README.md` and `BUILD_STATE.md` for verification and resume commands.
