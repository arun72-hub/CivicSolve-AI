import os

dirs = [
    "frontend/css",
    "frontend/js",
    "frontend/assets/icons",
    "frontend/assets/images",
    "backend-ready"
]

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
</head>
<body>
    <header class="navbar">
        <div class="logo">CivicSolve AI</div>
        <nav>
            <a href="login.html">Login</a>
            <a href="register.html">Register</a>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h1>From Citizen Problems to Real Solutions</h1>
            <p>Report civic problems, let AI analyze them, connect them with the right authority and bring communities, universities and innovators together to solve them.</p>
            <div class="cta-buttons">
                <a href="submit-problem.html" class="btn btn-primary">Report a Problem</a>
                <a href="login.html" class="btn btn-secondary">Government Login</a>
            </div>
        </section>
        <section class="stats">
            <div class="stat-card">
                <h3>12,458</h3>
                <p>Problems Reported</p>
            </div>
            <div class="stat-card">
                <h3>9,020</h3>
                <p>Problems Resolved</p>
            </div>
            <div class="stat-card">
                <h3>156</h3>
                <p>Authorities</p>
            </div>
        </section>
    </main>
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
    --dark: #0F172A;
    --muted: #64748B;
    --white: #FFFFFF;
}

body {
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
    background-color: var(--bg);
    color: var(--dark);
}

.navbar {
    display: flex;
    justify-content: space-between;
    padding: 1rem 2rem;
    background-color: var(--white);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.logo {
    font-weight: 700;
    font-size: 1.5rem;
    color: var(--primary);
}

.hero {
    text-align: center;
    padding: 5rem 2rem;
    background: linear-gradient(135deg, var(--bg) 0%, #e0e7ff 100%);
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.25rem;
    color: var(--muted);
    max-width: 800px;
    margin: 0 auto 2rem;
}

.btn {
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    text-decoration: none;
    font-weight: 600;
    display: inline-block;
    margin: 0 0.5rem;
}

.btn-primary {
    background-color: var(--primary);
    color: var(--white);
}

.btn-secondary {
    background-color: var(--white);
    color: var(--primary);
    border: 1px solid var(--primary);
}

.stats {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 4rem 2rem;
}

.stat-card {
    background: var(--white);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 200px;
}

.stat-card h3 {
    font-size: 2.5rem;
    color: var(--primary);
    margin: 0;
}

.stat-card p {
    color: var(--muted);
    margin-top: 0.5rem;
}
""",
    
    "frontend/css/dashboard.css": """
.dashboard-layout {
    display: flex;
    min-height: 100vh;
}
.sidebar {
    width: 250px;
    background: var(--white);
    border-right: 1px solid #e2e8f0;
    padding: 2rem 1rem;
}
.main-content {
    flex: 1;
    padding: 2rem;
}
""",
    
    "frontend/css/components.css": """
.card {
    background: var(--white);
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    padding: 1.5rem;
}
""",
    
    "frontend/css/responsive.css": """
@media (max-width: 768px) {
    .stats {
        flex-direction: column;
        align-items: center;
    }
    .dashboard-layout {
        flex-direction: column;
    }
    .sidebar {
        width: 100%;
    }
}
""",

    "frontend/js/app.js": """
console.log("CivicSolve AI Initialized");
""",
    
    "frontend/js/data.js": """
const mockProblems = [
    {
        id: "CS-2026-0001",
        title: "Large Pothole on Main Road",
        category: "Road",
        severity: "High",
        status: "Assigned"
    }
];
""",

    "frontend/citizen-dashboard.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Citizen Dashboard - CivicSolve AI</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/dashboard.css">
</head>
<body>
    <div class="dashboard-layout">
        <aside class="sidebar">
            <div class="logo">CivicSolve AI</div>
            <nav>
                <a href="citizen-dashboard.html">Dashboard</a>
                <a href="submit-problem.html">Report Problem</a>
                <a href="my-problems.html">My Problems</a>
                <a href="index.html">Logout</a>
            </nav>
        </aside>
        <main class="main-content">
            <h1>Good Evening, Citizen 👋</h1>
            <div class="stats">
                <div class="stat-card">
                    <h3>3</h3>
                    <p>Problems Submitted</p>
                </div>
            </div>
        </main>
    </div>
</body>
</html>""",

    "frontend/submit-problem.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Report Problem - CivicSolve AI</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/dashboard.css">
</head>
<body>
    <div class="dashboard-layout">
        <aside class="sidebar">
            <div class="logo">CivicSolve AI</div>
            <nav>
                <a href="citizen-dashboard.html">Dashboard</a>
                <a href="submit-problem.html">Report Problem</a>
            </nav>
        </aside>
        <main class="main-content">
            <h1>Report a Problem</h1>
            <form id="problemForm" class="card" style="max-width: 600px; margin: 0 auto; display:flex; flex-direction:column; gap:1rem;">
                <input type="text" placeholder="Problem Title" required style="padding:0.5rem;">
                <textarea placeholder="Description" required style="padding:0.5rem;"></textarea>
                <select style="padding:0.5rem;">
                    <option>Road</option>
                    <option>Water</option>
                    <option>Waste</option>
                </select>
                <button type="button" class="btn btn-primary" onclick="alert('Simulating AI Analysis and Submission...')">Submit to AI Analysis</button>
            </form>
        </main>
    </div>
</body>
</html>"""
}

# Create extra html stubs
html_pages = [
    "login.html", "register.html", "forgot-password.html", "my-problems.html",
    "problem-details.html", "social-feed.html", "notifications.html", "profile.html",
    "authority-dashboard.html", "authority-problems.html", "authority-problem-details.html",
    "authority-officers.html", "authority-reports.html", "government-dashboard.html",
    "government-monitoring.html", "government-map.html", "government-analytics.html",
    "escalation-center.html", "admin-dashboard.html", "user-management.html",
    "problem-verification.html", "authority-management.html", "system-analytics.html",
    "university-dashboard.html", "university-problems.html", "faculty-dashboard.html",
    "student-team-dashboard.html", "team-matching.html", "solution-workspace.html",
    "solution-details.html", "industry-dashboard.html", "industry-opportunities.html"
]

for page in html_pages:
    if f"frontend/{page}" not in files:
        files[f"frontend/{page}"] = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{page.replace('.html', '').replace('-', ' ').title()} - CivicSolve AI</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/dashboard.css">
</head>
<body>
    <div class="dashboard-layout">
        <aside class="sidebar">
            <div class="logo">CivicSolve AI</div>
            <nav>
                <a href="index.html">Home</a>
            </nav>
        </aside>
        <main class="main-content">
            <h1>{page.replace('.html', '').replace('-', ' ').title()}</h1>
            <p>This page is under construction.</p>
        </main>
    </div>
</body>
</html>'''

# Create extra js stubs
js_files = [
    "auth.js", "dashboard.js", "problems.js", "ai-analysis.js",
    "authority-routing.js", "notifications.js", "map.js", "social-feed.js",
    "analytics.js", "matching.js", "solutions.js", "utils.js"
]

for js in js_files:
    if f"frontend/js/{js}" not in files:
        files[f"frontend/js/{js}"] = f"// {js} placeholder"

# Create extra css stubs
css_files = ["animations.css"]
for css in css_files:
    if f"frontend/css/{css}" not in files:
        files[f"frontend/css/{css}"] = f"/* {css} placeholder */"

files["README.md"] = """# CivicSolve AI

AI-Powered Societal Problem Solving, Authority Routing & Collaborative Innovation Platform.

## Run
Open `frontend/index.html` with Live Server.
"""

files["backend-ready/README.md"] = "# Backend APIs placeholder\nWill contain FastAPI code."

for d in dirs:
    os.makedirs(d, exist_ok=True)

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Files generated successfully!")
