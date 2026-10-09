/**
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
