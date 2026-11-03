# JANMITRA - Comprehensive UI Presentation Screenshots Catalog

> **Civic Issue Management & Municipal Governance Platform**  
> **Documentation Version:** 1.0.0  
> **Date:** October 19, 2026  
> **System Architecture:** React 19 SPA, TailwindCSS / Vanilla CSS, Leaflet OpenStreetMap, Recharts Municipal Analytics, Django REST Framework

---

## Executive Summary

**JANMITRA** (जनमित्र - *Friend of the Citizen*) is an end-to-end municipal grievance redressal and urban operations platform. Designed for high civic transparency, strict Service Level Agreement (SLA) enforcement, and transparent field worker accountability, JANMITRA connects four core stakeholders across the urban administration lifecycle:

1. **Citizens:** Rapid issue logging with GPS geo-tagging, real-time lifecycle tracking, and citizen resolution verification with 5-star ratings.
2. **Field Workers:** Priority-queued mobile task lists, turn-by-turn navigation coordinates, and mandatory photographic proof-of-work submission.
3. **Department Officers:** Real-time departmental triaging, automated and manual worker assignments, and SLA breach monitors.
4. **Super Administrators:** Cross-departmental operational heatmaps, municipal ward health scores, automated worker rosters, and central audit ledgers.

This catalog presents **12 high-resolution screenshots** captured across the production-ready portal, accompanied by comprehensive architectural and civic governance UI annotations.

---

## Screenshot Inventory Summary

| # | Screen Name | Route | Primary Persona | Key Civic Governance UI Highlight |
|---|---|---|---|---|
| **01** | [Multi-Role Login Page](#screen-01-multi-role-login-page) | `/login` | Public / All Roles | Single-click municipal persona switching, secure token auth & guest citizen onboarding |
| **02** | [Citizen Home & Quick Stats](#screen-02-citizen-home--quick-stats) | `/citizen` | Citizen | Real-time grievance counts, quick-action tiles, emergency ward helpline banner |
| **03** | [Issue Submission with Leaflet GPS Map](#screen-03-issue-submission-with-leaflet-gps-map) | `/citizen/submit` | Citizen | Pinpoint GPS map locator, category-coded pins, auto-detected ward & photo evidence upload |
| **04** | [6-Step Lifecycle Stepper](#screen-04-6-step-lifecycle-stepper) | `/citizen/complaint/:id` | Citizen / Auditor | Transparent multi-stage timeline (`Submitted` → `Validated` → `Assigned` → `In-Progress` → `Work Done` → `Closed`) |
| **05** | [Worker Task List with Priority Badges](#screen-05-worker-task-list-with-priority-badges) | `/worker` | Field Worker | SLA urgency color pills, ward location tags, status toggle filters (`Pending`, `In Progress`, `Done`) |
| **06** | [Worker Proof-of-Work Photo Upload](#screen-06-worker-proof-of-work-photo-upload) | `/worker/task/:id` | Field Worker | Geo-tagged completion photo capture, timestamped worker notes & status escalation |
| **07** | [Citizen Verification & 5-Star Rating](#screen-07-citizen-verification--5-star-rating) | `/citizen/complaint/:id` | Citizen | Citizen sign-off modal, Before vs After photographic comparison & satisfaction rating |
| **08** | [Department Officer Dashboard](#screen-08-department-officer-dashboard) | `/officer` | Dept Officer (PWD / PHE / SWM / ELEC) | High-priority escalation queue, SLA breach warning pills & instant worker assign dropdown |
| **09** | [Super Admin Cross-Dept Overview & Heatmap](#screen-09-super-admin-cross-dept-overview--heatmap) | `/admin/reports` | Municipal Commissioner / Super Admin | Ward-level grievance density heatmap, resolution velocity chart & department radar |
| **10** | [Worker Management Panel](#screen-10-worker-management-panel) | `/admin/workers` | Admin / HR / Fleet Manager | Real-time worker availability roster, active job loads, department filters & phone contact |
| **11** | [System Health Diagnostics Page](#screen-11-system-health-diagnostics-page) | `/health` | SRE / DevOps / IT Auditor | Live backend API ping, PWA service worker status, localStorage token state & latency metrics |
| **12** | [Central Complaints Ledger & Audit Log](#screen-12-central-complaints-ledger--audit-log) | `/admin/complaints` | Municipal Vigilance / Super Admin | Comprehensive chronological audit ledger, search by tracking ID, category & ward filter |

---

## Detailed Screen Presentations & Civic Annotations

---

### Screen 01: Multi-Role Login Page
- **Route:** `/login`
- **Target Persona:** Citizen, Field Worker, Department Officer, Municipal Super Administrator
- **Screenshot Asset:** [screen01_multi_role_login.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen01_multi_role_login.png)

![Screen 01: Multi-Role Login Page](./screenshots/screen01_multi_role_login.png)

#### Core Objective
Serves as the unified, highly intuitive municipal entry point for all citizens and urban governance personnel. Eliminates login friction through quick-access demonstration badges while enforcing strict role-based access control (RBAC).

#### Key Civic Governance UI Annotations
1. **Persona Quick-Switch Grid:** 4 color-coded persona badges allow seamless testing and role validation:
   - **Citizen:** Direct guest or authenticated resident access.
   - **Worker:** Field worker interface with mobile-optimized workflow.
   - **Officer:** Department-scoped managerial oversight.
   - **Super Admin:** City-wide cross-departmental command.
2. **Bilingual Brand Identity:** Displays *"JANMITRA - नगर मित्र"* emphasizing citizen-first municipal governance under digital India initiatives.
3. **Secure Token Authentication:** Backed by JWT localStorage persistence with automatic redirection to role-specific default routes (`/citizen`, `/worker`, `/officer`, `/admin`).
4. **PWA Standalone Compliance:** Full responsive layout designed for mobile viewport home screen shortcuts.

---

### Screen 02: Citizen Home & Quick Stats
- **Route:** `/citizen`
- **Target Persona:** Citizen / Resident
- **Screenshot Asset:** [screen02_citizen_home_stats.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen02_citizen_home_stats.png)

![Screen 02: Citizen Home with Quick Stats](./screenshots/screen02_citizen_home_stats.png)

#### Core Objective
Provides residents with immediate visibility into their submitted civic complaints, overall neighborhood resolution rates, and one-tap access to file new grievances.

#### Key Civic Governance UI Annotations
1. **Real-Time Grievance Telemetry:** Metric cards displaying *Total Complaints*, *In Progress*, *Resolved*, and *Pending Action* with color-coded status rings.
2. **High-Contrast Quick Action Hero:** Prominent `"Report a New Issue"` primary call-to-action button, ensuring zero navigation delay during civic emergencies.
3. **Recent Grievance Ledger:** Dynamic card list showcasing recent complaints with tracking IDs (e.g. `CMP-2026-9041`), category tags (Roads, Sanitation, Water, Streetlights), and status pills.
4. **Emergency Helpline Banner:** Quick-dial contacts for Municipal Control Room, Water Emergency, Fire, and Sanitation dispatch.

---

### Screen 03: Issue Submission with Leaflet GPS Map
- **Route:** `/citizen/submit`
- **Target Persona:** Citizen / Resident
- **Screenshot Asset:** [screen03_issue_submission_map.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen03_issue_submission_map.png)

![Screen 03: Issue Submission with Leaflet GPS Map](./screenshots/screen03_issue_submission_map.png)

#### Core Objective
Enables citizens to submit a validated civic complaint with high spatial precision, photographic proof, and automated ward categorization within under 60 seconds.

#### Key Civic Governance UI Annotations
1. **Interactive Leaflet GPS Map:** OpenStreetMap wrapper with custom high-contrast SVG marker pin. Users can drag the pin or click anywhere across the municipal boundary to set the exact incident coordinates.
2. **Auto-Geocoding & Ward Detection:** Live latitude and longitude readout (`Lat: 28.6139, Lng: 77.2090`) with automatic ward assignment (e.g., *Ward 14 - Civil Lines*).
3. **Department Taxonomy Selector:** 4 standardized civic categories with visual icons and departmental routing:
   - 🔵 **PWD (Public Works):** Potholes, damaged footpaths, road cave-ins.
   - 🟢 **SWM (Solid Waste):** Garbage overflow, uncollected refuse, illegal dumping.
   - 🔷 **PHE (Public Health Eng.):** Pipeline leaks, contaminated water, sewage overflow.
   - 🟡 **Electrical:** Faulty streetlights, open transformers, loose high-tension cables.
4. **Camera & Photo Evidence Upload:** HTML5 file input supporting live camera capture with instant thumbnail preview and size validation.

---

### Screen 04: 6-Step Lifecycle Stepper
- **Route:** `/citizen/complaint/:id`
- **Target Persona:** Citizen, Municipal Vigilance Officer
- **Screenshot Asset:** [screen04_lifecycle_stepper.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen04_lifecycle_stepper.png)

![Screen 04: 6-Step Lifecycle Stepper](./screenshots/screen04_lifecycle_stepper.png)

#### Core Objective
Demystifies municipal operations by providing complete, timestamped transparency into every stage of the grievance redressal lifecycle.

#### Key Civic Governance UI Annotations
1. **6-Stage Progressive Stepper:**
   - **Step 1: Submitted:** Grievance recorded in central municipal ledger with tracking ID.
   - **Step 2: Validated:** Automated or officer-led AI validation for duplicate prevention.
   - **Step 3: Assigned:** Field worker assigned with officer badge and mobile contact.
   - **Step 4: In-Progress:** Field worker en-route or actively executing physical repairs.
   - **Step 5: Work Done:** Field worker submitted photo proof-of-work awaiting verification.
   - **Step 6: Closed:** Citizen satisfaction verified and ticket formally archived.
2. **Visual Progress Track:** Emerald green connectors for completed stages, pulsing cyan indicator for the current active stage, and neutral slate for upcoming phases.
3. **Municipal SLA Countdown Timer:** Explicit display of estimated resolution window (e.g., *"Resolution expected within 18 hrs"*), preventing bureaucratic stagnation.

---

### Screen 05: Worker Task List with Priority Badges
- **Route:** `/worker`
- **Target Persona:** Field Worker / Maintenance Crew
- **Screenshot Asset:** [screen05_worker_task_list.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen05_worker_task_list.png)

![Screen 05: Worker Task List with Priority Badges](./screenshots/screen05_worker_task_list.png)

#### Core Objective
Provides ground-level maintenance crews with a clean, touch-friendly, mobile-first task backlog prioritized by civic severity and geographic proximity.

#### Key Civic Governance UI Annotations
1. **SLA Priority Badges:**
   - 🔴 **CRITICAL:** Imminent safety hazard (e.g., broken sewer main, exposed high-voltage wire).
   - 🟠 **HIGH:** Urgent municipal disruption (e.g., arterial road pothole).
   - 🟡 **MEDIUM:** Standard neighborhood grievance.
   - 🟢 **LOW:** Scheduled routine maintenance.
2. **Status Tab Filters:** Quick toggling between `Pending Tasks`, `In Progress (1)`, and `Resolved (4)`.
3. **Turn-by-Turn Navigation Trigger:** Direct link to open GPS coordinates in native mapping applications for immediate site dispatch.
4. **Touch-Optimized CTA:** Full-width *"Start Work"* and *"Upload Proof"* action buttons designed for one-handed operation on mobile devices.

---

### Screen 06: Worker Proof-of-Work Photo Upload
- **Route:** `/worker/task/:id`
- **Target Persona:** Field Worker
- **Screenshot Asset:** [screen06_worker_proof_upload.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen06_worker_proof_upload.png)

![Screen 06: Worker Proof-of-Work Photo Upload](./screenshots/screen06_worker_proof_upload.png)

#### Core Objective
Enforces physical accountability by requiring field workers to upload geo-tagged, timestamped photographic proof before any grievance can transition to `Work Done`.

#### Key Civic Governance UI Annotations
1. **Camera Capture Modal:** Seamless camera trigger capturing repaired infrastructure (e.g. freshly asphalted pothole or cleared garbage bin).
2. **Worker Field Remarks:** Text input for notes on materials used, crew members present, and contractor details.
3. **Geo-Location Tamper Prevention:** Incorporates captured device coordinates to ensure worker was physically present within 50 meters of the reported complaint coordinates.
4. **One-Tap Completion Escalation:** Dispatches a push notification and SMS trigger to the reporting citizen announcing work completion.

---

### Screen 07: Citizen Verification & 5-Star Rating
- **Route:** `/citizen/complaint/:id`
- **Target Persona:** Citizen / Grievance Reporter
- **Screenshot Asset:** [screen07_citizen_verification_rating.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen07_citizen_verification_rating.png)

![Screen 07: Citizen Verification & 5-Star Rating](./screenshots/screen07_citizen_verification_rating.png)

#### Core Objective
Places the final authority on ticket closure into the citizen's hands, preventing premature or fraudulent closures by contractors or municipal staff.

#### Key Civic Governance UI Annotations
1. **Side-by-Side Photographic Verification:** Interactive comparison modal showing the citizen's original **Before Photo** alongside the field worker's **After (Proof-of-Work) Photo**.
2. **5-Star Quality Rating Widget:** Interactive gold-star rating system capturing citizen satisfaction with repair quality and turnaround speed.
3. **Dual Resolution Sign-Off:**
   - ✅ **"Approve & Close Complaint":** Submits citizen rating, awards performance points to worker, and closes ticket.
   - ⚠️ **"Dispute Work Quality":** Immediately reopens ticket and escalates directly to Department Executive Engineer for review.

---

### Screen 08: Department Officer Dashboard
- **Route:** `/officer`
- **Target Persona:** Department Officer (PWD / PHE / SWM / Electrical)
- **Screenshot Asset:** [screen08_officer_dashboard.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen08_officer_dashboard.png)

![Screen 08: Department Officer Dashboard](./screenshots/screen08_officer_dashboard.png)

#### Core Objective
Equips nodal officers with operational triage capabilities, allowing rapid allocation of incoming complaints to available field workers and monitoring SLA compliance.

#### Key Civic Governance UI Annotations
1. **High-Priority Escalation Queue:** Top banner highlighting unresolved critical tickets nearing SLA expiration.
2. **Worker Assignment Dropdown:** Real-time dropdown selector showing available field staff with active job counts (e.g. `Ramesh Kumar (2 active jobs)`).
3. **Department KPI Badges:** Key performance indicators including Average Resolution Time (e.g., *14.2 Hours*), 24-Hour Influx, and Worker Utilization rate.
4. **Direct Phone & Dispatch Link:** Quick click-to-call link to field team leads for urgent field reassignments.

---

### Screen 09: Super Admin Cross-Dept Overview & Heatmap
- **Route:** `/admin/reports`
- **Target Persona:** Municipal Commissioner, Mayor, City Administrator
- **Screenshot Asset:** [screen09_admin_crossdept_heatmap.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen09_admin_crossdept_heatmap.png)

![Screen 09: Super Admin Cross-Dept Overview & Heatmap](./screenshots/screen09_admin_crossdept_heatmap.png)

#### Core Objective
Delivers top-level strategic intelligence across all urban departments, identifying municipal hotspots, systemic failure patterns, and departmental efficiency benchmarks.

#### Key Civic Governance UI Annotations
1. **Ward Grievance Density Heatmap:** Spatial intensity grid highlighting wards with disproportionately high complaint volumes (e.g., Ward 14 drainage issues).
2. **Cross-Departmental Performance Matrix:** Comparative bar and radar charts comparing resolution velocities of PWD vs PHE vs SWM vs Electrical.
3. **Citizen Sentiment Score:** Aggregate municipal satisfaction index derived from verified 5-star ratings across all closed tickets.
4. **Data Export Suite:** One-click CSV and PDF report generation for municipal assembly and budget planning meetings.

---

### Screen 10: Worker Management Panel
- **Route:** `/admin/workers`
- **Target Persona:** Municipal Admin, Fleet Operations Manager
- **Screenshot Asset:** [screen10_worker_management_panel.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen10_worker_management_panel.png)

![Screen 10: Worker Management Panel](./screenshots/screen10_worker_management_panel.png)

#### Core Objective
Manages the municipal workforce roster across all wards, ensuring optimal task distribution, tracking on-duty status, and preventing worker burnout.

#### Key Civic Governance UI Annotations
1. **Active Roster Grid:** Displays registered field personnel with department tags, assigned ward zones, and contact numbers.
2. **Workload Utilization Meters:** Visual capacity bars indicating active ticket allocations (e.g., 2/5 jobs active vs at capacity).
3. **Availability State Toggles:** Instant toggle between `Available`, `On Duty`, and `Off Duty`.
4. **Worker Performance Metrics:** Lifetime completed task counts and citizen satisfaction ratings per worker.

---

### Screen 11: System Health & Diagnostics Page
- **Route:** `/health`
- **Target Persona:** SRE, Municipal IT Director, DevOps Auditor
- **Screenshot Asset:** [screen11_system_health_diagnostics.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen11_system_health_diagnostics.png)

![Screen 11: System Health & Diagnostics Page](./screenshots/screen11_system_health_diagnostics.png)

#### Core Objective
Provides real-time telemetry on the frontend client environment, service worker status, backend API connectivity, and client authentication integrity.

#### Key Civic Governance UI Annotations
1. **Live Backend Ping Indicator:** Dynamic round-trip ping calling `/api/v1/health/` with live millisecond latency readout and HTTP 200 OK verification.
2. **PWA Service Worker State:** Real-time registration state (`Active & Running` vs `Unregistered`) ensuring offline caching readiness.
3. **Auth Token Diagnostic:** Verifies presence, role claims, and expiration state of client JWT tokens.
4. **Configuration Inspection:** Safe, sanitized display of current API Base URL (`VITE_API_URL`) and environment runtime mode.

---

### Screen 12: Central Complaints Ledger & Audit Log
- **Route:** `/admin/complaints`
- **Target Persona:** Municipal Vigilance Officer, Central Auditor, Super Admin
- **Screenshot Asset:** [screen12_complaints_ledger_audit.png](file:///c:/Users/Victus/OneDrive/Documents/Frontend Lead (Officer & Worker Portals)/screenshots/screen12_complaints_ledger_audit.png)

![Screen 12: Central Complaints Ledger & Audit Log](./screenshots/screen12_complaints_ledger_audit.png)

#### Core Objective
Functions as the immutable civic audit log of all registered complaints across the municipality, supporting legal inquiries, RTI requests, and vigilance investigations.

#### Key Civic Governance UI Annotations
1. **Chronological Audit Table:** Tabular listing sorted by submission timestamp, complete with unique Tracking IDs, Citizen identities, and Ward numbers.
2. **Multi-Faceted Filter Engine:** Real-time search by complaint ID, category filter buttons (PWD, SWM, PHE, ELEC), and status pills.
3. **Full Audit Trace Drawer:** Clicking any complaint opens the complete chronological record including all reassignment timestamps, officer notes, and image attachments.
4. **Tamper-Evident State History:** Ensures every status modification is permanently attributed to a specific officer or worker user ID.

---

## Design System & Civic Aesthetic Principles

The JANMITRA platform follows a modern, high-contrast civic aesthetic engineered for diverse lighting conditions and high accessibility:

- **Primary Civic Identity:** `#0d2a53` (Deep Navy) — symbolizing institutional trust and municipal stability.
- **Department Taxonomy Colors:**
  - 🔵 **Public Works Department (PWD):** `#2563eb` (Royal Blue)
  - 🟢 **Solid Waste Management (SWM):** `#16a34a` (Emerald Green)
  - 🔷 **Public Health Engineering (PHE):** `#0891b2` (Cyan)
  - 🟡 **Electrical / Energy Department:** `#eab308` (Amber Yellow)
- **Status Indicators:**
  - 🔴 **Critical / SLA Breach:** `#ef4444`
  - 🟠 **In Progress / Dispatched:** `#f97316`
  - 🟢 **Resolved / Verified:** `#10b981`
- **Typography:** Inter & system sans-serif hierarchy for maximum legibility on mobile screens under direct sunlight.
- **PWA & Mobile-First Touch Target:** Minimum 48px interactive touch targets compliant with WCAG 2.1 AA accessibility standards.

---

*Catalog compiled and validated for JANMITRA civic infrastructure release v1.0.0.*
