/**
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
