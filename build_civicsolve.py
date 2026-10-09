"""
CivicSolve AI - Full Project Builder Script
Builds the complete suite of HTML, CSS, JS, and Asset files
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
CSS_DIR = os.path.join(FRONTEND_DIR, "css")
JS_DIR = os.path.join(FRONTEND_DIR, "js")
ASSETS_DIR = os.path.join(FRONTEND_DIR, "assets")
BACKEND_DIR = os.path.join(BASE_DIR, "backend-ready")

for d in [CSS_DIR, JS_DIR, ASSETS_DIR, BACKEND_DIR, os.path.join(ASSETS_DIR, "icons"), os.path.join(ASSETS_DIR, "images")]:
    os.makedirs(d, exist_ok=True)

# 1. Assets
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 21h18"/>
  <path d="M19 21v-4"/>
  <path d="M19 13V5a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v16"/>
  <path d="M9 9h6"/>
  <path d="M9 13h6"/>
  <path d="M9 17h2"/>
  <circle cx="17" cy="7" r="2" fill="#06B6D4" stroke="none"/>
</svg>"""

avatar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="40" height="40" fill="#64748B">
  <circle cx="12" cy="8" r="4"/>
  <path d="M4 20c0-4 4-6 8-6s8 2 8 6"/>
</svg>"""

with open(os.path.join(ASSETS_DIR, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)
with open(os.path.join(ASSETS_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)
with open(os.path.join(ASSETS_DIR, "default-avatar.svg"), "w", encoding="utf-8") as f:
    f.write(avatar_svg)

print("Assets created successfully.")
