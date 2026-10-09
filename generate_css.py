import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_DIR = os.path.join(BASE_DIR, "frontend", "css")
os.makedirs(CSS_DIR, exist_ok=True)

style_css = """/* ==========================================================================
   CivicSolve AI - Modern Global Design System
   ========================================================================== */

:root {
  --primary: #4F46E5;
  --primary-hover: #4338CA;
  --primary-light: #EEF2FF;
  --secondary: #7C3AED;
  --secondary-hover: #6D28D9;
  --accent: #06B6D4;
  --accent-light: #ECFEFF;
  --success: #10B981;
  --success-light: #ECFDF5;
  --warning: #F59E0B;
  --warning-light: #FFFBEB;
  --danger: #EF4444;
  --danger-light: #FEF2F2;
  --bg: #F8FAFC;
  --bg-card: #FFFFFF;
  --bg-subtle: #F1F5F9;
  --dark: #0F172A;
  --dark-surface: #1E293B;
  --muted: #64748B;
  --border: #E2E8F0;
  --white: #FFFFFF;

  --shadow-xs: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
  --shadow-sm: 0 1px 3px 0 rgba(15, 23, 42, 0.1), 0 1px 2px -1px rgba(15, 23, 42, 0.1);
  --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.1), 0 2px 4px -2px rgba(15, 23, 42, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(15, 23, 42, 0.1), 0 4px 6px -4px rgba(15, 23, 42, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(15, 23, 42, 0.1), 0 8px 10px -6px rgba(15, 23, 42, 0.1);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;
  --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="dark"] {
  --bg: #0B0F19;
  --bg-card: #131B2E;
  --bg-subtle: #1E293B;
  --dark: #F8FAFC;
  --muted: #94A3B8;
  --border: #243048;
  --white: #131B2E;
  --primary-light: #1E1B4B;
  --accent-light: #083344;
  --success-light: #064E3B;
  --warning-light: #451A03;
  --danger-light: #450A0A;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

body {
  background-color: var(--bg);
  color: var(--dark);
  line-height: 1.6;
  min-height: 100vh;
  transition: background-color 0.3s ease, color 0.3s ease;
  overflow-x: hidden;
}

a {
  text-decoration: none;
  color: inherit;
  transition: var(--transition);
}

ul {
  list-style: none;
}

img, video {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  color: var(--dark);
  font-weight: 700;
  line-height: 1.25;
}

p {
  color: var(--muted);
}

/* Containers */
.container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.container-fluid {
  width: 100%;
  padding: 0 1.5rem;
}

/* Common Layout Helpers */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.justify-center { justify-content: center; }
.gap-1 { gap: 0.5rem; }
.gap-2 { gap: 1rem; }
.gap-3 { gap: 1.5rem; }
.gap-4 { gap: 2rem; }
.grid { display: grid; }
.w-100 { width: 100%; }

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: var(--radius-md);
  border: 1px solid transparent;
  cursor: pointer;
  transition: var(--transition);
  white-space: nowrap;
}

.btn:active {
  transform: scale(0.98);
}

.btn-sm {
  padding: 0.45rem 0.9rem;
  font-size: 0.85rem;
}

.btn-lg {
  padding: 0.9rem 2rem;
  font-size: 1.05rem;
}

.btn-primary {
  background-color: var(--primary);
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
}

.btn-primary:hover {
  background-color: var(--primary-hover);
  box-shadow: 0 6px 20px rgba(79, 70, 229, 0.45);
  transform: translateY(-2px);
}

.btn-secondary {
  background-color: var(--bg-card);
  color: var(--dark) !important;
  border-color: var(--border);
}

.btn-secondary:hover {
  background-color: var(--bg-subtle);
  border-color: var(--muted);
}

.btn-accent {
  background-color: var(--accent);
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px rgba(6, 182, 212, 0.35);
}

.btn-accent:hover {
  opacity: 0.9;
  transform: translateY(-2px);
}

.btn-danger {
  background-color: var(--danger);
  color: #FFFFFF !important;
}

.btn-outline-primary {
  background: transparent;
  color: var(--primary) !important;
  border-color: var(--primary);
}

.btn-outline-primary:hover {
  background-color: var(--primary-light);
}

.btn-icon {
  width: 40px;
  height: 40px;
  padding: 0;
  border-radius: var(--radius-full);
}

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: var(--radius-full);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.badge-primary { background: var(--primary-light); color: var(--primary); }
.badge-secondary { background: #EDE9FE; color: var(--secondary); }
.badge-accent { background: var(--accent-light); color: var(--accent); }
.badge-success { background: var(--success-light); color: var(--success); }
.badge-warning { background: var(--warning-light); color: var(--warning); }
.badge-danger { background: var(--danger-light); color: var(--danger); }
.badge-neutral { background: var(--bg-subtle); color: var(--muted); }

/* Form Controls */
.form-group {
  margin-bottom: 1.25rem;
}

.form-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--dark);
}

.form-control, .form-select {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 0.95rem;
  background-color: var(--bg-card);
  color: var(--dark);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: var(--transition);
  outline: none;
}

.form-control:focus, .form-select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
}

textarea.form-control {
  min-height: 100px;
  resize: vertical;
}

/* Landing Header & Navigation */
.landing-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  transition: var(--transition);
}

[data-theme="dark"] .landing-header {
  background: rgba(19, 27, 46, 0.88);
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--dark);
  letter-spacing: -0.02em;
}

.brand-logo i, .brand-logo svg {
  color: var(--primary);
}

.brand-logo span.ai-tag {
  font-size: 0.7rem;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #fff;
  padding: 2px 6px;
  border-radius: var(--radius-sm);
  margin-left: 2px;
  vertical-align: middle;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.75rem;
}

.nav-link {
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--muted);
}

.nav-link:hover, .nav-link.active {
  color: var(--primary);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

/* Theme Switcher Button */
.theme-toggle-btn {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  color: var(--dark);
  border-radius: var(--radius-full);
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
}

.theme-toggle-btn:hover {
  background: var(--border);
}
"""

dashboard_css = """/* ==========================================================================
   CivicSolve AI - Dashboard Layout Styles
   ========================================================================== */

.app-wrapper {
  display: flex;
  min-height: 100vh;
  position: relative;
  background-color: var(--bg);
}

/* Sidebar */
.app-sidebar {
  width: 260px;
  background-color: var(--bg-card);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 1000;
  transition: var(--transition);
  overflow-y: auto;
}

.sidebar-header {
  height: 72px;
  padding: 0 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border);
}

.sidebar-role-badge {
  margin: 1rem 1.5rem 0.5rem;
  padding: 0.5rem 0.75rem;
  background: var(--primary-light);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sidebar-role-badge .role-title {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--primary);
  text-transform: uppercase;
}

.sidebar-nav {
  padding: 1rem 0;
  flex: 1;
}

.nav-section-title {
  padding: 0.5rem 1.5rem;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.sidebar-link {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.925rem;
  font-weight: 500;
  color: var(--muted);
  border-left: 3px solid transparent;
  transition: var(--transition);
}

.sidebar-link i {
  font-size: 1.1rem;
  width: 20px;
  text-align: center;
}

.sidebar-link:hover {
  color: var(--primary);
  background-color: var(--bg-subtle);
}

.sidebar-link.active {
  color: var(--primary);
  background-color: var(--primary-light);
  border-left-color: var(--primary);
  font-weight: 600;
}

.sidebar-footer {
  padding: 1rem 1.5rem;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.user-mini-avatar {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-full);
  background: var(--primary);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}

.user-mini-info {
  flex: 1;
  overflow: hidden;
}

.user-mini-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--dark);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-mini-role {
  font-size: 0.75rem;
  color: var(--muted);
}

/* Main App Content Container */
.app-main {
  margin-left: 260px;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: var(--transition);
}

/* Top App Bar */
.app-topbar {
  height: 72px;
  background-color: var(--bg-card);
  border-bottom: 1px solid var(--border);
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 900;
}

.topbar-search {
  position: relative;
  width: 340px;
}

.topbar-search input {
  width: 100%;
  padding: 0.6rem 1rem 0.6rem 2.5rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  color: var(--dark);
  outline: none;
}

.topbar-search input:focus {
  border-color: var(--primary);
  background: var(--bg-card);
}

.topbar-search i {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  font-size: 0.875rem;
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.topbar-btn {
  background: transparent;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--muted);
  cursor: pointer;
  position: relative;
  transition: var(--transition);
}

.topbar-btn:hover {
  background-color: var(--bg-subtle);
  color: var(--dark);
}

.topbar-badge {
  position: absolute;
  top: 6px;
  right: 6px;
  width: 8px;
  height: 8px;
  background-color: var(--danger);
  border-radius: var(--radius-full);
  border: 2px solid var(--bg-card);
}

/* Content Area */
.app-content {
  padding: 2rem;
  flex: 1;
}

.page-header {
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.page-title {
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.page-subtitle {
  color: var(--muted);
  font-size: 0.95rem;
  margin-top: 0.25rem;
}
"""

components_css = """/* ==========================================================================
   CivicSolve AI - Reusable UI Components
   ========================================================================== */

/* Modern Card */
.card {
  background-color: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.card:hover {
  box-shadow: var(--shadow-md);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.25rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--border);
}

.card-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--dark);
}

/* Stat Cards */
.stat-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  box-shadow: var(--shadow-sm);
  position: relative;
  overflow: hidden;
}

.stat-icon {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}

.stat-icon.primary { background: var(--primary-light); color: var(--primary); }
.stat-icon.success { background: var(--success-light); color: var(--success); }
.stat-icon.warning { background: var(--warning-light); color: var(--warning); }
.stat-icon.danger { background: var(--danger-light); color: var(--danger); }
.stat-icon.accent { background: var(--accent-light); color: var(--accent); }

.stat-info .stat-value {
  font-size: 1.85rem;
  font-weight: 800;
  color: var(--dark);
  line-height: 1.1;
}

.stat-info .stat-label {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--muted);
  margin-top: 0.25rem;
}

/* Problem Cards */
.problem-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.problem-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary);
}

.problem-thumb {
  height: 180px;
  background-color: var(--bg-subtle);
  position: relative;
  overflow: hidden;
}

.problem-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.problem-badge-overlay {
  position: absolute;
  top: 12px;
  left: 12px;
  display: flex;
  gap: 6px;
}

.problem-body {
  padding: 1.25rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.problem-id {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
  margin-bottom: 0.35rem;
}

.problem-title {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--dark);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.problem-desc {
  font-size: 0.875rem;
  color: var(--muted);
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.problem-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: auto;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border);
  font-size: 0.8rem;
  color: var(--muted);
}

/* AI Analysis Visual Card */
.ai-analysis-card {
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.04), rgba(6, 182, 212, 0.08));
  border: 1px solid rgba(79, 70, 229, 0.2);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
}

.ai-scan-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, transparent, var(--accent), var(--primary), transparent);
  animation: scan-horizontal 2.5s infinite linear;
}

.ai-metric-box {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1rem;
  text-align: center;
}

.ai-metric-val {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--primary);
}

/* Progress bar */
.progress-bar-wrap {
  width: 100%;
  height: 8px;
  background: var(--bg-subtle);
  border-radius: var(--radius-full);
  overflow: hidden;
  margin: 0.5rem 0;
}

.progress-fill {
  height: 100%;
  border-radius: var(--radius-full);
  background: linear-gradient(90deg, var(--primary), var(--accent));
  transition: width 0.5s ease;
}

/* Timeline */
.timeline {
  position: relative;
  padding-left: 2rem;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 0;
  bottom: 0;
  width: 2px;
  background-color: var(--border);
}

.timeline-item {
  position: relative;
  margin-bottom: 1.75rem;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-dot {
  position: absolute;
  left: -2rem;
  top: 4px;
  width: 16px;
  height: 16px;
  border-radius: var(--radius-full);
  background: var(--bg-card);
  border: 3px solid var(--primary);
}

.timeline-dot.active {
  background: var(--primary);
  box-shadow: 0 0 0 4px var(--primary-light);
}

.timeline-content h5 {
  font-size: 0.95rem;
  margin-bottom: 0.2rem;
}

.timeline-content time {
  font-size: 0.75rem;
  color: var(--muted);
  display: block;
  margin-bottom: 0.35rem;
}

/* Tables */
.table-responsive {
  width: 100%;
  overflow-x: auto;
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.custom-table th {
  padding: 0.9rem 1.2rem;
  background: var(--bg-subtle);
  color: var(--muted);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid var(--border);
}

.custom-table td {
  padding: 1rem 1.2rem;
  border-bottom: 1px solid var(--border);
  color: var(--dark);
  font-size: 0.9rem;
}

.custom-table tbody tr:hover {
  background-color: var(--bg-subtle);
}

/* Toast System */
.toast-container {
  position: fixed;
  top: 24px;
  right: 24px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.toast {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 1rem 1.25rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-width: 300px;
  max-width: 420px;
  animation: slideInRight 0.3s ease;
}

.toast.success { border-left: 4px solid var(--success); }
.toast.error { border-left: 4px solid var(--danger); }
.toast.warning { border-left: 4px solid var(--warning); }
.toast.info { border-left: 4px solid var(--primary); }

/* Modal System */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(4px);
  z-index: 2000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.modal-overlay.active {
  display: flex;
}

.modal-box {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  border: 1px solid var(--border);
  animation: zoomIn 0.25s ease;
}

.modal-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-body {
  padding: 1.5rem;
}

.modal-footer {
  padding: 1rem 1.5rem;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
}

/* Kanban Board */
.kanban-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
  align-items: flex-start;
}

.kanban-col {
  background: var(--bg-subtle);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  min-height: 500px;
}

.kanban-col-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  font-weight: 700;
}

.kanban-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1rem;
  margin-bottom: 0.75rem;
  box-shadow: var(--shadow-xs);
  cursor: grab;
  transition: var(--transition);
}

.kanban-card:hover {
  box-shadow: var(--shadow-md);
}

/* Map Containers */
#civicMap, #fullScreenMap {
  width: 100%;
  height: 480px;
  border-radius: var(--radius-lg);
  z-index: 10;
}
"""

responsive_css = """/* ==========================================================================
   CivicSolve AI - Responsive Breakpoints & Mobile Optimization
   ========================================================================== */

/* Large Screens */
@media (min-width: 1200px) {
  .dashboard-grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
  }
  .dashboard-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
  }
}

/* Tablets (iPad, etc.) */
@media (max-width: 1024px) {
  .app-sidebar {
    transform: translateX(-100%);
  }

  .app-sidebar.show {
    transform: translateX(0);
  }

  .app-main {
    margin-left: 0;
  }

  .dashboard-grid-4, .dashboard-grid-3 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }

  .topbar-search {
    width: 240px;
  }
}

/* Mobile Devices */
@media (max-width: 768px) {
  .nav-menu {
    display: none;
  }

  .hero-title {
    font-size: 2.5rem !important;
  }

  .hero-subtitle {
    font-size: 1.05rem !important;
  }

  .hero .cta-buttons {
    flex-direction: column;
  }

  .app-content {
    padding: 1.25rem;
  }

  .dashboard-grid-4, .dashboard-grid-3 {
    grid-template-columns: 1fr;
  }

  .topbar-search {
    display: none;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .custom-table thead {
    display: none;
  }

  .custom-table, .custom-table tbody, .custom-table tr, .custom-table td {
    display: block;
    width: 100%;
  }

  .custom-table tr {
    margin-bottom: 1rem;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    background: var(--bg-card);
    padding: 0.5rem 0;
  }

  .custom-table td {
    text-align: right;
    padding: 0.5rem 1rem;
    position: relative;
    border-bottom: 1px solid var(--border);
  }

  .custom-table td::before {
    content: attr(data-label);
    float: left;
    font-weight: 700;
    font-size: 0.75rem;
    text-transform: uppercase;
    color: var(--muted);
  }

  .custom-table td:last-child {
    border-bottom: none;
  }
}
"""

animations_css = """/* ==========================================================================
   CivicSolve AI - Modern Micro-Interactions & Keyframe Animations
   ========================================================================== */

@keyframes scan-horizontal {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(200%); }
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes zoomIn {
  from {
    transform: scale(0.95);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes pulseGlow {
  0%, 100% {
    box-shadow: 0 0 15px rgba(79, 70, 229, 0.4);
  }
  50% {
    box-shadow: 0 0 25px rgba(6, 182, 212, 0.6);
  }
}

.ai-pulsing {
  animation: pulseGlow 2.5s infinite;
}

.shimmer {
  background: linear-gradient(90deg, var(--bg-subtle) 25%, var(--border) 50%, var(--bg-subtle) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
"""

files = {
    "style.css": style_css,
    "dashboard.css": dashboard_css,
    "components.css": components_css,
    "responsive.css": responsive_css,
    "animations.css": animations_css
}

for name, content in files.items():
    with open(os.path.join(CSS_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)

print("CSS files created successfully!")
