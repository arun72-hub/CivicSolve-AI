/**
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
