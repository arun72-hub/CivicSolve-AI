/**
 * CivicSolve AI - Social Feed Interactions
 */
const SocialFeedController = {
  upvote(problemId) {
    const p = window.CivicDB.getProblemById(problemId);
    if (p) {
      p.upvotes = (p.upvotes || 0) + 1;
      window.CivicDB.saveProblem(p);
      CivicUtils.showToast(`Upvoted! Priority weight increased for ${problemId}`, "success");
    }
  }
};

window.SocialFeedController = SocialFeedController;