/**
 * CivicSolve AI - Notification Hub Controller
 */
const NotificationHub = {
  loadNotifications() {
    return window.CivicDB ? window.CivicDB.getNotifications() : [];
  },

  markAllAsRead() {
    const list = this.loadNotifications();
    list.forEach(n => n.read = true);
    localStorage.setItem("civic_notifications", JSON.stringify(list));
    if (window.CivicUtils) {
      CivicUtils.showToast("All notifications marked as read.", "success");
    }
  }
};

window.NotificationHub = NotificationHub;