import os

files = {
    "frontend/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CivicSolve AI - Empowering Citizens</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/responsive.css">
    <link rel="stylesheet" href="css/components.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <header class="navbar">
        <div class="container nav-container">
            <div class="logo">
                <i class="fa-solid fa-city"></i> CivicSolve AI
            </div>
            <nav class="nav-links">
                <a href="#how-it-works">How It Works</a>
                <a href="#stats">Impact</a>
                <a href="#categories">Categories</a>
                <a href="login.html" class="nav-link-login">Login</a>
                <a href="register.html" class="btn btn-primary btn-sm">Register</a>
            </nav>
        </div>
    </header>
    
    <main>
        <!-- HERO SECTION -->
        <section class="hero">
            <div class="container hero-content">
                <h1 class="hero-title">From Citizen Problems to <span>Real Solutions.</span></h1>
                <p class="hero-subtitle">Report civic problems, let AI analyze them, connect them with the right authority and bring communities, universities and innovators together to solve them.</p>
                <div class="cta-buttons">
                    <a href="submit-problem.html" class="btn btn-primary"><i class="fa-solid fa-bullhorn"></i> Report a Problem</a>
                    <a href="login.html" class="btn btn-secondary"><i class="fa-solid fa-building-columns"></i> Government Login</a>
                </div>
            </div>
        </section>

        <!-- HOW IT WORKS -->
        <section id="how-it-works" class="section">
            <div class="container">
                <h2 class="section-title">How It Works</h2>
                <div class="steps-grid">
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-camera"></i></div>
                        <h4>1. Report</h4>
                        <p>Citizen captures and submits the issue.</p>
                    </div>
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-microchip"></i></div>
                        <h4>2. AI Analyze</h4>
                        <p>AI categorizes and prioritizes.</p>
                    </div>
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-check-double"></i></div>
                        <h4>3. Verify</h4>
                        <p>Admin confirms problem details.</p>
                    </div>
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-route"></i></div>
                        <h4>4. Route</h4>
                        <p>Routed to correct authority.</p>
                    </div>
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-users-gear"></i></div>
                        <h4>5. Collaborate</h4>
                        <p>Universities & Industry join in.</p>
                    </div>
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-lightbulb"></i></div>
                        <h4>6. Solve</h4>
                        <p>Pilot testing and deployment.</p>
                    </div>
                    <div class="step-card">
                        <div class="step-icon"><i class="fa-solid fa-chart-pie"></i></div>
                        <h4>7. Impact</h4>
                        <p>Measure civic improvement.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- STATS SECTION -->
        <section id="stats" class="section bg-light">
            <div class="container">
                <h2 class="section-title">Platform Impact</h2>
                <div class="stats-grid">
                    <div class="stat-box">
                        <h3 class="counter">12,458</h3>
                        <p>Problems Reported</p>
                    </div>
                    <div class="stat-box">
                        <h3 class="counter text-success">9,020</h3>
                        <p>Problems Resolved</p>
                    </div>
                    <div class="stat-box">
                        <h3 class="counter text-warning">2,480</h3>
                        <p>Active Problems</p>
                    </div>
                    <div class="stat-box">
                        <h3 class="counter text-accent">340</h3>
                        <p>University Teams</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- CATEGORIES -->
        <section id="categories" class="section">
            <div class="container">
                <h2 class="section-title">Problem Categories</h2>
                <div class="categories-grid">
                    <div class="category-card"><i class="fa-solid fa-road"></i> Roads</div>
                    <div class="category-card"><i class="fa-solid fa-faucet-drip"></i> Water</div>
                    <div class="category-card"><i class="fa-solid fa-trash-can"></i> Waste</div>
                    <div class="category-card"><i class="fa-solid fa-bolt"></i> Electricity</div>
                    <div class="category-card"><i class="fa-solid fa-school"></i> Education</div>
                    <div class="category-card"><i class="fa-solid fa-hospital"></i> Healthcare</div>
                    <div class="category-card"><i class="fa-solid fa-bus"></i> Transport</div>
                    <div class="category-card"><i class="fa-solid fa-leaf"></i> Environment</div>
                </div>
            </div>
        </section>

    </main>
    
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h3>CivicSolve AI</h3>
                    <p>Building better cities together.</p>
                </div>
                <div>
                    <h4>Links</h4>
                    <a href="about.html">About</a>
                    <a href="contact.html">Contact</a>
                </div>
                <div>
                    <h4>Legal</h4>
                    <a href="#">Privacy</a>
                    <a href="#">Terms</a>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; 2026 CivicSolve AI. All rights reserved.
            </div>
        </div>
    </footer>
    <script src="js/app.js"></script>
</body>
</html>""",

    "frontend/css/style.css": """:root {
    --primary: #4F46E5;
    --secondary: #7C3AED;
    --accent: #06B6D4;
    --success: #10B981;
    --warning: #F59E0B;
    --danger: #EF4444;
    --bg: #F8FAFC;
    --bg-light: #F1F5F9;
    --dark: #0F172A;
    --muted: #64748B;
    --white: #FFFFFF;
    --border: #E2E8F0;
    
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg);
    color: var(--dark);
    line-height: 1.5;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

a {
    text-decoration: none;
    color: var(--primary);
}

/* NAVBAR */
.navbar {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: 1px solid var(--border);
}
.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
}
.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.nav-links {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}
.nav-links a {
    color: var(--muted);
    font-weight: 500;
    transition: color 0.3s;
}
.nav-links a:hover {
    color: var(--primary);
}
.nav-link-login {
    font-weight: 600 !important;
    color: var(--dark) !important;
}

/* BUTTONS */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    border: none;
}
.btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}
.btn-primary {
    background: var(--primary);
    color: var(--white);
    box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.39);
}
.btn-primary:hover {
    background: var(--secondary);
    color: var(--white);
    transform: translateY(-1px);
}
.btn-secondary {
    background: var(--white);
    color: var(--dark);
    border: 1px solid var(--border);
}
.btn-secondary:hover {
    background: var(--bg-light);
}

/* TYPOGRAPHY UTILS */
.text-success { color: var(--success); }
.text-warning { color: var(--warning); }
.text-accent { color: var(--accent); }

/* SECTIONS */
.section {
    padding: 5rem 0;
}
.bg-light {
    background-color: var(--bg-light);
}
.section-title {
    text-align: center;
    font-size: 2.25rem;
    margin-bottom: 3rem;
    color: var(--dark);
    font-weight: 700;
}

/* HERO */
.hero {
    padding: 8rem 0 6rem;
    text-align: center;
    background: linear-gradient(180deg, #EEF2FF 0%, var(--bg) 100%);
}
.hero-title {
    font-size: 4rem;
    font-weight: 800;
    letter-spacing: -0.025em;
    line-height: 1.1;
    margin-bottom: 1.5rem;
}
.hero-title span {
    background: linear-gradient(to right, var(--primary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 1.25rem;
    color: var(--muted);
    max-width: 700px;
    margin: 0 auto 2.5rem;
}
.hero .cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
}

/* HOW IT WORKS */
.steps-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.5rem;
}
.step-card {
    background: var(--white);
    padding: 1.5rem;
    border-radius: 1rem;
    text-align: center;
    box-shadow: var(--shadow-sm);
    transition: transform 0.3s, box-shadow 0.3s;
    border: 1px solid var(--border);
}
.step-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow);
}
.step-icon {
    width: 50px;
    height: 50px;
    margin: 0 auto 1rem;
    background: #EEF2FF;
    color: var(--primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
}
.step-card h4 {
    margin-bottom: 0.5rem;
    color: var(--dark);
}
.step-card p {
    font-size: 0.875rem;
    color: var(--muted);
}

/* STATS */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
}
.stat-box {
    background: var(--white);
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
}
.stat-box h3 {
    font-size: 3rem;
    font-weight: 700;
    color: var(--primary);
}
.stat-box p {
    color: var(--muted);
    font-weight: 500;
    margin-top: 0.5rem;
}

/* CATEGORIES */
.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 1.5rem;
}
.category-card {
    background: var(--white);
    border: 1px solid var(--border);
    padding: 1.5rem;
    border-radius: 1rem;
    text-align: center;
    font-weight: 600;
    color: var(--dark);
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: var(--shadow-sm);
}
.category-card i {
    display: block;
    font-size: 2rem;
    margin-bottom: 1rem;
    color: var(--accent);
}
.category-card:hover {
    border-color: var(--primary);
    transform: translateY(-2px);
    box-shadow: var(--shadow);
}

/* FOOTER */
.footer {
    background: var(--dark);
    color: var(--white);
    padding: 4rem 0 2rem;
}
.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 3rem;
    margin-bottom: 3rem;
}
.footer-grid h3 {
    margin-bottom: 1rem;
    font-size: 1.5rem;
}
.footer-grid h4 {
    margin-bottom: 1.5rem;
    color: var(--muted);
}
.footer-grid a {
    display: block;
    color: #94A3B8;
    margin-bottom: 0.75rem;
}
.footer-grid a:hover {
    color: var(--white);
}
.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid #334155;
    color: #94A3B8;
}
""",

    "frontend/login.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login - CivicSolve AI</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .auth-container { max-width: 400px; margin: 4rem auto; background: white; padding: 2rem; border-radius: 1rem; box-shadow: var(--shadow); }
        .auth-container h2 { text-align: center; margin-bottom: 2rem; }
        .form-group { margin-bottom: 1.5rem; }
        .form-group label { display: block; margin-bottom: 0.5rem; font-weight: 500; }
        .form-group input, .form-group select { width: 100%; padding: 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem; }
        .auth-btn { width: 100%; }
    </style>
</head>
<body>
    <header class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">CivicSolve AI</a>
        </div>
    </header>
    <div class="container">
        <div class="auth-container">
            <h2>Welcome Back</h2>
            <form id="loginForm">
                <div class="form-group">
                    <label>Role</label>
                    <select id="roleSelect">
                        <option value="citizen">Citizen</option>
                        <option value="authority">Authority Officer</option>
                        <option value="government">Government Official</option>
                        <option value="admin">System Admin</option>
                        <option value="university">University Team</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" placeholder="demo@civicsolve.ai" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="••••••••" required>
                </div>
                <button type="button" class="btn btn-primary auth-btn" onclick="handleLogin()">Login</button>
            </form>
            <p style="text-align:center; margin-top:1.5rem; color:var(--muted);">
                Don't have an account? <a href="register.html">Register here</a>
            </p>
        </div>
    </div>
    <script>
        function handleLogin() {
            const role = document.getElementById('roleSelect').value;
            window.location.href = role + '-dashboard.html';
        }
    </script>
</body>
</html>""",

    "frontend/register.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register - CivicSolve AI</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .auth-container { max-width: 500px; margin: 4rem auto; background: white; padding: 2rem; border-radius: 1rem; box-shadow: var(--shadow); }
        .auth-container h2 { text-align: center; margin-bottom: 2rem; }
        .form-group { margin-bottom: 1.5rem; }
        .form-group label { display: block; margin-bottom: 0.5rem; font-weight: 500; }
        .form-group input, .form-group select { width: 100%; padding: 0.75rem; border: 1px solid var(--border); border-radius: 0.5rem; }
        .auth-btn { width: 100%; }
    </style>
</head>
<body>
    <header class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">CivicSolve AI</a>
        </div>
    </header>
    <div class="container">
        <div class="auth-container">
            <h2>Create Account</h2>
            <form>
                <div class="form-group">
                    <label>I am a...</label>
                    <select>
                        <option>Citizen</option>
                        <option>Authority Officer</option>
                        <option>University/Student</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" placeholder="John Doe" required>
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" placeholder="john@example.com" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="••••••••" required>
                </div>
                <button type="button" class="btn btn-primary auth-btn" onclick="window.location.href='citizen-dashboard.html'">Register</button>
            </form>
            <p style="text-align:center; margin-top:1.5rem; color:var(--muted);">
                Already have an account? <a href="login.html">Login here</a>
            </p>
        </div>
    </div>
</body>
</html>"""
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Pages completed!")
