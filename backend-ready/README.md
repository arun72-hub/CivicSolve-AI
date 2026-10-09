# Backend Architecture & API Readiness Guide — CivicSolve AI

This directory documents the production-ready specifications for integrating the **FastAPI** Python backend, **PostgreSQL** relational database, and **AI/ML Inference Microservices** into the CivicSolve AI platform.

---

## 1. REST API Endpoints Specification

### Authentication & Users (`/api/auth`)
* `POST /api/auth/register`: Register user with role (`citizen`, `authority`, `government`, `admin`, `university`, `faculty`, `student`, `industry`).
* `POST /api/auth/login`: Authenticate credentials, return JWT Access & Refresh tokens.
* `GET /api/auth/me`: Retrieve current session user claims and profile details.

### Civic Problems Core (`/api/problems`)
* `GET /api/problems`: Filterable by category, status, severity, district, and priority score.
* `POST /api/problems`: Create problem with multipart upload (photos/video/PDF) and geo-coordinates.
* `GET /api/problems/{id}`: Fetch complete problem detail including timeline and solutions.
* `PUT /api/problems/{id}/status`: Authority and admin status updater (`Verified`, `Assigned`, `In Progress`, `Resolved`, `Escalated`).
* `POST /api/problems/{id}/upvote`: Increment community support counter.
* `POST /api/problems/{id}/comments`: Post citizen or departmental comments.

### AI Intelligence Microservices (`/api/ai`)
* `POST /api/ai/analyze`: Multi-modal analysis parsing text and evidence imagery.
* `POST /api/ai/duplicate-check`: Vector similarity lookup within geographical radius (PostGIS + pgvector).
* `POST /api/ai/priority`: Multi-factor prioritization algorithm scoring (1–100).
* `POST /api/ai/recommend-authority`: Jurisdiction and departmental mapping engine.

### Collaborative Innovation (`/api/solutions`)
* `GET /api/solutions`: Browse active prototypes and academic projects.
* `POST /api/solutions`: University teams submit prototype proposals.
* `POST /api/solutions/{id}/tasks`: Manage Kanban board work items.
* `POST /api/solutions/{id}/feedback`: Record citizen satisfaction ratings (1–5 stars) and sentiment analysis.

### Government Analytics (`/api/analytics`)
* `GET /api/analytics/overview`: High-level command center statistics.
* `GET /api/analytics/districts`: Comparative SLA performance across wards.
* `GET /api/analytics/map-markers`: GeoJSON feature collection for Leaflet/Mapbox layers.

---

## 2. PostgreSQL Relational Data Schema

```sql
-- Enums
CREATE TYPE user_role AS ENUM ('citizen', 'authority', 'government', 'admin', 'university', 'faculty', 'student', 'industry');
CREATE TYPE problem_severity AS ENUM ('Low', 'Medium', 'High', 'Critical');
CREATE TYPE problem_status AS ENUM ('Submitted', 'Under Review', 'Verified', 'Assigned', 'In Progress', 'Pilot Testing', 'Resolved', 'Rejected', 'Escalated');

-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role user_role NOT NULL,
    organization VARCHAR(150),
    phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Authorities Table
CREATE TABLE authorities (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    department VARCHAR(100) NOT NULL,
    jurisdiction VARCHAR(100) NOT NULL,
    sla_hours INTEGER DEFAULT 72,
    contact_email VARCHAR(100)
);

-- Problems Table with PostGIS
CREATE TABLE problems (
    id VARCHAR(30) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(100),
    severity problem_severity NOT NULL,
    priority_score INTEGER CHECK (priority_score BETWEEN 1 AND 100),
    status problem_status DEFAULT 'Submitted',
    affected_count INTEGER DEFAULT 0,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    address TEXT NOT NULL,
    district VARCHAR(100) NOT NULL,
    authority_id VARCHAR(50) REFERENCES authorities(id),
    assigned_officer VARCHAR(100),
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Timeline Events
CREATE TABLE timeline_events (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(30) REFERENCES problems(id) ON DELETE CASCADE,
    actor VARCHAR(100) NOT NULL,
    action VARCHAR(100) NOT NULL,
    note TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

## 3. Fast-Track FastAPI Integration Pattern

To swap the frontend `CivicDB` mock storage with live backend endpoints:

1. In `frontend/js/data.js`, replace the `localStorage` getters with `fetch('/api/...')` asynchronous promises.
2. The payload structure produced by `ProblemManager.submitFinalProblem()` in `problems.js` matches the `problems` SQL schema 1-to-1.
3. JWT tokens should be stored in `localStorage.setItem('civic_token', token)` and automatically appended to the `Authorization: Bearer <token>` header in `utils.js`.