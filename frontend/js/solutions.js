/**
 * CivicSolve AI - Kanban Task Board & Citizen Feedback
 */

const CivicSolutions = {
  // Star rating handler in citizen feedback
  initFeedbackRating() {
    const stars = document.querySelectorAll(".feedback-star");
    let currentRating = 5;

    stars.forEach(star => {
      star.addEventListener("click", () => {
        const val = parseInt(star.getAttribute("data-value"));
        currentRating = val;
        stars.forEach((s, idx) => {
          if (idx < val) {
            s.classList.add("text-warning");
            s.classList.remove("text-muted");
          } else {
            s.classList.remove("text-warning");
            s.classList.add("text-muted");
          }
        });
      });
    });

    const submitBtn = document.getElementById("btnSubmitFeedback");
    if (submitBtn) {
      submitBtn.addEventListener("click", () => {
        const comment = document.getElementById("feedbackComment") ? document.getElementById("feedbackComment").value : "";
        CivicUtils.showToast(`Thank you! Verified with ${currentRating}-star citizen rating.`, "success");
        setTimeout(() => {
          CivicUtils.closeModal("feedbackModal");
        }, 800);
      });
    }
  }
};

window.CivicSolutions = CivicSolutions;
