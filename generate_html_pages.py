import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
os.makedirs(FRONTEND_DIR, exist_ok=True)

def get_sidebar_html(active_role, active_page):
    roles = {
        "citizen": {
            "title": "Citizen Portal",
            "links": [
                ("citizen-dashboard.html", "fa-solid fa-house", "Dashboard"),
                ("submit-problem.html", "fa-solid fa-circle-plus", "Report Problem"),
                ("my-problems.html", "fa-solid fa-list-check", "My Problems"),
                ("social-feed.html", "fa-solid fa-comments", "Civic Feed"),
                ("notifications.html", "fa-solid fa-bell", "Notifications"),
                ("profile.html", "fa-solid fa-user", "My Profile")
            ]
        },
        "authority": {
            "title": "Authority Officer",
            "links": [
                ("authority-dashboard.html", "fa-solid fa-gauge-high", "Dashboard"),
                ("authority-problems.html", "fa-solid fa-inbox", "Work Queue"),
                ("authority-officers.html", "fa-solid fa-users", "Officers Roster"),
                ("authority-reports.html", "fa-solid fa-chart-line", "SLA Reports"),
                ("notifications.html", "fa-solid fa-bell", "Notifications"),
                ("profile.html", "fa-solid fa-id-badge", "Profile")
            ]
        },
        "government": {
            "title": "Civic Command Center",
            "links": [
                ("government-dashboard.html", "fa-solid fa-building-columns", "Command Center"),
                ("government-map.html", "fa-solid fa-map-location-dot", "Incident Map"),
                ("government-monitoring.html", "fa-solid fa-desktop", "Live Monitoring"),
                ("government-analytics.html", "fa-solid fa-chart-pie", "City Analytics"),
                ("escalation-center.html", "fa-solid fa-triangle-exclamation", "Escalation Desk"),
                ("profile.html", "fa-solid fa-user-tie", "Official Profile")
            ]
        },
        "admin": {
            "title": "System Administrator",
            "links": [
                ("admin-dashboard.html", "fa-solid fa-sliders", "Admin Control"),
                ("problem-verification.html", "fa-solid fa-clipboard-check", "Verification Queue"),
                ("user-management.html", "fa-solid fa-user-gear", "User Accounts"),
                ("authority-management.html", "fa-solid fa-landmark", "Routing Rules"),
                ("system-analytics.html", "fa-solid fa-shield-halved", "Audit Logs")
            ]
        },
        "university": {
            "title": "University Research",
            "links": [
                ("university-dashboard.html", "fa-solid fa-graduation-cap", "Innovation Hub"),
                ("university-problems.html", "fa-solid fa-book-open", "Civic Problems"),
                ("team-matching.html", "fa-solid fa-wand-magic-sparkles", "Smart Matching"),
                ("solution-workspace.html", "fa-solid fa-flask-vial", "Workspace"),
                ("profile.html", "fa-solid fa-school", "Profile")
            ]
        },
        "faculty": {
            "title": "Faculty Mentor",
            "links": [
                ("faculty-dashboard.html", "fa-solid fa-chalkboard-user", "Mentorship Desk"),
                ("team-matching.html", "fa-solid fa-people-arrows", "Team Matching"),
                ("solution-workspace.html", "fa-solid fa-code-branch", "Prototypes Review"),
                ("profile.html", "fa-solid fa-user-graduate", "Mentor Profile")
            ]
        },
        "student": {
            "title": "Student Innovator",
            "links": [
                ("student-team-dashboard.html", "fa-solid fa-laptop-code", "Team Workspace"),
                ("solution-workspace.html", "fa-solid fa-bars-progress", "Kanban Tasks"),
                ("solution-details.html", "fa-solid fa-lightbulb", "Solution Details"),
                ("social-feed.html", "fa-solid fa-earth-americas", "Civic Feed"),
                ("profile.html", "fa-solid fa-user", "Student Profile")
            ]
        },
        "industry": {
            "title": "Industry Partner",
            "links": [
                ("industry-dashboard.html", "fa-solid fa-briefcase", "CSR Dashboard"),
                ("industry-opportunities.html", "fa-solid fa-hand-holding-dollar", "Opportunities"),
                ("solution-details.html", "fa-solid fa-rocket", "Pilot Deployments"),
                ("profile.html", "fa-solid fa-building", "Partner Profile")
            ]
        }
    }

    role_data = roles.get(active_role, roles["citizen"])
    links_html = ""
    for href, icon, title in role_data["links"]:
        is_active = "active" if href == active_page else ""
        links_html += f"""
        <a href="{href}" class="sidebar-link {is_active}">
          <i class="{icon}"></i>
          <span>{title}</span>
        </a>
        """

    return f"""
    <aside class="app-sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="brand-logo">
          <i class="fa-solid fa-city"></i>
          <span>CivicSolve<span class="ai-tag">AI</span></span>
        </a>
      </div>
      <div class="sidebar-role-badge">
        <span class="role-title">{role_data["title"]}</span>
        <span class="badge badge-primary"><i class="fa-solid fa-shield"></i> Verified</span>
      </div>
      <nav class="sidebar-nav">
        <div class="nav-section-title">Navigation Menu</div>
        {links_html}
        <div class="nav-section-title" style="margin-top:1.5rem;">Quick Switch Role</div>
        <a href="login.html" class="sidebar-link">
          <i class="fa-solid fa-repeat"></i>
          <span>Switch User / Role</span>
        </a>
        <a href="index.html" class="sidebar-link">
          <i class="fa-solid fa-globe"></i>
          <span>Public Website</span>
        </a>
      </nav>
      <div class="sidebar-footer">
        <div class="user-mini-avatar">CS</div>
        <div class="user-mini-info">
          <div class="user-mini-name">Logged In User</div>
          <div class="user-mini-role">{role_data["title"]}</div>
        </div>
        <button class="btn btn-icon btn-secondary" onclick="CivicAuth.logout()" title="Logout">
          <i class="fa-solid fa-right-from-bracket"></i>
        </button>
      </div>
    </aside>
    """

def get_topbar_html():
    return """
    <header class="app-topbar">
      <div class="flex items-center gap-2">
        <button id="mobileMenuToggle" class="btn btn-icon btn-secondary" style="display:none;" title="Toggle Menu">
          <i class="fa-solid fa-bars"></i>
        </button>
        <div class="topbar-search">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="text" placeholder="Search problem ID, category, ward, or keyword...">
        </div>
      </div>
      <div class="topbar-actions">
        <!-- Demo Mode Role Selector -->
        <div class="flex items-center gap-1">
          <span style="font-size:0.75rem; font-weight:700; color:var(--muted); text-transform:uppercase;">Demo Role:</span>
          <select id="demoRoleSelector" class="form-select" style="padding:0.35rem 0.65rem; font-size:0.85rem; width:auto;">
            <option value="citizen">Citizen</option>
            <option value="authority">Authority Officer</option>
            <option value="government">Government Official</option>
            <option value="admin">System Admin</option>
            <option value="university">University Team</option>
            <option value="faculty">Faculty Mentor</option>
            <option value="student">Student Team</option>
            <option value="industry">Industry Partner</option>
          </select>
        </div>

        <button class="theme-toggle-btn" title="Toggle Dark/Light Mode">
          <i class="fa-solid fa-moon"></i>
        </button>

        <a href="notifications.html" class="topbar-btn" title="Notifications">
          <i class="fa-solid fa-bell"></i>
          <span class="topbar-badge"></span>
        </a>

        <a href="submit-problem.html" class="btn btn-sm btn-primary">
          <i class="fa-solid fa-circle-plus"></i> Report Issue
        </a>
      </div>
    </header>
    """

def build_dashboard_page(filename, title, subtitle, role, content_html, extra_head="", extra_scripts=""):
    sidebar_html = get_sidebar_html(role, filename)
    topbar_html = get_topbar_html()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - CivicSolve AI</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/dashboard.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="css/animations.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  {extra_head}
</head>
<body>
  <div class="app-wrapper">
    {sidebar_html}
    <div class="app-main">
      {topbar_html}
      <main class="app-content">
        <div class="page-header">
          <div>
            <h1 class="page-title">{title}</h1>
            <p class="page-subtitle">{subtitle}</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="badge badge-neutral"><i class="fa-regular fa-clock"></i> Live Synced</span>
          </div>
        </div>
        {content_html}
      </main>
    </div>
  </div>

  <div id="toastContainer" class="toast-container"></div>

  <script src="js/data.js"></script>
  <script src="js/utils.js"></script>
  <script src="js/auth.js"></script>
  <script src="js/ai-analysis.js"></script>
  <script src="js/app.js"></script>
  {extra_scripts}
</body>
</html>"""

# Now write specific pages
pages = {}

# 1. citizen-dashboard.html
pages["citizen-dashboard.html"] = build_dashboard_page(
    "citizen-dashboard.html",
    "Good Evening, Citizen 👋",
    "Track your reported community issues, view AI analysis status and stay updated with your neighborhood.",
    "citizen",
    """
    <!-- Quick Stats -->
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-bullhorn"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statSubmitted">3</div>
          <div class="stat-label">Problems Submitted</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-hourglass-half"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statUnderReview">1</div>
          <div class="stat-label">Under AI Review</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-screwdriver-wrench"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statInProgress">1</div>
          <div class="stat-label">Work in Progress</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-circle-check"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statResolved">1</div>
          <div class="stat-label">Verified Resolved</div>
        </div>
      </div>
    </div>

    <!-- AI Insight Alert Banner -->
    <div class="ai-analysis-card" style="margin-bottom: 2rem;">
      <div class="ai-scan-bar"></div>
      <div class="flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-2">
          <span class="badge badge-primary"><i class="fa-solid fa-microchip"></i> Civic AI Advisory</span>
          <span style="font-weight:700; color:var(--dark);">Pothole on MG Road (CS-2026-0001) elevated to Priority 92/100</span>
        </div>
        <span class="badge badge-warning"><i class="fa-solid fa-bolt"></i> High Priority Action</span>
      </div>
      <p style="font-size:0.9rem; color:var(--muted); margin-top:0.5rem;">
        Public Works Department has mobilized asphalt machinery. An engineering student team from NIT has also proposed a high-durability recycled plastic road composite solution!
      </p>
    </div>

    <!-- Recent Complaints Table / Cards -->
    <div class="card" style="margin-bottom: 2rem;">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-clock-rotate-left"></i> Your Submitted Community Issues</h3>
        <a href="submit-problem.html" class="btn btn-sm btn-primary"><i class="fa-solid fa-plus"></i> New Complaint</a>
      </div>
      <div class="table-responsive">
        <table class="custom-table" id="citizenComplaintsTable">
          <thead>
            <tr>
              <th>Problem ID</th>
              <th>Title</th>
              <th>Category</th>
              <th>Severity</th>
              <th>Assigned Authority</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CS-2026-0001</strong></td>
              <td>Hazardous Deep Potholes on MG Road Junction</td>
              <td><span class="badge badge-neutral">Road</span></td>
              <td><span class="badge badge-warning">High</span></td>
              <td>Public Works Department</td>
              <td><span class="badge badge-primary">In Progress</span></td>
              <td><a href="problem-details.html?id=CS-2026-0001" class="btn btn-sm btn-secondary">View Track</a></td>
            </tr>
            <tr>
              <td><strong>CS-2026-0002</strong></td>
              <td>Contaminated Turbid Drinking Water Supply</td>
              <td><span class="badge badge-neutral">Water</span></td>
              <td><span class="badge badge-danger">Critical</span></td>
              <td>Water Supply Board (BWSSB)</td>
              <td><span class="badge badge-danger">Escalated</span></td>
              <td><a href="problem-details.html?id=CS-2026-0002" class="btn btn-sm btn-secondary">View Track</a></td>
            </tr>
            <tr>
              <td><strong>CS-2026-0006</strong></td>
              <td>Primary Health Center Lacks Cold Chain & Vaccines</td>
              <td><span class="badge badge-neutral">Healthcare</span></td>
              <td><span class="badge badge-warning">High</span></td>
              <td>Health & Family Welfare Dept</td>
              <td><span class="badge badge-success">Resolved</span></td>
              <td><a href="problem-details.html?id=CS-2026-0006" class="btn btn-sm btn-secondary">View Track</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Nearby Map Preview -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-map-pin text-primary"></i> Issues in Your Local Ward (1.5km Radius)</h3>
        <a href="government-map.html" class="btn btn-sm btn-secondary">Full Screen Map</a>
      </div>
      <div id="civicMap" style="height:320px;"></div>
    </div>
    """,
    """<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />""",
    """
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="js/map.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        CivicMap.init("civicMap", 12.9716, 77.5946, 13);
      });
    </script>
    """
)

# 2. submit-problem.html
pages["submit-problem.html"] = build_dashboard_page(
    "submit-problem.html",
    "Submit a Civic Problem",
    "Multi-step wizard with real browser GPS, live camera capture, and real-time AI categorization & duplicate check.",
    "citizen",
    """
    <!-- Wizard Step Progress -->
    <div class="card" style="margin-bottom: 2rem; padding: 1.25rem 2rem;">
      <div class="flex items-center justify-between" style="position:relative;">
        <div class="step-indicator-item active" id="ind1" style="text-align:center;">
          <div style="width:36px; height:36px; border-radius:50%; background:var(--primary); color:#fff; display:flex; align-items:center; justify-content:center; margin:0 auto; font-weight:700;">1</div>
          <span style="font-size:0.8rem; font-weight:600; margin-top:0.35rem; display:block;">Problem Info</span>
        </div>
        <div class="step-indicator-item" id="ind2" style="text-align:center;">
          <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-subtle); color:var(--muted); display:flex; align-items:center; justify-content:center; margin:0 auto; font-weight:700;">2</div>
          <span style="font-size:0.8rem; font-weight:600; margin-top:0.35rem; display:block;">Location GPS</span>
        </div>
        <div class="step-indicator-item" id="ind3" style="text-align:center;">
          <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-subtle); color:var(--muted); display:flex; align-items:center; justify-content:center; margin:0 auto; font-weight:700;">3</div>
          <span style="font-size:0.8rem; font-weight:600; margin-top:0.35rem; display:block;">Camera Proof</span>
        </div>
        <div class="step-indicator-item" id="ind4" style="text-align:center;">
          <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-subtle); color:var(--muted); display:flex; align-items:center; justify-content:center; margin:0 auto; font-weight:700;">4</div>
          <span style="font-size:0.8rem; font-weight:600; margin-top:0.35rem; display:block;">AI Analysis</span>
        </div>
        <div class="step-indicator-item" id="ind5" style="text-align:center;">
          <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-subtle); color:var(--muted); display:flex; align-items:center; justify-content:center; margin:0 auto; font-weight:700;">5</div>
          <span style="font-size:0.8rem; font-weight:600; margin-top:0.35rem; display:block;">Review & Route</span>
        </div>
      </div>
    </div>

    <!-- Wizard Step Forms -->
    <div class="card" style="max-width: 800px; margin: 0 auto;">
      
      <!-- STEP 1: Problem Details -->
      <div id="step1" class="form-step">
        <h3 style="margin-bottom: 1.5rem;"><i class="fa-solid fa-circle-info text-primary"></i> Step 1: Problem Information</h3>
        <div class="form-group">
          <label class="form-label">Problem Title *</label>
          <input type="text" id="inputTitle" class="form-control" placeholder="e.g. Hazardous deep crater potholes near metro pillar 42" required>
        </div>
        <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
          <div class="form-group">
            <label class="form-label">Category *</label>
            <select id="inputCategory" class="form-select">
              <option value="Road">Road & Bridges</option>
              <option value="Water">Water & Sanitation</option>
              <option value="Waste">Solid Waste & Dumps</option>
              <option value="Electricity">Electricity & Power</option>
              <option value="Transport">Traffic & Transport</option>
              <option value="Healthcare">Healthcare Clinics</option>
              <option value="Education">School Infrastructure</option>
              <option value="Environment">Environmental Pollution</option>
              <option value="Public Safety">Public Safety & Lighting</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Severity Level</label>
            <select id="inputSeverity" class="form-select">
              <option value="High">High - Significant Safety Risk</option>
              <option value="Critical">Critical - Immediate Life Danger</option>
              <option value="Medium">Medium - Regular Disruption</option>
              <option value="Low">Low - Minor Inconvenience</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Detailed Description *</label>
          <textarea id="inputDesc" class="form-control" rows="4" placeholder="Describe when the issue began, hazards observed, affected landmark, and impact on local residents..."></textarea>
        </div>
        <div class="flex justify-between" style="margin-top:2rem;">
          <div></div>
          <button type="button" class="btn btn-primary" onclick="ProblemManager.goToStep(2)">Next: Location GPS →</button>
        </div>
      </div>

      <!-- STEP 2: Location -->
      <div id="step2" class="form-step" style="display:none;">
        <h3 style="margin-bottom: 1.5rem;"><i class="fa-solid fa-location-dot text-primary"></i> Step 2: Accurate Geolocation</h3>
        
        <div style="background:var(--bg-subtle); padding:1.25rem; border-radius:var(--radius-md); margin-bottom:1.5rem; text-align:center;">
          <p style="margin-bottom:0.75rem;">Detect your current device GPS coordinates for immediate satellite precision:</p>
          <button type="button" class="btn btn-accent" onclick="ProblemManager.detectLocation()">
            <i class="fa-solid fa-crosshairs"></i> Use Device Live GPS Location
          </button>
          <div id="geoStatus" style="font-size:0.85rem; margin-top:0.75rem; color:var(--muted);">Click to trigger browser Geolocation API.</div>
        </div>

        <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
          <div class="form-group">
            <label class="form-label">Latitude</label>
            <input type="text" id="inputLat" class="form-control" value="12.9716">
          </div>
          <div class="form-group">
            <label class="form-label">Longitude</label>
            <input type="text" id="inputLng" class="form-control" value="77.5946">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Street Address & Landmark</label>
          <input type="text" id="inputAddress" class="form-control" placeholder="Near Gate 2, Metro Pillar 42, MG Road">
        </div>

        <div class="flex justify-between" style="margin-top:2rem;">
          <button type="button" class="btn btn-secondary" onclick="ProblemManager.goToStep(1)">← Back</button>
          <button type="button" class="btn btn-primary" onclick="ProblemManager.goToStep(3)">Next: Camera Evidence →</button>
        </div>
      </div>

      <!-- STEP 3: Camera Evidence -->
      <div id="step3" class="form-step" style="display:none;">
        <h3 style="margin-bottom: 1.5rem;"><i class="fa-solid fa-camera text-primary"></i> Step 3: Evidence Capture</h3>
        
        <!-- Live Camera Container -->
        <div style="background:var(--bg-subtle); border:2px dashed var(--border); border-radius:var(--radius-lg); padding:1.5rem; text-align:center; margin-bottom:1.5rem;">
          <div id="cameraPlaceholder">
            <i class="fa-solid fa-camera-retro" style="font-size:3rem; color:var(--muted); margin-bottom:1rem;"></i>
            <p style="font-weight:600; margin-bottom:1rem;">Take photo directly with device camera via WebRTC:</p>
            <button type="button" class="btn btn-primary" onclick="ProblemManager.startCamera()">
              <i class="fa-solid fa-video"></i> Start Device Camera
            </button>
          </div>

          <div id="cameraLiveBox" style="display:none;">
            <video id="cameraVideo" autoplay playsinline style="width:100%; max-height:300px; border-radius:var(--radius-md); background:#000; margin-bottom:1rem;"></video>
            <div class="flex justify-center gap-2">
              <button type="button" class="btn btn-success" onclick="ProblemManager.capturePhoto()">
                <i class="fa-solid fa-circle-dot"></i> Snap Photo
              </button>
              <button type="button" class="btn btn-secondary" onclick="ProblemManager.stopCamera()">
                <i class="fa-solid fa-stop"></i> Stop Camera
              </button>
            </div>
          </div>

          <canvas id="cameraCanvas" style="display:none;"></canvas>
          <img id="capturedPhotoPreview" style="display:none; max-height:220px; margin:1rem auto; border-radius:var(--radius-md); border:2px solid var(--success);" alt="Captured Evidence">
        </div>

        <div class="form-group">
          <label class="form-label">Or upload images / video / PDF document</label>
          <input type="file" class="form-control" accept="image/*,video/*,.pdf" onchange="CivicUtils.showToast('File selected for upload validation.', 'info')">
        </div>

        <div class="flex justify-between" style="margin-top:2rem;">
          <button type="button" class="btn btn-secondary" onclick="ProblemManager.goToStep(2)">← Back</button>
          <button type="button" class="btn btn-primary" onclick="ProblemManager.goToStep(4)">Next: Run AI Analysis →</button>
        </div>
      </div>

      <!-- STEP 4: AI Analysis Simulator -->
      <div id="step4" class="form-step" style="display:none;">
        <h3 style="margin-bottom: 1.5rem;"><i class="fa-solid fa-microchip text-primary"></i> Step 4: AI Prioritization & Duplicate Detection</h3>
        
        <div id="aiAnalysisResults">
          <div style="text-align:center; padding:3rem 1rem;">
            <i class="fa-solid fa-brain fa-spin" style="font-size:3rem; color:var(--primary); margin-bottom:1.5rem;"></i>
            <h4>Civic AI Engine Running Semantic & Visual Extraction...</h4>
            <p>Scanning category taxonomy, detecting geographical duplicates, and calculating societal priority score...</p>
          </div>
        </div>

        <div class="flex justify-between" style="margin-top:2rem;">
          <button type="button" class="btn btn-secondary" onclick="ProblemManager.goToStep(3)">← Back</button>
          <button type="button" class="btn btn-primary" onclick="ProblemManager.goToStep(5)">Next: Review & Submit →</button>
        </div>
      </div>

      <!-- STEP 5: Final Review & Submission -->
      <div id="step5" class="form-step" style="display:none;">
        <h3 style="margin-bottom: 1.5rem;"><i class="fa-solid fa-clipboard-check text-primary"></i> Step 5: Review & Official Submission</h3>

        <div style="background:var(--bg-subtle); border-radius:var(--radius-lg); padding:1.5rem; margin-bottom:1.5rem;">
          <div class="flex items-center justify-between" style="margin-bottom:1rem;">
            <span style="font-size:0.85rem; color:var(--muted); font-weight:700;">ASSIGNED COMPLAINT TICKET ID:</span>
            <span class="badge badge-primary" id="revId" style="font-size:0.9rem;">CS-2026-0021</span>
          </div>
          <h4 id="revTitle" style="margin-bottom:0.75rem;">Hazardous Potholes</h4>
          <div class="flex items-center gap-3" style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">
            <span>Category: <strong id="revCat" class="text-dark">Road</strong></span>
            <span>•</span>
            <span>Target Authority: <strong id="revAuth" class="text-dark">PWD</strong></span>
          </div>
          <p style="font-size:0.85rem; color:var(--muted);">
            By submitting, your problem will be entered into the Admin Verification Desk and prioritized on the Government Command Center according to AI urgency scores.
          </p>
        </div>

        <div class="flex justify-between" style="margin-top:2rem;">
          <button type="button" class="btn btn-secondary" onclick="ProblemManager.goToStep(4)">← Back</button>
          <button type="button" class="btn btn-success btn-lg" onclick="ProblemManager.submitFinalProblem()">
            <i class="fa-solid fa-paper-plane"></i> Confirm & Submit to Authority
          </button>
        </div>
      </div>

    </div>
    """,
    "",
    """
    <script src="js/problems.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        // Auto initialize step 1
        ProblemManager.goToStep(1);
      });
    </script>
    """
)

# 3. my-problems.html
pages["my-problems.html"] = build_dashboard_page(
    "my-problems.html",
    "My Reported Problems",
    "Track all community complaints you have submitted, monitor progress bars, and view live status updates.",
    "citizen",
    """
    <!-- Filter bar -->
    <div class="card" style="margin-bottom: 2rem;">
      <div class="flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-2 flex-wrap">
          <button class="btn btn-sm btn-primary" onclick="filterProblems('All')">All (20)</button>
          <button class="btn btn-sm btn-secondary" onclick="filterProblems('Under Review')">Under Review</button>
          <button class="btn btn-sm btn-secondary" onclick="filterProblems('In Progress')">In Progress</button>
          <button class="btn btn-sm btn-secondary" onclick="filterProblems('Escalated')">Escalated</button>
          <button class="btn btn-sm btn-secondary" onclick="filterProblems('Resolved')">Resolved</button>
        </div>
        <a href="submit-problem.html" class="btn btn-sm btn-primary"><i class="fa-solid fa-plus"></i> Report Issue</a>
      </div>
    </div>

    <!-- Problems Cards Grid -->
    <div id="myProblemsGrid" class="dashboard-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem;">
      <!-- Populated dynamically by JS -->
    </div>
    """,
    "",
    """
    <script>
      function renderProblemCards(filter = 'All') {
        const grid = document.getElementById("myProblemsGrid");
        if (!grid) return;
        const problems = window.CivicDB.getProblems();
        
        let filtered = problems;
        if (filter !== 'All') {
          filtered = problems.filter(p => p.status.toLowerCase() === filter.toLowerCase());
        }

        grid.innerHTML = filtered.map(p => `
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="${p.images[0]}" alt="${p.title}">
              <div class="problem-badge-overlay">
                ${CivicUtils.getSeverityBadge(p.severity)}
                ${CivicUtils.getStatusBadge(p.status)}
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">${p.id} • ${p.category}</div>
              <h4 class="problem-title">${p.title}</h4>
              <p class="problem-desc">${p.description}</p>
              
              <div style="margin: 0.75rem 0;">
                <div class="flex justify-between" style="font-size:0.75rem; font-weight:600; color:var(--muted);">
                  <span>Resolution Progress</span>
                  <span>${p.status === 'Resolved' ? '100%' : (p.status === 'In Progress' ? '65%' : '20%')}</span>
                </div>
                <div class="progress-bar-wrap">
                  <div class="progress-fill" style="width: ${p.status === 'Resolved' ? '100%' : (p.status === 'In Progress' ? '65%' : '20%')};"></div>
                </div>
              </div>

              <div class="problem-meta">
                <span><i class="fa-solid fa-building-columns"></i> ${p.authorityName || 'Assigned Dept'}</span>
                <a href="problem-details.html?id=${p.id}" class="btn btn-sm btn-primary" style="padding:0.35rem 0.75rem;">Details →</a>
              </div>
            </div>
          </div>
        `).join("");
      }

      function filterProblems(st) {
        renderProblemCards(st);
      }

      document.addEventListener("DOMContentLoaded", () => {
        renderProblemCards('All');
      });
    </script>
    """
)

# 4. problem-details.html
pages["problem-details.html"] = build_dashboard_page(
    "problem-details.html",
    "Complaint Details & Full Lifecycle",
    "Complete transparency timeline from citizen submission to AI verification, authority dispatch, student prototyping and resolution.",
    "citizen",
    """
    <div style="display:grid; grid-template-columns: 2fr 1fr; gap: 2rem;" class="dashboard-grid-detail">
      
      <!-- Left Column: Details, Timeline, Feedback -->
      <div>
        <div class="card" style="margin-bottom: 2rem;">
          <div class="flex items-center justify-between flex-wrap gap-2" style="margin-bottom:1rem;">
            <div class="flex items-center gap-2">
              <span class="badge badge-primary" id="detId" style="font-size:0.9rem;">CS-2026-0001</span>
              <span id="detCategory" class="badge badge-neutral">Road</span>
              <span id="detSeverity"><span class="badge badge-warning">High</span></span>
            </div>
            <div id="detStatus"><span class="badge badge-primary">In Progress</span></div>
          </div>
          
          <h2 id="detTitle" style="margin-bottom:0.75rem;">Hazardous Deep Potholes on MG Road Junction</h2>
          <p id="detDesc" style="color:var(--muted); font-size:1rem; margin-bottom:1.5rem;"></p>

          <div style="border-radius:var(--radius-md); overflow:hidden; margin-bottom:1.5rem; max-height:360px;">
            <img id="detImg" src="https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?w=1200&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;">
          </div>

          <div class="flex items-center justify-between flex-wrap gap-2" style="padding-top:1rem; border-top:1px solid var(--border);">
            <div class="flex items-center gap-3">
              <button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('Upvoted! Priority weight increased.', 'success')">
                <i class="fa-solid fa-thumbs-up text-primary"></i> <span id="detUpvotes">184 Upvotes</span>
              </button>
              <button class="btn btn-sm btn-secondary" onclick="CivicUtils.shareProblem(document.getElementById('detTitle').textContent)">
                <i class="fa-solid fa-share-nodes"></i> Share
              </button>
            </div>
            <button class="btn btn-sm btn-success" onclick="CivicUtils.openModal('feedbackModal')">
              <i class="fa-solid fa-star"></i> Submit Citizen Feedback
            </button>
          </div>
        </div>

        <!-- Complete 11-Stage Workflow Timeline -->
        <div class="card" style="margin-bottom: 2rem;">
          <h3 class="card-title" style="margin-bottom: 1.5rem;"><i class="fa-solid fa-timeline text-primary"></i> End-to-End Problem Lifecycle</h3>
          <div class="timeline" id="detTimeline">
            <!-- Rendered by JS -->
          </div>
        </div>

        <!-- Community Comments -->
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 1rem;"><i class="fa-solid fa-comments"></i> Community Comments & Updates</h3>
          <div class="flex gap-2" style="margin-bottom:1.5rem;">
            <input type="text" id="newCommentInput" class="form-control" placeholder="Add an official observation or community update...">
            <button class="btn btn-primary" onclick="addComment()"><i class="fa-solid fa-paper-plane"></i></button>
          </div>
          <div id="commentsList">
            <!-- Rendered by JS -->
          </div>
        </div>
      </div>

      <!-- Right Column: AI Scorecard, Assigned Authority, Map -->
      <div>
        <!-- AI Card -->
        <div class="ai-analysis-card" style="margin-bottom: 2rem;">
          <div class="ai-scan-bar"></div>
          <div class="flex items-center justify-between" style="margin-bottom:1rem;">
            <span class="badge badge-primary"><i class="fa-solid fa-microchip"></i> Civic AI Metric</span>
            <span class="ai-metric-val" id="detPriorityScore">92/100</span>
          </div>
          <p style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">
            Severity, affected population density, and social impact indicators were analyzed to generate this score.
          </p>
          <div class="ai-metric-box">
            <div style="font-size:0.75rem; color:var(--muted); font-weight:700;">ESTIMATED CITIZENS AFFECTED</div>
            <div class="ai-metric-val" id="detAffectedCount" style="color:var(--accent);">1,400+</div>
          </div>
        </div>

        <!-- Authority Routing Box -->
        <div class="card" style="margin-bottom: 2rem;">
          <h3 class="card-title" style="margin-bottom: 1rem;"><i class="fa-solid fa-building-columns text-primary"></i> Assigned Authority</h3>
          <div style="font-weight:700; color:var(--dark); margin-bottom:0.25rem;" id="detAuthName">Public Works Department</div>
          <div style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;" id="detOfficer">Officer: Er. Rajesh Verma</div>
          
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:var(--radius-md); font-size:0.85rem; margin-bottom:1rem;">
            <div class="flex justify-between" style="margin-bottom:0.25rem;">
              <span>SLA Target:</span>
              <strong class="text-success">72 Hours</strong>
            </div>
            <div class="flex justify-between">
              <span>Time Left:</span>
              <strong class="text-warning" id="detSLA">18 Hours</strong>
            </div>
          </div>

          <div class="flex gap-2">
            <button class="btn btn-sm btn-secondary w-100" onclick="CivicUtils.showToast('Reminder alert dispatched to Zonal Officer desk.', 'info')">
              <i class="fa-solid fa-bell"></i> Send Reminder
            </button>
            <button class="btn btn-sm btn-danger w-100" onclick="CivicUtils.showToast('Escalation request submitted to District Magistrate.', 'warning')">
              <i class="fa-solid fa-fire"></i> Escalate
            </button>
          </div>
        </div>

        <!-- University Solution Card -->
        <div class="card">
          <h3 class="card-title" style="margin-bottom: 1rem;"><i class="fa-solid fa-graduation-cap text-primary"></i> Academic Solution</h3>
          <p style="font-size:0.85rem; color:var(--muted); margin-bottom:0.75rem;">
            Matched student innovation team developing pilot solution:
          </p>
          <div style="font-weight:700; color:var(--dark);">EcoPave Student Innovators</div>
          <div style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">National Institute of Technology</div>
          <a href="solution-workspace.html" class="btn btn-sm btn-accent w-100">
            <i class="fa-solid fa-flask"></i> View Solution Workspace
          </a>
        </div>
      </div>

    </div>

    <!-- Citizen Feedback Modal -->
    <div id="feedbackModal" class="modal-overlay">
      <div class="modal-box">
        <div class="modal-header">
          <h3 style="font-size:1.15rem; font-weight:700;"><i class="fa-solid fa-check-to-slot text-success"></i> Citizen Resolution Verification</h3>
          <button class="btn btn-icon btn-secondary" onclick="CivicUtils.closeModal('feedbackModal')"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="modal-body">
          <p style="font-size:0.95rem; margin-bottom:1.5rem;">Has this problem been resolved to your satisfaction by the assigned government authority?</p>
          
          <div class="flex justify-center gap-3" style="margin-bottom:2rem;">
            <button type="button" class="btn btn-lg btn-success" style="flex:1;" onclick="CivicUtils.showToast('Marked as Resolved by Citizen!', 'success')">
              <i class="fa-solid fa-thumbs-up"></i> Yes, Resolved
            </button>
            <button type="button" class="btn btn-lg btn-secondary" style="flex:1;" onclick="CivicUtils.showToast('Issue marked as Incomplete. Escalation triggered.', 'warning')">
              <i class="fa-solid fa-thumbs-down"></i> No, Not Solved
            </button>
          </div>

          <div class="form-group" style="text-align:center;">
            <label class="form-label">Rate Quality of Resolution</label>
            <div class="flex justify-center gap-2" style="font-size:1.75rem; cursor:pointer;">
              <i class="fa-solid fa-star text-warning feedback-star" data-value="1"></i>
              <i class="fa-solid fa-star text-warning feedback-star" data-value="2"></i>
              <i class="fa-solid fa-star text-warning feedback-star" data-value="3"></i>
              <i class="fa-solid fa-star text-warning feedback-star" data-value="4"></i>
              <i class="fa-solid fa-star text-warning feedback-star" data-value="5"></i>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Feedback Comments</label>
            <textarea id="feedbackComment" class="form-control" rows="3" placeholder="Provide any comments regarding work quality..."></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" onclick="CivicUtils.closeModal('feedbackModal')">Cancel</button>
          <button id="btnSubmitFeedback" class="btn btn-primary">Submit Verification</button>
        </div>
      </div>
    </div>
    """,
    "",
    """
    <script src="js/solutions.js"></script>
    <script>
      let currentProblem = null;

      document.addEventListener("DOMContentLoaded", () => {
        const urlParams = new URLSearchParams(window.location.search);
        const probId = urlParams.get('id') || 'CS-2026-0001';

        currentProblem = window.CivicDB.getProblemById(probId) || window.CivicDB.getProblems()[0];

        // Fill fields
        document.getElementById("detId").textContent = currentProblem.id;
        document.getElementById("detTitle").textContent = currentProblem.title;
        document.getElementById("detDesc").textContent = currentProblem.description;
        document.getElementById("detCategory").textContent = currentProblem.category;
        document.getElementById("detSeverity").innerHTML = CivicUtils.getSeverityBadge(currentProblem.severity);
        document.getElementById("detStatus").innerHTML = CivicUtils.getStatusBadge(currentProblem.status);
        document.getElementById("detPriorityScore").textContent = (currentProblem.priorityScore || 85) + "/100 Priority";
        document.getElementById("detAffectedCount").textContent = (currentProblem.affectedCount || 1000) + "+ Citizens";
        document.getElementById("detAuthName").textContent = currentProblem.authorityName || 'Assigned Authority';
        document.getElementById("detOfficer").textContent = "Assigned: " + (currentProblem.assignedOfficer || 'Zonal Officer');
        document.getElementById("detUpvotes").textContent = (currentProblem.upvotes || 42) + " Upvotes";
        if (currentProblem.images && currentProblem.images[0]) {
          document.getElementById("detImg").src = currentProblem.images[0];
        }

        renderTimeline(currentProblem.timeline || []);
        renderComments(currentProblem.comments || []);
        CivicSolutions.initFeedbackRating();
      });

      function renderTimeline(timeline) {
        const container = document.getElementById("detTimeline");
        if (!container) return;

        const defaultStages = [
          { date: "2026-09-24 10:30", actor: "Citizen", action: "1. Problem Submitted", note: "Reported with live GPS verification." },
          { date: "2026-09-24 10:32", actor: "Civic AI Core", action: "2. AI Analysis & Priority Score", note: "Severity calculated. Duplicates checked." },
          { date: "2026-09-24 14:15", actor: "Admin Verification", action: "3. Admin Verified", note: "Authenticity confirmed by desk." },
          { date: "2026-09-25 09:00", actor: "Government Desk", action: "4. Authority Routed & SLA Started", note: "Assigned to department work queue." },
          { date: "2026-09-25 11:30", actor: "Zonal Officer", action: "5. Officer Accepted & Work Mobilized", note: "Inspection scheduled on site." },
          { date: "2026-09-26 14:00", actor: "University Partner", action: "6. Collaborative Solution Linked", note: "Student innovation team matched." }
        ];

        const list = timeline.length > 0 ? timeline : defaultStages;

        container.innerHTML = list.map((item, idx) => `
          <div class="timeline-item">
            <div class="timeline-dot ${idx === list.length - 1 ? 'active' : ''}"></div>
            <div class="timeline-content">
              <h5>${item.action}</h5>
              <time><i class="fa-regular fa-clock"></i> ${item.date} • by <strong>${item.actor}</strong></time>
              <p style="font-size:0.875rem; color:var(--dark);">${item.note}</p>
            </div>
          </div>
        `).join("");
      }

      function renderComments(comments) {
        const container = document.getElementById("commentsList");
        if (!container) return;

        if (comments.length === 0) {
          container.innerHTML = '<p style="color:var(--muted); font-size:0.85rem;">No community comments yet. Be the first to add an update!</p>';
          return;
        }

        container.innerHTML = comments.map(c => `
          <div style="background:var(--bg-subtle); padding:0.75rem 1rem; border-radius:var(--radius-md); margin-bottom:0.75rem;">
            <div class="flex justify-between" style="font-size:0.8rem; font-weight:700; color:var(--dark); margin-bottom:0.25rem;">
              <span>${c.user}</span>
              <span style="color:var(--muted);">${c.date || 'Recent'}</span>
            </div>
            <p style="font-size:0.85rem; color:var(--dark);">${c.text}</p>
          </div>
        `).join("");
      }

      function addComment() {
        const input = document.getElementById("newCommentInput");
        if (!input || !input.value.trim()) return;

        const newComment = {
          user: CivicAuth.getUser().name,
          text: input.value.trim(),
          date: "Just now"
        };

        if (currentProblem) {
          currentProblem.comments = currentProblem.comments || [];
          currentProblem.comments.unshift(newComment);
          window.CivicDB.saveProblem(currentProblem);
          renderComments(currentProblem.comments);
          input.value = "";
          CivicUtils.showToast("Comment added to official discussion.", "success");
        }
      }
    </script>
    """
)

# 5. government-dashboard.html
pages["government-dashboard.html"] = build_dashboard_page(
    "government-dashboard.html",
    "Government Civic Command Center",
    "Executive-level overview of citywide problems, real-time SLA health, department allocations, and AI analytics.",
    "government",
    """
    <!-- 8 Executive Stats -->
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-city"></i></div>
        <div class="stat-info">
          <div class="stat-value">12,458</div>
          <div class="stat-label">Total Problems</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon danger"><i class="fa-solid fa-triangle-exclamation"></i></div>
        <div class="stat-info">
          <div class="stat-value">28</div>
          <div class="stat-label">Critical Incidents</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-bolt"></i></div>
        <div class="stat-info">
          <div class="stat-value">142</div>
          <div class="stat-label">High Priority</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-spinner"></i></div>
        <div class="stat-info">
          <div class="stat-value">2,480</div>
          <div class="stat-label">In Progress</div>
        </div>
      </div>
    </div>

    <!-- AI Command Assistant Panel -->
    <div class="ai-analysis-card" style="margin-bottom: 2rem;">
      <div class="ai-scan-bar"></div>
      <h3 style="margin-bottom: 0.5rem;"><i class="fa-solid fa-brain text-primary"></i> AI Command Query Assistant</h3>
      <p style="font-size:0.9rem; color:var(--muted); margin-bottom:1rem;">
        Ask high-level queries across municipal databases for immediate AI synthesized intelligence:
      </p>
      <div class="flex gap-2 flex-wrap" style="margin-bottom:1rem;">
        <button class="btn btn-sm btn-secondary" onclick="askAIPrompt('Show critical road problems')">"Show critical road problems"</button>
        <button class="btn btn-sm btn-secondary" onclick="askAIPrompt('Which district has the most unresolved waste issues?')">"Which district has most waste issues?"</button>
        <button class="btn btn-sm btn-secondary" onclick="askAIPrompt('Show overdue SLA problems')">"Show overdue problems"</button>
        <button class="btn btn-sm btn-secondary" onclick="askAIPrompt('Find duplicate complaints')">"Find duplicate complaints"</button>
      </div>
      <div id="aiPromptOutput" style="display:none; background:var(--bg-card); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border); font-size:0.9rem;">
        <!-- Populated by JS -->
      </div>
    </div>

    <!-- Charts Row 1 -->
    <div class="dashboard-grid-2" style="display:grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
      <div class="card">
        <div class="card-header">
          <h3 class="card-title"><i class="fa-solid fa-chart-pie text-primary"></i> Problems by Category</h3>
          <span class="badge badge-neutral">Live</span>
        </div>
        <canvas id="chartCategory" style="max-height:280px;"></canvas>
      </div>

      <div class="card">
        <div class="card-header">
          <h3 class="card-title"><i class="fa-solid fa-chart-line text-success"></i> Resolution Trends (Monthly)</h3>
          <span class="badge badge-success">+14% Growth</span>
        </div>
        <canvas id="chartTrends" style="max-height:280px;"></canvas>
      </div>
    </div>

    <!-- Charts Row 2 -->
    <div class="dashboard-grid-2" style="display:grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
      <div class="card">
        <div class="card-header">
          <h3 class="card-title"><i class="fa-solid fa-chart-column text-accent"></i> District Workload Comparison</h3>
          <a href="government-analytics.html" class="btn btn-sm btn-secondary">Deep Dive</a>
        </div>
        <canvas id="chartDistricts" style="max-height:280px;"></canvas>
      </div>

      <div class="card">
        <div class="card-header">
          <h3 class="card-title"><i class="fa-solid fa-signal text-warning"></i> Incident Severity Distribution</h3>
        </div>
        <canvas id="chartSeverity" style="max-height:280px;"></canvas>
      </div>
    </div>

    <!-- Escalation Quick Center -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-triangle-exclamation text-danger"></i> Urgent SLA Breaches Requiring Commissioner Review</h3>
        <a href="escalation-center.html" class="btn btn-sm btn-danger">Escalation Center →</a>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Incident</th>
              <th>Authority</th>
              <th>Officer</th>
              <th>SLA Status</th>
              <th>Escalation Level</th>
              <th>Direct Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CS-2026-0002</strong></td>
              <td>Contaminated Turbid Drinking Water Supply</td>
              <td>Water Supply Board (BWSSB)</td>
              <td>Smt. Kavita Rao</td>
              <td><span class="badge badge-danger">-12h Overdue</span></td>
              <td><span class="badge badge-warning">Tier-2 Senior Officer</span></td>
              <td><button class="btn btn-sm btn-danger" onclick="CivicUtils.showToast('Urgent commissioner summons issued to BWSSB chief.', 'warning')">Summon Chief</button></td>
            </tr>
            <tr>
              <td><strong>CS-2026-0014</strong></td>
              <td>Unsegregated Medical Waste Dumped Behind Clinic</td>
              <td>Health & Pollution Board</td>
              <td>Dr. B. Manjunath</td>
              <td><span class="badge badge-warning">2h Remaining</span></td>
              <td><span class="badge badge-accent">Tier-1 Authority Reminder</span></td>
              <td><button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('Reminder pushed to Zonal Officer phone.', 'info')">Send Alert</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """,
    """<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>""",
    """
    <script src="js/analytics.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        CivicAnalytics.initCharts();
      });

      function askAIPrompt(query) {
        const out = document.getElementById("aiPromptOutput");
        out.style.display = "block";
        out.innerHTML = `<em>Querying city civic data lake for: "${query}"...</em>`;

        setTimeout(() => {
          let response = "";
          if (query.includes("road")) {
            response = "<strong>AI Finding:</strong> Found 4 Critical road incidents. Highest risk is <strong>CS-2026-0001 (MG Road)</strong> and <strong>CS-2026-0010 (Kengeri Underpass)</strong> with 6,600 total citizens affected.";
          } else if (query.includes("waste")) {
            response = "<strong>AI Finding:</strong> <strong>Central District</strong> has the highest volume of waste complaints (18 complaints), with Ward 12 and Ward 14 needing immediate truck deployment.";
          } else if (query.includes("overdue")) {
            response = "<strong>AI Finding:</strong> 1 Critical complaint has breached SLA: <strong>CS-2026-0002 (Drinking Water Contamination)</strong> - 12 hours overdue.";
          } else {
            response = "<strong>AI Finding:</strong> Analyzed 20 complaints in active grid. 2 complaints flagged with 85%+ semantic similarity for merging in East District.";
          }

          out.innerHTML = `
            <div class="flex items-center gap-2" style="margin-bottom:0.5rem; color:var(--primary); font-weight:700;">
              <i class="fa-solid fa-sparkles"></i> Civic AI Assistant Response
            </div>
            <p>${response}</p>
          `;
        }, 600);
      }
    </script>
    """
)

# 6. government-map.html
pages["government-map.html"] = build_dashboard_page(
    "government-map.html",
    "Government Citywide Incident Map",
    "Geographic visualization of all reported societal issues color-coded by priority with interactive filtering.",
    "government",
    """
    <!-- Map Filters Bar -->
    <div class="card" style="margin-bottom: 1.5rem;">
      <div class="flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-2 flex-wrap">
          <label style="font-size:0.85rem; font-weight:600; color:var(--muted);">Filter Category:</label>
          <select id="mapFilterCat" class="form-select" style="width:auto;" onchange="updateMapMarkers()">
            <option value="All">All Categories</option>
            <option value="Road">Road</option>
            <option value="Water">Water</option>
            <option value="Waste">Waste</option>
            <option value="Electricity">Electricity</option>
            <option value="Transport">Transport</option>
            <option value="Healthcare">Healthcare</option>
          </select>

          <label style="font-size:0.85rem; font-weight:600; color:var(--muted); margin-left:1rem;">Priority:</label>
          <select id="mapFilterPri" class="form-select" style="width:auto;" onchange="updateMapMarkers()">
            <option value="All">All Priorities</option>
            <option value="Critical">Critical</option>
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>

        <div class="flex items-center gap-3">
          <span style="font-size:0.8rem; font-weight:700; color:#EF4444;"><i class="fa-solid fa-circle"></i> Critical</span>
          <span style="font-size:0.8rem; font-weight:700; color:#F59E0B;"><i class="fa-solid fa-circle"></i> High</span>
          <span style="font-size:0.8rem; font-weight:700; color:#06B6D4;"><i class="fa-solid fa-circle"></i> Medium</span>
          <span style="font-size:0.8rem; font-weight:700; color:#10B981;"><i class="fa-solid fa-circle"></i> Low</span>
        </div>
      </div>
    </div>

    <!-- Map Container -->
    <div class="card" style="padding: 0; overflow: hidden;">
      <div id="fullScreenMap" style="height: 600px; width: 100%;"></div>
    </div>
    """,
    """<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />""",
    """
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="js/map.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        CivicMap.init("fullScreenMap", 12.9716, 77.5946, 12);
      });

      function updateMapMarkers() {
        const cat = document.getElementById("mapFilterCat").value;
        const pri = document.getElementById("mapFilterPri").value;
        CivicMap.loadProblemMarkers(cat, pri);
        CivicUtils.showToast(`Map updated for: ${cat} / ${pri}`, "info", 1500);
      }
    </script>
    """
)

# 7. social-feed.html
pages["social-feed.html"] = build_dashboard_page(
    "social-feed.html",
    "Civic Community Social Feed",
    "Public engagement stream where citizens upvote priority issues, participate in discussions, and share verified complaints to social media.",
    "citizen",
    """
    <div style="display:grid; grid-template-columns: 2fr 1fr; gap: 2rem;" class="dashboard-grid-detail">
      
      <!-- Feed Stream -->
      <div>
        <div class="card" style="margin-bottom: 2rem;">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <button class="btn btn-sm btn-primary">Trending</button>
              <button class="btn btn-sm btn-secondary">Near Me</button>
              <button class="btn btn-sm btn-secondary">Critical</button>
              <button class="btn btn-sm btn-secondary">Resolved</button>
            </div>
            <a href="submit-problem.html" class="btn btn-sm btn-outline-primary"><i class="fa-solid fa-bullhorn"></i> Post Issue</a>
          </div>
        </div>

        <div id="socialFeedPosts">
          <!-- Rendered by JS -->
        </div>
      </div>

      <!-- Right Trending & AI Share Card -->
      <div>
        <!-- AI Generated Shareable Graphic Card -->
        <div class="ai-analysis-card" style="margin-bottom: 2rem;">
          <div class="ai-scan-bar"></div>
          <h4 style="margin-bottom: 0.5rem;"><i class="fa-solid fa-share-nodes text-primary"></i> AI Shareable Poster</h4>
          <p style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">
            Generate an instant verified awareness graphic for WhatsApp groups or Twitter / X:
          </p>
          <div style="background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-md); padding:1rem; margin-bottom:1rem;">
            <div style="font-size:0.75rem; font-weight:700; color:var(--danger);"><i class="fa-solid fa-bell"></i> CITIZEN REPORT HIGHLIGHT</div>
            <h5 style="margin:0.25rem 0;">Hazardous Potholes on MG Road</h5>
            <p style="font-size:0.8rem; color:var(--muted);">1,400+ Citizens Impacted • PWD Assigned</p>
          </div>
          <button class="btn btn-sm btn-primary w-100" onclick="CivicUtils.shareProblem('Hazardous Potholes on MG Road')">
            <i class="fa-solid fa-paper-plane"></i> Share to WhatsApp / Social Media
          </button>
        </div>

        <!-- Trending Topics -->
        <div class="card">
          <h4 class="card-title" style="margin-bottom: 1rem;"><i class="fa-solid fa-arrow-trend-up text-accent"></i> Top Trending Hotspots</h4>
          <ul style="display:flex; flex-direction:column; gap:0.75rem;">
            <li class="flex justify-between items-center" style="font-size:0.9rem;">
              <span>#ShastriNagarWater</span>
              <span class="badge badge-danger">342 Upvotes</span>
            </li>
            <li class="flex justify-between items-center" style="font-size:0.9rem;">
              <span>#MGRoadPotholes</span>
              <span class="badge badge-warning">184 Upvotes</span>
            </li>
            <li class="flex justify-between items-center" style="font-size:0.9rem;">
              <span>#VarthurLakeFoam</span>
              <span class="badge badge-accent">512 Upvotes</span>
            </li>
            <li class="flex justify-between items-center" style="font-size:0.9rem;">
              <span>#KoramangalaPowerLines</span>
              <span class="badge badge-danger">412 Upvotes</span>
            </li>
          </ul>
        </div>
      </div>

    </div>
    """,
    "",
    """
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        const container = document.getElementById("socialFeedPosts");
        if (!container) return;

        const problems = window.CivicDB.getProblems().slice(0, 5);

        container.innerHTML = problems.map(p => `
          <div class="card" style="margin-bottom: 1.5rem;">
            <div class="flex items-center justify-between" style="margin-bottom:1rem;">
              <div class="flex items-center gap-2">
                <div class="user-mini-avatar" style="width:36px; height:36px; font-size:0.8rem;">CR</div>
                <div>
                  <div style="font-weight:700; font-size:0.9rem; color:var(--dark);">Citizen Reporter</div>
                  <div style="font-size:0.75rem; color:var(--muted);">${p.location ? p.location.address : 'Central Ward'}</div>
                </div>
              </div>
              <div>${CivicUtils.getStatusBadge(p.status)}</div>
            </div>

            <h3 style="font-size:1.15rem; margin-bottom:0.5rem; color:var(--dark);">${p.title}</h3>
            <p style="font-size:0.9rem; color:var(--muted); margin-bottom:1rem;">${p.description}</p>

            <div style="height:240px; border-radius:var(--radius-md); overflow:hidden; margin-bottom:1rem;">
              <img src="${p.images[0]}" style="width:100%; height:100%; object-fit:cover;">
            </div>

            <div class="flex items-center justify-between flex-wrap gap-2" style="padding-top:0.75rem; border-top:1px solid var(--border);">
              <div class="flex items-center gap-3">
                <button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('Upvoted!', 'success')">
                  <i class="fa-solid fa-thumbs-up text-primary"></i> ${p.upvotes || 45}
                </button>
                <a href="problem-details.html?id=${p.id}" class="btn btn-sm btn-secondary">
                  <i class="fa-solid fa-comment"></i> Comments
                </a>
              </div>
              <button class="btn btn-sm btn-secondary" onclick="CivicUtils.shareProblem('${p.title}')">
                <i class="fa-solid fa-share-nodes"></i> Share
              </button>
            </div>
          </div>
        `).join("");
      });
    </script>
    """
)

# 8. solution-workspace.html
pages["solution-workspace.html"] = build_dashboard_page(
    "solution-workspace.html",
    "Solution Innovation Workspace",
    "Collaborative workspace connecting Student Teams, Faculty Mentors, and Industry Sponsors to engineer and test pilot solutions.",
    "student",
    """
    <!-- Workspace Overview Header -->
    <div class="card" style="margin-bottom: 2rem;">
      <div class="flex items-center justify-between flex-wrap gap-3">
        <div>
          <div class="flex items-center gap-2" style="margin-bottom:0.5rem;">
            <span class="badge badge-primary">Active Innovation Project</span>
            <span class="badge badge-success">Faculty Approved</span>
          </div>
          <h2>SmartFlow: Computer-Vision Adaptive Signal Timing</h2>
          <p style="font-size:0.9rem; color:var(--muted);">
            Assigned Civic Issue: <strong>CS-2026-0005 (Indiranagar Traffic Congestion Hotspot)</strong> • Team: EcoPave / RV College
          </p>
        </div>
        <div class="flex gap-2">
          <a href="https://github.com" target="_blank" class="btn btn-secondary"><i class="fa-brands fa-github"></i> GitHub Repo</a>
          <button class="btn btn-primary" onclick="CivicUtils.showToast('Pilot testing metrics submitted to Traffic Dept!', 'success')">
            <i class="fa-solid fa-rocket"></i> Submit Pilot Data
          </button>
        </div>
      </div>
    </div>

    <!-- AI Evaluation Radar / Feasibility Box -->
    <div class="ai-analysis-card" style="margin-bottom: 2rem;">
      <div class="ai-scan-bar"></div>
      <div class="flex items-center justify-between flex-wrap gap-2" style="margin-bottom:1rem;">
        <h4 style="color:var(--dark);"><i class="fa-solid fa-wand-magic-sparkles text-primary"></i> AI Solution Feasibility & Impact Evaluation</h4>
        <span class="badge badge-success" style="font-size:0.85rem;">Overall AI Score: 94 / 100</span>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:1rem;">
        <div class="ai-metric-box">
          <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">PROBLEM RELEVANCE</div>
          <div class="ai-metric-val">98%</div>
        </div>
        <div class="ai-metric-box">
          <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">TECHNICAL FEASIBILITY</div>
          <div class="ai-metric-val">92%</div>
        </div>
        <div class="ai-metric-box">
          <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">SCALABILITY</div>
          <div class="ai-metric-val">88%</div>
        </div>
        <div class="ai-metric-box">
          <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">ESTIMATED COST SAVING</div>
          <div class="ai-metric-val text-success">₹ 14.2 Lakhs</div>
        </div>
      </div>
    </div>

    <!-- Kanban Task Board -->
    <div class="kanban-grid">
      <!-- Column 1: To Do -->
      <div class="kanban-col">
        <div class="kanban-col-header">
          <span><i class="fa-solid fa-list-check text-muted"></i> To Do (2)</span>
          <button class="btn btn-icon btn-sm btn-secondary" onclick="CivicUtils.showToast('Task creation modal opened.', 'info')"><i class="fa-solid fa-plus"></i></button>
        </div>
        <div class="kanban-card">
          <div class="badge badge-neutral" style="margin-bottom:0.5rem;">Hardware</div>
          <h5 style="margin-bottom:0.25rem;">Procure Edge AI Jetson Nano</h5>
          <p style="font-size:0.8rem; color:var(--muted);">Acquire sensor enclosure for monsoon weatherproofing.</p>
        </div>
        <div class="kanban-card">
          <div class="badge badge-accent" style="margin-bottom:0.5rem;">Documentation</div>
          <h5 style="margin-bottom:0.25rem;">Safety Clearance Filing</h5>
          <p style="font-size:0.8rem; color:var(--muted);">Submit technical safety spec to Traffic Police Ward.</p>
        </div>
      </div>

      <!-- Column 2: In Progress -->
      <div class="kanban-col">
        <div class="kanban-col-header">
          <span><i class="fa-solid fa-spinner text-primary"></i> In Progress (2)</span>
        </div>
        <div class="kanban-card">
          <div class="badge badge-primary" style="margin-bottom:0.5rem;">Computer Vision</div>
          <h5 style="margin-bottom:0.25rem;">YOLOv8 Vehicle Density Counter</h5>
          <p style="font-size:0.8rem; color:var(--muted);">Optimizing inference speed for real-time intersection cameras.</p>
        </div>
        <div class="kanban-card">
          <div class="badge badge-warning" style="margin-bottom:0.5rem;">IoT Firmware</div>
          <h5 style="margin-bottom:0.25rem;">Relay Trigger Logic</h5>
          <p style="font-size:0.8rem; color:var(--muted);">Syncing green light duration with queue length.</p>
        </div>
      </div>

      <!-- Column 3: Review -->
      <div class="kanban-col">
        <div class="kanban-col-header">
          <span><i class="fa-solid fa-eye text-warning"></i> Faculty Review (1)</span>
        </div>
        <div class="kanban-card">
          <div class="badge badge-secondary" style="margin-bottom:0.5rem;">Mentor Verification</div>
          <h5 style="margin-bottom:0.25rem;">Pilot Simulation Results</h5>
          <p style="font-size:0.8rem; color:var(--muted);">Reviewed by Dr. Meera Nambiar (38% queue reduction verified).</p>
        </div>
      </div>

      <!-- Column 4: Completed -->
      <div class="kanban-col">
        <div class="kanban-col-header">
          <span><i class="fa-solid fa-circle-check text-success"></i> Completed (3)</span>
        </div>
        <div class="kanban-card">
          <div class="badge badge-success" style="margin-bottom:0.5rem;">Problem Intake</div>
          <h5 style="margin-bottom:0.25rem;">Dataset Collection on Indiranagar 100ft</h5>
          <p style="font-size:0.8rem; color:var(--muted);">Annotated 5,000 video frames of peak rush traffic.</p>
        </div>
      </div>
    </div>
    """
)

# 9. escalation-center.html
pages["escalation-center.html"] = build_dashboard_page(
    "escalation-center.html",
    "SLA Escalation Center",
    "Automated governmental oversight tracking SLA violations across departments and triggering multi-tier administrative reviews.",
    "government",
    """
    <!-- Escalation Rules Hierarchy Banner -->
    <div class="card" style="margin-bottom: 2rem;">
      <h3 class="card-title" style="margin-bottom: 1rem;"><i class="fa-solid fa-gavel text-primary"></i> 4-Tier Automated Escalation Protocol</h3>
      <div class="dashboard-grid-4">
        <div style="background:var(--bg-subtle); padding:1rem; border-radius:var(--radius-md);">
          <strong class="text-primary">Tier 1: 0–2 Days</strong>
          <p style="font-size:0.8rem; margin-top:0.25rem;">Automated SMS & Dashboard reminder to Assigned Authority Officer.</p>
        </div>
        <div style="background:var(--warning-light); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--warning);">
          <strong class="text-warning">Tier 2: 3–5 Days</strong>
          <p style="font-size:0.8rem; margin-top:0.25rem;">Escalation dispatched to Zonal Executive Engineer & Deputy Director.</p>
        </div>
        <div style="background:var(--danger-light); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--danger);">
          <strong class="text-danger">Tier 3: 6–10 Days</strong>
          <p style="font-size:0.8rem; margin-top:0.25rem;">Summons dispatched to Department Head & Municipal Chief.</p>
        </div>
        <div style="background:var(--primary-light); padding:1rem; border-radius:var(--radius-md);">
          <strong class="text-primary">Tier 4: 10+ Days</strong>
          <p style="font-size:0.8rem; margin-top:0.25rem;">Commissioner & District Magistrate executive review docket.</p>
        </div>
      </div>
    </div>

    <!-- Overdue Table -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-triangle-exclamation text-danger"></i> Overdue Complaints Requiring Intervention</h3>
        <button class="btn btn-sm btn-danger" onclick="CivicUtils.showToast('Batch escalation notices transmitted!', 'warning')">Escalate All</button>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>Problem ID</th>
              <th>Incident</th>
              <th>Category</th>
              <th>Current Authority</th>
              <th>Assigned Officer</th>
              <th>Overdue By</th>
              <th>Escalation Level</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CS-2026-0002</strong></td>
              <td>Contaminated Turbid Drinking Water Supply</td>
              <td><span class="badge badge-neutral">Water</span></td>
              <td>Water Supply Board (BWSSB)</td>
              <td>Smt. Kavita Rao</td>
              <td><span class="badge badge-danger">-12 Hours</span></td>
              <td><span class="badge badge-danger">Tier 3: Head Review</span></td>
              <td>
                <button class="btn btn-sm btn-danger" onclick="CivicUtils.showToast('Official re-routed to Special Taskforce.', 'success')">Reassign</button>
              </td>
            </tr>
            <tr>
              <td><strong>CS-2026-0014</strong></td>
              <td>Unsegregated Medical Waste Dumped Behind Clinic</td>
              <td><span class="badge badge-neutral">Healthcare</span></td>
              <td>Health & Pollution Board</td>
              <td>Dr. B. Manjunath</td>
              <td><span class="badge badge-warning">Approaching SLA</span></td>
              <td><span class="badge badge-warning">Tier 2: Senior Officer</span></td>
              <td>
                <button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('Reminder sent.', 'info')">Send Alert</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# 10. authority-dashboard.html
pages["authority-dashboard.html"] = build_dashboard_page(
    "authority-dashboard.html",
    "Departmental Work Queue & Resolution",
    "Authority control panel to accept incoming verified complaints, assign zonal field officers, and upload resolution proof.",
    "authority",
    """
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-inbox"></i></div>
        <div class="stat-info">
          <div class="stat-value">18</div>
          <div class="stat-label">Assigned Work Queue</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-clock-rotate-left"></i></div>
        <div class="stat-info">
          <div class="stat-value">4</div>
          <div class="stat-label">New Today</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon danger"><i class="fa-solid fa-fire"></i></div>
        <div class="stat-info">
          <div class="stat-value">2</div>
          <div class="stat-label">SLA Overdue</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-circle-check"></i></div>
        <div class="stat-info">
          <div class="stat-value">124</div>
          <div class="stat-label">Resolved This Month</div>
        </div>
      </div>
    </div>

    <!-- Work Queue Table -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-list-check"></i> Active Department Complaints</h3>
        <span class="badge badge-primary">Public Works Department</span>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Priority</th>
              <th>Location</th>
              <th>Assigned Officer</th>
              <th>SLA Hours</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CS-2026-0001</strong></td>
              <td>Hazardous Deep Potholes on MG Road Junction</td>
              <td><span class="badge badge-warning">High</span></td>
              <td>MG Road Metro Pillar 42</td>
              <td>Er. Rajesh Verma</td>
              <td>18h Remaining</td>
              <td><span class="badge badge-primary">In Progress</span></td>
              <td>
                <div class="flex gap-1">
                  <a href="problem-details.html?id=CS-2026-0001" class="btn btn-sm btn-secondary">Details</a>
                  <button class="btn btn-sm btn-success" onclick="CivicUtils.showToast('Problem marked resolved! Verification request sent to citizen.', 'success')">Resolve</button>
                </div>
              </td>
            </tr>
            <tr>
              <td><strong>CS-2026-0010</strong></td>
              <td>Flooding on Underpass After Moderate Rains</td>
              <td><span class="badge badge-warning">High</span></td>
              <td>Kengeri Satellite Town</td>
              <td>Er. Sanjeev Hegde</td>
              <td>40h Remaining</td>
              <td><span class="badge badge-neutral">Assigned</span></td>
              <td>
                <div class="flex gap-1">
                  <a href="problem-details.html?id=CS-2026-0010" class="btn btn-sm btn-secondary">Details</a>
                  <button class="btn btn-sm btn-primary" onclick="CivicUtils.showToast('Officer dispatched to underpass drainage pump.', 'info')">Dispatch</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# 11. team-matching.html (AI Smart Matching)
pages["team-matching.html"] = build_dashboard_page(
    "team-matching.html",
    "AI Smart Matching",
    "Smart recommendations matching real-world municipal problems with specialized university research departments, student teams, and mentors.",
    "university",
    """
    <div class="card" style="margin-bottom: 2rem;">
      <p style="font-size:0.95rem; color:var(--muted);">
        Civic AI analyzes technical skills, domain depth, previous prototype experience, and geographical proximity to recommend the best academic and student teams.
        <em style="display:block; margin-top:0.35rem; font-size:0.8rem; color:var(--dark);">* Note: Recommendations are advisory and subject to faculty verification.</em>
      </p>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1.5rem;">
      
      <!-- Match Card 1 -->
      <div class="card">
        <div class="flex items-center justify-between" style="margin-bottom:1rem;">
          <span class="badge badge-primary">Problem Match</span>
          <span class="badge badge-success" style="font-size:0.85rem;"><i class="fa-solid fa-sparkles"></i> 96% Match</span>
        </div>
        <h4>CS-2026-0005: Indiranagar Signal Timing Bottleneck</h4>
        <p style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">
          Requires: Computer Vision, Embedded IoT, Real-Time Edge Processing, Traffic Flow Optimization.
        </p>

        <div style="background:var(--bg-subtle); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
          <div style="font-size:0.8rem; font-weight:700; color:var(--muted);">RECOMMENDED STUDENT INNOVATION TEAM</div>
          <div style="font-weight:700; color:var(--dark); margin:0.25rem 0;">SmartFlow AI Team</div>
          <div style="font-size:0.85rem; color:var(--muted);">RV College of Engineering • Dept of AI & Machine Learning</div>
        </div>

        <div class="flex gap-2">
          <a href="solution-workspace.html" class="btn btn-sm btn-primary w-100">Open Workspace</a>
          <button class="btn btn-sm btn-secondary w-100" onclick="CivicUtils.showToast('Collaboration request sent to Team Lead!', 'success')">Connect Team</button>
        </div>
      </div>

      <!-- Match Card 2 -->
      <div class="card">
        <div class="flex items-center justify-between" style="margin-bottom:1rem;">
          <span class="badge badge-primary">Problem Match</span>
          <span class="badge badge-success" style="font-size:0.85rem;"><i class="fa-solid fa-sparkles"></i> 92% Match</span>
        </div>
        <h4>CS-2026-0001: Pothole & Road Base Failure on MG Road</h4>
        <p style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">
          Requires: Civil Engineering, Pavement Materials, Recycled Plastics, Rapid Curing Bitumen.
        </p>

        <div style="background:var(--bg-subtle); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
          <div style="font-size:0.8rem; font-weight:700; color:var(--muted);">RECOMMENDED STUDENT INNOVATION TEAM</div>
          <div style="font-weight:700; color:var(--dark); margin:0.25rem 0;">EcoPave Materials Squad</div>
          <div style="font-size:0.85rem; color:var(--muted);">National Institute of Technology • Civil & Environmental Eng</div>
        </div>

        <div class="flex gap-2">
          <a href="solution-workspace.html" class="btn btn-sm btn-primary w-100">Open Workspace</a>
          <button class="btn btn-sm btn-secondary w-100" onclick="CivicUtils.showToast('Collaboration request sent to Team Lead!', 'success')">Connect Team</button>
        </div>
      </div>

      <!-- Match Card 3 -->
      <div class="card">
        <div class="flex items-center justify-between" style="margin-bottom:1rem;">
          <span class="badge badge-primary">Problem Match</span>
          <span class="badge badge-accent" style="font-size:0.85rem;"><i class="fa-solid fa-sparkles"></i> 88% Match</span>
        </div>
        <h4>CS-2026-0008: Toxic Effluent Foaming in Varthur Lake</h4>
        <p style="font-size:0.85rem; color:var(--muted); margin-bottom:1rem;">
          Requires: Chemical Sensor Arrays, Autonomous Water Surface Drone, Biological Remediation.
        </p>

        <div style="background:var(--bg-subtle); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
          <div style="font-size:0.8rem; font-weight:700; color:var(--muted);">RECOMMENDED STUDENT INNOVATION TEAM</div>
          <div style="font-weight:700; color:var(--dark); margin:0.25rem 0;">AquaClean Robotics</div>
          <div style="font-size:0.85rem; color:var(--muted);">Indian Institute of Science • Bio-Chemical Engineering</div>
        </div>

        <div class="flex gap-2">
          <a href="solution-workspace.html" class="btn btn-sm btn-primary w-100">Open Workspace</a>
          <button class="btn btn-sm btn-secondary w-100" onclick="CivicUtils.showToast('Collaboration request sent to Team Lead!', 'success')">Connect Team</button>
        </div>
      </div>

    </div>
    """
)

# 12. notifications.html
pages["notifications.html"] = build_dashboard_page(
    "notifications.html",
    "Notification Center",
    "Real-time notifications regarding problem verification, authority assignments, and citizen feedback alerts.",
    "citizen",
    """
    <div class="card" style="margin-bottom: 2rem;">
      <div class="flex items-center justify-between flex-wrap gap-2">
        <div class="flex gap-2">
          <button class="btn btn-sm btn-primary">All (4)</button>
          <button class="btn btn-sm btn-secondary">Unread (2)</button>
        </div>
        <button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('All notifications marked as read.', 'success')">
          <i class="fa-solid fa-check-double"></i> Mark All as Read
        </button>
      </div>
    </div>

    <div class="card">
      <ul style="display:flex; flex-direction:column; gap:1rem;">
        <li style="padding:1rem; border-radius:var(--radius-md); background:var(--bg-subtle); border-left:4px solid var(--success);">
          <div class="flex justify-between" style="font-size:0.8rem; color:var(--muted); margin-bottom:0.25rem;">
            <strong class="text-success"><i class="fa-solid fa-circle-check"></i> Problem Verified by Admin</strong>
            <span>10 mins ago</span>
          </div>
          <p style="font-size:0.9rem; color:var(--dark);">Your reported complaint (CS-2026-0001) has been verified and routed to Public Works Department.</p>
        </li>
        <li style="padding:1rem; border-radius:var(--radius-md); background:var(--bg-subtle); border-left:4px solid var(--warning);">
          <div class="flex justify-between" style="font-size:0.8rem; color:var(--muted); margin-bottom:0.25rem;">
            <strong class="text-warning"><i class="fa-solid fa-triangle-exclamation"></i> SLA Warning Alert</strong>
            <span>1 hour ago</span>
          </div>
          <p style="font-size:0.9rem; color:var(--dark);">Water Contamination (CS-2026-0002) has 4 hours remaining before Tier-2 escalation.</p>
        </li>
        <li style="padding:1rem; border-radius:var(--radius-md); background:var(--bg-card); border:1px solid var(--border); border-left:4px solid var(--primary);">
          <div class="flex justify-between" style="font-size:0.8rem; color:var(--muted); margin-bottom:0.25rem;">
            <strong class="text-primary"><i class="fa-solid fa-graduation-cap"></i> Student Team Proposed Solution</strong>
            <span>4 hours ago</span>
          </div>
          <p style="font-size:0.9rem; color:var(--dark);">RV College of Engineering submitted a smart traffic prototype for Indiranagar Junction.</p>
        </li>
      </ul>
    </div>
    """
)

# 13. profile.html
pages["profile.html"] = build_dashboard_page(
    "profile.html",
    "User Profile & Account",
    "Manage your profile credentials, linked organization, notification preferences, and verification status.",
    "citizen",
    """
    <div style="display:grid; grid-template-columns:1fr 2fr; gap:2rem;" class="dashboard-grid-detail">
      
      <!-- Profile Card -->
      <div class="card" style="text-align:center;">
        <div style="width:84px; height:84px; border-radius:50%; background:var(--primary); color:#fff; display:flex; align-items:center; justify-content:center; font-size:2rem; font-weight:700; margin:0 auto 1rem;">
          AS
        </div>
        <h3 style="margin-bottom:0.25rem;">Ananya Sharma</h3>
        <span class="badge badge-primary" style="margin-bottom:1rem;">Citizen Reporter</span>
        <p style="font-size:0.85rem; color:var(--muted); margin-bottom:1.5rem;">Indiranagar Resident, Central Ward Bangalore</p>
        
        <div style="border-top:1px solid var(--border); padding-top:1rem; text-align:left; font-size:0.85rem;">
          <div style="margin-bottom:0.5rem;"><i class="fa-solid fa-envelope text-muted"></i> ananya.sharma@example.com</div>
          <div style="margin-bottom:0.5rem;"><i class="fa-solid fa-phone text-muted"></i> +91 98450 12345</div>
          <div><i class="fa-solid fa-calendar-check text-muted"></i> Joined August 2026</div>
        </div>
      </div>

      <!-- Account Settings -->
      <div class="card">
        <h3 class="card-title" style="margin-bottom:1.5rem;">Account Information</h3>
        <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
          <div class="form-group">
            <label class="form-label">Full Name</label>
            <input type="text" class="form-control" value="Ananya Sharma">
          </div>
          <div class="form-group">
            <label class="form-label">Email Address</label>
            <input type="email" class="form-control" value="ananya.sharma@example.com">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Resident Ward & District</label>
          <input type="text" class="form-control" value="Ward 112, Indiranagar, Central District">
        </div>
        <div class="form-group">
          <label class="form-label">Notification Channels</label>
          <div class="flex items-center gap-4">
            <label style="font-size:0.9rem;"><input type="checkbox" checked> SMS Alerts</label>
            <label style="font-size:0.9rem;"><input type="checkbox" checked> WhatsApp Updates</label>
            <label style="font-size:0.9rem;"><input type="checkbox" checked> Email Digest</label>
          </div>
        </div>
        <button class="btn btn-primary" onclick="CivicUtils.showToast('Profile updated successfully!', 'success')">Save Changes</button>
      </div>

    </div>
    """
)

# 14. admin-dashboard.html
pages["admin-dashboard.html"] = build_dashboard_page(
    "admin-dashboard.html",
    "System Administrator Control Center",
    "Monitor user authentications, audit logs, category taxonomies, and manage authority routing configurations.",
    "admin",
    """
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-users"></i></div>
        <div class="stat-info">
          <div class="stat-value">8,410</div>
          <div class="stat-label">Registered Citizens</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-building-columns"></i></div>
        <div class="stat-info">
          <div class="stat-value">156</div>
          <div class="stat-label">Government Authorities</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-graduation-cap"></i></div>
        <div class="stat-info">
          <div class="stat-value">340</div>
          <div class="stat-label">University Teams</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-handshake"></i></div>
        <div class="stat-info">
          <div class="stat-value">48</div>
          <div class="stat-label">Industry Sponsors</div>
        </div>
      </div>
    </div>

    <!-- Audit Logs Table -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-shield-halved text-primary"></i> Real-Time Platform Audit Log</h3>
        <span class="badge badge-neutral">Tamper-Proof Log</span>
      </div>
      <div class="table-responsive">
        <table class="custom-table" id="auditLogTable">
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>User</th>
              <th>Action</th>
              <th>Entity</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2026-09-30 20:15:22</td>
              <td>Admin Desk</td>
              <td><span class="badge badge-primary">VERIFY_PROBLEM</span></td>
              <td>CS-2026-0004</td>
              <td><span class="badge badge-success">SUCCESS</span></td>
            </tr>
            <tr>
              <td>2026-09-30 19:40:11</td>
              <td>Er. Rajesh Verma</td>
              <td><span class="badge badge-accent">ASSIGN_CONTRACTOR</span></td>
              <td>CS-2026-0001</td>
              <td><span class="badge badge-success">SUCCESS</span></td>
            </tr>
            <tr>
              <td>2026-09-30 18:22:05</td>
              <td>System Watchdog</td>
              <td><span class="badge badge-danger">AUTO_ESCALATION</span></td>
              <td>CS-2026-0002</td>
              <td><span class="badge badge-warning">TRIGGERED</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# 15. problem-verification.html (Admin verification queue)
pages["problem-verification.html"] = build_dashboard_page(
    "problem-verification.html",
    "Complaint Verification Queue",
    "Verify freshly submitted citizen complaints before dispatching to official government work queues.",
    "admin",
    """
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-clipboard-check text-primary"></i> Pending Citizen Submissions</h3>
        <span class="badge badge-warning">2 Awaiting Review</span>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>Ticket ID</th>
              <th>Title</th>
              <th>Category</th>
              <th>AI Priority</th>
              <th>Reported Address</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CS-2026-0004</strong></td>
              <td>Dangling High Voltage Cable Near Playground</td>
              <td><span class="badge badge-neutral">Electricity</span></td>
              <td><span class="badge badge-danger">99/100</span></td>
              <td>Koramangala 4th Block Children Park</td>
              <td>
                <div class="flex gap-1">
                  <button class="btn btn-sm btn-success" onclick="CivicUtils.showToast('Verified and dispatched to BESCOM power grid dispatch!', 'success')">Verify & Route</button>
                  <button class="btn btn-sm btn-danger" onclick="CivicUtils.showToast('Rejected as invalid duplicate.', 'warning')">Reject</button>
                </div>
              </td>
            </tr>
            <tr>
              <td><strong>CS-2026-0008</strong></td>
              <td>Industrial Effluent Foaming in Varthur Lake</td>
              <td><span class="badge badge-neutral">Environment</span></td>
              <td><span class="badge badge-danger">95/100</span></td>
              <td>Varthur Lake South Inflow Channel</td>
              <td>
                <div class="flex gap-1">
                  <button class="btn btn-sm btn-success" onclick="CivicUtils.showToast('Verified and routed to Pollution Control Board!', 'success')">Verify & Route</button>
                  <button class="btn btn-sm btn-danger" onclick="CivicUtils.showToast('Rejected.', 'warning')">Reject</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# Write all the constructed pages
for filename, content in pages.items():
    with open(os.path.join(FRONTEND_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Created {len(pages)} key dashboard pages successfully!")
