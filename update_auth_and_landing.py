import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# 1. login.html
login_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login - CivicSolve AI</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="css/animations.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%); min-height:100vh; display:flex; flex-direction:column;">

  <!-- Header -->
  <header style="padding:1.5rem 2rem; display:flex; justify-content:space-between; align-items:center;">
    <a href="index.html" class="brand-logo">
      <i class="fa-solid fa-city"></i>
      <span>CivicSolve<span class="ai-tag">AI</span></span>
    </a>
    <div class="flex items-center gap-2">
      <button class="theme-toggle-btn" title="Toggle Theme"><i class="fa-solid fa-moon"></i></button>
      <a href="index.html" class="btn btn-sm btn-secondary"><i class="fa-solid fa-arrow-left"></i> Home</a>
    </div>
  </header>

  <main style="flex:1; display:flex; align-items:center; justify-content:center; padding:1.5rem;">
    <div style="width:100%; max-width:540px; background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-xl);">
      
      <div style="text-align:center; margin-bottom:2rem;">
        <span class="badge badge-primary" style="margin-bottom:0.5rem;"><i class="fa-solid fa-shield"></i> Secure Single Sign-On</span>
        <h2 style="font-size:1.75rem; font-weight:800; color:var(--dark);">Sign in to CivicSolve AI</h2>
        <p style="font-size:0.9rem; color:var(--muted); margin-top:0.25rem;">Access role-tailored dashboards and municipal resolution workspaces.</p>
      </div>

      <!-- Quick 1-Click Demo Login Selector -->
      <div style="background:var(--bg-subtle); border:1px solid var(--border); border-radius:var(--radius-md); padding:1rem; margin-bottom:1.75rem;">
        <div class="flex items-center justify-between" style="margin-bottom:0.75rem;">
          <span style="font-size:0.8rem; font-weight:700; color:var(--primary); text-transform:uppercase;">
            <i class="fa-solid fa-bolt"></i> 1-Click Demo Persona Launch
          </span>
          <span class="badge badge-success">Instant Access</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;">
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('citizen')"><i class="fa-solid fa-user"></i> Citizen</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('authority')"><i class="fa-solid fa-building-user"></i> Authority Officer</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('government')"><i class="fa-solid fa-building-columns"></i> Government Desk</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('admin')"><i class="fa-solid fa-shield-halved"></i> Administrator</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('university')"><i class="fa-solid fa-graduation-cap"></i> University Dean</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('faculty')"><i class="fa-solid fa-chalkboard-user"></i> Faculty Mentor</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('student')"><i class="fa-solid fa-laptop-code"></i> Student Team</button>
          <button class="btn btn-sm btn-secondary" onclick="CivicAuth.loginAs('industry')"><i class="fa-solid fa-briefcase"></i> Industry Partner</button>
        </div>
      </div>

      <!-- Standard Form -->
      <form id="standardLoginForm" onsubmit="event.preventDefault(); handleCustomLogin();">
        <div class="form-group">
          <label class="form-label">Select Account Role</label>
          <select id="loginRoleSelect" class="form-select">
            <option value="citizen">Citizen Reporter</option>
            <option value="authority">Government Authority Officer</option>
            <option value="government">Government Commissioner / Official</option>
            <option value="admin">System Administrator</option>
            <option value="university">University Innovation Cell</option>
            <option value="faculty">Faculty Mentor</option>
            <option value="student">Student Team Innovator</option>
            <option value="industry">Industry CSR Partner</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input type="email" id="loginEmail" class="form-control" placeholder="user@civicsolve.ai" value="demo@civicsolve.ai" required>
        </div>

        <div class="form-group">
          <div class="flex justify-between items-center" style="margin-bottom:0.5rem;">
            <label class="form-label" style="margin-bottom:0;">Password</label>
            <a href="forgot-password.html" style="font-size:0.8rem; color:var(--primary); font-weight:600;">Forgot password?</a>
          </div>
          <input type="password" class="form-control" value="••••••••" required>
        </div>

        <button type="submit" class="btn btn-primary w-100" style="padding:0.85rem; font-size:1rem; margin-top:0.5rem;">
          <i class="fa-solid fa-right-to-bracket"></i> Sign In to Dashboard
        </button>
      </form>

      <p style="text-align:center; margin-top:1.5rem; font-size:0.875rem; color:var(--muted);">
        Don't have an account yet? <a href="register.html" style="color:var(--primary); font-weight:600;">Register as Citizen or Innovator</a>
      </p>
    </div>
  </main>

  <div id="toastContainer" class="toast-container"></div>

  <script src="js/data.js"></script>
  <script src="js/utils.js"></script>
  <script src="js/auth.js"></script>
  <script src="js/app.js"></script>
  <script>
    function handleCustomLogin() {
      const role = document.getElementById("loginRoleSelect").value;
      CivicUtils.showToast("Authenticating session...", "info", 1000);
      setTimeout(() => {
        CivicAuth.loginAs(role);
      }, 500);
    }
  </script>
</body>
</html>"""

# 2. register.html
register_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Register - CivicSolve AI</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%); min-height:100vh; display:flex; flex-direction:column;">

  <header style="padding:1.5rem 2rem; display:flex; justify-content:space-between; align-items:center;">
    <a href="index.html" class="brand-logo">
      <i class="fa-solid fa-city"></i>
      <span>CivicSolve<span class="ai-tag">AI</span></span>
    </a>
    <a href="login.html" class="btn btn-sm btn-secondary">Sign In</a>
  </header>

  <main style="flex:1; display:flex; align-items:center; justify-content:center; padding:1.5rem;">
    <div style="width:100%; max-width:540px; background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-xl);">
      <div style="text-align:center; margin-bottom:2rem;">
        <h2 style="font-size:1.75rem; font-weight:800; color:var(--dark);">Create Your Account</h2>
        <p style="font-size:0.9rem; color:var(--muted); margin-top:0.25rem;">Join thousands of citizens, engineers, and officials collaborating for societal progress.</p>
      </div>

      <form onsubmit="event.preventDefault(); CivicUtils.showToast('Registration successful! Redirecting to citizen dashboard...', 'success'); setTimeout(() => CivicAuth.loginAs('citizen'), 1000);">
        <div class="form-group">
          <label class="form-label">I am registering as *</label>
          <select class="form-select" id="regRole">
            <option value="citizen">Citizen / Resident</option>
            <option value="student">Student Innovator / Engineering Team</option>
            <option value="faculty">University Faculty Mentor</option>
            <option value="authority">Government Authority Officer</option>
            <option value="industry">Industry CSR Representative</option>
          </select>
        </div>

        <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
          <div class="form-group">
            <label class="form-label">Full Name *</label>
            <input type="text" class="form-control" placeholder="Priya Sharma" required>
          </div>
          <div class="form-group">
            <label class="form-label">Phone Number *</label>
            <input type="tel" class="form-control" placeholder="+91 98450 12345" required>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Email Address *</label>
          <input type="email" class="form-control" placeholder="priya@example.com" required>
        </div>

        <div class="form-group">
          <label class="form-label">Password *</label>
          <input type="password" class="form-control" placeholder="Create strong password" required>
        </div>

        <button type="submit" class="btn btn-primary w-100" style="padding:0.85rem; font-size:1rem; margin-top:0.5rem;">
          Create Free Account
        </button>
      </form>

      <p style="text-align:center; margin-top:1.5rem; font-size:0.875rem; color:var(--muted);">
        Already registered? <a href="login.html" style="color:var(--primary); font-weight:600;">Sign in here</a>
      </p>
    </div>
  </main>

  <div id="toastContainer" class="toast-container"></div>
  <script src="js/data.js"></script>
  <script src="js/utils.js"></script>
  <script src="js/auth.js"></script>
  <script src="js/app.js"></script>
</body>
</html>"""

# 3. forgot-password.html
forgot_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Forgot Password - CivicSolve AI</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%); min-height:100vh; display:flex; flex-direction:column;">
  <header style="padding:1.5rem 2rem; display:flex; justify-content:space-between; align-items:center;">
    <a href="index.html" class="brand-logo">
      <i class="fa-solid fa-city"></i>
      <span>CivicSolve<span class="ai-tag">AI</span></span>
    </a>
    <a href="login.html" class="btn btn-sm btn-secondary">Sign In</a>
  </header>

  <main style="flex:1; display:flex; align-items:center; justify-content:center; padding:1.5rem;">
    <div style="width:100%; max-width:440px; background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-xl);">
      <h2 style="font-size:1.5rem; font-weight:800; margin-bottom:0.5rem;">Reset Password</h2>
      <p style="font-size:0.875rem; color:var(--muted); margin-bottom:1.5rem;">Enter your verified registered email address to receive an official password reset link.</p>
      
      <form onsubmit="event.preventDefault(); CivicUtils.showToast('Password recovery link dispatched to your email!', 'success');">
        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input type="email" class="form-control" placeholder="name@domain.com" required>
        </div>
        <button type="submit" class="btn btn-primary w-100">Send Recovery Link</button>
      </form>

      <div style="text-align:center; margin-top:1.5rem;">
        <a href="login.html" style="font-size:0.85rem; color:var(--primary); font-weight:600;">← Return to Login</a>
      </div>
    </div>
  </main>
  <div id="toastContainer" class="toast-container"></div>
  <script src="js/utils.js"></script>
</body>
</html>"""

# 4. index.html (Ultimate Landing Page)
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CivicSolve AI - AI-Powered Societal Problem Solving & Collaborative Innovation</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="css/animations.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>

  <!-- Landing Topbar -->
  <header class="landing-header">
    <div class="container navbar">
      <a href="index.html" class="brand-logo">
        <i class="fa-solid fa-city"></i>
        <span>CivicSolve<span class="ai-tag">AI</span></span>
      </a>

      <nav class="nav-menu">
        <a href="#how-it-works" class="nav-link">How It Works</a>
        <a href="#impact-stats" class="nav-link">Platform Impact</a>
        <a href="#problem-categories" class="nav-link">Categories</a>
        <a href="#featured-problems" class="nav-link">Live Incidents</a>
        <a href="#success-stories" class="nav-link">Success Stories</a>
        <a href="social-feed.html" class="nav-link">Civic Feed</a>
      </nav>

      <div class="nav-actions">
        <button class="theme-toggle-btn" title="Toggle Dark/Light Mode">
          <i class="fa-solid fa-moon"></i>
        </button>
        <a href="login.html" class="btn btn-sm btn-secondary">Login</a>
        <a href="submit-problem.html" class="btn btn-sm btn-primary">
          <i class="fa-solid fa-bullhorn"></i> Report Issue
        </a>
      </div>
    </div>
  </header>

  <main>
    <!-- HERO SECTION -->
    <section class="hero" style="position:relative; overflow:hidden;">
      <div class="container hero-content">
        <div style="display:inline-flex; align-items:center; gap:0.5rem; background:rgba(79, 70, 229, 0.08); border:1px solid rgba(79, 70, 229, 0.2); padding:0.4rem 1rem; border-radius:var(--radius-full); margin-bottom:1.5rem;">
          <span class="badge badge-primary"><i class="fa-solid fa-bolt"></i> Next-Gen Civic Tech</span>
          <span style="font-size:0.85rem; font-weight:600; color:var(--primary);">AI-Driven Societal Resolution Engine</span>
        </div>

        <h1 class="hero-title" style="font-size:3.75rem; font-weight:900; letter-spacing:-0.03em; margin-bottom:1.5rem;">
          From Citizen Problems to <br><span>Real Measurable Solutions.</span>
        </h1>

        <p class="hero-subtitle" style="font-size:1.25rem; color:var(--muted); max-width:800px; margin:0 auto 2.5rem; line-height:1.6;">
          Report civic issues in seconds. Let artificial intelligence analyze urgency, remove duplicates, identify responsible government authorities, and mobilize university engineering teams to co-create lasting solutions.
        </p>

        <div class="cta-buttons" style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; margin-bottom:3.5rem;">
          <a href="submit-problem.html" class="btn btn-lg btn-primary">
            <i class="fa-solid fa-camera"></i> Report a Problem (GPS & Camera)
          </a>
          <a href="government-dashboard.html" class="btn btn-lg btn-secondary">
            <i class="fa-solid fa-building-columns"></i> Government Command Center
          </a>
          <a href="login.html" class="btn btn-lg btn-accent">
            <i class="fa-solid fa-repeat"></i> Try Demo Mode (8 Roles)
          </a>
        </div>

        <!-- Hero Journey Graphic: Citizen -> AI -> Authority -> University -> Solution -> Impact -->
        <div style="background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-xl); padding:1.75rem; box-shadow:var(--shadow-xl); max-width:1050px; margin:0 auto;">
          <div style="font-size:0.8rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:1.25rem; text-align:center;">
            Complete Civic Resolution Journey
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(140px, 1fr)); gap:1rem; align-items:center; text-align:center;">
            <div style="padding:0.75rem; background:var(--bg-subtle); border-radius:var(--radius-md);">
              <i class="fa-solid fa-user-check text-primary" style="font-size:1.75rem; margin-bottom:0.35rem;"></i>
              <div style="font-weight:700; font-size:0.9rem;">1. Citizen</div>
              <div style="font-size:0.75rem; color:var(--muted);">GPS & Video Intake</div>
            </div>
            <div style="color:var(--muted); font-size:1.25rem;"><i class="fa-solid fa-arrow-right"></i></div>
            <div style="padding:0.75rem; background:rgba(6, 182, 212, 0.1); border:1px solid var(--accent); border-radius:var(--radius-md);">
              <i class="fa-solid fa-brain text-accent" style="font-size:1.75rem; margin-bottom:0.35rem;"></i>
              <div style="font-weight:700; font-size:0.9rem; color:var(--accent);">2. Civic AI</div>
              <div style="font-size:0.75rem; color:var(--muted);">Deduplication & SLA</div>
            </div>
            <div style="color:var(--muted); font-size:1.25rem;"><i class="fa-solid fa-arrow-right"></i></div>
            <div style="padding:0.75rem; background:var(--bg-subtle); border-radius:var(--radius-md);">
              <i class="fa-solid fa-building-columns text-warning" style="font-size:1.75rem; margin-bottom:0.35rem;"></i>
              <div style="font-weight:700; font-size:0.9rem;">3. Authority</div>
              <div style="font-size:0.75rem; color:var(--muted);">Auto-Routed Desk</div>
            </div>
            <div style="color:var(--muted); font-size:1.25rem;"><i class="fa-solid fa-arrow-right"></i></div>
            <div style="padding:0.75rem; background:var(--bg-subtle); border-radius:var(--radius-md);">
              <i class="fa-solid fa-graduation-cap text-secondary" style="font-size:1.75rem; margin-bottom:0.35rem;"></i>
              <div style="font-weight:700; font-size:0.9rem;">4. University</div>
              <div style="font-size:0.75rem; color:var(--muted);">Student Prototypes</div>
            </div>
            <div style="color:var(--muted); font-size:1.25rem;"><i class="fa-solid fa-arrow-right"></i></div>
            <div style="padding:0.75rem; background:var(--success-light); border:1px solid var(--success); border-radius:var(--radius-md);">
              <i class="fa-solid fa-award text-success" style="font-size:1.75rem; margin-bottom:0.35rem;"></i>
              <div style="font-weight:700; font-size:0.9rem; color:var(--success);">5. Resolution</div>
              <div style="font-size:0.75rem; color:var(--muted);">Citizen Verified</div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- IMPACT STATISTICS (Animated Counters) -->
    <section id="impact-stats" class="section bg-light">
      <div class="container">
        <h2 class="section-title">Citywide Impact Statistics</h2>
        <div class="stats-grid">
          <div class="stat-box">
            <h3 class="counter">12,458</h3>
            <p>Problems Reported</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-success">9,020</h3>
            <p>Problems Resolved (72.4%)</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-warning">2,480</h3>
            <p>Active Work Queue</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-accent">340</h3>
            <p>University Teams Matched</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-primary">156</h3>
            <p>Government Authorities</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-success">1.8M</h3>
            <p>Citizens Positively Impacted</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 7 STEPS HOW IT WORKS -->
    <section id="how-it-works" class="section">
      <div class="container">
        <h2 class="section-title">The 7-Step Resolution Engine</h2>
        <div class="steps-grid">
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-camera"></i></div>
            <h4>1. Report</h4>
            <p>Citizen captures photo or video with live browser GPS coordinates.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-microchip"></i></div>
            <h4>2. AI Analyze</h4>
            <p>Natural language extraction determines category, priority and eliminates duplicates.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-clipboard-check"></i></div>
            <h4>3. Verify</h4>
            <p>Desk validates authenticity and prevents spam complaints.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-route"></i></div>
            <h4>4. Route</h4>
            <p>Instant dispatch to exact departmental ward and starts SLA countdown.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-people-group"></i></div>
            <h4>5. Collaborate</h4>
            <p>University student teams and faculty mentors match with chronic issues.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-vial"></i></div>
            <h4>6. Solve & Pilot</h4>
            <p>Field deployment of rapid engineering or municipal repair solutions.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-chart-line"></i></div>
            <h4>7. Measure Impact</h4>
            <p>Residents verify resolution with star ratings and feedback verification.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- PROBLEM CATEGORIES -->
    <section id="problem-categories" class="section bg-light">
      <div class="container">
        <h2 class="section-title">Covered Civic Problem Domains</h2>
        <div class="categories-grid">
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-road"></i> Roads & Bridges</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-faucet-drip"></i> Water Supply</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-trash-can"></i> Solid Waste</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-bolt"></i> Electricity Grid</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-traffic-light"></i> Traffic & Transit</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-hospital"></i> Healthcare Clinics</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-school"></i> School Buildings</div>
          <div class="category-card" onclick="window.location.href='my-problems.html'"><i class="fa-solid fa-tree"></i> Environment & Lakes</div>
        </div>
      </div>
    </section>

    <!-- FEATURED PROBLEMS -->
    <section id="featured-problems" class="section">
      <div class="container">
        <div class="flex items-center justify-between" style="margin-bottom:2.5rem;">
          <div>
            <h2 style="font-size:2.25rem; font-weight:800;">Featured Real-World Complaints</h2>
            <p style="color:var(--muted);">Live complaints currently in progress across metropolitan wards.</p>
          </div>
          <a href="my-problems.html" class="btn btn-secondary">View All Incidents →</a>
        </div>

        <div class="dashboard-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem;">
          <!-- Problem 1 -->
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?w=600&auto=format&fit=crop" alt="Potholes">
              <div class="problem-badge-overlay">
                <span class="badge badge-warning">High Priority</span>
                <span class="badge badge-primary">In Progress</span>
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">CS-2026-0001 • Road</div>
              <h4 class="problem-title">Hazardous Deep Potholes on MG Road Junction</h4>
              <p class="problem-desc">Dangerous road crater disrupting two-wheeler transit. PWD mobilized with NIT team recycled asphalt prototype.</p>
              <div class="problem-meta">
                <span><i class="fa-solid fa-thumbs-up text-primary"></i> 184 Upvotes</span>
                <a href="problem-details.html?id=CS-2026-0001" class="btn btn-sm btn-primary">Track Details</a>
              </div>
            </div>
          </div>

          <!-- Problem 2 -->
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=600&auto=format&fit=crop" alt="Water">
              <div class="problem-badge-overlay">
                <span class="badge badge-danger">Critical</span>
                <span class="badge badge-danger">Escalated</span>
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">CS-2026-0002 • Water</div>
              <h4 class="problem-title">Contaminated Turbid Drinking Water Supply</h4>
              <p class="problem-desc">Tap water in Sector 4 running brown and turbid for 3 consecutive days. Direct risk of gastro infections.</p>
              <div class="problem-meta">
                <span><i class="fa-solid fa-thumbs-up text-primary"></i> 342 Upvotes</span>
                <a href="problem-details.html?id=CS-2026-0002" class="btn btn-sm btn-primary">Track Details</a>
              </div>
            </div>
          </div>

          <!-- Problem 3 -->
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="https://images.unsplash.com/photo-1506521781263-d8422e82f27a?w=600&auto=format&fit=crop" alt="Traffic">
              <div class="problem-badge-overlay">
                <span class="badge badge-accent">Medium</span>
                <span class="badge badge-secondary">Pilot Testing</span>
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">CS-2026-0005 • Transport</div>
              <h4 class="problem-title">Non-functional Traffic Signal at Busy 4-Way Cross</h4>
              <p class="problem-desc">Indiranagar 100ft road congestion solved via RV College IoT Computer-Vision adaptive timing pilot.</p>
              <div class="problem-meta">
                <span><i class="fa-solid fa-thumbs-up text-primary"></i> 215 Upvotes</span>
                <a href="problem-details.html?id=CS-2026-0005" class="btn btn-sm btn-primary">Track Details</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SUCCESS STORIES (Before & After) -->
    <section id="success-stories" class="section bg-light">
      <div class="container">
        <h2 class="section-title">Proven Before vs. After Impact</h2>
        <div class="dashboard-grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;">
          
          <div class="card">
            <div class="flex items-center justify-between" style="margin-bottom:1rem;">
              <span class="badge badge-success">Resolved & Verified</span>
              <span class="text-warning"><i class="fa-solid fa-star"></i> 5.0 Rating</span>
            </div>
            <h3>Rural Primary Health Clinic Solar Refrigeration</h3>
            <p style="font-size:0.9rem; color:var(--muted); margin-bottom:1.5rem;">
              Vaccines were spoiling due to grid cuts in Hebbal Ward. Tata Power CSR sponsored battery backup and student team configured remote temperature alarms.
            </p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; text-align:center;">
              <div style="background:var(--danger-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--danger);">BEFORE</div>
                <div style="font-size:1.25rem; font-weight:800; color:var(--danger);">120 Spoilages/mo</div>
              </div>
              <div style="background:var(--success-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--success);">AFTER</div>
                <div style="font-size:1.25rem; font-weight:800; color:var(--success);">0 Spoilages / 100%</div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="flex items-center justify-between" style="margin-bottom:1rem;">
              <span class="badge badge-success">Resolved & Verified</span>
              <span class="text-warning"><i class="fa-solid fa-star"></i> 4.8 Rating</span>
            </div>
            <h3>Indiranagar 100ft Road AI Signal Controller</h3>
            <p style="font-size:0.9rem; color:var(--muted); margin-bottom:1.5rem;">
              Traffic congestion caused 22-minute delays during morning hours. AI camera timing controller reduced idle times dynamically.
            </p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; text-align:center;">
              <div style="background:var(--warning-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--warning);">BEFORE</div>
                <div style="font-size:1.25rem; font-weight:800; color:var(--warning);">22 Mins Delay</div>
              </div>
              <div style="background:var(--success-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--success);">AFTER</div>
                <div style="font-size:1.25rem; font-weight:800; color:var(--success);">8 Mins Delay (-63%)</div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- PARTNERS -->
    <section class="section" style="text-align:center;">
      <div class="container">
        <h4 style="font-size:0.85rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:2rem;">
          Collaborating Municipal Agencies & Institutions
        </h4>
        <div class="flex justify-center items-center gap-4 flex-wrap" style="color:var(--muted); font-weight:700; font-size:1.15rem;">
          <span><i class="fa-solid fa-building-columns"></i> City Municipal Corporation</span>
          <span>•</span>
          <span><i class="fa-solid fa-road"></i> Public Works Dept</span>
          <span>•</span>
          <span><i class="fa-solid fa-faucet-drip"></i> Water Supply Board</span>
          <span>•</span>
          <span><i class="fa-solid fa-bolt"></i> State Electricity Grid</span>
          <span>•</span>
          <span><i class="fa-solid fa-graduation-cap"></i> NIT & RVCE Engineering</span>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="brand-logo" style="color:#fff; margin-bottom:1rem;">
            <i class="fa-solid fa-city" style="color:var(--accent);"></i>
            <span>CivicSolve<span class="ai-tag">AI</span></span>
          </div>
          <p style="font-size:0.9rem; color:#94A3B8;">
            AI-Powered Societal Problem Solving, Authority Routing & Collaborative Innovation Platform for smarter, cleaner, and safer cities.
          </p>
        </div>

        <div>
          <h4>Dashboards</h4>
          <a href="citizen-dashboard.html">Citizen Dashboard</a>
          <a href="government-dashboard.html">Government Command Center</a>
          <a href="authority-dashboard.html">Authority Work Queue</a>
          <a href="university-dashboard.html">University Innovation Hub</a>
          <a href="admin-dashboard.html">Admin Control Center</a>
        </div>

        <div>
          <h4>Resources</h4>
          <a href="submit-problem.html">Report Civic Issue</a>
          <a href="government-map.html">Incident Map</a>
          <a href="social-feed.html">Civic Social Feed</a>
          <a href="escalation-center.html">SLA Escalation Center</a>
        </div>

        <div>
          <h4>Quick Access</h4>
          <a href="login.html">Sign In</a>
          <a href="register.html">Register</a>
          <a href="my-problems.html">Track Complaint</a>
        </div>
      </div>

      <div class="footer-bottom">
        &copy; 2026 CivicSolve AI. Built with precision for production-grade societal impact demonstrations.
      </div>
    </div>
  </footer>

  <div id="toastContainer" class="toast-container"></div>

  <script src="js/data.js"></script>
  <script src="js/utils.js"></script>
  <script src="js/auth.js"></script>
  <script src="js/app.js"></script>
</body>
</html>"""

files_to_write = {
    "login.html": login_html,
    "register.html": register_html,
    "forgot-password.html": forgot_html,
    "index.html": index_html
}

for name, content in files_to_write.items():
    with open(os.path.join(FRONTEND_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)

print("Auth and Landing pages updated with complete modern UI!")
