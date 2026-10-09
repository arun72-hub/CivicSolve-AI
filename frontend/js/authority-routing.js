/**
 * CivicSolve AI - Authority Routing Engine & SLA Watchdog
 */
const AuthorityRouter = {
  getRules() {
    return [
      { category: "Road", authorityId: "AUTH-PWD-01", department: "Roads & Bridges", defaultSla: 72 },
      { category: "Water", authorityId: "AUTH-WATER-02", department: "Hydraulic Engineering", defaultSla: 48 },
      { category: "Waste", authorityId: "AUTH-BBMP-03", department: "Solid Waste Management", defaultSla: 24 },
      { category: "Electricity", authorityId: "AUTH-BESCOM-04", department: "Power Transmission", defaultSla: 12 },
      { category: "Transport", authorityId: "AUTH-TRAFFIC-05", department: "Traffic Engineering", defaultSla: 48 },
      { category: "Healthcare", authorityId: "AUTH-HEALTH-06", department: "Public Clinics", defaultSla: 24 },
      { category: "Education", authorityId: "AUTH-EDU-07", department: "School Infrastructure", defaultSla: 120 },
      { category: "Environment", authorityId: "AUTH-PCB-08", department: "Environmental Protection", defaultSla: 48 }
    ];
  },

  routeProblem(category, severity, district) {
    const rules = this.getRules();
    const match = rules.find(r => r.category.toLowerCase() === (category || "").toLowerCase()) || rules[0];
    
    // SLA adjustment by severity
    let adjustedSla = match.defaultSla;
    if (severity === "Critical") adjustedSla = Math.max(6, Math.floor(match.defaultSla * 0.25));
    if (severity === "High") adjustedSla = Math.floor(match.defaultSla * 0.5);

    return {
      authorityId: match.authorityId,
      department: match.department,
      slaHours: adjustedSla,
      matchedReason: `Matched rule: Category '${category}' mapped to ${match.department} in ${district || 'Urban District'}. SLA calculated as ${adjustedSla} hours.`
    };
  }
};

window.AuthorityRouter = AuthorityRouter;