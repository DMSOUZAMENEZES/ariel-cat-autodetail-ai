# AutoDetail AI

Foundation for a multi-tenant automotive detailing SaaS.

## Local stack

Copy environment defaults when needed:

```bash
cp .env.example .env
```

Start the Sprint 01/02 stack:

```bash
docker compose up -d
```

Active services in this sprint:

- Next.js frontend on `http://localhost:3000`
- FastAPI backend on `http://localhost:8000`
- PostgreSQL 16 on `localhost:5432`
- Redis on `localhost:6379`

Out of scope for this sprint: AI, WhatsApp, n8n, PDF generation, worker and nginx.

## Workspace

Install frontend workspace dependencies:

```bash
pnpm install
```

Run the frontend locally:

```bash
pnpm --filter @autodetail/frontend dev
```

## Backend database

Run migrations from `apps/backend`:

```bash
alembic upgrade head
```

Run demo seeds:

```bash
python -m app.db.seed
```
