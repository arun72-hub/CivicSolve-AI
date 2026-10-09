/**
 * CivicSolve AI - University & Student Team Matching Engine
 */
const CivicMatching = {
  calculateMatchScore(problem, team) {
    let score = 70;
    if (problem.category === "Transport" && team.domain === "AI & Vision") score += 26;
    if (problem.category === "Road" && team.domain === "Civil Materials") score += 22;
    if (problem.category === "Environment" && team.domain === "Robotics") score += 18;
    return Math.min(99, score);
  },

  getRecommendedTeams(problemId) {
    const teams = [
      { id: "TEAM-1", name: "SmartFlow AI Team", college: "RV College of Engineering", domain: "AI & Vision", matchPct: 96 },
      { id: "TEAM-2", name: "EcoPave Innovators", college: "National Institute of Technology", domain: "Civil Materials", matchPct: 92 },
      { id: "TEAM-3", name: "AquaClean Robotics", college: "IISc Bio-Lab", domain: "Robotics", matchPct: 88 }
    ];
    return teams;
  }
};

window.CivicMatching = CivicMatching;