# JANMITRA – Frontend Lead Contribution (`jmff`)

**Contributor:** Om Gadekar  
**Role:** Frontend Lead (Officer & Worker Portals)  
**Reference Specification:** `11_Day_by_Day_Prompts_JANMITRA.pdf` (Days 01–40)  
**Project:** JANMITRA – Civic Issue Reporting & Management System for Nagpur Municipal Corporation (NMC)

---

## 1. Overview & Scope

This directory (`jmff`) contains only the completed, verified frontend code and documentation matching the individual tasks assigned specifically to **Om Gadekar (Frontend Lead: Officer & Worker Portals)** in the master 40-day specification document (`11_Day_by_Day_Prompts_JANMITRA.pdf`).

> [!IMPORTANT]
> **Selected Contribution Archive, Not a Standalone Application**  
> This folder is a modular extraction of individual frontend deliverables prepared for review and integration into the team's central repository. It is **not** a standalone runnable application. Core global configuration files, backend services, AI models, and modules belonging exclusively to other team members (Citizen Portal by Faizan Rayeen, AI pipeline by Anurag Deshmukh, Backend Infrastructure by Anas Shaikh) have been intentionally omitted or flagged for integration.

---

## 2. Included Modules & Deliverables

### A. Municipal Department Officer Dashboard & Workflows
* **`src/pages/officer/Dashboard.jsx`** (Days 07, 17): Primary departmental command center with KPI summary cards, Recharts civic category distribution, ward issue density meters, and SLA filters.
* **`src/pages/officer/ValidationQueue.jsx`** (Days 08, 16): Manual review queue for edge cases flagged by AI (confidence < 50%) with side-by-side photo inspection and Approve/Reject controls.
* **`src/pages/officer/WorkerRoster.jsx`** (Day 25): Departmental worker availability roster, workload distribution meters (Green/Amber/Red), and direct task reassignment.
* **`src/pages/officer/HighPriorityQueue.jsx` & `HighPriorityList.jsx`** (Days 08, 18): Critical/High incident triage table with SLA countdown risk indicators and quick worker assignment modal.
* **`src/pages/officer/AssignWorker.jsx`** (Day 08): Dept + Ward matching worker dispatch modal with admin override logic.
* **`src/pages/officer/ComplaintDetailModal.jsx`** (Day 08): Reusable modal with full complaint metadata, citizen description, status timeline, and GPS map.
* **`src/pages/officer/OfficerSettings.jsx`** (Day 28): Departmental notification preferences, SLA threshold view, and shift parameters.

### B. Field Worker Mobile Portal & Offline Operations
* **`src/pages/worker/TaskList.jsx`** (Days 05, 11, 19): Mobile-first task list with priority borders (Critical/High/Med/Low), status filters (Assigned, In-Progress, Completed), pull-to-refresh, and offline cached task feed.
* **`src/pages/worker/TaskDetail.jsx`** (Days 06, 12, 13): Detailed task execution interface with OpenStreetMap directions, "Start Work" status transition, and Proof-of-Work photo upload modal with repair remarks.
* **`src/pages/worker/CompletedTasks.jsx`** (Day 14): Historical task archive with before/after photo comparison and search.
* **`src/pages/worker/Profile.jsx`** (Day 15): Worker profile, NMC employee badge, ward assignment, shift toggle ("Active On-Duty" vs "On Leave"), and turnaround stats.
* **`src/layouts/WorkerLayout.jsx`** (Day 11): Mobile-first bottom tab navigation layout (`Tasks`, `Completed`, `Profile`) with active tab highlights.

### C. Super Admin & Cross-Department Management
* **`src/pages/admin/WorkerManagement.jsx`** (Days 21, 22): Central administrative worker management table with search, dept/ward filters, active tasks badge, and edit/toggle deactivation modals.
* **`src/pages/admin/CrossDeptDashboard.jsx`** (Days 23, 24): Super Admin inter-agency coordination dashboard with department switcher tabs, 4 cross-dept KPI cards, Recharts volume bar chart, and 4x4 Ward Heatmap matrix.
* **`src/pages/admin/ComplaintsLedger.jsx`** (Day 26): Central municipal database ledger with search by complaint ID, citizen phone, category, and audit stepper modal.
* **`src/pages/admin/SystemSettings.jsx`** (Day 27): Municipal SLA configurations (Critical 24h, High 48h, Medium 72h, Auto-close 72h) and civic emergency broadcast editor.
* **`src/pages/admin/AdminPanel.jsx`** (Days 01, 10, 28): Admin landing panel routing and summary cards.

### D. Shared Reusable UI Components
* **`src/components/StatusBadge.jsx`** (Day 02): Coloured pill for all 8 lifecycle statuses (Submitted, Validated, Routed, Assigned, In-Progress, Work Done, Closed, Rejected).
* **`src/components/PriorityBadge.jsx`** (Day 02): Priority indicators with pulsing red animation for Critical SLA issues.
* **`src/components/CategoryBadge.jsx`** (Day 02): Visual emoji icons and colors for Roads (PWD), Waste (SWM), Water (PHE), and Lighting (ELEC).
* **`src/components/WardBadge.jsx`** (Day 02): Dark blue ward identifier tag (Ward 1–4).
* **`src/components/KPICard.jsx`** (Day 02): Dashboard summary card with metric value, subtitle, and color accents.
* **`src/components/LoadingSpinner.jsx` & `LoadingSkeleton.jsx`** (Days 02, 20): Accessible loading states and data grid skeletons.
* **`src/components/ErrorMessage.jsx`** (Day 02): Error display banner with retry button.
* **`src/components/LeafletMap.jsx`** (Days 03, 30): OpenStreetMap Leaflet component supporting both location picking and read-only GPS display.
* **`src/components/ImageUploader.jsx`** (Day 03): Multi-image upload component with client-side verification state handling.
* **`src/components/OfficerSidebarDrawer.jsx`** (Day 20): Responsive drawer navigation for municipal department officers.
* **`src/components/WorkerRegistrationForm.jsx`** (Day 22): Modal form for onboarding municipal field workers.
* **`src/components/WorkerRouteMap.jsx`** (Day 30): Interactive multi-stop route map showing assigned task pins with category color-coding.
* **`src/components/ErrorBoundary.jsx`** (Day 29): Global React error boundary component with friendly fallback UI.
* **`src/components/PWAInstallBanner.jsx`** (Day 40): Install banner prompting mobile workers to install the PWA on phone home screens.

### E. Utilities & State Helpers
* **`src/utils/chartHelpers.js`** (Day 10): Label formatters, status colors, ward names, and human-friendly date formatters.
* **`src/utils/errorHandler.js`** (Day 09): Django REST Framework error serializer parser converting API error payloads into user-friendly messages.
* **`src/utils/mapIcons.js`** (Day 30): Custom Leaflet SVG marker pin generators with civic category styling and worker GPS pins.
* **`src/utils/offlineStorage.js`** (Day 19): Offline caching and background synchronization engine for field workers.
* **`src/utils/complaintStore.js`**: Supporting offline-resilient store and local mock fallback for continuous operational capability.

### F. Diagnostics & PWA Public Assets
* **`src/pages/HealthCheck.jsx`** (Day 34): System diagnostics page inspecting API baseURL, backend health ping, service worker status, and session state.
* **`public/manifest.json`** (Day 36): Web App Manifest defining home-screen installability for Nagpur municipal workers.
* **`public/_redirects`** (Day 32): Single-page application route rewrite rule for static hosting deployments.
* **`public/icons/` & favicons** (Day 36): PWA icons (192px, 512px), SVG icons, and touch icons.

### G. Documentation & Presentations (`docs/`)
* **`docs/frontend_test_plan.md`** (Day 09): End-to-end frontend manual testing scripts and setup troubleshooting matrix.
* **`docs/FRONTEND_DEPLOYMENT_CHECKLIST.md`** (Day 33): Static hosting deployment verification guide.
* **`docs/FRONTEND_SMOKE_TEST_REPORT.md`** (Day 35): Production smoke testing audit across all 4 municipal portals.
* **`docs/UI_SCREENSHOTS_CATALOG.md` & `docs/screenshots/`** (Day 37): 12-screen presentation-quality screenshot catalog with annotations and device mockups.
* **`docs/SEMINAR_PRESENTATION_OUTLINE.md`** (Day 38): Comprehensive academic seminar outline for project defense.
* **`docs/generate_presentation.py` & `docs/JANMITRA_Seminar_Presentation.pptx`** (Day 38): 12-slide automated PowerPoint deck generation script and generated PPTX presentation.
* **`docs/LIVE_DEMO_TIMED_SCRIPT.md`** (Day 39): Minute-by-minute 10-minute presentation and live demo script.
* **`docs/UI_COMPONENT_GUIDE.md`** (Day 40): Design token reference and component inventory.
* **`docs/FRONTEND_HANDOVER_DOCUMENTATION.md`** (Day 40): Engineering handover architecture and state management documentation.

---

## 3. Directory Layout

```text
jmff/
│
├── README.md
├── FILE_MAPPING.md
│
├── src/
│   ├── components/
│   │   ├── CategoryBadge.jsx
│   │   ├── ErrorBoundary.jsx
│   │   ├── ErrorMessage.jsx
│   │   ├── HighPriorityQueue.jsx
│   │   ├── ImageUploader.jsx
│   │   ├── index.js
│   │   ├── KPICard.jsx
│   │   ├── LeafletMap.jsx
│   │   ├── LoadingSkeleton.jsx
│   │   ├── LoadingSpinner.jsx
│   │   ├── OfficerSidebarDrawer.jsx
│   │   ├── PriorityBadge.jsx
│   │   ├── PWAInstallBanner.jsx
│   │   ├── StatusBadge.jsx
│   │   ├── WardBadge.jsx
│   │   ├── WorkerRegistrationForm.jsx
│   │   └── WorkerRouteMap.jsx
│   ├── layouts/
│   │   └── WorkerLayout.jsx
│   ├── pages/
│   │   ├── admin/
│   │   │   ├── AdminPanel.jsx
│   │   │   ├── ComplaintsLedger.jsx
│   │   │   ├── CrossDeptDashboard.jsx
│   │   │   ├── SystemSettings.jsx
│   │   │   └── WorkerManagement.jsx
│   │   ├── officer/
│   │   │   ├── AssignWorker.jsx
│   │   │   ├── ComplaintDetailModal.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── HighPriorityList.jsx
│   │   │   ├── HighPriorityQueue.jsx
│   │   │   ├── OfficerSettings.jsx
│   │   │   ├── ValidationQueue.jsx
│   │   └── worker/
│   │       ├── CompletedTasks.jsx
│   │       ├── Profile.jsx
│   │       ├── TaskDetail.jsx
│   │       ├── TaskList.jsx
│   │       └── WorkerLayout.jsx
│   │   └── HealthCheck.jsx
│   └── utils/
│       ├── chartHelpers.js
│       ├── complaintStore.js
│       ├── errorHandler.js
│       ├── mapIcons.js
│       └── offlineStorage.js
│
├── public/
│   ├── _redirects
│   ├── apple-touch-icon.png
│   ├── favicon.svg
│   ├── icon-192x192.png
│   ├── icon-512x512.png
│   ├── icons.svg
│   └── manifest.json
│
└── docs/
    ├── frontend_test_plan.md
    ├── FRONTEND_DEPLOYMENT_CHECKLIST.md
    ├── FRONTEND_HANDOVER_DOCUMENTATION.md
    ├── FRONTEND_SMOKE_TEST_REPORT.md
    ├── generate_presentation.py
    ├── JANMITRA_Seminar_Presentation.pptx
    ├── LIVE_DEMO_TIMED_SCRIPT.md
    ├── SEMINAR_PRESENTATION_OUTLINE.md
    ├── UI_COMPONENT_GUIDE.md
    ├── UI_SCREENSHOTS_CATALOG.md
    └── screenshots/
```

---

## 4. Integration Notes for Team Merge

To integrate these files into the final team repository (`JANMITRA_FINAL`):
1. Copy the pages, layouts, components, and utils into `frontend/src/`.
2. Keep the team's shared `App.jsx`, `AuthContext.jsx`, `api/client.js`, and `package.json`, ensuring the routes detailed in `FILE_MAPPING.md` are mounted into the root router.
3. Consult `FILE_MAPPING.md` for complete cross-reference information.

