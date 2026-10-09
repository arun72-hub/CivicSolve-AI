import os
from generate_html_pages import build_dashboard_page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

extra_pages = {}

# 1. university-dashboard.html
extra_pages["university-dashboard.html"] = build_dashboard_page(
    "university-dashboard.html",
    "University Research & Innovation Hub",
    "Connect faculty, researcher labs, and student engineering teams to tackle real-world municipal and civic challenges.",
    "university",
    """
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-lightbulb"></i></div>
        <div class="stat-info">
          <div class="stat-value">42</div>
          <div class="stat-label">Recommended Problems</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-code-fork"></i></div>
        <div class="stat-info">
          <div class="stat-value">14</div>
          <div class="stat-label">Active Prototypes</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-users-gear"></i></div>
        <div class="stat-info">
          <div class="stat-value">28</div>
          <div class="stat-label">Student Teams</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-award"></i></div>
        <div class="stat-info">
          <div class="stat-value">₹ 28.5L</div>
          <div class="stat-label">CSR Grants Awarded</div>
        </div>
      </div>
    </div>

    <!-- Recommended Problems for Academia -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-sparkles text-primary"></i> High-Impact Civic Challenges Seeking Solutions</h3>
        <a href="team-matching.html" class="btn btn-sm btn-primary"><i class="fa-solid fa-wand-magic-sparkles"></i> AI Smart Matching</a>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Problem Challenge</th>
              <th>Category</th>
              <th>Complexity</th>
              <th>Relevant Departments</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CS-2026-0005</strong></td>
              <td>Adaptive Computer Vision Signal Controller for Congestion</td>
              <td><span class="badge badge-neutral">Transport</span></td>
              <td><span class="badge badge-danger">High</span></td>
              <td>AI, Computer Science, Electronics</td>
              <td><a href="solution-workspace.html" class="btn btn-sm btn-primary">Workspace</a></td>
            </tr>
            <tr>
              <td><strong>CS-2026-0001</strong></td>
              <td>Recycled Plastic Bitumen Blend for Pothole Prevention</td>
              <td><span class="badge badge-neutral">Road</span></td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td>Civil & Material Science</td>
              <td><a href="team-matching.html" class="btn btn-sm btn-secondary">Match Team</a></td>
            </tr>
            <tr>
              <td><strong>CS-2026-0008</strong></td>
              <td>Autonomous Lake Foam Neutralizing Drone</td>
              <td><span class="badge badge-neutral">Environment</span></td>
              <td><span class="badge badge-danger">High</span></td>
              <td>Robotics & Chemical Eng</td>
              <td><a href="team-matching.html" class="btn btn-sm btn-secondary">Match Team</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# 2. faculty-dashboard.html
extra_pages["faculty-dashboard.html"] = build_dashboard_page(
    "faculty-dashboard.html",
    "Faculty Mentorship & Prototype Review",
    "Review student innovation designs, mentor engineering teams, and validate technical safety before municipal field trials.",
    "faculty",
    """
    <div class="dashboard-grid-3" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-chalkboard-user"></i></div>
        <div class="stat-info">
          <div class="stat-value">6</div>
          <div class="stat-label">Mentored Teams</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-file-signature"></i></div>
        <div class="stat-info">
          <div class="stat-value">2</div>
          <div class="stat-label">Prototypes Awaiting Review</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-rocket"></i></div>
        <div class="stat-info">
          <div class="stat-value">4</div>
          <div class="stat-label">Approved Municipal Pilots</div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-microscope text-primary"></i> Prototypes In Mentorship Review</h3>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>Team</th>
              <th>Civic Issue</th>
              <th>Prototype Title</th>
              <th>Status</th>
              <th>Mentor Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>SmartFlow AI Team</strong></td>
              <td>CS-2026-0005 (Traffic Bottleneck)</td>
              <td>Edge AI Dynamic Green Cycle Microcontroller</td>
              <td><span class="badge badge-warning">Awaiting Approval</span></td>
              <td>
                <div class="flex gap-1">
                  <a href="solution-workspace.html" class="btn btn-sm btn-secondary">Inspect Code</a>
                  <button class="btn btn-sm btn-success" onclick="CivicUtils.showToast('Prototype approved for Traffic Police field trial!', 'success')">Approve Pilot</button>
                </div>
              </td>
            </tr>
            <tr>
              <td><strong>EcoPave Squad</strong></td>
              <td>CS-2026-0001 (MG Road Potholes)</td>
              <td>Recycled Polymer Cold Mix Patching Formula</td>
              <td><span class="badge badge-success">Pilot Approved</span></td>
              <td>
                <a href="solution-details.html" class="btn btn-sm btn-primary">View Report</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# 3. student-team-dashboard.html
extra_pages["student-team-dashboard.html"] = build_dashboard_page(
    "student-team-dashboard.html",
    "Student Team Innovation Workspace",
    "Collaborate on real community engineering solutions, track GitHub milestones, test hardware and software prototypes.",
    "student",
    """
    <div class="card" style="margin-bottom: 2rem;">
      <div class="flex items-center justify-between flex-wrap gap-2">
        <div>
          <h2>Team: SmartFlow AI Innovators</h2>
          <p style="font-size:0.9rem; color:var(--muted);">Department of Computer Science & AI • RV College of Engineering</p>
        </div>
        <a href="solution-workspace.html" class="btn btn-primary"><i class="fa-solid fa-bars-progress"></i> Open Kanban Board</a>
      </div>
    </div>

    <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;">
      <div class="card">
        <h3 class="card-title" style="margin-bottom:1rem;"><i class="fa-solid fa-users text-primary"></i> Team Roster</h3>
        <ul style="display:flex; flex-direction:column; gap:0.75rem;">
          <li class="flex justify-between items-center" style="font-size:0.9rem;">
            <span><strong>Rohan Varma</strong> (Team Lead & Embedded AI)</span>
            <span class="badge badge-primary">Lead</span>
          </li>
          <li class="flex justify-between items-center" style="font-size:0.9rem;">
            <span><strong>Anjali Nair</strong> (Computer Vision Specialist)</span>
            <span class="badge badge-neutral">Developer</span>
          </li>
          <li class="flex justify-between items-center" style="font-size:0.9rem;">
            <span><strong>Vikramaditya S.</strong> (IoT Firmware & Sensors)</span>
            <span class="badge badge-neutral">Hardware</span>
          </li>
        </ul>
      </div>

      <div class="card">
        <h3 class="card-title" style="margin-bottom:1rem;"><i class="fa-solid fa-bullseye text-accent"></i> Project Milestone Timeline</h3>
        <div class="flex flex-col gap-2">
          <div class="flex justify-between text-muted" style="font-size:0.85rem;">
            <span>Hardware Breadboard Complete</span>
            <span class="text-success"><i class="fa-solid fa-check"></i> Done</span>
          </div>
          <div class="flex justify-between text-muted" style="font-size:0.85rem;">
            <span>YOLOv8 Model Inference Under 12ms</span>
            <span class="text-success"><i class="fa-solid fa-check"></i> Done</span>
          </div>
          <div class="flex justify-between text-dark" style="font-size:0.85rem; font-weight:700;">
            <span>Field Trial at Indiranagar 100ft Road</span>
            <span class="text-warning">In Progress</span>
          </div>
          <div class="flex justify-between text-muted" style="font-size:0.85rem;">
            <span>Citizen Post-Resolution Survey</span>
            <span>Pending</span>
          </div>
        </div>
      </div>
    </div>
    """
)

# 4. industry-dashboard.html
extra_pages["industry-dashboard.html"] = build_dashboard_page(
    "industry-dashboard.html",
    "Industry Innovation & CSR Dashboard",
    "Partner with municipal authorities and university engineering teams to fund, mentor, and sponsor sustainable civic solutions.",
    "industry",
    """
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-hand-holding-dollar"></i></div>
        <div class="stat-info">
          <div class="stat-value">₹ 45.0 L</div>
          <div class="stat-label">CSR Budget Allocated</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-leaf"></i></div>
        <div class="stat-info">
          <div class="stat-value">8</div>
          <div class="stat-label">Funded Civic Pilots</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-graduation-cap"></i></div>
        <div class="stat-info">
          <div class="stat-value">12</div>
          <div class="stat-label">Partner Colleges</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-users"></i></div>
        <div class="stat-info">
          <div class="stat-value">1.8M</div>
          <div class="stat-label">Citizens Benefited</div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><i class="fa-solid fa-handshake text-primary"></i> High-Priority CSR Sponsorship Opportunities</h3>
        <a href="industry-opportunities.html" class="btn btn-sm btn-primary">Browse All Grants</a>
      </div>
      <div class="table-responsive">
        <table class="custom-table">
          <thead>
            <tr>
              <th>Opportunity Title</th>
              <th>Focus Area</th>
              <th>Matched University</th>
              <th>Funding Needed</th>
              <th>Impact Potential</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Solar Inverter Storage for 12 Rural Primary Health Clinics</strong></td>
              <td><span class="badge badge-success">Healthcare</span></td>
              <td>IISc Energy Lab</td>
              <td>₹ 6.5 Lakhs</td>
              <td>24,000 villagers with vaccine safety</td>
              <td><button class="btn btn-sm btn-primary" onclick="CivicUtils.showToast('Grant sponsorship committed!', 'success')">Sponsor Grant</button></td>
            </tr>
            <tr>
              <td><strong>AI Smart Traffic Controllers for 10 Congestion Bottlenecks</strong></td>
              <td><span class="badge badge-primary">Urban Mobility</span></td>
              <td>RV College AI Team</td>
              <td>₹ 8.0 Lakhs</td>
              <td>35% drop in carbon idle emissions</td>
              <td><button class="btn btn-sm btn-primary" onclick="CivicUtils.showToast('Grant sponsorship committed!', 'success')">Sponsor Grant</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
)

# 5. government-monitoring.html
extra_pages["government-monitoring.html"] = build_dashboard_page(
    "government-monitoring.html",
    "Live Municipal Activity Monitoring",
    "Real-time event stream of incoming complaints, AI duplicate flags, officer dispatches, and citizen verification updates.",
    "government",
    """
    <div style="display:grid; grid-template-columns: 2fr 1fr; gap: 2rem;" class="dashboard-grid-detail">
      
      <div class="card">
        <div class="card-header">
          <h3 class="card-title"><i class="fa-solid fa-satellite-dish text-primary"></i> Live Ticker Feed</h3>
          <span class="badge badge-success"><i class="fa-solid fa-circle fa-beat"></i> Streaming</span>
        </div>
        <ul style="display:flex; flex-direction:column; gap:1rem;">
          <li style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--bg-subtle);">
            <div class="flex justify-between" style="font-size:0.8rem; color:var(--muted); margin-bottom:0.25rem;">
              <span>Public Works Department</span>
              <span>2 mins ago</span>
            </div>
            <strong class="text-dark">Problem CS-2026-0001 (MG Road) assigned to contractor for asphalt leveling.</strong>
          </li>
          <li style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--danger-light); border:1px solid var(--danger);">
            <div class="flex justify-between" style="font-size:0.8rem; color:var(--danger); margin-bottom:0.25rem;">
              <span>SLA Watchdog System</span>
              <span>15 mins ago</span>
            </div>
            <strong class="text-danger">Problem CS-2026-0002 breached SLA threshold (-12h). Escalated to Tier-2.</strong>
          </li>
          <li style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--success-light); border:1px solid var(--success);">
            <div class="flex justify-between" style="font-size:0.8rem; color:var(--success); margin-bottom:0.25rem;">
              <span>Citizen Verification Desk</span>
              <span>42 mins ago</span>
            </div>
            <strong class="text-success">Citizen verified resolution of Primary Health Center vaccine clinic (CS-2026-0006).</strong>
          </li>
        </ul>
      </div>

      <div class="card">
        <h3 class="card-title" style="margin-bottom:1rem;"><i class="fa-solid fa-chart-simple text-accent"></i> Department Workloads</h3>
        <ul style="display:flex; flex-direction:column; gap:0.75rem; font-size:0.9rem;">
          <li class="flex justify-between">
            <span>BBMP Municipal Waste</span>
            <span class="badge badge-danger">310 Active</span>
          </li>
          <li class="flex justify-between">
            <span>Electricity (BESCOM)</span>
            <span class="badge badge-warning">145 Active</span>
          </li>
          <li class="flex justify-between">
            <span>Roads & PWD</span>
            <span class="badge badge-primary">128 Active</span>
          </li>
          <li class="flex justify-between">
            <span>Water Supply (BWSSB)</span>
            <span class="badge badge-accent">94 Active</span>
          </li>
        </ul>
      </div>

    </div>
    """
)

# 6. government-analytics.html
extra_pages["government-analytics.html"] = build_dashboard_page(
    "government-analytics.html",
    "Citywide Civic Analytics & Impact Metrics",
    "Deep performance metrics on resolution velocity, cost savings, departmental SLA compliance, and citizen satisfaction ratings.",
    "government",
    """
    <div class="dashboard-grid-4" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-gauge-high"></i></div>
        <div class="stat-info">
          <div class="stat-value">91.4%</div>
          <div class="stat-label">Resolution SLA Rate</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-clock"></i></div>
        <div class="stat-info">
          <div class="stat-value">34 Hours</div>
          <div class="stat-label">Avg. Resolution Time</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-star"></i></div>
        <div class="stat-info">
          <div class="stat-value">4.7 / 5</div>
          <div class="stat-label">Citizen Satisfaction</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon warning"><i class="fa-solid fa-piggy-bank"></i></div>
        <div class="stat-info">
          <div class="stat-value">₹ 1.2 Cr</div>
          <div class="stat-label">Estimated Cost Saved</div>
        </div>
      </div>
    </div>

    <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;">
      <div class="card">
        <h3 class="card-title" style="margin-bottom:1rem;"><i class="fa-solid fa-chart-line text-primary"></i> Citizen Satisfaction Growth</h3>
        <canvas id="chartTrends" style="max-height:280px;"></canvas>
      </div>

      <div class="card">
        <h3 class="card-title" style="margin-bottom:1rem;"><i class="fa-solid fa-chart-column text-accent"></i> Department SLA Compliance %</h3>
        <canvas id="chartDistricts" style="max-height:280px;"></canvas>
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
    </script>
    """
)

# 7. solution-details.html
extra_pages["solution-details.html"] = build_dashboard_page(
    "solution-details.html",
    "Pilot Solution Specification & Test Data",
    "Detailed technical breakdown of deployed pilot prototypes, before-and-after citizen metrics, and municipal validation certificates.",
    "student",
    """
    <div class="card" style="margin-bottom: 2rem;">
      <div class="flex items-center justify-between flex-wrap gap-2" style="margin-bottom:1rem;">
        <span class="badge badge-success">Pilot Testing Complete</span>
        <button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('Official PDF test report downloaded.', 'success')"><i class="fa-solid fa-download"></i> Export PDF Spec</button>
      </div>
      <h2>SmartFlow AI: Edge IoT Adaptive Signal Controller</h2>
      <p style="font-size:0.95rem; color:var(--muted);">
        Deployed at Indiranagar 100ft Junction for 14-day municipal validation trial in partnership with City Traffic Police.
      </p>
    </div>

    <div class="dashboard-grid-3" style="margin-bottom: 2rem;">
      <div class="stat-card">
        <div class="stat-icon success"><i class="fa-solid fa-arrow-down"></i></div>
        <div class="stat-info">
          <div class="stat-value">38%</div>
          <div class="stat-label">Queue Length Reduction</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon primary"><i class="fa-solid fa-stopwatch"></i></div>
        <div class="stat-info">
          <div class="stat-value">11 mins</div>
          <div class="stat-label">Commuter Time Saved / Trip</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon accent"><i class="fa-solid fa-leaf"></i></div>
        <div class="stat-info">
          <div class="stat-value">220 kg</div>
          <div class="stat-label">CO2 Emissions Avoided</div>
        </div>
      </div>
    </div>
    """
)

# 8. Remaining stubs linked smoothly:
stubs = [
    ("university-problems.html", "University Civic Problem Catalog", "Explore research and prototyping challenges", "university"),
    ("authority-problems.html", "Department Work Queue", "Inspect, prioritize, and allocate field teams", "authority"),
    ("authority-problem-details.html", "Authority Incident Investigation", "Assign officer and submit resolution proof", "authority"),
    ("authority-officers.html", "Officer Duty Roster", "View workload distribution across zonal teams", "authority"),
    ("authority-reports.html", "SLA & Resolution Reports", "Export monthly departmental performance data", "authority"),
    ("user-management.html", "Platform User Accounts", "Manage citizen and institutional access permissions", "admin"),
    ("authority-management.html", "Authority Routing Config", "Configure jurisdiction boundaries and SLA timelines", "admin"),
    ("system-analytics.html", "System Health & Server Telemetry", "Monitor platform uptime and AI inference latencies", "admin"),
    ("industry-opportunities.html", "CSR Sponsorship Opportunities", "Review verified civic grant proposals", "industry")
]

for file, title, desc, role in stubs:
    extra_pages[file] = build_dashboard_page(
        file,
        title,
        desc,
        role,
        f"""
        <div class="card">
          <div class="flex items-center justify-between" style="margin-bottom:1.5rem;">
            <h3 class="card-title"><i class="fa-solid fa-table-list text-primary"></i> {title} Records</h3>
            <span class="badge badge-success">Live Synchronized</span>
          </div>
          <p style="color:var(--muted); font-size:0.95rem; margin-bottom:1.5rem;">
            All system entities in this module are connected with real-time localStorage persistence and ready for PostgreSQL integration.
          </p>
          <div class="table-responsive">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>Reference</th>
                  <th>Description</th>
                  <th>Category / Ward</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>REC-2026-01</strong></td>
                  <td>Sample Live Operational Record</td>
                  <td>Central Ward</td>
                  <td><span class="badge badge-success">Active</span></td>
                  <td><button class="btn btn-sm btn-secondary" onclick="CivicUtils.showToast('Action logged in audit trail.', 'info')">Manage</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        """
    )

for filename, content in extra_pages.items():
    with open(os.path.join(FRONTEND_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(extra_pages)} extra dashboard pages!")
