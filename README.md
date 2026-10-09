# CivicSolve AI

### AI-Powered Societal Problem Solving, Authority Routing & Collaborative Innovation Platform

CivicSolve AI is an enterprise-grade civic technology platform connecting citizens, municipal authorities, universities, and industry partners to report, triage, engineer, and deploy measurable solutions for real-world municipal problems.

---

## 🚀 Key Platform Features

1. **End-to-End Civic Journey**:
   - `Citizen Report` ➔ `AI Multimodal Analysis` ➔ `Duplicate Elimination` ➔ `Priority Calculation (1–100)` ➔ `Admin Desk Verification` ➔ `Departmental Authority Routing` ➔ `SLA Countdown Watchdog` ➔ `University/Student Innovation Matching` ➔ `Collaborative Kanban Workspace` ➔ `Pilot Field Testing` ➔ `Citizen Verification Rating` ➔ `Measurable Impact Dashboard`.

2. **8 Role-Based Workspaces**:
   - **Citizen**: GPS & live camera intake, personal complaint tracking, social civic feed, and star rating verification.
   - **Authority Officer**: Work queue triage, field officer assignment, and evidence resolution uploads.
   - **Government Official / Commissioner**: Executive Command Center, 8 live metrics, Chart.js visualizations, AI natural-language query assistant, and SLA escalation tracking.
   - **System Administrator**: Verification queue, configurable routing rules, and tamper-proof audit trails.
   - **University Research & Dean**: Academic problem catalog and research grant opportunities.
   - **Faculty Mentor**: Engineering design approvals and student prototype supervision.
   - **Student Team**: Collaborative Kanban task board, YOLOv8/IoT project milestones, and GitHub integration.
   - **Industry CSR Partner**: Grant sponsorship, carbon offset measurement, and funding allocations.

3. **Advanced Frontend Engineering**:
   - **Live Device Geolocation**: Uses the real HTML5 `navigator.geolocation` API with satellite coordinate fallbacks.
   - **Live WebRTC Camera Stream**: Live video streaming (`navigator.mediaDevices.getUserMedia`), canvas snapshot frame capture, and retake controls.
   - **Interactive Incident Map**: Leaflet.js map with custom SVG priority pins (Critical, High, Medium, Low), popups, and district filters.
   - **AI Analysis Visualizer**: Holographic scanning beam, keyword tag clouds, duplicate alert banner, and urgency breakdown.
   - **Persistent LocalStorage Engine (`CivicDB`)**: Preloaded with 20 realistic multi-category civic problems, pre-configured authorities, notifications, and audit logs.
   - **Seamless Dark/Light Mode**: Smooth CSS variable transitions with persistent preference retention.

---

## 📂 Project Structure

```
CivicSolveAI/
├── frontend/
│   ├── index.html                   # Flagship landing page with counters & journey graphic
│   ├── login.html                   # 1-Click Demo Persona selector & standard login
│   ├── register.html                # Multi-role citizen/innovator registration
│   ├── forgot-password.html         # Password recovery simulator
│   ├── citizen-dashboard.html       # Citizen dashboard with stats, recent issues, and ward map
│   ├── submit-problem.html          # 5-step wizard (Form -> Live GPS -> Camera -> AI -> Review)
│   ├── my-problems.html             # Filterable complaints list with progress indicators
│   ├── problem-details.html         # 11-stage full transparent timeline & citizen star feedback
│   ├── social-feed.html             # Public community feed, upvotes, and AI share posters
│   ├── notifications.html           # Categorized notification center
│   ├── profile.html                 # Profile settings & credentials
│   │
│   ├── authority-dashboard.html     # Department work queue & officer dispatch
│   ├── authority-problems.html      # Filterable work queue
│   ├── authority-problem-details.html # Authority investigation & resolution proof
│   ├── authority-officers.html      # Officer roster and workload metrics
│   ├── authority-reports.html       # SLA compliance reports
│   │
│   ├── government-dashboard.html    # Executive Command Center with Chart.js & AI assistant
│   ├── government-monitoring.html   # Real-time event ticker & department workload
│   ├── government-map.html          # Full-screen incident map with priority layers
│   ├── government-analytics.html    # Deep dive resolution velocity & satisfaction charts
│   ├── escalation-center.html       # 4-tier automated SLA breach escalation protocol
│   │
│   ├── admin-dashboard.html         # Administrator control center & system health
│   ├── user-management.html         # Account permissions & role management
│   ├── problem-verification.html    # Incoming citizen complaint verification desk
│   ├── authority-management.html    # Dynamic routing rule configurations
│   ├── system-analytics.html        # Platform audit logs & telemetry
│   │
│   ├── university-dashboard.html    # University innovation cell & grant hub
│   ├── university-problems.html     # Academic problem challenges catalog
│   ├── faculty-dashboard.html       # Faculty mentor review & pilot approval
│   ├── student-team-dashboard.html  # Student team roster & project milestones
│   ├── team-matching.html           # AI Smart Matching algorithm (% compatibility score)
│   ├── solution-workspace.html      # Interactive Kanban task board (To Do, In Progress, Review, Done)
│   ├── solution-details.html        # Pilot testing results & before/after data
│   │
│   ├── industry-dashboard.html      # CSR funding & grant sponsorship
│   ├── industry-opportunities.html  # Open innovation challenges for sponsors
│   │
│   ├── css/
│   │   ├── style.css                # Global tokens, buttons, dark/light themes
│   │   ├── dashboard.css            # Sidebar layout, topbar, search, user dropdown
│   │   ├── components.css           # Cards, badges, modals, toasts, AI scanning, Kanban
│   │   ├── responsive.css           # Tablet and mobile viewport optimization
│   │   └── animations.css           # Micro-interactions, laser scanning, shimmer
│   │
│   ├── js/
│   │   ├── data.js                  # 20+ realistic mock problems, authorities, localStorage engine
│   │   ├── utils.js                 # Toast notifications, modal helpers, ID generator
│   │   ├── auth.js                  # Session and persona switcher
│   │   ├── app.js                   # Theme toggle, search, and navigation events
│   │   ├── ai-analysis.js           # Semantic analysis, duplicate detection, priority scoring
│   │   ├── problems.js              # Wizard form, Geolocation API, WebRTC camera capture
│   │   ├── map.js                   # Leaflet map instance and priority markers
│   │   ├── analytics.js             # Chart.js charts (Doughnut, Bar, Line, Horizontal Bar)
│   │   └── solutions.js             # Kanban task board logic and star rating widget
│   │
│   └── assets/
│       ├── logo.svg
│       ├── favicon.svg
│       └── default-avatar.svg
│
├── backend-ready/
│   └── README.md                    # FastAPI schemas, PostgreSQL DDL, REST endpoints
│
└── README.md
```

---

## 🛠️ How to Run Locally

1. Open the `civicsolve_ai` project root folder in **Visual Studio Code**.
2. Make sure you have the **Live Server** extension installed (`ritwickdey.LiveServer`).
3. Right-click on `frontend/index.html` in the file explorer.
4. Select **"Open with Live Server"** (or click "Go Live" in the bottom status bar).
5. The application will launch in your browser at `http://127.0.0.1:5500/frontend/index.html`.

---

## 🔑 Demo Login & Role Switching

You can test all 8 distinct personas effortlessly:
1. Navigate to `login.html`.
2. Click any of the **1-Click Demo Persona Launch** buttons:
   - **Citizen**: `citizen-dashboard.html`
   - **Authority Officer**: `authority-dashboard.html`
   - **Government Official**: `government-dashboard.html`
   - **Administrator**: `admin-dashboard.html`
   - **University Dean**: `university-dashboard.html`
   - **Faculty Mentor**: `faculty-dashboard.html`
   - **Student Team**: `student-team-dashboard.html`
   - **Industry Partner**: `industry-dashboard.html`
3. In any dashboard, use the **Demo Role** dropdown in the top navigation bar to switch roles instantaneously.

---

## 📷 Camera & GPS Implementation

* **Camera (`submit-problem.html` - Step 3)**:
  - Invokes `navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })`.
  - Live video streams to the HTML `<video>` element.
  - Clicking "Snap Photo" draws the current frame into an offscreen `<canvas>` and creates an image preview.
  - Memory cleanup: `track.stop()` is automatically executed when taking snapshots or stopping the camera stream.
* **Geolocation (`submit-problem.html` - Step 2)**:
  - Invokes `navigator.geolocation.getCurrentPosition()`.
  - Captures high-accuracy device latitude and longitude and auto-populates the street address and municipal ward coordinates.
  - Includes a fallback to central city coordinates if permissions are denied in non-HTTPS testing environments.

---

## 🧠 Future AI & Backend Integration

The frontend architecture is 100% backend-ready:
* Pre-configured data structures in `data.js` match standard PostgreSQL / PostGIS schemas.
* See [backend-ready/README.md](backend-ready/README.md) for full FastAPI endpoint routes, JSON payloads, and PostgreSQL table DDL.
