# JANMITRA - Frontend UI Component Architecture Guide

> **Civic Issue Management & Municipal Governance Platform**  
> **Document:** `UI_COMPONENT_GUIDE.md`  
> **Target Version:** 1.0.0 (Production Release)  
> **Framework:** React 19 + Vite 6 + TailwindCSS / Custom Design Tokens

---

## 1. Architectural Overview & Design System

The JANMITRA user interface is built on a modular, component-driven design system optimized for high accessibility (WCAG 2.1 AA), responsive mobile-first field operations, and real-time civic governance telemetry.

### Core Design Tokens

| Token | Hex Value | Semantic Usage |
|---|---|---|
| `primary` | `#0d2a53` | Municipal Deep Navy — institutional headers, primary buttons, brand logos |
| `primary-light` | `#173e73` | Elevated cards, secondary navigation tabs, active state rings |
| `pwd-blue` | `#2563eb` | Public Works Department (Roads, Potholes, Footpaths, Paver Blocks) |
| `swm-green` | `#16a34a` | Solid Waste Management (Garbage Heaps, Bins, Refuse, Cleanliness) |
| `phe-cyan` | `#0891b2` | Public Health Engineering (Water Supply, Drainage, Sewerage) |
| `elec-yellow` | `#eab308` | Electrical / Energy Department (Streetlights, Cables, Transformers) |
| `danger` | `#ef4444` | SLA Breach Warning, Critical Priority, Emergency Alerts |
| `warning` | `#f59e0b` | High Priority, 4h SLA Warning Horizon |
| `success` | `#10b981` | Closed / Resolved Status, Approved Work Verification |
| `background` | `#f8fafc` | Neutral slate background for high contrast under direct sunlight |

---

## 2. Global Layout & Shell Components

---

### `CitizenLayout`
- **Source Path:** [frontend/src/components/CitizenLayout.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/CitizenLayout.jsx)
- **Role:** Master wrapper for all resident-facing views (`/citizen`, `/citizen/submit`, `/citizen/complaints`, `/citizen/profile`, `/citizen/help`).
- **Key Features:**
  - **Sticky Top Bar:** Displays JANMITRA monogram, role badge (`Citizen`), assigned ward badge, and quick logout.
  - **Mobile Bottom Navigation Bar:** Fixed bottom ribbon on `< 768px` screens with 5 touch tabs:
    1. *Home* (`/citizen`)
    2. *Report Issue* (`/citizen/submit` — highlighted primary circle action)
    3. *Complaints* (`/citizen/complaints`)
    4. *Help* (`/citizen/help`)
    5. *Profile* (`/citizen/profile`)
  - **Safe Area Insets:** Employs `pb-24` on main content area to prevent mobile bottom navigation from occluding content.
- **Props:**
  - `children` (*ReactNode*): View content.
  - `activeTab` (*String*): Explicitly set active tab identifier (`'home' | 'report' | 'status' | 'help' | 'profile'`).

---

### `WorkerLayout`
- **Source Path:** [frontend/src/components/WorkerLayout.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/WorkerLayout.jsx)
- **Role:** High-contrast mobile interface for ground maintenance personnel.
- **Key Features:**
  - Top header displaying worker on-duty badge, assigned ward, and quick task summary counter.
  - Bottom navigation bar switching between *Active Tasks*, *Route Map*, *Completed Tasks*, and *Profile*.
  - Large 48px touch targets for gloved or outdoor operation.

---

### `OfficerSidebarDrawer`
- **Source Path:** [frontend/src/components/OfficerSidebarDrawer.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/OfficerSidebarDrawer.jsx)
- **Role:** Collapsible desktop sidebar and mobile slide-out drawer for Department Nodal Officers.
- **Navigation Links:**
  - *Dashboard* (`/officer`)
  - *Validation Queue* (`/officer/validation`)
  - *Worker Roster* (`/officer/workers`)
  - *Settings* (`/officer/settings`)

---

### `PWAInstallBanner`
- **Source Path:** [frontend/src/components/PWAInstallBanner.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/PWAInstallBanner.jsx)
- **Role:** Automatic PWA install prompt handler and modal banner.
- **Key Features:**
  - Intercepts browser `beforeinstallprompt` event and defers trigger until user clicks *"Install App"*.
  - Detects if running in `standalone` mode and self-terminates rendering.
  - Contains platform-specific iOS Safari guide ("Tap Share ⎙ $\rightarrow$ Add to Home Screen ➕").
  - Remembers user dismissal for 24 hours via `localStorage`.

---

## 3. Civic Geospatial & Mapping Components

---

### `LeafletMap`
- **Source Path:** [frontend/src/components/LeafletMap.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/LeafletMap.jsx)
- **Role:** Interactive OpenStreetMap GIS locator for issue submission and spatial verification.
- **Props:**
  - `latitude` (*Number*): Center and marker latitude (default: `28.6139` or Nagpur coordinates `21.1458`).
  - `longitude` (*Number*): Center and marker longitude.
  - `category` (*String*): Department category used to dynamically color the SVG marker pin (`'PWD' | 'SWM' | 'PHE' | 'ELECTRICAL'`).
  - `interactive` (*Boolean*): When `true`, user can click or drag marker to update location coordinates.
  - `onLocationSelect` (*Function*): Callback receiving `{ lat, lng }` upon pin repositioning.
- **Key Technical Details:**
  - Uses `mapIcons.js` custom SVG marker pins with high-contrast shadows.
  - Touch-optimized smooth pinch-to-zoom and double-tap zoom for mobile devices.

---

### `WorkerRouteMap`
- **Source Path:** [frontend/src/components/WorkerRouteMap.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/WorkerRouteMap.jsx)
- **Role:** Renders all assigned tasks on a single map view for route planning.
- **Key Features:**
  - Auto-fits bounding box (`map.fitBounds`) to encapsulate all task coordinates within the viewport.
  - Color-codes markers by SLA urgency (Red for Critical, Yellow for Medium).
  - Tapping a pin opens a popup with task title, address, and direct *"Navigate"* link.

---

## 4. Civic Badges & Status Indicators

---

### `CategoryBadge`
- **Source Path:** [frontend/src/components/CategoryBadge.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/CategoryBadge.jsx)
- **Props:**
  - `category` (*String*): Department name or code.
  - `size` (*String*): `'sm' | 'md' | 'lg'`.
- **Styling Rules:**
  - `PWD`: `bg-blue-50 text-blue-700 border-blue-200`
  - `SWM`: `bg-emerald-50 text-emerald-700 border-emerald-200`
  - `PHE`: `bg-cyan-50 text-cyan-700 border-cyan-200`
  - `ELECTRICAL`: `bg-amber-50 text-amber-700 border-amber-200`

---

### `PriorityBadge`
- **Source Path:** [frontend/src/components/PriorityBadge.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/PriorityBadge.jsx)
- **Props:**
  - `priority` (*String*): `'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'`.
- **Visual Presentation:**
  - `CRITICAL`: Pulsing red dot with `bg-red-50 text-red-700 border-red-200`.
  - `HIGH`: Amber indicator with `bg-orange-50 text-orange-700 border-orange-200`.
  - `MEDIUM`: Yellow indicator with `bg-amber-50 text-amber-700 border-amber-200`.
  - `LOW`: Muted green indicator with `bg-slate-100 text-slate-700 border-slate-200`.

---

### `StatusBadge`
- **Source Path:** [frontend/src/components/StatusBadge.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/StatusBadge.jsx)
- **6-Step Lifecycle Statuses Supported:**
  - `SUBMITTED`: 📝 Blue Pill
  - `VALIDATED`: 🤖 Cyan Pill
  - `ASSIGNED`: 👤 Indigo Pill
  - `IN_PROGRESS`: 🚧 Amber Pill (with pulsing gear animation)
  - `WORK_DONE`: 📸 Purple Pill (awaiting citizen approval)
  - `CLOSED`: ✅ Emerald Green Pill

---

### `WardBadge`
- **Source Path:** [frontend/src/components/WardBadge.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/WardBadge.jsx)
- **Props:** `ward` (*Number | String*).
- **Renders:** Compact municipal ward identifier badge (e.g., `Ward 14`).

---

## 5. Operations & Triage Components

---

### `HighPriorityQueue`
- **Source Path:** [frontend/src/components/HighPriorityQueue.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/HighPriorityQueue.jsx)
- **Role:** Officer console component showing complaints approaching SLA breach.
- **Key Features:**
  - Live countdown timers (e.g., `3h 42m remaining`).
  - Red flashing border when `< 2 hours` remain.
  - Instant worker reassignment button.

---

### `KPICard`
- **Source Path:** [frontend/src/components/KPICard.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/KPICard.jsx)
- **Props:**
  - `title` (*String*): Metric title (e.g. *Total Complaints*).
  - `value` (*Number | String*): Metric value (e.g. *1,248*).
  - `change` (*String*): Growth or reduction percentage (e.g. *+12% vs last week*).
  - `icon` (*ReactNode*): SVG or Lucide icon.
  - `color` (*String*): Accent highlight color.

---

### `ImageUploader`
- **Source Path:** [frontend/src/components/ImageUploader.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/ImageUploader.jsx)
- **Role:** Mobile camera-triggered evidence capture widget.
- **Key Features:**
  - Forces camera capture via `capture="environment"`.
  - Client-side image compression and thumbnail preview.
  - File size validation (< 5 MB) and format verification.

---

## 6. Feedback & Accessibility Components

---

### `ErrorBoundary`
- **Source Path:** [frontend/src/components/ErrorBoundary.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/ErrorBoundary.jsx)
- **Role:** Catch-all React class boundary preventing white-screen crashes.
- **Renders:** Clean municipal error view with *"Reload Portal"* and *"Return to Login"* recovery buttons.

---

### `LoadingSpinner` & `LoadingSkeleton`
- **Source Paths:**
  - [frontend/src/components/LoadingSpinner.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/LoadingSpinner.jsx)
  - [frontend/src/components/LoadingSkeleton.jsx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/frontend/src/components/LoadingSkeleton.jsx)
- **Role:** Smooth suspense state placeholders with animated shimmer effects matching card aspect ratios.

---

## 7. Performance & Code Splitting Map

All heavy administrative and citizen modules are dynamically imported using `React.lazy()` to maintain an ultra-light initial bundle:

```javascript
// Dynamic Chunks:
const CrossDeptDashboard = React.lazy(() => import('./pages/admin/CrossDeptDashboard'));
const OfficerDashboard   = React.lazy(() => import('./pages/officer/Dashboard'));
const MyComplaints       = React.lazy(() => import('./pages/citizen/MyComplaints'));
const ComplaintsLedger   = React.lazy(() => import('./pages/admin/ComplaintsLedger'));
const WorkerManagement   = React.lazy(() => import('./pages/admin/WorkerManagement'));
const ValidationQueue    = React.lazy(() => import('./pages/officer/ValidationQueue'));
const TaskList           = React.lazy(() => import('./pages/worker/TaskList'));
const SubmitForm         = React.lazy(() => import('./pages/citizen/SubmitForm'));
const ComplaintDetail    = React.lazy(() => import('./pages/citizen/ComplaintDetail'));
const HealthCheck        = React.lazy(() => import('./pages/HealthCheck'));
```

---

*Component architecture documented for JANMITRA frontend release v1.0.0.*
