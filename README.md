# CV-Tailor

> A web application that automatically generates a tailored CV for any job description by combining your complete profile data with the target job posting.

---

## 📖 Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Repository Structure](#repository-structure)
4. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Environment Variables](#environment-variables)
   * [Installation & Local Development](#installation--local-development)
5. [Testing & CI](#testing--ci)
6. [Deployment](#deployment)

   * [Frontend (Vercel)](#frontend-vercel)
   * [Backend (Railway)](#backend-railway)
7. [Next Steps](#next-steps)
8. [License](#license)

---

## Project Overview

**CV-Tailor** streamlines the CV customization process by:

* Storing your entire profile (experiences, projects, skills, education).
* Accepting any job description (URL or pasted text).
* Using OpenAI’s API to generate a prioritized, role-specific CV in HTML format.
* (Future) Exporting to PDF, adding OAuth, and GitHub/LinkedIn imports.

This MVP focuses on core text-generation without authentication or PDF rendering.

---

## Tech Stack

| Layer              | Technology                             |
| ------------------ | -------------------------------------- |
| **Backend**        | FastAPI, Uvicorn, SQLAlchemy, Alembic  |
| **Frontend**       | React (JavaScript), Vite, Material‑UI  |
| **Database**       | PostgreSQL (via Railway plugin)        |
| **DevOps**         | Docker, Docker Compose, GitHub Actions |
| **AI Integration** | OpenAI ChatCompletion API              |

---

## Repository Structure

```
/ (root)
├── backend/                # FastAPI application
│   ├── main.py             # API entrypoint
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Container spec for backend
│   ├── .env.example        # Example env variables
│   └── tests/              # Pytest smoke tests
│       └── test_root.py    # Basic endpoint test
│
├── frontend/               # React application
│   ├── src/                # React source code
│   ├── package.json        # NPM scripts & dependencies
│   ├── vite.config.js      # Vite config
│   └── src/App.test.js     # Jest smoke test
│
├── docker-compose.yml      # Local dev orchestration (api + db)
├── .github/
│   └── workflows/ci.yml    # GitHub Actions CI pipeline
├── .gitignore
└── README.md               # This file
```

---

## Getting Started

### Prerequisites

* [Docker & Docker Compose](https://docs.docker.com/)
* [Git](https://git-scm.com/)
* A free [Railway](https://railway.app/) account (for remote DB & API)
* A free [Vercel](https://vercel.com/) account (for hosting the React app)
* [OpenAI API Key](https://platform.openai.com/account/api-keys)

### Environment Variables

Copy `backend/.env.example` to `backend/.env` and fill in:

```dotenv
DATABASE_URL=postgresql://<USER>:<PASS>@db:5432/<DB_NAME>
OPENAI_API_KEY=sk-...
JWT_SECRET=<your-jwt-secret>
```

> **Note:** `.env` is ignored by Git. Never commit secrets.

### Installation & Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/cv-tailor.git
   cd cv-tailor
   ```

2. **Start services with Docker Compose**

   ```bash
   docker-compose up --build
   ```

   * **API** available at: `http://localhost:8000`
   * **Database** on the `db` service

3. **Frontend**

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

   Open [http://localhost:5173](http://localhost:5173) in your browser.

4. **Run tests**

   ```bash
   # Backend tests
   docker-compose exec api pytest

   # Frontend tests
   cd frontend && npm test -- --watchAll=false
   ```

---

## Testing & CI

This repo uses **GitHub Actions** to run tests on every push and PR:

* **Backend**: spins up a Postgres service and runs `pytest`.
* **Frontend**: installs dependencies and runs `npm test`.

Check the **Actions** tab on GitHub for build status.

---

## Deployment

### Frontend (Vercel)

1. Import the GitHub repo in Vercel.
2. Set **Root Directory** to `/frontend`.
3. Add **Environment Variables** if needed.
4. Auto-deploys on every push to `main`.

### Backend (Railway)

1. Connect your GitHub repository.
2. Select the `backend` folder and enable **Docker deployment**.
3. Add **PostgreSQL plugin** for a managed database.
4. Set Railway environment variables to match `backend/.env`.
5. Deploy — your API gets a public URL.

---

## Next Steps

* Implement user authentication (JWT + OAuth)
* Integrate LinkedIn & GitHub imports
* Swap HTML output for PDF rendering (WeasyPrint or Puppeteer)
* Add UI polish and multi-template support

---

## License

This project is MIT‑licensed. See [LICENSE](LICENSE) for details.
