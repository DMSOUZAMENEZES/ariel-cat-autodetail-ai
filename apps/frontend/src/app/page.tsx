import { Activity, Car, Database, Server } from "lucide-react";

const items = [
  { label: "Frontend", value: "Next.js", icon: Activity },
  { label: "Backend", value: "FastAPI", icon: Server },
  { label: "Database", value: "PostgreSQL 16", icon: Database },
  { label: "Domain", value: "Automotive detailing", icon: Car }
];

export default function Home() {
  return (
    <main className="min-h-screen bg-background">
      <section className="mx-auto flex min-h-screen w-full max-w-6xl flex-col px-6 py-6">
        <header className="flex items-center justify-between border-b pb-4">
          <div>
            <p className="text-sm font-medium text-muted-foreground">AutoDetail AI</p>
            <h1 className="text-2xl font-semibold tracking-normal">Foundation workspace</h1>
          </div>
          <div className="rounded-md bg-primary px-3 py-2 text-sm font-medium text-primary-foreground">
            Sprint 01/02
          </div>
        </header>

        <div className="grid flex-1 items-center gap-6 py-10 md:grid-cols-[1.1fr_0.9fr]">
          <div className="max-w-2xl">
            <p className="text-sm font-semibold uppercase tracking-normal text-primary">
              SaaS foundation
            </p>
            <h2 className="mt-3 text-4xl font-semibold tracking-normal text-foreground md:text-5xl">
              Technical base for automotive aesthetic evaluations.
            </h2>
            <p className="mt-5 max-w-xl text-base leading-7 text-muted-foreground">
              Initial monorepo, containers, database models, migrations and seed data for the
              product described in the project documentation.
            </p>
          </div>

          <div className="grid gap-3">
            {items.map((item) => (
              <div
                key={item.label}
                className="flex min-h-20 items-center gap-4 rounded-lg border bg-white px-4"
              >
                <div className="flex size-10 items-center justify-center rounded-md bg-muted">
                  <item.icon className="size-5 text-primary" aria-hidden="true" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">{item.label}</p>
                  <p className="font-medium">{item.value}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
