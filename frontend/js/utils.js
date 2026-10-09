/**
 * CivicSolve AI - Common Utilities, Toasts, Modals & Helpers
 */

const CivicUtils = {
  // Toast notification
  showToast(message, type = "info", duration = 4000) {
    let container = document.getElementById("toastContainer");
    if (!container) {
      container = document.createElement("div");
      container.id = "toastContainer";
      container.className = "toast-container";
      document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    
    const icons = {
      success: '<i class="fa-solid fa-circle-check text-success"></i>',
      error: '<i class="fa-solid fa-circle-xmark text-danger"></i>',
      warning: '<i class="fa-solid fa-triangle-exclamation text-warning"></i>',
      info: '<i class="fa-solid fa-circle-info text-accent"></i>'
    };

    toast.innerHTML = `
      ${icons[type] || icons.info}
      <div style="flex:1; font-size:0.9rem; font-weight:500;">${message}</div>
      <button style="background:none;border:none;cursor:pointer;color:var(--muted);" onclick="this.parentElement.remove()">
        <i class="fa-solid fa-xmark"></i>
      </button>
    `;

    container.appendChild(toast);
    setTimeout(() => {
      if (toast.parentElement) toast.remove();
    }, duration);
  },

  // Modal helpers
  openModal(modalId) {
    const el = document.getElementById(modalId);
    if (el) el.classList.add("active");
  },

  closeModal(modalId) {
    const el = document.getElementById(modalId);
    if (el) el.classList.remove("active");
  },

  // Generate unique problem ID
  generateProblemId() {
    const problems = window.CivicDB ? window.CivicDB.getProblems() : [];
    const nextNum = String(problems.length + 1).padStart(4, '0');
    return `CS-2026-${nextNum}`;
  },

  // Format Date
  formatDate(isoString) {
    if (!isoString) return "N/A";
    const d = new Date(isoString);
    return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
  },

  // Severity color badge
  getSeverityBadge(sev) {
    const s = (sev || "").toLowerCase();
    if (s === "critical") return '<span class="badge badge-danger"><i class="fa-solid fa-bolt"></i> Critical</span>';
    if (s === "high") return '<span class="badge badge-warning"><i class="fa-solid fa-triangle-exclamation"></i> High</span>';
    if (s === "medium") return '<span class="badge badge-accent">Medium</span>';
    return '<span class="badge badge-neutral">Low</span>';
  },

  // Status color badge
  getStatusBadge(st) {
    const s = (st || "").toLowerCase();
    if (s === "resolved") return '<span class="badge badge-success"><i class="fa-solid fa-check"></i> Resolved</span>';
    if (s === "in progress") return '<span class="badge badge-primary"><i class="fa-solid fa-spinner fa-spin"></i> In Progress</span>';
    if (s === "escalated") return '<span class="badge badge-danger"><i class="fa-solid fa-fire"></i> Escalated</span>';
    if (s === "pilot testing") return '<span class="badge badge-secondary"><i class="fa-solid fa-flask"></i> Pilot Testing</span>';
    if (s === "verified") return '<span class="badge badge-accent">Verified</span>';
    return `<span class="badge badge-neutral">${st || 'Submitted'}</span>`;
  },

  // Social Share helper
  shareProblem(title, url = window.location.href) {
    if (navigator.share) {
      navigator.share({
        title: `CivicSolve AI: ${title}`,
        text: `Check out this civic issue reported on CivicSolve AI: ${title}`,
        url: url
      }).catch(() => {});
    } else {
      navigator.clipboard.writeText(url);
      CivicUtils.showToast("Link copied to clipboard for sharing!", "success");
    }
  }
};

window.CivicUtils = CivicUtils;
