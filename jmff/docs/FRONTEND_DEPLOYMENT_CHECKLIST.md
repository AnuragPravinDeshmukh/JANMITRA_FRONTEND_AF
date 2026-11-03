# JANMITRA Frontend — Render Static Site Deployment Checklist

This checklist provides end-to-end instructions for deploying the **JANMITRA (Municipal Civic Portal)** React + Vite frontend as a **Render Static Site**.

---

## 1. Quick Service Specifications (Render Dashboard)

| Configuration Field | Target Production Value | Notes |
| :--- | :--- | :--- |
| **Service Type** | **Static Site** | Zero server maintenance, free global CDN & SSL |
| **Name** | `janmitra-frontend` *(or `resolveit-frontend`)* | Unique name on Render |
| **Repository** | Connected GitHub repository | Automatic Git push deployments |
| **Branch** | `main` | Production deployment branch |
| **Root Directory** | `frontend` | Set to `frontend` if repo has root subfolder |
| **Build Command** | `npm install && npm run build` | Installs dependencies & runs Vite production build |
| **Publish Directory** | `dist` | Generated production artifact folder |
| **Auto-Deploy** | `Yes` | Continuous deployment on git commit/push |

---

## 2. Environment Variables Configuration

Set this variable under **Render Dashboard → Environment** tab:

| Variable Key | Value | Description |
| :--- | :--- | :--- |
| `VITE_API_URL` | `https://resolveit-backend.onrender.com` | Production REST API Gateway endpoint |
| `VITE_API_BASE_URL` | `https://resolveit-backend.onrender.com` | Fallback alias supported in Axios client |

> [!NOTE]
> Vite embeds `import.meta.env.VITE_*` variables into client-side JavaScript bundles at **build time**. If you change this environment variable on Render, trigger a **Manual Deploy → Clear build cache & deploy**.

---

## 3. SPA Routing & Redirects Configuration

Single Page Applications require all non-asset requests to route through `/index.html` so React Router can resolve nested dynamic URLs (`/admin/workers`, `/citizen/complaint/CMP-20481`, `/officer/validation`).

### Method A: Automated `_redirects` file (Active)
The file [`public/_redirects`](./frontend/public/_redirects) is included in the build and copied to `dist/_redirects`:
```text
/* /index.html 200
```

### Method B: Render Dashboard "Redirects/Rewrites" (Recommended Safety Net)
In the Render dashboard for your static site:
1. Navigate to **Redirects / Rewrites**.
2. Click **Add Rule**:
   - **Type**: `Rewrite`
   - **Source**: `/*`
   - **Destination**: `/index.html`
3. Click **Save Changes**.

---

## 4. Pre-Flight Verification Checklist

Before triggering production deployment, verify these locally:

- [x] **Local Build Succeeded**:
  ```bash
  npm run build
  ```
- [x] **Optimized Code Splitting Chunks Generated**:
  - `dist/assets/js/index-*.js` (~183 kB)
  - `dist/assets/js/vendor-react-*.js` (~247 kB)
  - `dist/assets/js/vendor-charts-*.js` (~416 kB)
  - `dist/assets/js/vendor-leaflet-*.js` (~153 kB)
  - `dist/assets/js/CrossDeptDashboard-*.js` (~40 kB)
  - `dist/assets/js/Dashboard-*.js` (~62 kB)
  - `dist/assets/js/MyComplaints-*.js` (~6 kB)
- [x] **`_redirects` file exists in `dist/`**:
  ```bash
  cat dist/_redirects
  # Must output: /* /index.html 200
  ```
- [x] **Axios API Client Configured**:
  [`frontend/src/api/client.js`](./frontend/src/api/client.js) respects `VITE_API_URL` and strips trailing slashes.
- [x] **Nested Route Fallbacks**: Direct page refreshes on `/admin/workers`, `/citizen/complaint/123`, and `/worker` resolve cleanly without 404s.

---

## 5. Step-by-Step Render Deployment Guide

### Step 1: Connect GitHub to Render
1. Log in to [dashboard.render.com](https://dashboard.render.com/).
2. Click **New +** in the top navigation bar and select **Static Site**.
3. Choose your GitHub repository (`Frontend Lead (Officer & Worker Portals)` or `JANMITRA`).
4. Click **Connect**.

### Step 2: Configure Service Settings
Fill in the deployment parameters:
- **Name**: `janmitra-frontend`
- **Branch**: `main`
- **Root Directory**: `frontend` *(if root folder contains `frontend/`)*
- **Build Command**: `npm install && npm run build`
- **Publish Directory**: `dist`

### Step 3: Add Environment Variables
1. Scroll down to **Environment Variables**.
2. Click **Add Environment Variable**:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://resolveit-backend.onrender.com`
3. Click **Create Static Site**.

### Step 4: Monitor Build Logs
Watch Render's live deployment terminal:
```text
==> Cloning from https://github.com/...
==> Running build command 'npm install && npm run build'...
==> vite build
✓ 739 modules transformed.
✓ built in ~4s
==> Uploading build...
==> Build successful 🎉
==> Deploying...
==> Site is live at https://janmitra-frontend.onrender.com
```

---

## 6. Post-Deployment Smoke Test Suite

Once the site is live, perform these verification checks on the live URL:

1. **Authentication Flow**:
   - [ ] Visit `/login`
   - [ ] Log in as **Citizen**, **Worker**, **Department Officer**, and **Admin**
2. **Citizen Portal**:
   - [ ] Visit `/citizen/submit` — check category selection and GPS pin placement
   - [ ] Visit `/citizen/complaints` — verify complaint list loads via `MyComplaints` lazy chunk
   - [ ] Visit `/citizen/complaint/CMP-20481` directly in address bar — verify no 404 and category SVG map marker renders
3. **Worker Portal**:
   - [ ] Visit `/worker` — verify **Card View** and **Route View** toggle
   - [ ] Toggle **Route View** — verify auto-fit bounds on assigned tasks with category SVG markers (Blue PWD, Green SWM, Cyan PHE, Yellow Electrical)
4. **Officer & Admin Dashboards**:
   - [ ] Visit `/officer` — check OfficerDashboard KPI widgets
   - [ ] Visit `/admin/reports` — verify CrossDeptDashboard heatmap and Recharts graph
   - [ ] Visit `/admin/workers` — verify worker roster and management view
5. **Hard Refresh Verification**:
   - [ ] Press `Ctrl + F5` (or `Cmd + Shift + R`) on any nested route (`/admin/complaints`, `/officer/validation`, `/citizen/help`)
   - [ ] Confirm page renders correctly without HTTP 404 or white screen
