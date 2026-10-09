import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "frontend", "index.html")

new_index_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CivicSolve AI - AI-Powered Societal Problem Solving & Collaborative Innovation Platform</title>
  
  <!-- CSS Stylesheets -->
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="css/animations.css">
  
  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    /* Premium landing micro-enhancements */
    .hero-glow {
      position: absolute;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(79, 70, 229, 0.15) 0%, rgba(6, 182, 212, 0.08) 50%, transparent 70%);
      top: -100px;
      left: 50%;
      transform: translateX(-50%);
      border-radius: 50%;
      z-index: 0;
      pointer-events: none;
    }

    .pipeline-node {
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .pipeline-node:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
    }

    .counter {
      display: inline-block;
      font-variant-numeric: tabular-nums;
    }
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="landing-header">
    <div class="container navbar">
      <a href="index.html" class="brand-logo">
        <i class="fa-solid fa-city"></i>
        <span>CivicSolve<span class="ai-tag">AI</span></span>
      </a>

      <!-- Desktop Nav -->
      <nav class="nav-menu">
        <a href="#how-it-works" class="nav-link">How It Works</a>
        <a href="#impact-stats" class="nav-link">Platform Impact</a>
        <a href="#problem-categories" class="nav-link">Categories</a>
        <a href="#featured-problems" class="nav-link">Live Incidents</a>
        <a href="#success-stories" class="nav-link">Success Stories</a>
        <a href="#faq" class="nav-link">FAQ</a>
        <a href="social-feed.html" class="nav-link">Civic Feed</a>
      </nav>

      <!-- Actions -->
      <div class="nav-actions">
        <button class="theme-toggle-btn" title="Toggle Dark/Light Mode">
          <i class="fa-solid fa-moon"></i>
        </button>
        <a href="login.html" class="btn btn-sm btn-secondary" style="display:inline-flex;">Sign In</a>
        <a href="submit-problem.html" class="btn btn-sm btn-primary">
          <i class="fa-solid fa-bullhorn"></i> Report Issue
        </a>
        <button id="landingMobileToggle" class="mobile-nav-toggle" aria-label="Open Navigation Menu">
          <i class="fa-solid fa-bars"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Slide-In Navigation Drawer -->
  <div id="mobileDrawerOverlay" class="mobile-drawer-overlay"></div>
  <aside id="mobileNavDrawer" class="mobile-nav-drawer">
    <div class="flex items-center justify-between" style="padding-bottom:1rem; border-bottom:1px solid var(--border);">
      <a href="index.html" class="brand-logo" style="font-size:1.15rem;">
        <i class="fa-solid fa-city"></i>
        <span>CivicSolve<span class="ai-tag">AI</span></span>
      </a>
      <button id="mobileDrawerClose" class="btn btn-icon btn-secondary" aria-label="Close Navigation Menu">
        <i class="fa-solid fa-xmark"></i>
      </button>
    </div>

    <div class="mobile-drawer-links">
      <a href="#how-it-works" class="mobile-link"><i class="fa-solid fa-circle-nodes text-primary"></i> How It Works</a>
      <a href="#impact-stats" class="mobile-link"><i class="fa-solid fa-chart-line text-success"></i> Platform Impact</a>
      <a href="#problem-categories" class="mobile-link"><i class="fa-solid fa-layer-group text-accent"></i> Categories</a>
      <a href="#featured-problems" class="mobile-link"><i class="fa-solid fa-triangle-exclamation text-warning"></i> Live Incidents</a>
      <a href="#success-stories" class="mobile-link"><i class="fa-solid fa-award text-secondary"></i> Success Stories</a>
      <a href="government-map.html" class="mobile-link"><i class="fa-solid fa-map-location-dot text-primary"></i> Incident Map</a>
      <a href="social-feed.html" class="mobile-link"><i class="fa-solid fa-comments text-accent"></i> Civic Social Feed</a>
      <a href="login.html" class="mobile-link"><i class="fa-solid fa-bolt text-warning"></i> 1-Click Demo (8 Roles)</a>
    </div>

    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid var(--border); display:flex; flex-direction:column; gap:0.75rem;">
      <a href="submit-problem.html" class="btn btn-primary w-100">
        <i class="fa-solid fa-camera"></i> Report a Problem
      </a>
      <a href="login.html" class="btn btn-secondary w-100">
        <i class="fa-solid fa-right-to-bracket"></i> Sign In to Account
      </a>
    </div>
  </aside>

  <main>
    <!-- HERO SECTION -->
    <section class="hero" style="position:relative; overflow:hidden;">
      <div class="hero-glow"></div>

      <div class="container hero-content" style="position:relative; z-index:1;">
        
        <!-- Top Status Pill -->
        <div style="display:inline-flex; align-items:center; gap:0.6rem; background:rgba(79, 70, 229, 0.08); border:1px solid rgba(79, 70, 229, 0.2); padding:0.45rem 1.25rem; border-radius:var(--radius-full); margin-bottom:1.5rem;">
          <span class="badge badge-primary"><i class="fa-solid fa-microchip"></i> Civic AI Core v4.2</span>
          <span style="font-size:0.85rem; font-weight:600; color:var(--dark);">Live Government Routing & SLA Watchdog</span>
          <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:var(--success);"></span>
        </div>

        <!-- Main Heading -->
        <h1 class="hero-title" style="font-family:'Outfit', sans-serif; font-size:clamp(2.2rem, 5.5vw, 3.85rem); font-weight:900; letter-spacing:-0.03em; margin-bottom:1.25rem;">
          From Citizen Problems to <br><span>Real Measurable Solutions.</span>
        </h1>

        <!-- Subtitle -->
        <p class="hero-subtitle" style="font-size:clamp(1rem, 2vw, 1.25rem); color:var(--muted); max-width:820px; margin:0 auto 2.25rem; line-height:1.65;">
          Report civic and societal problems in seconds. Our AI categorizes urgency, removes duplicates, identifies the responsible government department, and mobilizes university engineering teams to co-create lasting solutions.
        </p>

        <!-- CTA Buttons Group (Desktop, Laptop, Mobile Responsive) -->
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

        <!-- INTERACTIVE LIVE AI SCENARIO SIMULATOR -->
        <div class="pipeline-card">
          <div class="ai-scan-bar"></div>

          <div class="flex items-center justify-between flex-wrap gap-2" style="margin-bottom:1.25rem;">
            <div>
              <span class="badge badge-primary" style="margin-bottom:0.25rem;"><i class="fa-solid fa-wand-magic-sparkles"></i> Interactive AI Engine Demo</span>
              <h3 style="font-size:1.2rem; color:var(--dark);">Select a civic scenario to witness the live triage flow:</h3>
            </div>
            <span class="badge badge-success"><i class="fa-solid fa-bolt"></i> Real-Time Synthesis</span>
          </div>

          <!-- Scenario Pills -->
          <div class="flex gap-2 flex-wrap" style="margin-bottom:1.75rem;">
            <button class="scenario-pill active" onclick="switchScenario(0)">
              <i class="fa-solid fa-road"></i> MG Road Deep Potholes
            </button>
            <button class="scenario-pill" onclick="switchScenario(1)">
              <i class="fa-solid fa-faucet-drip"></i> Contaminated Water Supply
            </button>
            <button class="scenario-pill" onclick="switchScenario(2)">
              <i class="fa-solid fa-bolt"></i> Dangling 11kV Power Wire
            </button>
            <button class="scenario-pill" onclick="switchScenario(3)">
              <i class="fa-solid fa-traffic-light"></i> Indiranagar Traffic Congestion
            </button>
          </div>

          <!-- Flow Pipeline Steps Grid -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(170px, 1fr)); gap:1rem; text-align:center; margin-bottom:1.5rem;">
            
            <div class="pipeline-node" style="padding:1rem; background:var(--bg-subtle); border-radius:var(--radius-md); border:1px solid var(--border);">
              <div style="width:38px; height:38px; border-radius:50%; background:var(--primary-light); color:var(--primary); display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; font-size:1.1rem;">
                <i class="fa-solid fa-camera"></i>
              </div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">1. INTAKE</div>
              <div id="simIntake" style="font-weight:700; font-size:0.875rem; color:var(--dark); margin-top:2px;">Live GPS & Photo</div>
            </div>

            <div class="pipeline-node" style="padding:1rem; background:rgba(6, 182, 212, 0.08); border-radius:var(--radius-md); border:1px solid var(--accent);">
              <div style="width:38px; height:38px; border-radius:50%; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; font-size:1.1rem;">
                <i class="fa-solid fa-brain"></i>
              </div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--accent);">2. AI SCORING</div>
              <div id="simScore" style="font-weight:800; font-size:1.1rem; color:var(--accent); margin-top:2px;">92/100 Priority</div>
            </div>

            <div class="pipeline-node" style="padding:1rem; background:var(--bg-subtle); border-radius:var(--radius-md); border:1px solid var(--border);">
              <div style="width:38px; height:38px; border-radius:50%; background:var(--warning-light); color:var(--warning); display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; font-size:1.1rem;">
                <i class="fa-solid fa-building-columns"></i>
              </div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">3. ROUTED AUTHORITY</div>
              <div id="simAuth" style="font-weight:700; font-size:0.875rem; color:var(--dark); margin-top:2px;">Public Works Dept</div>
            </div>

            <div class="pipeline-node" style="padding:1rem; background:var(--bg-subtle); border-radius:var(--radius-md); border:1px solid var(--border);">
              <div style="width:38px; height:38px; border-radius:50%; background:#EDE9FE; color:var(--secondary); display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; font-size:1.1rem;">
                <i class="fa-solid fa-graduation-cap"></i>
              </div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--muted);">4. ACADEMIC MATCH</div>
              <div id="simTeam" style="font-weight:700; font-size:0.875rem; color:var(--dark); margin-top:2px;">NIT Materials Squad</div>
            </div>

            <div class="pipeline-node" style="padding:1rem; background:var(--success-light); border-radius:var(--radius-md); border:1px solid var(--success);">
              <div style="width:38px; height:38px; border-radius:50%; background:#D1FAE5; color:var(--success); display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; font-size:1.1rem;">
                <i class="fa-solid fa-award"></i>
              </div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--success);">5. VERIFIED OUTCOME</div>
              <div id="simOutcome" style="font-weight:700; font-size:0.875rem; color:var(--success); margin-top:2px;">Recycled Asphalt Pilot</div>
            </div>

          </div>

          <!-- Scenario Details Banner -->
          <div style="background:var(--bg-subtle); padding:1rem 1.25rem; border-radius:var(--radius-md); border-left:4px solid var(--primary); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.75rem;">
            <div style="font-size:0.875rem; color:var(--dark);" id="simDescription">
              <strong>Simulated Action:</strong> Potholes near Metro Pillar 42 routed to PWD. SLA set to 72 hours. NIT student prototype linked for cold-mix recycled road patching.
            </div>
            <a href="problem-details.html?id=CS-2026-0001" id="simLink" class="btn btn-sm btn-primary">Inspect Full Timeline →</a>
          </div>

        </div>

      </div>
    </section>

    <!-- IMPACT STATISTICS (Animated JavaScript Counters) -->
    <section id="impact-stats" class="section bg-light">
      <div class="container">
        <h2 class="section-title">Citywide Measurable Impact</h2>
        <div class="stats-grid">
          <div class="stat-box">
            <h3 class="counter" data-target="12458">0</h3>
            <p>Problems Reported</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-success" data-target="9020">0</h3>
            <p>Problems Resolved (72.4%)</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-warning" data-target="2480">0</h3>
            <p>Active Work Queue</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-accent" data-target="340">0</h3>
            <p>University Teams Matched</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-primary" data-target="156">0</h3>
            <p>Government Authorities</p>
          </div>
          <div class="stat-box">
            <h3 class="counter text-success" data-target="1800000">0</h3>
            <p>Citizens Benefited</p>
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
            <p>NLP & computer vision extract category, priority and eliminate duplicate complaints.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-clipboard-check"></i></div>
            <h4>3. Verify</h4>
            <p>Admin desk validates authenticity and prevents frivolous or fraudulent reports.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-route"></i></div>
            <h4>4. Route</h4>
            <p>Instant dispatch to exact departmental ward and initializes SLA timer.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-people-group"></i></div>
            <h4>5. Collaborate</h4>
            <p>University student teams and faculty mentors match with systemic challenges.</p>
          </div>
          <div class="step-card">
            <div class="step-icon"><i class="fa-solid fa-vial"></i></div>
            <h4>6. Solve & Pilot</h4>
            <p>Field deployment of rapid engineering or municipal repair prototypes.</p>
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
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-road"></i>
            <div>Roads & Bridges</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">142 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-faucet-drip"></i>
            <div>Water Supply</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">94 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-trash-can"></i>
            <div>Solid Waste</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">310 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-bolt"></i>
            <div>Electricity Grid</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">145 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-traffic-light"></i>
            <div>Traffic & Transit</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">82 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-hospital"></i>
            <div>Healthcare Clinics</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">49 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-school"></i>
            <div>School Buildings</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">33 Active</span>
          </div>
          <div class="category-card" onclick="window.location.href='my-problems.html'">
            <i class="fa-solid fa-tree"></i>
            <div>Environment & Lakes</div>
            <span class="badge badge-neutral" style="margin-top:0.35rem;">67 Active</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURED LIVE PROBLEMS -->
    <section id="featured-problems" class="section">
      <div class="container">
        <div class="flex items-center justify-between flex-wrap gap-2" style="margin-bottom:2.5rem;">
          <div>
            <h2 style="font-size:2.25rem; font-weight:800;">Featured Real-World Incidents</h2>
            <p style="color:var(--muted);">Live complaints currently in progress across metropolitan wards.</p>
          </div>
          <div class="flex gap-2">
            <a href="government-map.html" class="btn btn-sm btn-secondary"><i class="fa-solid fa-map"></i> View Map</a>
            <a href="my-problems.html" class="btn btn-sm btn-primary">Browse All Issues →</a>
          </div>
        </div>

        <div class="dashboard-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem;">
          
          <!-- Card 1 -->
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?w=600&auto=format&fit=crop" alt="Potholes">
              <div class="problem-badge-overlay">
                <span class="badge badge-warning"><i class="fa-solid fa-bolt"></i> High Priority</span>
                <span class="badge badge-primary">In Progress</span>
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">CS-2026-0001 • Road</div>
              <h4 class="problem-title">Hazardous Deep Potholes on MG Road Junction</h4>
              <p class="problem-desc">Dangerous road crater disrupting two-wheeler transit. PWD mobilized with NIT team recycled asphalt prototype.</p>
              <div class="problem-meta">
                <button class="btn btn-sm btn-secondary" onclick="upvoteHome('CS-2026-0001', this)">
                  <i class="fa-solid fa-thumbs-up text-primary"></i> <span class="vote-count">184</span> Upvotes
                </button>
                <a href="problem-details.html?id=CS-2026-0001" class="btn btn-sm btn-primary">Track Details →</a>
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=600&auto=format&fit=crop" alt="Water">
              <div class="problem-badge-overlay">
                <span class="badge badge-danger"><i class="fa-solid fa-fire"></i> Critical</span>
                <span class="badge badge-danger">Escalated</span>
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">CS-2026-0002 • Water</div>
              <h4 class="problem-title">Contaminated Turbid Drinking Water Supply</h4>
              <p class="problem-desc">Tap water in Sector 4 running brown and turbid for 3 consecutive days. Direct risk of gastro infections.</p>
              <div class="problem-meta">
                <button class="btn btn-sm btn-secondary" onclick="upvoteHome('CS-2026-0002', this)">
                  <i class="fa-solid fa-thumbs-up text-primary"></i> <span class="vote-count">342</span> Upvotes
                </button>
                <a href="problem-details.html?id=CS-2026-0002" class="btn btn-sm btn-primary">Track Details →</a>
              </div>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="problem-card">
            <div class="problem-thumb">
              <img src="https://images.unsplash.com/photo-1506521781263-d8422e82f27a?w=600&auto=format&fit=crop" alt="Traffic">
              <div class="problem-badge-overlay">
                <span class="badge badge-accent">Medium</span>
                <span class="badge badge-secondary"><i class="fa-solid fa-flask"></i> Pilot Testing</span>
              </div>
            </div>
            <div class="problem-body">
              <div class="problem-id">CS-2026-0005 • Transport</div>
              <h4 class="problem-title">Non-functional Traffic Signal at Busy 4-Way Cross</h4>
              <p class="problem-desc">Indiranagar 100ft road congestion solved via RV College IoT Computer-Vision adaptive timing pilot.</p>
              <div class="problem-meta">
                <button class="btn btn-sm btn-secondary" onclick="upvoteHome('CS-2026-0005', this)">
                  <i class="fa-solid fa-thumbs-up text-primary"></i> <span class="vote-count">215</span> Upvotes
                </button>
                <a href="problem-details.html?id=CS-2026-0005" class="btn btn-sm btn-primary">Track Details →</a>
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
              <span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> Resolved & Verified</span>
              <span class="text-warning"><i class="fa-solid fa-star"></i> 5.0 Rating</span>
            </div>
            <h3>Rural Primary Health Clinic Solar Refrigeration</h3>
            <p style="font-size:0.9rem; color:var(--muted); margin-bottom:1.5rem;">
              Vaccines were spoiling due to grid cuts in Hebbal Ward. Tata Power CSR sponsored battery backup and student team configured remote temperature alarms.
            </p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; text-align:center;">
              <div style="background:var(--danger-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--danger);">BEFORE</div>
                <div style="font-size:1.35rem; font-weight:800; color:var(--danger);">120 Spoilages/mo</div>
              </div>
              <div style="background:var(--success-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--success);">AFTER</div>
                <div style="font-size:1.35rem; font-weight:800; color:var(--success);">0 Spoilages (100% Save)</div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="flex items-center justify-between" style="margin-bottom:1rem;">
              <span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> Resolved & Verified</span>
              <span class="text-warning"><i class="fa-solid fa-star"></i> 4.8 Rating</span>
            </div>
            <h3>Indiranagar 100ft Road AI Signal Controller</h3>
            <p style="font-size:0.9rem; color:var(--muted); margin-bottom:1.5rem;">
              Traffic congestion caused 22-minute delays during morning hours. AI camera timing controller reduced idle times dynamically.
            </p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; text-align:center;">
              <div style="background:var(--warning-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--warning);">BEFORE</div>
                <div style="font-size:1.35rem; font-weight:800; color:var(--warning);">22 Mins Delay</div>
              </div>
              <div style="background:var(--success-light); padding:1rem; border-radius:var(--radius-md);">
                <div style="font-size:0.8rem; font-weight:700; color:var(--success);">AFTER</div>
                <div style="font-size:1.35rem; font-weight:800; color:var(--success);">8 Mins Delay (-63%)</div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- TESTIMONIALS -->
    <section class="section">
      <div class="container">
        <h2 class="section-title">Trusted by Citizens, Authorities & Innovators</h2>
        <div class="dashboard-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.5rem;">
          
          <div class="testimonial-card">
            <p style="font-size:0.95rem; color:var(--dark); margin-bottom:1.5rem; line-height:1.6;">
              "Reporting the contaminated water supply in our ward took less than 2 minutes. The live SLA tracking kept the authority accountable, and water supply was restored within 24 hours!"
            </p>
            <div class="flex items-center gap-2">
              <div class="user-mini-avatar" style="width:42px; height:42px; background:var(--primary);">AS</div>
              <div>
                <strong style="display:block; font-size:0.9rem;">Ananya Sharma</strong>
                <span style="font-size:0.8rem; color:var(--muted);">Resident, Ward 112</span>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <p style="font-size:0.95rem; color:var(--dark); margin-bottom:1.5rem; line-height:1.6;">
              "The AI categorization and duplicate check filters out 40% of redundant noise. My zonal team receives clean, prioritized coordinates with photographic evidence."
            </p>
            <div class="flex items-center gap-2">
              <div class="user-mini-avatar" style="width:42px; height:42px; background:var(--warning);">RV</div>
              <div>
                <strong style="display:block; font-size:0.9rem;">Er. Rajesh Verma</strong>
                <span style="font-size:0.8rem; color:var(--muted);">Executive Engineer, PWD</span>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <p style="font-size:0.95rem; color:var(--dark); margin-bottom:1.5rem; line-height:1.6;">
              "Our student team got direct access to test our computer vision traffic timing model on actual municipal intersections. It bridged the gap between academic theory and real-world impact."
            </p>
            <div class="flex items-center gap-2">
              <div class="user-mini-avatar" style="width:42px; height:42px; background:var(--secondary);">RO</div>
              <div>
                <strong style="display:block; font-size:0.9rem;">Rohan Varma</strong>
                <span style="font-size:0.8rem; color:var(--muted);">Lead, SmartFlow AI (RVCE)</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- FAQ ACCORDION -->
    <section id="faq" class="section bg-light">
      <div class="container">
        <h2 class="section-title">Frequently Asked Questions</h2>
        
        <div class="faq-list">
          <div class="faq-item active">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>How does CivicSolve AI identify the correct government authority?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer">
              Our natural language and spatial classification engine cross-references the reported problem category, description keywords, and precise GPS coordinates against administrative municipal boundaries and departmental mandates (e.g. Roads to PWD, Water pipelines to Water Supply & Sewerage Board).
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>What happens if an authority fails to act within the SLA timeframe?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer">
              CivicSolve AI triggers an automated 4-tier escalation protocol. After Tier 1 reminders (0–2 days), unresolved complaints escalate to the Zonal Senior Officer (Tier 2), Department Head (Tier 3), and ultimately the District Magistrate & Municipal Commissioner review docket (Tier 4).
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>How do universities and student teams collaborate?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer">
              Chronic or recurring civic issues are published to the Academic Innovation Hub. Faculty mentors and student teams apply via AI Smart Matching to engineer hardware/software prototypes. Approved prototypes enter field pilot testing with municipal clearance and CSR sponsorship.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>How are duplicate complaints prevented?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer">
              When a citizen prepares to submit a problem, the AI performs a real-time semantic and geographic proximity scan within a 1.5 km radius. If a matching report is found, the citizen is notified and invited to upvote or add evidence to the existing ticket instead of creating a duplicate.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>Is CivicSolve AI mobile-friendly?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer">
              Yes! The platform is 100% responsive on smartphones, tablets, laptops, and desktop screens. It features mobile slide drawers, touch-friendly bottom navigation, direct device GPS integration, and browser WebRTC camera access.
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- PARTNERS -->
    <section class="section" style="text-align:center; padding:3rem 0;">
      <div class="container">
        <h4 style="font-size:0.85rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:1.5rem;">
          Collaborating Municipal Agencies & Institutions
        </h4>
        <div class="flex justify-center items-center gap-4 flex-wrap" style="color:var(--muted); font-weight:700; font-size:1.1rem;">
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
          <p style="font-size:0.9rem; color:#94A3B8; margin-bottom:1.25rem;">
            AI-Powered Societal Problem Solving, Authority Routing & Collaborative Innovation Platform for smarter, cleaner, and safer cities.
          </p>
          <div style="display:inline-flex; align-items:center; gap:0.5rem; background:#1E293B; padding:0.4rem 0.85rem; border-radius:var(--radius-full); font-size:0.75rem; color:#10B981; border:1px solid #334155;">
            <i class="fa-solid fa-circle fa-beat"></i> All Municipal Systems Operational
          </div>
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
          <a href="register.html">Register Account</a>
          <a href="my-problems.html">Track Complaint</a>
          <a href="team-matching.html">AI Smart Matching</a>
        </div>
      </div>

      <div class="footer-bottom">
        &copy; 2026 CivicSolve AI. Built with precision for production-grade societal impact demonstrations.
      </div>
    </div>
  </footer>

  <!-- MOBILE BOTTOM ACTION BAR -->
  <nav class="mobile-bottom-bar" aria-label="Mobile Navigation">
    <a href="index.html" class="bottom-bar-link active">
      <i class="fa-solid fa-house"></i>
      <span>Home</span>
    </a>
    <a href="submit-problem.html" class="bottom-bar-link">
      <i class="fa-solid fa-camera"></i>
      <span>Report</span>
    </a>
    <a href="government-map.html" class="bottom-bar-link">
      <i class="fa-solid fa-map-location-dot"></i>
      <span>Map</span>
    </a>
    <a href="social-feed.html" class="bottom-bar-link">
      <i class="fa-solid fa-comments"></i>
      <span>Feed</span>
    </a>
    <a href="login.html" class="bottom-bar-link">
      <i class="fa-solid fa-user-lock"></i>
      <span>Roles</span>
    </a>
  </nav>

  <!-- Toast Notification Container -->
  <div id="toastContainer" class="toast-container"></div>

  <!-- Core Scripts -->
  <script src="js/data.js"></script>
  <script src="js/utils.js"></script>
  <script src="js/auth.js"></script>
  <script src="js/app.js"></script>

  <!-- Landing Interactions Script -->
  <script>
    // 1. Mobile Navigation Drawer Toggle
    const mobileToggleBtn = document.getElementById("landingMobileToggle");
    const mobileDrawer = document.getElementById("mobileNavDrawer");
    const mobileOverlay = document.getElementById("mobileDrawerOverlay");
    const mobileDrawerClose = document.getElementById("mobileDrawerClose");

    function openMobileDrawer() {
      if (mobileDrawer) mobileDrawer.classList.add("open");
      if (mobileOverlay) mobileOverlay.classList.add("active");
      document.body.style.overflow = "hidden";
    }

    function closeMobileDrawer() {
      if (mobileDrawer) mobileDrawer.classList.remove("open");
      if (mobileOverlay) mobileOverlay.classList.remove("active");
      document.body.style.overflow = "";
    }

    if (mobileToggleBtn) mobileToggleBtn.addEventListener("click", openMobileDrawer);
    if (mobileDrawerClose) mobileDrawerClose.addEventListener("click", closeMobileDrawer);
    if (mobileOverlay) mobileOverlay.addEventListener("click", closeMobileDrawer);

    document.querySelectorAll(".mobile-link").forEach(link => {
      link.addEventListener("click", closeMobileDrawer);
    });

    // 2. Animated Stats Counter (IntersectionObserver)
    const counters = document.querySelectorAll(".counter");
    let countersStarted = false;

    function startCounters() {
      if (countersStarted) return;
      countersStarted = true;

      counters.forEach(counter => {
        const target = +counter.getAttribute("data-target");
        let count = 0;
        const speed = target / 60; // 60 frames

        const updateCount = () => {
          count += speed;
          if (count < target) {
            if (target >= 1000000) {
              counter.innerText = (count / 1000000).toFixed(1) + "M";
            } else {
              counter.innerText = Math.floor(count).toLocaleString();
            }
            requestAnimationFrame(updateCount);
          } else {
            if (target >= 1000000) {
              counter.innerText = (target / 1000000).toFixed(1) + "M";
            } else {
              counter.innerText = target.toLocaleString();
            }
          }
        };
        updateCount();
      });
    }

    const statsSection = document.getElementById("impact-stats");
    if (statsSection && 'IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            startCounters();
          }
        });
      }, { threshold: 0.2 });
      observer.observe(statsSection);
    } else {
      startCounters();
    }

    // 3. Interactive Scenario Switcher
    const scenarios = [
      {
        intake: "Live GPS & Photo",
        score: "92/100 Priority",
        auth: "Public Works Dept (PWD)",
        team: "NIT Materials Squad",
        outcome: "Recycled Asphalt Pilot",
        desc: "<strong>Simulated Action:</strong> Potholes near Metro Pillar 42 routed to PWD. SLA set to 72 hours. NIT student prototype linked for cold-mix recycled road patching.",
        link: "problem-details.html?id=CS-2026-0001"
      },
      {
        intake: "Tap Turbidity Sample",
        score: "98/100 Priority",
        auth: "Water Supply Board (BWSSB)",
        team: "IISc Environmental Lab",
        outcome: "Urgent Pipeline Flush",
        desc: "<strong>Simulated Action:</strong> High gastro risk detected. Escalation priority triggered. Direct alert pushed to Chief Sanitation Officer.",
        link: "problem-details.html?id=CS-2026-0002"
      },
      {
        intake: "Overhead Wire Snap",
        score: "99/100 Priority",
        auth: "Electricity Grid (BESCOM)",
        team: "Rapid Grid Response Squad",
        outcome: "Substation Trip Dispatched",
        desc: "<strong>Simulated Action:</strong> Critical 11kV line near park playground. Immediate automated trip signal sent to zonal power substation.",
        link: "problem-details.html?id=CS-2026-0004"
      },
      {
        intake: "Camera Junction Video",
        score: "76/100 Priority",
        auth: "City Traffic Police",
        team: "SmartFlow AI Team (RVCE)",
        outcome: "Dynamic Signal Controller",
        desc: "<strong>Simulated Action:</strong> 100ft road congestion detected. RV College AI team deployed computer-vision dynamic signal timing pilot.",
        link: "problem-details.html?id=CS-2026-0005"
      }
    ];

    function switchScenario(index) {
      document.querySelectorAll(".scenario-pill").forEach((btn, idx) => {
        if (idx === index) btn.classList.add("active");
        else btn.classList.remove("active");
      });

      const s = scenarios[index];
      const intakeEl = document.getElementById("simIntake");
      const scoreEl = document.getElementById("simScore");
      const authEl = document.getElementById("simAuth");
      const teamEl = document.getElementById("simTeam");
      const outcomeEl = document.getElementById("simOutcome");
      const descEl = document.getElementById("simDescription");
      const linkEl = document.getElementById("simLink");

      if (intakeEl) intakeEl.textContent = s.intake;
      if (scoreEl) scoreEl.textContent = s.score;
      if (authEl) authEl.textContent = s.auth;
      if (teamEl) teamEl.textContent = s.team;
      if (outcomeEl) outcomeEl.textContent = s.outcome;
      if (descEl) descEl.innerHTML = s.desc;
      if (linkEl) linkEl.href = s.link;
    }

    // 4. FAQ Accordion Toggle
    function toggleFaq(element) {
      const parent = element.parentElement;
      const wasActive = parent.classList.contains("active");

      document.querySelectorAll(".faq-item").forEach(item => {
        item.classList.remove("active");
      });

      if (!wasActive) {
        parent.classList.add("active");
      }
    }

    // 5. Upvote from Home Page
    function upvoteHome(probId, btn) {
      const countEl = btn.querySelector(".vote-count");
      if (countEl) {
        let current = parseInt(countEl.textContent) || 0;
        countEl.textContent = current + 1;
        btn.classList.add("btn-primary");
        btn.classList.remove("btn-secondary");
        CivicUtils.showToast("Upvoted! Priority weight increased.", "success");
      }
    }
  </script>
</body>
</html>
"""

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(new_index_content)

print("Updated index.html with complete responsive enhancements, mobile drawer, bottom bar, and interactive scenario simulator!")
