# Memory Integration Template (OMEGA)

Add this section to the end of any agent's prompt file to enable persistent memory via OMEGA.

---

## Memory Integration

When you start a session, call `omega_welcome()` to load context from previous sessions. Review the briefing for prior decisions, pending tasks, and relevant context before proceeding.

When you make a key decision — choosing a technology, defining a contract, setting a constraint — store it:

```
omega_store("Chose PostgreSQL for user data due to ACID requirements and JSON support",
            event_type="decision",
            metadata={"project": "project-name", "topic": "database"})
```

When you learn something from a mistake or unexpected behavior, store it as a lesson:

```
omega_store("SQLite WAL mode required for concurrent read/write in multi-agent setups",
            event_type="lesson_learned",
            metadata={"project": "project-name"})
```

When you encounter an error pattern worth remembering:

```
omega_store("Race condition in connection pool when >10 concurrent queries; fixed with semaphore",
            event_type="error_pattern",
            metadata={"project": "project-name"})
```

When you need to find relevant context from past sessions, search semantically:

```
omega_query("database connection pooling strategy", mode="semantic")
```

When you need to pause and resume later, checkpoint your progress:

```
omega_checkpoint("Completed API routes for /users and /products. Next: /orders endpoint and auth middleware.")
```

When handing off to another agent, store a summary tagged for them:

```
omega_store("API spec complete: REST with JWT auth, 12 endpoints documented. Frontend can begin integration.",
            event_type="task_completion",
            metadata={"project": "project-name", "handoff_to": "frontend-developer"})
```

When resuming a previous task:

```
omega_resume_task()
```

---

Copy the **Memory Integration** section above (everything between the `---` markers) and paste it at the end of any agent file. Replace `project-name` with the actual project name.
