import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JS_DIR = os.path.join(BASE_DIR, "frontend", "js")
os.makedirs(JS_DIR, exist_ok=True)

# 1. data.js
data_js = """/**
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
"""

# 2. utils.js
utils_js = """/**
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
"""

# 3. auth.js
auth_js = """/**
 * CivicSolve AI - Authentication & Role Manager
 */

const CivicAuth = {
  getRole() {
    return localStorage.getItem("civic_role") || "citizen";
  },

  getUser() {
    const defaultUsers = {
      citizen: { name: "Ananya Sharma", role: "Citizen Reporter", email: "ananya.sharma@example.com", avatar: "AS", org: "Indiranagar Resident" },
      authority: { name: "Er. Rajesh Verma", role: "Executive Engineer", email: "rajesh.verma@pwd.gov.in", avatar: "RV", org: "Public Works Department" },
      government: { name: "Dr. K. Srinivas IAS", role: "District Magistrate & Commissioner", email: "commissioner@gov.in", avatar: "KS", org: "Central Secretariat" },
      admin: { name: "Devendra Patel", role: "System Administrator", email: "admin@civicsolve.ai", avatar: "DP", org: "CivicSolve AI Platform" },
      university: { name: "Prof. Sudhir Rao", role: "Innovation Dean", email: "dean.research@nitk.edu", avatar: "SR", org: "National Institute of Technology" },
      faculty: { name: "Dr. Meera Nambiar", role: "Faculty Mentor (Civil/AI)", email: "meera.n@rvce.edu.in", avatar: "MN", org: "RV College of Engineering" },
      student: { name: "Rohan Varma", role: "Student Team Lead", email: "rohan.v@students.rvce.edu", avatar: "RV", org: "EcoPave Student Innovators" },
      industry: { name: "Vikram Malhotra", role: "CSR Innovation Director", email: "v.malhotra@tatatech.com", avatar: "VM", org: "Tata Technologies Sustainability" }
    };
    const role = this.getRole();
    return defaultUsers[role] || defaultUsers.citizen;
  },

  setRole(role) {
    localStorage.setItem("civic_role", role);
  },

  loginAs(role) {
    this.setRole(role);
    const routes = {
      citizen: "citizen-dashboard.html",
      authority: "authority-dashboard.html",
      government: "government-dashboard.html",
      admin: "admin-dashboard.html",
      university: "university-dashboard.html",
      faculty: "faculty-dashboard.html",
      student: "student-team-dashboard.html",
      industry: "industry-dashboard.html"
    };
    window.location.href = routes[role] || "citizen-dashboard.html";
  },

  logout() {
    this.setRole("citizen");
    window.location.href = "login.html";
  }
};

window.CivicAuth = CivicAuth;
"""

# 4. app.js
app_js = """/**
 * CivicSolve AI - Global UI Controller & Shell Handlers
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. Theme Initializer
  const savedTheme = localStorage.getItem("civic_theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  // 2. Global Dark Mode Toggle Button Bindings
  document.querySelectorAll(".theme-toggle-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("civic_theme", next);
      updateThemeIcons(next);
      if (window.CivicUtils) {
        CivicUtils.showToast(`Switched to ${next} theme mode.`, "info", 2000);
      }
    });
  });

  function updateThemeIcons(theme) {
    document.querySelectorAll(".theme-toggle-btn i").forEach(icon => {
      if (theme === "dark") {
        icon.className = "fa-solid fa-sun";
      } else {
        icon.className = "fa-solid fa-moon";
      }
    });
  }
  updateThemeIcons(savedTheme);

  // 3. Populate current user mini profile in sidebar if available
  const user = window.CivicAuth ? CivicAuth.getUser() : null;
  if (user) {
    const avatarEl = document.querySelector(".user-mini-avatar");
    const nameEl = document.querySelector(".user-mini-name");
    const roleEl = document.querySelector(".user-mini-role");
    if (avatarEl) avatarEl.textContent = user.avatar;
    if (nameEl) nameEl.textContent = user.name;
    if (roleEl) roleEl.textContent = user.role;
  }

  // 4. Mobile Sidebar Hamburger Handler
  const menuBtn = document.getElementById("mobileMenuToggle");
  const sidebar = document.querySelector(".app-sidebar");
  if (menuBtn && sidebar) {
    menuBtn.addEventListener("click", () => {
      sidebar.classList.toggle("show");
    });
  }

  // 5. Global Search Bar instant filter
  const searchInput = document.querySelector(".topbar-search input");
  if (searchInput) {
    searchInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter" && searchInput.value.trim()) {
        window.location.href = `my-problems.html?search=${encodeURIComponent(searchInput.value.trim())}`;
      }
    });
  }

  // 6. Highlight active sidebar link
  const currentPath = window.location.pathname.split("/").pop();
  document.querySelectorAll(".sidebar-link").forEach(link => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    }
  });

  // 7. Demo mode quick switcher button in navbar if element exists
  const demoSwitcher = document.getElementById("demoRoleSelector");
  if (demoSwitcher) {
    demoSwitcher.value = CivicAuth.getRole();
    demoSwitcher.addEventListener("change", (e) => {
      CivicAuth.loginAs(e.target.value);
    });
  }
});
"""

# 5. ai-analysis.js
ai_analysis_js = """/**
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
"""

# 6. problems.js
problems_js = """/**
 * CivicSolve AI - Problem Submission, Camera, Geolocation & List Management
 */

let cameraStream = null;

const ProblemManager = {
  // Step navigation in submit-problem.html
  goToStep(stepNumber) {
    document.querySelectorAll(".form-step").forEach(el => el.style.display = "none");
    const active = document.getElementById(`step${stepNumber}`);
    if (active) active.style.display = "block";

    // Update wizard indicators
    document.querySelectorAll(".step-indicator-item").forEach((el, idx) => {
      if (idx + 1 === stepNumber) {
        el.classList.add("active");
        el.classList.remove("completed");
      } else if (idx + 1 < stepNumber) {
        el.classList.add("completed");
        el.classList.remove("active");
      } else {
        el.classList.remove("active", "completed");
      }
    });

    // Step specific actions
    if (stepNumber === 4) {
      this.runAISimulation();
    }
  },

  // Live Geolocation
  detectLocation() {
    const statusText = document.getElementById("geoStatus");
    if (statusText) statusText.textContent = "Requesting device GPS coordinates...";

    if (!navigator.geolocation) {
      CivicUtils.showToast("Geolocation is not supported by your browser.", "error");
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const lat = pos.coords.latitude.toFixed(4);
        const lng = pos.coords.longitude.toFixed(4);
        
        document.getElementById("inputLat").value = lat;
        document.getElementById("inputLng").value = lng;
        document.getElementById("inputAddress").value = `Verified GPS Location (Lat: ${lat}, Lng: ${lng}), Central Ward`;
        
        if (statusText) {
          statusText.innerHTML = `<span class="text-success"><i class="fa-solid fa-check-circle"></i> Coordinates acquired: ${lat}, ${lng}</span>`;
        }
        CivicUtils.showToast("Precise GPS location locked successfully!", "success");
      },
      (err) => {
        if (statusText) statusText.innerHTML = `<span class="text-warning">Permission denied or unavailable. Fallback to default city center.</span>`;
        document.getElementById("inputLat").value = "12.9716";
        document.getElementById("inputLng").value = "77.5946";
        document.getElementById("inputAddress").value = "MG Road Corridor, Central Bangalore";
        CivicUtils.showToast("Location permission unavailable. Filled default ward coordinates.", "warning");
      },
      { timeout: 10000, enableHighAccuracy: true }
    );
  },

  // Camera integration (getUserMedia)
  async startCamera() {
    const video = document.getElementById("cameraVideo");
    const placeholder = document.getElementById("cameraPlaceholder");
    const liveContainer = document.getElementById("cameraLiveBox");

    try {
      cameraStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
      if (video) {
        video.srcObject = cameraStream;
        video.play();
        if (placeholder) placeholder.style.display = "none";
        if (liveContainer) liveContainer.style.display = "block";
      }
      CivicUtils.showToast("Camera stream started.", "info");
    } catch (err) {
      CivicUtils.showToast("Camera access denied or no camera device found. You can upload an image file instead.", "warning");
    }
  },

  capturePhoto() {
    const video = document.getElementById("cameraVideo");
    const canvas = document.getElementById("cameraCanvas");
    const photoPreview = document.getElementById("capturedPhotoPreview");

    if (!video || !canvas) return;

    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataUrl = canvas.toDataURL("image/jpeg");
    if (photoPreview) {
      photoPreview.src = dataUrl;
      photoPreview.style.display = "block";
    }
    
    // Stop camera
    this.stopCamera();
    CivicUtils.showToast("Photo captured from live camera feed!", "success");
  },

  stopCamera() {
    if (cameraStream) {
      cameraStream.getTracks().forEach(track => track.stop());
      cameraStream = null;
    }
    const liveContainer = document.getElementById("cameraLiveBox");
    if (liveContainer) liveContainer.style.display = "none";
  },

  // Run AI simulation in wizard step 4
  runAISimulation() {
    const title = document.getElementById("inputTitle") ? document.getElementById("inputTitle").value : "Civic Problem";
    const desc = document.getElementById("inputDesc") ? document.getElementById("inputDesc").value : "Description";

    const aiRes = CivicAI.analyzeText(title, desc);
    const duplicates = CivicAI.checkDuplicates(title, 12.97, 77.59);

    setTimeout(() => {
      const container = document.getElementById("aiAnalysisResults");
      if (!container) return;

      container.innerHTML = `
        <div class="ai-analysis-card">
          <div class="ai-scan-bar"></div>
          <div class="flex items-center justify-between" style="margin-bottom:1rem;">
            <div class="flex items-center gap-2">
              <span class="badge badge-primary"><i class="fa-solid fa-microchip"></i> Civic AI Engine v4.2</span>
              <span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> Analysis Complete</span>
            </div>
            <span class="ai-metric-val">${aiRes.priorityScore}/100 Priority</span>
          </div>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div class="ai-metric-box">
              <div style="font-size:0.8rem; color:var(--muted); font-weight:700;">CATEGORY DETECTED</div>
              <div style="font-weight:700; color:var(--dark); font-size:1.1rem; margin-top:0.25rem;">${aiRes.category}</div>
            </div>
            <div class="ai-metric-box">
              <div style="font-size:0.8rem; color:var(--muted); font-weight:700;">CALCULATED SEVERITY</div>
              <div style="margin-top:0.25rem;">${CivicUtils.getSeverityBadge(aiRes.severity)}</div>
            </div>
            <div class="ai-metric-box">
              <div style="font-size:0.8rem; color:var(--muted); font-weight:700;">ESTIMATED CITIZENS AFFECTED</div>
              <div style="font-weight:800; color:var(--accent); font-size:1.2rem; margin-top:0.25rem;">~${aiRes.estimatedImpact} People</div>
            </div>
          </div>

          <div style="background:var(--bg-card); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border); margin-bottom:1rem;">
            <h5 style="margin-bottom:0.5rem;"><i class="fa-solid fa-building-columns text-primary"></i> Recommended Government Authority</h5>
            <p style="font-size:0.9rem; color:var(--dark); font-weight:600;">${aiRes.recommendedAuthority.name}</p>
            <p style="font-size:0.85rem; color:var(--muted);">${aiRes.suggestedAction}</p>
          </div>

          ${duplicates.length > 0 ? `
            <div style="background:var(--warning-light); border:1px solid var(--warning); padding:1rem; border-radius:var(--radius-md);">
              <h5 style="color:var(--warning); margin-bottom:0.35rem;"><i class="fa-solid fa-clone"></i> Duplicate Detection: ${duplicates.length} Similar Reports Nearby</h5>
              <p style="font-size:0.85rem; color:var(--dark);">Similar report "${duplicates[0].title}" found (${duplicates[0].similarity}% match). You can still submit to add citizen weight or merge.</p>
            </div>
          ` : `
            <div style="background:var(--success-light); border:1px solid var(--success); padding:0.75rem 1rem; border-radius:var(--radius-md); font-size:0.85rem; color:var(--success);">
              <i class="fa-solid fa-check"></i> No direct duplicate complaints detected in this 1.5km grid.
            </div>
          `}
        </div>
      `;

      // Fill in Step 5 Review
      const revId = document.getElementById("revId");
      const revTitle = document.getElementById("revTitle");
      const revCat = document.getElementById("revCat");
      const revAuth = document.getElementById("revAuth");

      if (revId) revId.textContent = CivicUtils.generateProblemId();
      if (revTitle) revTitle.textContent = title;
      if (revCat) revCat.textContent = aiRes.category;
      if (revAuth) revAuth.textContent = aiRes.recommendedAuthority.name;
    }, 1200);
  },

  // Final Submission
  submitFinalProblem() {
    const title = document.getElementById("inputTitle") ? document.getElementById("inputTitle").value : "New Issue";
    const desc = document.getElementById("inputDesc") ? document.getElementById("inputDesc").value : "No description";
    const cat = document.getElementById("inputCategory") ? document.getElementById("inputCategory").value : "Road";
    const sev = document.getElementById("inputSeverity") ? document.getElementById("inputSeverity").value : "High";
    const lat = parseFloat(document.getElementById("inputLat").value) || 12.9716;
    const lng = parseFloat(document.getElementById("inputLng").value) || 77.5946;
    const address = document.getElementById("inputAddress").value || "City Municipal Ward";

    const aiRes = CivicAI.analyzeText(title, desc);
    const newId = CivicUtils.generateProblemId();

    const newProblem = {
      id: newId,
      title: title,
      description: desc,
      category: cat || aiRes.category,
      subcategory: cat + " Problem",
      severity: sev || aiRes.severity,
      priorityScore: aiRes.priorityScore,
      status: "Under Review",
      affectedCount: aiRes.estimatedImpact,
      location: {
        latitude: lat,
        longitude: lng,
        address: address,
        district: "Central District",
        city: "Bangalore",
        state: "Karnataka"
      },
      authorityId: aiRes.recommendedAuthority.id,
      authorityName: aiRes.recommendedAuthority.name,
      assignedOfficer: "Pending Verification",
      createdAt: new Date().toISOString(),
      slaHoursRemaining: 72,
      upvotes: 1,
      images: ["https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?w=600&auto=format&fit=crop"],
      timeline: [
        { date: new Date().toISOString().replace('T', ' ').substring(0, 16), actor: "Citizen", action: "Submitted", note: "Report created and sent to Admin Verification Queue." }
      ],
      comments: []
    };

    window.CivicDB.saveProblem(newProblem);
    window.CivicDB.addAuditLog("Citizen Reporter", "CREATE_PROBLEM", newId, "SUCCESS");

    CivicUtils.showToast("Problem submitted and routed to verification successfully!", "success");
    setTimeout(() => {
      window.location.href = `problem-details.html?id=${newId}`;
    }, 1000);
  }
};

window.ProblemManager = ProblemManager;
"""

# 7. map.js
map_js = """/**
 * CivicSolve AI - Leaflet Map Integration with Priority Markers
 */

const CivicMap = {
  mapInstance: null,

  init(elementId = "civicMap", centerLat = 12.9716, centerLng = 77.5946, zoom = 12) {
    const el = document.getElementById(elementId);
    if (!el || typeof L === 'undefined') return;

    this.mapInstance = L.map(elementId).setView([centerLat, centerLng], zoom);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors | CivicSolve AI'
    }).addTo(this.mapInstance);

    this.loadProblemMarkers();
  },

  loadProblemMarkers(filterCategory = "All", filterPriority = "All") {
    if (!this.mapInstance) return;

    const problems = window.CivicDB ? window.CivicDB.getProblems() : [];
    
    // Clear old markers if layer group exists
    if (this.markerGroup) {
      this.markerGroup.clearLayers();
    } else {
      this.markerGroup = L.layerGroup().addTo(this.mapInstance);
    }

    const priorityColors = {
      "Critical": "#EF4444",
      "High": "#F59E0B",
      "Medium": "#06B6D4",
      "Low": "#10B981"
    };

    problems.forEach(p => {
      if (filterCategory !== "All" && p.category !== filterCategory) return;
      if (filterPriority !== "All" && p.severity !== filterPriority) return;

      const lat = p.location ? p.location.latitude : 12.9716;
      const lng = p.location ? p.location.longitude : 77.5946;
      const color = priorityColors[p.severity] || "#4F46E5";

      const customIcon = L.divIcon({
        className: 'custom-map-marker',
        html: `<div style="background-color:${color}; width:24px; height:24px; border-radius:50%; border:3px solid #fff; box-shadow:0 2px 6px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; color:#fff; font-size:10px; font-weight:700;">${p.priorityScore || '!'}</div>`,
        iconSize: [24, 24],
        iconAnchor: [12, 12]
      });

      const popupContent = `
        <div style="min-width:200px; font-family:'Inter',sans-serif;">
          <div style="font-size:0.75rem; font-weight:700; color:#64748B;">${p.id} • ${p.category}</div>
          <h4 style="font-size:0.95rem; font-weight:700; margin:4px 0; color:#0F172A;">${p.title}</h4>
          <p style="font-size:0.8rem; color:#64748B; margin-bottom:8px;">${p.location ? p.location.address : ''}</p>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:0.75rem; font-weight:700; color:${color};">${p.severity} Priority</span>
            <a href="problem-details.html?id=${p.id}" style="font-size:0.8rem; font-weight:600; color:#4F46E5; text-decoration:underline;">View Details →</a>
          </div>
        </div>
      `;

      L.marker([lat, lng], { icon: customIcon })
        .bindPopup(popupContent)
        .addTo(this.markerGroup);
    });
  }
};

window.CivicMap = CivicMap;
"""

# 8. analytics.js
analytics_js = """/**
 * CivicSolve AI - Chart.js Dashboards & Visualizations
 */

const CivicAnalytics = {
  initCharts() {
    if (typeof Chart === 'undefined') return;

    // 1. Category Doughnut Chart
    const catCanvas = document.getElementById("chartCategory");
    if (catCanvas) {
      new Chart(catCanvas, {
        type: 'doughnut',
        data: {
          labels: ['Roads', 'Water', 'Waste', 'Electricity', 'Transport', 'Healthcare', 'Education'],
          datasets: [{
            data: [35, 22, 18, 12, 8, 4, 3],
            backgroundColor: ['#4F46E5', '#06B6D4', '#10B981', '#F59E0B', '#7C3AED', '#EF4444', '#64748B']
          }]
        },
        options: {
          responsive: true,
          plugins: { legend: { position: 'bottom' } }
        }
      });
    }

    // 2. Monthly Trend Line Chart
    const trendCanvas = document.getElementById("chartTrends");
    if (trendCanvas) {
      new Chart(trendCanvas, {
        type: 'line',
        data: {
          labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
          datasets: [
            {
              label: 'Reported',
              data: [820, 1140, 1420, 1680, 2100, 2480],
              borderColor: '#4F46E5',
              backgroundColor: 'rgba(79, 70, 229, 0.1)',
              fill: true,
              tension: 0.3
            },
            {
              label: 'Resolved',
              data: [610, 890, 1200, 1510, 1920, 2240],
              borderColor: '#10B981',
              backgroundColor: 'rgba(16, 185, 129, 0.1)',
              fill: true,
              tension: 0.3
            }
          ]
        },
        options: {
          responsive: true,
          plugins: { legend: { position: 'top' } }
        }
      });
    }

    // 3. District Comparison Horizontal Bar
    const distCanvas = document.getElementById("chartDistricts");
    if (distCanvas) {
      new Chart(distCanvas, {
        type: 'bar',
        data: {
          labels: ['Central', 'East', 'South', 'West', 'North', 'South-East'],
          datasets: [{
            label: 'Active Problems',
            data: [142, 185, 120, 95, 84, 110],
            backgroundColor: '#06B6D4'
          }]
        },
        options: {
          indexAxis: 'y',
          responsive: true,
          plugins: { legend: { display: false } }
        }
      });
    }

    // 4. Severity Distribution Bar
    const sevCanvas = document.getElementById("chartSeverity");
    if (sevCanvas) {
      new Chart(sevCanvas, {
        type: 'bar',
        data: {
          labels: ['Critical', 'High', 'Medium', 'Low'],
          datasets: [{
            label: 'Incident Severity Count',
            data: [28, 64, 112, 45],
            backgroundColor: ['#EF4444', '#F59E0B', '#06B6D4', '#10B981']
          }]
        },
        options: {
          responsive: true,
          plugins: { legend: { display: false } }
        }
      });
    }
  }
};

window.CivicAnalytics = CivicAnalytics;
"""

# 9. solutions.js
solutions_js = """/**
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
"""

files = {
    "data.js": data_js,
    "utils.js": utils_js,
    "auth.js": auth_js,
    "app.js": app_js,
    "ai-analysis.js": ai_analysis_js,
    "problems.js": problems_js,
    "map.js": map_js,
    "analytics.js": analytics_js,
    "solutions.js": solutions_js
}

for name, content in files.items():
    with open(os.path.join(JS_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)

print("JS files created successfully!")
