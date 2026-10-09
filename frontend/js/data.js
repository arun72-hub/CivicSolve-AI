/**
 * CivicSolve AI - Central Mock Database & LocalStorage Engine
 */

const INITIAL_PROBLEMS = [
  {
    id: "CS-2026-0001",
    title: "Hazardous Deep Potholes on MG Road Junction",
    description: "Multiple severe potholes causing severe traffic disruption and two accidents during monsoon rains near the Metro station entrance.",
    category: "Road",
    subcategory: "Pothole & Asphalt Damage",
    severity: "High",
    priorityScore: 92,
    status: "In Progress",
    affectedCount: 1400,
    location: {
      latitude: 12.9716,
      longitude: 77.5946,
      address: "MG Road Metro Station Pillar 42, Central Ward",
      district: "Central District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-PWD-01",
    authorityName: "Public Works Department (PWD)",
    assignedOfficer: "Er. Rajesh Verma (Executive Engineer)",
    createdAt: "2026-09-24T10:30:00Z",
    slaHoursRemaining: 18,
    upvotes: 184,
    images: ["https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-24 10:30", actor: "Citizen", action: "Problem Reported", note: "Submitted via mobile portal with live GPS coordinates." },
      { date: "2026-09-24 10:32", actor: "Civic AI Core", action: "AI Classification", note: "Category verified: Road. Priority: 92/100. High severity." },
      { date: "2026-09-24 14:15", actor: "Admin Desk", action: "Admin Verified", note: "Valid community complaint, routed to Roads Division." },
      { date: "2026-09-25 09:00", actor: "PWD Dept", action: "Officer Assigned", note: "Assigned to Er. Rajesh Verma for immediate asphalt filling." },
      { date: "2026-09-26 11:30", actor: "Roads Contractor", action: "Work In Progress", note: "Road leveling machinery mobilized on site." }
    ],
    comments: [
      { user: "Priya S.", text: "Two-wheelers were skidding badly here yesterday. Great to see work started!", date: "2 days ago" },
      { user: "Amit Kumar", text: "Please also check drainage next to pillar 42 to prevent waterlogging.", date: "1 day ago" }
    ],
    solutionTeam: {
      teamName: "EcoPave Innovators",
      university: "National Institute of Technology",
      prototype: "Recycled Plastic Asphalt Composite"
    }
  },
  {
    id: "CS-2026-0002",
    title: "Contaminated Turbid Drinking Water Supply",
    description: "Tap water in Shastri Nagar sector 4 has been coming brown and foul smelling for the past 3 days. Risk of gastro infections.",
    category: "Water",
    subcategory: "Drinking Water Quality",
    severity: "Critical",
    priorityScore: 98,
    status: "Escalated",
    affectedCount: 3200,
    location: {
      latitude: 12.9815,
      longitude: 77.5821,
      address: "Sector 4, Shastri Nagar, West Zone",
      district: "West District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-WATER-02",
    authorityName: "Water Supply & Sewerage Board (BWSSB)",
    assignedOfficer: "Smt. Kavita Rao (Chief Sanitation Officer)",
    createdAt: "2026-09-21T08:15:00Z",
    slaHoursRemaining: -12,
    upvotes: 342,
    images: ["https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-21 08:15", actor: "Citizen", action: "Problem Reported", note: "Urgent health hazard reported." },
      { date: "2026-09-21 08:20", actor: "Civic AI Core", action: "AI Prioritization", note: "Classified as CRITICAL health risk (Priority 98)." },
      { date: "2026-09-21 09:30", actor: "Admin Desk", action: "Urgent Routing", note: "Forwarded directly to Chief Water Quality Engineer." },
      { date: "2026-09-24 18:00", actor: "System Watchdog", action: "SLA Breached", note: "Escalated to Tier-2 District Magistrate Review." }
    ],
    comments: [
      { user: "Dr. N. Hegde", text: "Several clinic patients reported stomach infections today. Needs immediate pipe flush!", date: "3 days ago" }
    ]
  },
  {
    id: "CS-2026-0003",
    title: "Overflowing Garbage Dump & Toxic Burning",
    description: "Illegal community dumping site near Government Primary School. Stagnant solid waste has not been collected for a week.",
    category: "Waste",
    subcategory: "Solid Waste & Illegal Dumping",
    severity: "High",
    priorityScore: 84,
    status: "Assigned",
    affectedCount: 850,
    location: {
      latitude: 12.9558,
      longitude: 77.5612,
      address: "Cross Road 8, Near Govt Model School, South Ward",
      district: "South District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-BBMP-03",
    authorityName: "City Municipal Corporation (Solid Waste Dept)",
    assignedOfficer: "Shri M. Ramesh (Zonal Health Inspector)",
    createdAt: "2026-09-27T11:45:00Z",
    slaHoursRemaining: 34,
    upvotes: 95,
    images: ["https://images.unsplash.com/photo-1530587191325-3db32d826c18?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-27 11:45", actor: "Citizen", action: "Problem Reported", note: "Health hazard to school students." },
      { date: "2026-09-27 11:48", actor: "Civic AI Core", action: "AI Routing", note: "Routed to Municipal Waste Management." },
      { date: "2026-09-27 15:00", actor: "Municipal Desk", action: "Accepted", note: "Truck scheduled for morning clearance." }
    ],
    comments: []
  },
  {
    id: "CS-2026-0004",
    title: "Dangling High Voltage Cable Near Playground",
    description: "Storm caused tree branch to snap 11kV distribution line. The live insulated wire is hanging at shoulder level.",
    category: "Electricity",
    subcategory: "Power Grid & Hazardous Lines",
    severity: "Critical",
    priorityScore: 99,
    status: "Verified",
    affectedCount: 500,
    location: {
      latitude: 12.9344,
      longitude: 77.6101,
      address: "Koramangala 4th Block Children Park boundary",
      district: "South-East District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-BESCOM-04",
    authorityName: "Electricity Supply Company (BESCOM)",
    assignedOfficer: "Pending Assignment",
    createdAt: "2026-09-29T14:10:00Z",
    slaHoursRemaining: 4,
    upvotes: 412,
    images: ["https://images.unsplash.com/photo-1509390144018-eeaf65052242?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-29 14:10", actor: "Citizen", action: "Problem Reported", note: "Direct emergency report." },
      { date: "2026-09-29 14:12", actor: "Civic AI Core", action: "Critical Alert", note: "Dispatched immediate automated SMS alert to substation." }
    ],
    comments: [
      { user: "Sunil D.", text: "Substation confirmed power trip to this branch line already!", date: "2 hours ago" }
    ]
  },
  {
    id: "CS-2026-0005",
    title: "Non-functional Traffic Signal at Busy 4-Way Cross",
    description: "Traffic lights stuck on blinking yellow for 5 days. Heavy gridlock and near-misses during peak morning hours.",
    category: "Transport",
    subcategory: "Traffic Lights & Junction Safety",
    severity: "Medium",
    priorityScore: 76,
    status: "Pilot Testing",
    affectedCount: 6500,
    location: {
      latitude: 12.9611,
      longitude: 77.6362,
      address: "Indiranagar 100ft Road & 12th Main Crossing",
      district: "East District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-TRAFFIC-05",
    authorityName: "City Traffic Police & Transport Dept",
    assignedOfficer: "Insp. S. Jagadeesh (Traffic Ward)",
    createdAt: "2026-09-22T09:20:00Z",
    slaHoursRemaining: 48,
    upvotes: 215,
    images: ["https://images.unsplash.com/photo-1506521781263-d8422e82f27a?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-22 09:20", actor: "Citizen", action: "Reported", note: "Congestion hotspot." },
      { date: "2026-09-23 11:00", actor: "University Partner", action: "Solution Proposed", note: "RV College IoT Team submitted AI Adaptive Traffic Timing Controller." },
      { date: "2026-09-26 10:00", actor: "Traffic Police", action: "Pilot Approved", note: "Smart sensor kit installed on pilot testing trial." }
    ],
    comments: [],
    solutionTeam: {
      teamName: "SmartFlow AI Team",
      university: "RV College of Engineering",
      prototype: "Computer-Vision Dynamic Signal Timing Microcontroller"
    }
  },
  {
    id: "CS-2026-0006",
    title: "Primary Health Center Lacks Cold Chain & Vaccines",
    description: "Solar refrigerator battery broken at Community Health Center. Children vaccination drives stalled.",
    category: "Healthcare",
    subcategory: "Public Health Infrastructure",
    severity: "High",
    priorityScore: 88,
    status: "Resolved",
    affectedCount: 2100,
    location: {
      latitude: 13.0358,
      longitude: 77.5970,
      address: "Hebbal Rural Primary Health Center, Ward 7",
      district: "North District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-HEALTH-06",
    authorityName: "Department of Health & Family Welfare",
    assignedOfficer: "Dr. Ananya Sen",
    createdAt: "2026-09-15T10:00:00Z",
    slaHoursRemaining: 0,
    upvotes: 167,
    images: ["https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-15 10:00", actor: "Citizen", action: "Reported", note: "Immunization clinic impact." },
      { date: "2026-09-17 14:00", actor: "Industry Sponsor", action: "CSR Grant", note: "Tata Power Renewables sponsored solar inverter replacement." },
      { date: "2026-09-20 16:30", actor: "Health Officer", action: "Resolved", note: "Refrigeration restored and temperature monitoring verified." },
      { date: "2026-09-22 11:00", actor: "Citizen Feedback", action: "Verified by Citizens", note: "5/5 Star rating confirmed by 42 neighborhood parents." }
    ],
    comments: []
  },
  {
    id: "CS-2026-0007",
    title: "Broken Roof & No Toilets in Govt Girls Primary School",
    description: "Rainwater leakage inside grade 3 & 4 classrooms. Sanitation block non-functional causing high girl student absenteeism.",
    category: "Education",
    subcategory: "School Infrastructure & Sanitation",
    severity: "High",
    priorityScore: 89,
    status: "In Progress",
    affectedCount: 380,
    location: {
      latitude: 12.9122,
      longitude: 77.6445,
      address: "Govt Girls Primary School, HSR Layout Sector 2",
      district: "South District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-EDU-07",
    authorityName: "Department of School Education & Literacy",
    assignedOfficer: "Shri K. Natarajan (Block Education Officer)",
    createdAt: "2026-09-23T11:00:00Z",
    slaHoursRemaining: 72,
    upvotes: 278,
    images: ["https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-23 11:00", actor: "Citizen", action: "Reported", note: "Urgent student welfare." },
      { date: "2026-09-25 15:00", actor: "Authority", action: "Tender Issued", note: "Waterproofing and eco-sanitation repair contract allocated." }
    ],
    comments: []
  },
  {
    id: "CS-2026-0008",
    title: "Industrial Effluent Foaming in Varthur Lake Canal",
    description: "Heavy white chemical foam billowing from storm drain into lake. Pungent odor affecting neighboring residential apartments.",
    category: "Environment",
    subcategory: "Water Pollution & Lake Preservation",
    severity: "Critical",
    priorityScore: 95,
    status: "Under Review",
    affectedCount: 8000,
    location: {
      latitude: 12.9563,
      longitude: 77.7410,
      address: "Varthur Lake South Inflow Channel, Whitefield",
      district: "East District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-PCB-08",
    authorityName: "State Pollution Control Board (KSPCB)",
    assignedOfficer: "Dr. B. Manjunath (Senior Environmental Officer)",
    createdAt: "2026-09-29T16:40:00Z",
    slaHoursRemaining: 24,
    upvotes: 512,
    images: ["https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-29 16:40", actor: "Citizen", action: "Reported", note: "Video evidence of toxic discharge uploaded." },
      { date: "2026-09-29 16:42", actor: "Civic AI Core", action: "AI Water Index", note: "High toxicity correlation detected from visual evidence." }
    ],
    comments: []
  },
  {
    id: "CS-2026-0009",
    title: "Dark Stretches - 14 Consecutive Streetlights Dead",
    description: "Entire 1.2km stretch of Ring Road bypass is completely pitch black at night. Multiple safety concerns for women commuters.",
    category: "Public Safety",
    subcategory: "Street Lighting & Night Safety",
    severity: "Medium",
    priorityScore: 79,
    status: "Assigned",
    affectedCount: 4500,
    location: {
      latitude: 12.9288,
      longitude: 77.6833,
      address: "Sarjapur Outer Ring Road Service Lane",
      district: "East District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-BBMP-03",
    authorityName: "City Municipal Corporation (Electrical Wing)",
    assignedOfficer: "Er. George Thomas",
    createdAt: "2026-09-26T19:30:00Z",
    slaHoursRemaining: 30,
    upvotes: 189,
    images: ["https://images.unsplash.com/photo-1509114397022-ed747cca3f65?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-26 19:30", actor: "Citizen", action: "Reported", note: "Women safety hazard." }
    ],
    comments: []
  },
  {
    id: "CS-2026-0010",
    title: "Flooding on Underpass After Moderate Rains",
    description: "Kengeri Railway underpass submerged under 3 feet of water. Vehicles stranded and public transit buses halted.",
    category: "Road",
    subcategory: "Stormwater Drainage & Flooding",
    severity: "High",
    priorityScore: 86,
    status: "Assigned",
    affectedCount: 5200,
    location: {
      latitude: 12.9177,
      longitude: 77.4839,
      address: "Kengeri Satellite Town Railway Underpass",
      district: "West District",
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-PWD-01",
    authorityName: "Public Works Department (PWD)",
    assignedOfficer: "Er. Sanjeev Hegde",
    createdAt: "2026-09-28T07:15:00Z",
    slaHoursRemaining: 40,
    upvotes: 143,
    images: ["https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?w=600&auto=format&fit=crop"],
    timeline: [],
    comments: []
  }
];

// Add 10 more mock problems for a total of 20 realistic problems
const ADDITIONAL_PROBLEMS = [
  {
    id: "CS-2026-0011",
    title: "Open Drainage Sump on Pedestrian Footpath",
    description: "Concrete slab missing over 8-foot deep stormwater drain right in front of vegetable market.",
    category: "Public Safety",
    severity: "Critical",
    priorityScore: 94,
    status: "Verified",
    affectedCount: 2500,
    district: "Central District",
    authorityName: "Municipal Corporation",
    upvotes: 231
  },
  {
    id: "CS-2026-0012",
    title: "Burst Main Water Pipeline Spilling Millions of Liters",
    description: "High pressure pipeline ruptured on Airport Road. Drinking water gushing into vacant lots while residents have zero supply.",
    category: "Water",
    severity: "High",
    priorityScore: 91,
    status: "In Progress",
    affectedCount: 7800,
    district: "North District",
    authorityName: "Water Supply Board",
    upvotes: 310
  },
  {
    id: "CS-2026-0013",
    title: "Frequent Low Voltage Trips Damaging Home Appliances",
    description: "Voltage fluctuates between 140V to 270V in residential layout. Refrigerator compressors burnt.",
    category: "Electricity",
    severity: "Medium",
    priorityScore: 71,
    status: "Assigned",
    affectedCount: 420,
    district: "West District",
    authorityName: "Electricity Distribution Corp",
    upvotes: 68
  },
  {
    id: "CS-2026-0014",
    title: "Unsegregated Medical Waste Dumped Behind Clinic",
    description: "Used syringes, blood bags and biohazard waste left in unsealed open plastic sacks next to public park.",
    category: "Healthcare",
    severity: "Critical",
    priorityScore: 97,
    status: "Escalated",
    affectedCount: 1600,
    district: "South District",
    authorityName: "Health & Pollution Control",
    upvotes: 420
  },
  {
    id: "CS-2026-0015",
    title: "Defaced Pedestrian Crossing Lines at Blind Corner",
    description: "Zebra crossing completely faded at school zone curve. Vehicles refusing to yield to crossing children.",
    category: "Transport",
    severity: "Medium",
    priorityScore: 74,
    status: "Resolved",
    affectedCount: 900,
    district: "East District",
    authorityName: "Traffic Police",
    upvotes: 112
  },
  {
    id: "CS-2026-0016",
    title: "Tree Canopy Touching Overhead 440V Power Lines",
    description: "Large banyan branches entangling overhead cables, sparking during windy evenings.",
    category: "Electricity",
    severity: "High",
    priorityScore: 85,
    status: "In Progress",
    affectedCount: 650,
    district: "Central District",
    authorityName: "Electricity & Forest Dept",
    upvotes: 94
  },
  {
    id: "CS-2026-0017",
    title: "Clogged Sewer Overflowing onto Commercial Street",
    description: "Manhole backflow covering market road with sewage effluent. Customers unable to access storefronts.",
    category: "Waste",
    severity: "High",
    priorityScore: 88,
    status: "Assigned",
    affectedCount: 1900,
    district: "Central District",
    authorityName: "Water & Sewerage Board",
    upvotes: 178
  },
  {
    id: "CS-2026-0018",
    title: "Air Pollution from Unregulated Construction Dust",
    description: "10-acre commercial project grinding concrete without water sprinklers or green nets. PM2.5 levels through the roof.",
    category: "Environment",
    severity: "Medium",
    priorityScore: 77,
    status: "Under Review",
    affectedCount: 3500,
    district: "East District",
    authorityName: "Pollution Control Board",
    upvotes: 210
  },
  {
    id: "CS-2026-0019",
    title: "Cracked Ceiling in Community Library Building",
    description: "Plaster falling in reading hall. Structural audit required before public usage can safely resume.",
    category: "Education",
    severity: "Medium",
    priorityScore: 68,
    status: "Pilot Testing",
    affectedCount: 450,
    district: "North District",
    authorityName: "Public Libraries Dept",
    upvotes: 54
  },
  {
    id: "CS-2026-0020",
    title: "Absence of Speed Breaker on Dangerous School Road",
    description: "Speeding tipper trucks using narrow residential lane as shortcut. Urgent speed calming required.",
    category: "Road",
    severity: "High",
    priorityScore: 86,
    status: "Resolved",
    affectedCount: 1200,
    district: "South District",
    authorityName: "Traffic Police & PWD",
    upvotes: 315
  }
];

// Combine into standard 20 problems
const FULL_MOCK_PROBLEMS = [...INITIAL_PROBLEMS];
ADDITIONAL_PROBLEMS.forEach((p, idx) => {
  FULL_MOCK_PROBLEMS.push({
    ...p,
    subcategory: p.category + " Issue",
    location: {
      latitude: 12.95 + (idx * 0.01),
      longitude: 77.58 + (idx * 0.01),
      address: `Ward ${idx + 10}, ${p.district}`,
      district: p.district,
      city: "Bangalore",
      state: "Karnataka"
    },
    authorityId: "AUTH-DEPT-0" + (idx % 5 + 1),
    assignedOfficer: "Officer " + (idx + 1),
    createdAt: new Date(Date.now() - (idx + 1) * 86400000).toISOString(),
    slaHoursRemaining: 24 + idx * 6,
    images: ["https://images.unsplash.com/photo-1541888946425-d0fbb186c5f7?w=600&auto=format&fit=crop"],
    timeline: [
      { date: "2026-09-25 10:00", actor: "Citizen", action: "Reported", note: "Standard intake" }
    ],
    comments: []
  });
});

const AUTHORITIES = [
  { id: "AUTH-PWD-01", name: "Public Works Department (PWD)", department: "Roads & Bridges", jurisdiction: "Statewide Urban", officerCount: 42, activeLoad: 128 },
  { id: "AUTH-WATER-02", name: "Water Supply & Sewerage Board (BWSSB)", department: "Hydraulic Engineering", jurisdiction: "Metropolitan Area", officerCount: 38, activeLoad: 94 },
  { id: "AUTH-BBMP-03", name: "City Municipal Corporation (BBMP)", department: "Solid Waste & Health", jurisdiction: "Municipal Wards 1-198", officerCount: 120, activeLoad: 310 },
  { id: "AUTH-BESCOM-04", name: "Electricity Supply Company (BESCOM)", department: "Power Transmission & Grid", jurisdiction: "City Zones", officerCount: 65, activeLoad: 145 },
  { id: "AUTH-TRAFFIC-05", name: "City Traffic Police & Transport", department: "Traffic Engineering", jurisdiction: "Urban Arterial Roads", officerCount: 50, activeLoad: 82 },
  { id: "AUTH-HEALTH-06", name: "Department of Health & Family Welfare", department: "Public Clinics & Sanitation", jurisdiction: "District Health", officerCount: 28, activeLoad: 49 },
  { id: "AUTH-EDU-07", name: "Department of School Education", department: "Government School Infrastructure", jurisdiction: "Educational District", officerCount: 19, activeLoad: 33 },
  { id: "AUTH-PCB-08", name: "State Pollution Control Board (KSPCB)", department: "Environmental Protection", jurisdiction: "Statewide Industries", officerCount: 31, activeLoad: 67 }
];

const NOTIFICATIONS = [
  { id: "NOTIF-1", title: "Problem Verified by Admin", message: "Your reported Pothole complaint (CS-2026-0001) has been verified and assigned to PWD.", date: "10 mins ago", type: "success", read: false },
  { id: "NOTIF-2", title: "SLA Warning Alert", message: "Water Contamination (CS-2026-0002) has 4 hours remaining before Tier-2 escalation.", date: "1 hour ago", type: "warning", read: false },
  { id: "NOTIF-3", title: "Student Team Proposed Solution", message: "RV College of Engineering submitted a smart traffic prototype for Indiranagar Junction.", date: "4 hours ago", type: "info", read: true },
  { id: "NOTIF-4", title: "Resolution Verified by 40+ Citizens", message: "Primary Health Center refrigeration issue marked fully resolved with 5-star rating.", date: "1 day ago", type: "success", read: true }
];

const AUDIT_LOGS = [
  { timestamp: "2026-09-30 20:15:22", user: "Admin (admin@civicsolve.ai)", action: "VERIFY_PROBLEM", entity: "CS-2026-0004", status: "SUCCESS" },
  { timestamp: "2026-09-30 19:40:11", user: "Er. Rajesh Verma", action: "ASSIGN_CONTRACTOR", entity: "CS-2026-0001", status: "SUCCESS" },
  { timestamp: "2026-09-30 18:22:05", user: "System Watchdog", action: "AUTO_ESCALATION", entity: "CS-2026-0002", status: "TRIGGERED" },
  { timestamp: "2026-09-30 16:10:48", user: "Citizen (priya@domain.com)", action: "SUBMIT_PROBLEM", entity: "CS-2026-0020", status: "CREATED" },
  { timestamp: "2026-09-30 14:05:00", user: "System AI Engine", action: "DUPLICATE_CHECK", entity: "CS-2026-0020", status: "CLEARED" }
];

// Initialize LocalStorage Data Store
class CivicDatabase {
  constructor() {
    this.initStorage();
  }

  initStorage() {
    if (!localStorage.getItem("civic_problems")) {
      localStorage.setItem("civic_problems", JSON.stringify(FULL_MOCK_PROBLEMS));
    }
    if (!localStorage.getItem("civic_authorities")) {
      localStorage.setItem("civic_authorities", JSON.stringify(AUTHORITIES));
    }
    if (!localStorage.getItem("civic_notifications")) {
      localStorage.setItem("civic_notifications", JSON.stringify(NOTIFICATIONS));
    }
    if (!localStorage.getItem("civic_audit_logs")) {
      localStorage.setItem("civic_audit_logs", JSON.stringify(AUDIT_LOGS));
    }
  }

  getProblems() {
    return JSON.parse(localStorage.getItem("civic_problems") || "[]");
  }

  getProblemById(id) {
    const list = this.getProblems();
    return list.find(p => p.id === id) || null;
  }

  saveProblem(problem) {
    const list = this.getProblems();
    const index = list.findIndex(p => p.id === problem.id);
    if (index >= 0) {
      list[index] = problem;
    } else {
      list.unshift(problem);
    }
    localStorage.setItem("civic_problems", JSON.stringify(list));
    return problem;
  }

  getAuthorities() {
    return JSON.parse(localStorage.getItem("civic_authorities") || "[]");
  }

  getNotifications() {
    return JSON.parse(localStorage.getItem("civic_notifications") || "[]");
  }

  getAuditLogs() {
    return JSON.parse(localStorage.getItem("civic_audit_logs") || "[]");
  }

  addAuditLog(user, action, entity, status = "SUCCESS") {
    const logs = this.getAuditLogs();
    logs.unshift({
      timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
      user,
      action,
      entity,
      status
    });
    localStorage.setItem("civic_audit_logs", JSON.stringify(logs.slice(0, 50)));
  }
}

window.CivicDB = new CivicDatabase();
