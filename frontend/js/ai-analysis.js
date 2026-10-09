/**
 * CivicSolve AI - Problem Analysis & Duplicate Detection Simulator
 */

const CivicAI = {
  analyzeText(title, description) {
    const combined = `${title} ${description}`.toLowerCase();
    
    let detectedCategory = "Road";
    let keywords = ["civic infrastructure"];
    let severity = "Medium";
    let baseScore = 65;

    if (combined.includes("pothole") || combined.includes("road") || combined.includes("asphalt") || combined.includes("bridge") || combined.includes("underpass")) {
      detectedCategory = "Road";
      keywords = ["pothole", "tar damage", "vehicle risk", "arterial road"];
      baseScore = 80;
    } else if (combined.includes("water") || combined.includes("pipe") || combined.includes("contamination") || combined.includes("leak") || combined.includes("sewage")) {
      detectedCategory = "Water";
      keywords = ["water supply", "contamination", "pipeline breach", "sanitation"];
      baseScore = 88;
    } else if (combined.includes("garbage") || combined.includes("waste") || combined.includes("dump") || combined.includes("smell") || combined.includes("trash")) {
      detectedCategory = "Waste";
      keywords = ["solid waste", "illegal dump", "health risk", "cleansing"];
      baseScore = 75;
    } else if (combined.includes("wire") || combined.includes("electric") || combined.includes("cable") || combined.includes("shock") || combined.includes("transformer")) {
      detectedCategory = "Electricity";
      keywords = ["high tension", "power cable", "electrocution risk", "grid"];
      baseScore = 95;
    } else if (combined.includes("traffic") || combined.includes("signal") || combined.includes("crossing") || combined.includes("bus")) {
      detectedCategory = "Transport";
      keywords = ["traffic signal", "junction delay", "commuter bottleneck"];
      baseScore = 72;
    } else if (combined.includes("hospital") || combined.includes("health") || combined.includes("clinic") || combined.includes("medicine")) {
      detectedCategory = "Healthcare";
      keywords = ["health clinic", "public welfare", "medical supply"];
      baseScore = 85;
    } else if (combined.includes("school") || combined.includes("student") || combined.includes("classroom") || combined.includes("education")) {
      detectedCategory = "Education";
      keywords = ["primary education", "school building", "child welfare"];
      baseScore = 82;
    }

    // Determine severity
    if (combined.includes("danger") || combined.includes("death") || combined.includes("accident") || combined.includes("poison") || combined.includes("spark") || combined.includes("burst")) {
      severity = "Critical";
      baseScore = Math.min(99, baseScore + 12);
    } else if (combined.includes("severe") || combined.includes("foul") || combined.includes("deep") || combined.includes("broken")) {
      severity = "High";
      baseScore = Math.min(92, baseScore + 6);
    }

    return {
      category: detectedCategory,
      keywords: keywords,
      severity: severity,
      priorityScore: baseScore,
      estimatedImpact: Math.floor(Math.random() * 4000) + 500,
      recommendedAuthority: this.getAuthorityForCategory(detectedCategory),
      suggestedAction: `Deploy inspection crew and notify ${detectedCategory} zonal squad immediately.`
    };
  },

  getAuthorityForCategory(cat) {
    const map = {
      "Road": { id: "AUTH-PWD-01", name: "Public Works Department (PWD)", dept: "Roads Division" },
      "Water": { id: "AUTH-WATER-02", name: "Water Supply & Sewerage Board (BWSSB)", dept: "Hydraulic Wing" },
      "Waste": { id: "AUTH-BBMP-03", name: "Municipal Corporation", dept: "Solid Waste Management" },
      "Electricity": { id: "AUTH-BESCOM-04", name: "Electricity Supply Corporation (BESCOM)", dept: "Distribution Grid" },
      "Transport": { id: "AUTH-TRAFFIC-05", name: "City Traffic Police & Transport", dept: "Traffic Engineering" },
      "Healthcare": { id: "AUTH-HEALTH-06", name: "Health & Family Welfare Dept", dept: "Public Health" },
      "Education": { id: "AUTH-EDU-07", name: "School Education Department", dept: "Infrastructure Wing" },
      "Environment": { id: "AUTH-PCB-08", name: "State Pollution Control Board", dept: "Environmental Monitoring" }
    };
    return map[cat] || map["Road"];
  },

  checkDuplicates(title, lat, lng) {
    const existing = window.CivicDB ? window.CivicDB.getProblems() : [];
    const results = [];
    
    existing.forEach(p => {
      // Simple string match or mock proximity
      if (p.title.toLowerCase().includes(title.toLowerCase().split(" ")[0])) {
        results.push({
          id: p.id,
          title: p.title,
          similarity: Math.floor(Math.random() * 20) + 75,
          distance: (Math.random() * 1.5 + 0.2).toFixed(1) + " km",
          status: p.status
        });
      }
    });

    return results.slice(0, 2);
  }
};

window.CivicAI = CivicAI;
