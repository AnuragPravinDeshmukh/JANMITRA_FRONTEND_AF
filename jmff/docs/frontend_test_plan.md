# JANMITRA Frontend End-to-End Test Plan & Troubleshooting Guide

This document contains detailed manual test scripts for JANMITRA civic portal flows, the verification checkpoints, and fixes for the top 5 most common integration issues between the React frontend and Django REST Framework backend.

---

## E2E Test Scenario 1: Citizen Submission & Verification Flow

### Objective
Verify that a citizen can register their profile, log into their ward, report an infrastructure grievance with verified photos and GPS coordinates, and track real-time AI validation and push notification triggers.

| Step | Action | Input / Data | Expected Result | Pass/Fail |
|---|---|---|---|---|
| **1** | Open Web App | Browse to `http://localhost:5173` | Login/Portal entry screen loads cleanly without errors. | [ ] |
| **2** | Switch to Register Tab | Click **"Register (Citizen)"** tab | Citizen registration form appears with fields: Name, Mobile, Ward, Password. | [ ] |
| **3** | Fill Registration Details | **Name**: `Test Citizen`<br>**Mobile**: `9876543210`<br>**Ward**: `Ward 2`<br>**Password**: `test1234` | All fields accept input; Ward 2 is selected from the dropdown. | [ ] |
| **4** | Submit Registration | Click **"Register as Citizen"** | Account created via `POST /api/v1/auth/register/`. JWT token stored in `localStorage`, redirects to `/citizen`. | [ ] |
| **5** | Verify Citizen Dashboard | Observe home screen | Shows *"Welcome, Test Citizen!"* and registered Ward: **Ward 2**. | [ ] |
| **6** | Navigate to Issue Form | Click **"Report New Issue"** | Navigates to `/citizen/submit`. Single-page complaint form opens. | [ ] |
| **7** | Select Category | Click card **"Roads & Infrastructure"** | Card highlights with thick blue border, soft blue background fill, and `✓` checkmark. | [ ] |
| **8** | Verify Ward Selection | Inspect Ward pills | **Ward 2** is automatically pre-selected with solid blue fill based on user context. | [ ] |
| **9** | Enter Description | Type: `"Large pothole on main road causing accidents"` | Character counter updates to `45 / 20 minimum` (turns green). | [ ] |
| **10** | Upload Valid Phone Photo | Upload a phone camera photo containing EXIF/GPS | Shows *"Verifying photo..."* spinner overlay while backend check runs; turns into a green checkmark badge upon verification. Counter shows `1/3 photos added`. | [ ] |
| **11** | Upload Unverified / Screenshot Photo | Upload a computer screenshot or image without camera EXIF | Backend returns `{ real: false }`. Image is removed from preview and red alert appears: *"This image cannot be verified. Please upload a real photo taken by your phone camera."* | [ ] |
| **12** | Verify Leaflet Map | Inspect Location section | Map renders OpenStreetMap tiles centered on citizen's GPS coordinates. Pin is draggable. Reverse geocode shows address below. | [ ] |
| **13** | Submit Grievance | Click sticky button **"Submit Complaint"** | Button displays spinner. Submits `multipart/form-data` to `POST /api/v1/complaints/`. Success toast appears, then redirects to `/citizen/complaint/:id`. | [ ] |
| **14** | Status Transition Check | Observe status badge on complaint page | Initial badge shows grey `Submitted`. Within 30 seconds, background polling updates status to blue `Validated`. | [ ] |
| **15** | Browser Push Notification | Observe browser alerts | Browser push notification prompts/fires with alert: *"AI & Ward Officer verified your report: Status updated to Validated!"*. | [ ] |

---

## Top 5 Most Common Setup Issues & Technical Solutions

### Issue 1: Leaflet Map Tiles Not Rendering / Grey Grid / Broken Markers
- **Symptom**: Map container renders as blank grey blocks or markers appear as broken image links.
- **Root Cause**: 
  1. `leaflet.css` stylesheet not imported in the global entry bundle.
  2. Vite/Webpack asset bundling hashes marker image paths (`marker-icon.png`, `marker-shadow.png`).
- **Solution**:
  1. Add global stylesheet import in `src/main.jsx`:
     ```javascript
     import 'leaflet/dist/leaflet.css';
     ```
  2. Fix Leaflet's default icon URLs with explicit CDN asset anchors in `LeafletMap.jsx`:
     ```javascript
     delete L.Icon.Default.prototype._getIconUrl;
     L.Icon.Default.mergeOptions({
       iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
       iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
       shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
     });
     ```

---

### Issue 2: CORS Blocked When Calling Django Backend from Vite
- **Symptom**: Console error: `Access to XMLHttpRequest at 'http://localhost:8000/api/...' from origin 'http://localhost:5173' has been blocked by CORS policy`.
- **Root Cause**: Django backend missing `django-cors-headers` middleware or port `5173` is not whitelisted.
- **Solution (in Django `settings.py`)**:
  ```python
  INSTALLED_APPS = [
      ...
      'corsheaders',
      'rest_framework',
  ]

  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',  # MUST be before CommonMiddleware
      'django.middleware.common.CommonMiddleware',
      ...
  ]

  CORS_ALLOWED_ORIGINS = [
      "http://localhost:5173",
      "http://127.0.0.1:5173",
  ]
  CORS_ALLOW_CREDENTIALS = True
  ```

---

### Issue 3: JWT Token Expiration and Missing Automatic Refresh
- **Symptom**: After token TTL expires (e.g. 5–15 mins), user gets abrupt `401 Unauthorized` errors and gets booted from the app while filling forms.
- **Root Cause**: Single access token stored without Axios response interceptor for token rotation (`/api/auth/token/refresh/`).
- **Solution (in `src/api/client.js`)**:
  - Implemented queue-based 401 retry interceptor:
  - If a request returns `401`, intercepts call, reads `janmitra_refresh_token`, requests new access token from `/api/auth/token/refresh/`, updates `localStorage`, and replays original failed request seamlessly without user disruption.

---

### Issue 4: Image Upload Fails / Broken Image URLs in Production
- **Symptom**: `POST /api/v1/complaints/` returns `500 Server Error` or images uploaded fail to display on detail cards.
- **Root Cause**: Django `MEDIA_ROOT` and `MEDIA_URL` not configured, or static media routing missing in `urls.py`.
- **Solution (in Django `settings.py` & `urls.py`)**:
  ```python
  # settings.py
  import os
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB limit

  # urls.py
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('complaints.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

---

### Issue 5: Raw Technical Django Errors Displayed to Citizens
- **Symptom**: Forms display ugly raw JSON like `{"description": ["Ensure this field has at least 20 characters."]}` or crash when errors are nested.
- **Root Cause**: DRF serializes validation errors as dictionary of lists; frontend components expect clean string messages.
- **Solution (in `src/utils/errorHandler.js`)**:
  - Implemented `formatDRFError(error)` and `getFieldErrors(error)` utility.
  - Automatically translates HTTP status codes (`401`, `403`, `413`, `500`) into plain English.
  - Recursively flattens DRF field error dictionaries into clear, formatted strings:
    - Example: `"Description: Ensure this field has at least 20 characters."`

---

## Test Verification Sign-off

- [x] Global Leaflet CSS import integrated in `src/main.jsx`.
- [x] Auto-refresh Axios interceptor added in `src/api/client.js`.
- [x] Centralized DRF error handler added in `src/utils/errorHandler.js`.
- [x] Registration flow added to `src/pages/auth/LoginPage.jsx`.
- [x] Status polling & push notifications enabled in `src/pages/citizen/ComplaintDetail.jsx`.
- [x] Frontend compiled cleanly via `vite build`.
