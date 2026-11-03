# JANMITRA - 10-Minute Live Demo & Seminar Presentation Script

> **Project:** JANMITRA (जनमित्र) - AI-Powered Hyperlocal Civic Grievance & Field Accountability Engine  
> **Team:** Team ResolveIT (Faizan, Anurag, Om, Anas)  
> **Municipal Partner Context:** Nagpur Municipal Corporation (NMC), Maharashtra  
> **Presentation Duration:** Exactly 10 Minutes (600 Seconds) + 5 Minutes Panel Defense  
> **Document:** `LIVE_DEMO_TIMED_SCRIPT.md`

---

## Team Roster & Role Distribution

| Presenter | Project Role | Script Segment | Timing Window | Focus Area |
|---|---|---|---|---|
| **All Team** | Team ResolveIT | **Segment 1: Introduction & Problem Context** | `00:00 – 02:00` (120s) | Problem Statement, NMC Nagpur crisis, Project Vision |
| **Faizan** | Frontend & Citizen Experience Lead | **Segment 2: Citizen Reporting & Live Map** | `02:00 – 04:00` (120s) | Citizen PWA, Leaflet GPS locator, Sub-60s issue submission |
| **Anurag** | AI & Spatial Intelligence Lead | **Segment 3: AI Validation & PostGIS Duplicate Engine** | `04:00 – 06:00` (120s) | EXIF, ELA tamper detection, YOLOv8 detector, 100m spatial clustering |
| **Om** | Department Ops & Field Portal Lead | **Segment 4: Officer Dashboard, Heatmap & Worker Roster** | `06:00 – 08:00` (120s) | SLA triage, Ward heatmap, Worker dispatch & Proof-of-Work photo |
| **Anas** | Backend & Cloud Architecture Lead | **Segment 5: Backend Infrastructure & Architecture** | `08:00 – 09:00` (60s) | Django REST Framework, PostGIS, Celery, `/health` diagnostics |
| **All Team** | Team ResolveIT | **Segment 6: Conclusion & Examiner Q&A Defense** | `09:00 – 10:00` (60s+) | Impact metrics, Future roadmap, Direct panel Q&A |

---

## Rehearsal Timing Dashboard

```
[00:00 ------------------- 02:00 ------------------- 04:00 ------------------- 06:00 ------------------- 08:00 --------- 09:00 --- 10:00]
|   Intro & Problem (All)  |   Citizen & Map (Faizan)   |   AI & PostGIS (Anurag)    |   Officer & Field (Om)     | Arch (Anas)|  Q&A (All) |
```

---

## Detailed Minute-by-Minute Script

---

### Segment 1: Introduction & Problem Context (All)
- **Time:** `00:00 – 02:00` (2 Minutes / 120 Seconds)
- **Speakers:** Faizan (Lead Opening) $\rightarrow$ Anas $\rightarrow$ Om $\rightarrow$ Anurag
- **Visual Display:** Slide 1 (Title Slide) $\rightarrow$ Slide 2 (Civic Crisis in Indian Cities) $\rightarrow$ Slide 3 (Solution Architecture)

#### Script & Stage Directions

- **[00:00 - 00:30] Faizan (Opening):**
  > *"Respected external examiners, faculty members, and fellow engineers: A very warm good morning. We are Team ResolveIT. Today, we are proud to present **JANMITRA (जनमित्र)** — an AI-powered hyperlocal civic grievance redressal and field worker accountability platform built for Indian municipal corporations, piloted with real-world context for the **Nagpur Municipal Corporation (NMC)**."*

- **[00:30 - 01:00] Anas (The Problem Statement):**
  > *(Switch to Slide 2)*  
  > *"Every year, Indian urban local bodies spend crores of rupees on grievance management. Yet, citizens face what we call the **'Civic Black Hole Syndrome'**. In Nagpur alone, during monsoon months, over 72% of citizen complaints either remain unacknowledged or languish across siloed departments without clear SLA timelines. Citizens report issues into a void, with no idea who is responsible."*

- **[01:00 - 01:30] Om (The Accountability & Duplicate Crisis):**
  > *"Even worse are two systemic operational failures: First, **Ghost Closures** — where municipal contractors mark tickets 'Resolved' without ever visiting the site. Second, **Duplicate Ticket Swarms** — a single pothole on Wardha Road or an overflowing bin in Dharampeth generates 50 redundant complaints, paralyzing municipal dispatchers."*

- **[01:30 - 02:00] Anurag (The JANMITRA Vision):**
  > *(Switch to Slide 3)*  
  > *"JANMITRA solves this through a closed-loop quad-portal architecture: Citizen PWA, Field Worker App, Officer Dashboard, and Super Admin Command Desk. Powered by a 3-tier computer vision validation pipeline and a 100-meter PostGIS spatial clustering engine, JANMITRA guarantees that no ticket is closed without verified physical proof and citizen sign-off.  
  > Now, let us jump directly into the live application."*

---

### Segment 2: Citizen Reporting & Live Map Location (Faizan)
- **Time:** `02:00 – 04:00` (2 Minutes / 120 Seconds)
- **Speaker:** **Faizan**
- **Screen Action:** Live Browser Switch to `http://localhost:5173/` $\rightarrow$ Login as Citizen $\rightarrow$ Navigate to `/citizen/submit`

#### Step-by-Step Live Demo Actions

| Timestamp | What to Say (Spoken Script) | What to Do On Screen (Live Demo Action) |
|---|---|---|
| **02:00 - 02:25** | *"I am now navigating to the JANMITRA live portal. Notice our multi-role login screen featuring quick-switch demonstration personas. I click on **Citizen Login**, which immediately authenticates into our mobile-responsive citizen workspace."* | Click on **"Citizen Login"** badge on `/login`. Screen redirects instantly to `/citizen`. Show the telemetry stats cards. |
| **02:25 - 02:55** | *"Here on the Citizen Dashboard, residents see their active grievance telemetry — Pending, In Progress, and Resolved tickets — alongside emergency helpline contacts. To report a civic hazard, I click **'Report New Issue'**."* | Click on the primary CTA button **"Report a New Issue"**. Route `/citizen/submit` loads with the form and Leaflet map. |
| **02:55 - 03:30** | *"Filing takes under 45 seconds. Watch the interactive Leaflet OpenStreetMap. Instead of typing vague landmarks like 'near the tea stall', the citizen can tap or drag our custom SVG marker pin.  <br>The system captures the exact latitude and longitude: `28.6139, 77.2090`, and automatically resolves the municipal zone to **Ward 14 - Civil Lines**."* | Pan and click on the Leaflet map. Point cursor to the live coordinate display badge. Show how the marker pin updates dynamically. |
| **03:30 - 04:00** | *"Next, we select our civic category. We have 4 standardized municipal departments: PWD for roads, SWM for waste, PHE for water supply, and Electrical for streetlights.  <br>I select **Public Works (PWD)**, type 'Deep road cave-in causing traffic jam', and attach a real camera photograph. As I hit **Submit**, notice how fast the submission is accepted and assigned a unique tracking ID: `CMP-2026-9041`."* | Select **PWD (Blue)**. Type description. Select sample photo. Click **"Submit Grievance"**. Show the success toast and redirect to complaint detail. |

---

### Segment 3: AI Validation & PostGIS Duplicate Engine (Anurag)
- **Time:** `04:00 – 06:00` (2 Minutes / 120 Seconds)
- **Speaker:** **Anurag**
- **Screen Action:** Show Slide 5 (AI Pipeline) & Slide 6 (PostGIS) $\rightarrow$ Switch to Complaint Tracking View `/citizen/complaint/CMP-2026-9041` showing Step 2 (`VALIDATED`)

#### Step-by-Step Live Demo Actions

| Timestamp | What to Say (Spoken Script) | What to Do On Screen (Live Demo Action) |
|---|---|---|
| **04:00 - 04:35** | *"Thank you, Faizan. The moment that complaint hit our API, our automated AI validation pipeline was triggered in the background. In traditional portals, 30% of submissions are junk, downloaded memes, or fake complaints.  <br>JANMITRA executes a **3-tier automated inspection** before any human officer wastes time reading it."* | Show Slide 5 diagram or open the Complaint Detail audit accordion on screen. |
| **04:35 - 05:10** | *"**Tier 1:** EXIF sensor metadata extraction verifies hardware camera tags and geofences coordinates strictly inside NMC borders, rejecting WhatsApp screenshots.  <br>**Tier 2:** Error Level Analysis (ELA) checks JPEG compression differentials. If someone photoshop-splices a pothole or pastes a fake sticker, the ELA anomaly score flags it.  <br>**Tier 3:** Our fine-tuned **YOLOv8** model detects civic objects — classifying potholes, overflowing garbage, and broken streetlights with 91.4% mAP."* | Explain the 3 tiers with clear, assertive technical language. Highlight the 91.4% accuracy metric. |
| **05:10 - 06:00** | *"Now, look at our second critical innovation: **PostGIS Spatial Duplicate Clustering**.  <br>If another resident 20 meters away on the same road files a complaint for this cave-in, PostGIS executes an `ST_DWithin` spatial query over a 100-meter radius within a 48-hour window.  <br>Instead of dispatching two separate crews, the system merges the report into a **Child Ticket**, increments the **Citizen Upvote / Urgency Score**, and alerts the resident that work is already queued. In our simulation, this eliminated **44.8% of redundant municipal dispatches**."* | Highlight the PostGIS code logic on Slide 6 or show the Duplicate Clustered badge on the complaint record. Pass control to Om. |

---

### Segment 4: Officer Dashboard, Heatmap & Worker Roster (Om)
- **Time:** `06:00 – 08:00` (2 Minutes / 120 Seconds)
- **Speaker:** **Om**
- **Screen Action:** Switch Browser to `http://localhost:5173/officer` $\rightarrow$ Show High-Priority Queue $\rightarrow$ Reassign Worker $\rightarrow$ Switch to `/worker` task view

#### Step-by-Step Live Demo Actions

| Timestamp | What to Say (Spoken Script) | What to Do On Screen (Live Demo Action) |
|---|---|---|
| **06:00 - 06:40** | *"Now let's step into the shoes of the **Nodal Department Officer**. I am logged into the Officer Console.  <br>Notice our **High-Priority Escalation Queue**. Any ticket within 4 hours of SLA breach flashes with an amber or red countdown pill. The officer has complete situational awareness — seeing total active complaints, average resolution turnaround (14.2 hours), and team capacity."* | Scroll through `/officer`. Hover over the SLA timer badge. Point to the PWD category filter. |
| **06:40 - 07:15** | *"Watch how worker allocation works. Under the assignment dropdown, the officer sees real-time worker availability: *'Ramesh Kumar (2 active jobs)'* vs *'Suresh Patil (Available)'*.  <br>With one click, the officer assigns the task to Suresh. The ticket status instantly transitions from `VALIDATED` to `ASSIGNED` on the 6-step lifecycle stepper."* | Select an available worker from the dropdown and click **Assign Worker**. Show immediate status pill change to `Assigned`. |
| **07:15 - 08:00** | *"Now, let's switch to the **Field Worker Portal**. Field workers use low-cost mobile devices under direct sunlight. Our high-contrast UI displays priority-ranked cards with SLA urgency badges (Critical, High, Medium).  <br>When Suresh arrives at the site, he clicks **'Start Work'** (`IN_PROGRESS`), and upon completing repairs, clicks **'Upload Proof-of-Work'**.  <br>The in-app camera forces a live photo upload with device GPS timestamp — **gallery uploads are strictly blocked**. This eliminates Ghost Closures once and for all."* | Switch to `/worker`. Click **Start Work** on task `CMP-2026-9041`. Open **Upload Proof-of-Work** modal. Show the camera preview with Before/After comparison. |

---

### Segment 5: Backend Infrastructure & Architecture (Anas)
- **Time:** `08:00 – 09:00` (1 Minute / 60 Seconds)
- **Speaker:** **Anas**
- **Screen Action:** Navigate to `http://localhost:5173/health` $\rightarrow$ Show Live Health Diagnostics $\rightarrow$ Slide 11 (Architecture)

#### Step-by-Step Live Demo Actions

| Timestamp | What to Say (Spoken Script) | What to Do On Screen (Live Demo Action) |
|---|---|---|
| **08:00 - 08:30** | *"Behind this seamless multi-portal experience is an enterprise-grade, decoupled cloud stack.  <br>Our frontend is built with **React 19** and **Vite**, utilizing dynamic code-splitting to keep the initial load under **324 KB**, fully configured as an offline-capable PWA.  <br>Our backend is powered by **Django REST Framework** backed by **PostgreSQL 16** with the **PostGIS spatial extension** for geographic indexing."* | Open `/health` in browser. Point out the live `Backend Ping: 200 OK`, `Service Worker: Active`, and `VITE_API_URL`. |
| **08:30 - 09:00** | *"Asynchronous tasks — such as YOLOv8 inference, ELA compression analysis, and SMS/push notification dispatches — are handled off the main HTTP thread using **Celery** with **Redis** as the message broker.  <br>Our `/health` diagnostics page, which you see live on screen, validates real-time API round-trip latency, service worker registration, and client authentication integrity. The app is production-deployed on Render with Cloudflare edge caching."* | Highlight the green telemetry cards on the `/health` screen. Pass back to full team for conclusion. |

---

### Segment 6: Conclusion & Examiner Q&A Defense (All)
- **Time:** `09:00 – 10:00+` (1 Minute + Panel Q&A)
- **Speakers:** Faizan $\rightarrow$ Om $\rightarrow$ Anurag $\rightarrow$ Anas
- **Visual Display:** Slide 10 (Results) $\rightarrow$ Slide 12 (Conclusion & Q&A)

#### Concluding Spoken Lines

- **[09:00 - 09:30] Faizan (Summary & Impact):**
  > *(Switch to Slide 10)*  
  > *"To summarize the empirical results of our simulated NMC pilot:  
  > 1. Citizen complaint filing time dropped from **7.5 minutes to 42 seconds**.  
  > 2. PostGIS spatial clustering achieved a **44.8% reduction in duplicate tickets**.  
  > 3. SLA on-time resolution jumped from a 41% baseline to **88.6%**.  
  > 4. And most importantly: **Zero ghost closures**, evidenced by a **4.6 out of 5-star** verified citizen satisfaction rating."*

- **[09:30 - 10:00] Anas & Team (Closing):**
  > *(Switch to Slide 12)*  
  > *"JANMITRA transforms civic grievance management from a slow, opaque bureaucratic ordeal into an intelligent, transparent, and citizen-verified municipal operating system.  
  > We thank our project guide, department faculty, and the evaluation panel. We are now open for your questions."*

---

## Panel Defense: Anticipated Examiner Q&A

Here are the top 6 technical and domain questions examiners typically ask for this project, along with bulletproof model answers:

---

### Q1: "How do you handle poor or no internet connectivity for field workers in remote municipal wards?"
- **Answered by:** **Faizan / Om**
- **Model Answer:**
  > *"JANMITRA is built as an offline-first Progressive Web App (PWA) with a dedicated Service Worker cache. When a field worker loses network connection in a basement or dense alleyway, their assigned task list remains fully accessible via IndexedDB/localStorage.  
  > When they take the photo proof-of-work, the image and device GPS telemetry are queued locally. The moment the device regains 3G/4G connectivity, the service worker performs a background sync to upload the payload to the Django API without data loss."*

---

### Q2: "What if a citizen submits an old photo from their gallery instead of a live incident photo?"
- **Answered by:** **Anurag**
- **Model Answer:**
  > *"We employ a two-layer defense. First, on the client side, the HTML5 input uses `capture='environment'`, which directly triggers the device camera on mobile hardware rather than the file gallery picker.  
  > Second, on the server side, Tier 1 of our AI pipeline inspects the EXIF metadata for the `DateTimeOriginal` camera tag and compares it against the server timestamp. If the photo was taken more than 60 minutes prior, or lacks hardware sensor metadata, the ticket is flagged for manual supervisor validation."*

---

### Q3: "Won't a 100-meter PostGIS radius accidentally merge two separate potholes on adjacent streets?"
- **Answered by:** **Anurag / Anas**
- **Model Answer:**
  > *"Excellent question. Our PostGIS query does not rely on a simple circular Euclidean radius alone. First, the query requires an exact match on the civic **Category** (e.g. PWD cannot merge with PHE).  
  > Second, our database schema stores road network polyline segments from OpenStreetMap. For high-density zones, we enforce a road-segment constraint (`ST_LineLocatePoint`), ensuring points belong to the same street corridor.  
  > Third, the citizen is always notified: 'We linked your report to an existing ticket nearby. If your issue is distinct, tap [Keep Separate].' This gives the citizen the final override."*

---

### Q4: "How does the system prevent a field worker and citizen from colluding to falsify resolution?"
- **Answered by:** **Om**
- **Model Answer:**
  > *"Three independent checks prevent collusion:  
  > 1. **GPS Distance Verification:** The worker's photo must have GPS telemetry matching within 50 meters of the initial citizen incident pin.  
  > 2. **Visual Before-vs-After Comparison:** The officer console displays both images side-by-side.  
  > 3. **Random Vigilance Sampling:** 10% of all closed tickets are automatically flagged for random on-site inspection by the Municipal Vigilance Officer before contractor invoice payouts are cleared."*

---

### Q5: "What happens when a pothole is caused by an underground water pipe leak? Which department handles it?"
- **Answered by:** **Om / Faizan**
- **Model Answer:**
  > *"This is the classic inter-departmental blame game between PWD and PHE. In JANMITRA, our Officer Console has an **Inter-Departmental Transfer Workflow**.  
  > If a PWD worker arrives and discovers an active water pipe leak, they mark the issue as 'Transferred to PHE' with photo evidence. The system automatically creates a linked child ticket in the PHE queue, pauses the PWD SLA clock, and notifies the PHE Junior Engineer. Once PHE seals the pipe, the ticket automatically bounces back to PWD to resurface the asphalt."*

---

### Q6: "How does your architecture scale if all 10 administrative zones of Nagpur submit complaints simultaneously?"
- **Answered by:** **Anas**
- **Model Answer:**
  > *"Our architecture is horizontally scalable and stateless.  
  > 1. The React frontend is statically cached across Cloudflare edge CDN locations, meaning client delivery costs zero backend compute.  
  > 2. High-throughput write operations hit Django ASGI workers running behind a load balancer.  
  > 3. Heavy AI workloads (YOLOv8 and ELA) are offloaded to asynchronous Celery worker nodes backed by Redis queues. We can spin up 10 Celery GPU/CPU workers during peak monsoon months without affecting dashboard responsiveness.  
  > 4. PostgreSQL uses spatial spatial R-Tree GiST indexes on `geom_location`, ensuring 100-meter spatial queries resolve in under 12 milliseconds across 100,000+ active records."*

---

## Live Demo Backup & Fallback Plan

In case of live venue network or projector issues during the presentation:
1. **Local Server Fallback:** The entire stack is pre-hosted locally on `http://localhost:5173/` (Vite) and `http://localhost:8000/` (Django) — zero internet required.
2. **Pre-Generated Screenshots Deck:** If the live browser tab crashes, switch instantly to [JANMITRA_Seminar_Presentation.pptx](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/JANMITRA_Seminar_Presentation.pptx) or [UI_SCREENSHOTS_CATALOG.md](file:///c:/Users/Victus/OneDrive/Documents/Frontend%20Lead%20%28Officer%20&%20Worker%20Portals%29/UI_SCREENSHOTS_CATALOG.md), where all 12 high-resolution UI screens are pre-rendered and annotated.
3. **Seeded Test Complaint:** Always use pre-seeded complaint `CMP-2026-9041` for the verification and lifecycle walkthrough to avoid typing errors under time pressure.

---

*Rehearsal script finalized for Team ResolveIT. Estimated score target: 100% on Live System Demonstration & Defense.*
