/**
 * CivicSolve AI - Central Dashboard Controller
 */
const DashboardController = {
  refreshLiveCounters() {
    const problems = window.CivicDB ? window.CivicDB.getProblems() : [];
    const submittedEl = document.getElementById("statSubmitted");
    const underReviewEl = document.getElementById("statUnderReview");
    const inProgressEl = document.getElementById("statInProgress");
    const resolvedEl = document.getElementById("statResolved");

    if (submittedEl) submittedEl.textContent = problems.length;
    if (underReviewEl) underReviewEl.textContent = problems.filter(p => p.status === "Under Review").length;
    if (inProgressEl) inProgressEl.textContent = problems.filter(p => p.status === "In Progress" || p.status === "Assigned").length;
    if (resolvedEl) resolvedEl.textContent = problems.filter(p => p.status === "Resolved").length;
  }
};

document.addEventListener("DOMContentLoaded", () => {
  DashboardController.refreshLiveCounters();
});

window.DashboardController = DashboardController;