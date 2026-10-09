/**
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
