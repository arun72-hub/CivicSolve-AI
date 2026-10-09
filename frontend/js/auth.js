/**
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
