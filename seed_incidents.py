from memory import store_incident

incidents = [
    ("payment-service read replica lagging 40 minutes behind primary",
     "A long-running analytics query on the replica blocked replication",
     "Moved analytics queries to a dedicated replica and set statement_timeout to 30s",
     "2026-08-12T10:00:00Z"),
    ("checkout-api p99 latency above 5 seconds after release 4.12",
     "N+1 database query introduced in the new cart endpoint",
     "Rolled back release 4.12, then re-released with eager loading on the cart query",
     "2026-08-19T14:30:00Z"),
    ("notification-service not sending customer emails, no errors in app logs",
     "SMTP provider API key had expired",
     "Rotated the API key and added an alert 14 days before key expiry",
     "2026-08-26T09:15:00Z"),
    ("cache-layer Redis timeouts during flash sale, second time this quarter",
     "Application opened a new Redis connection per request instead of reusing them, hitting the max connections limit",
     "Enabled client-side connection pooling so connections are reused",
     "2026-09-03T18:45:00Z"),
    ("api-gateway returning 502 errors right after deployment",
     "Health check path was changed, so the load balancer marked every pod unhealthy",
     "Restored the health check path and added a post-deploy health check step to the pipeline",
     "2026-09-09T11:20:00Z"),
    ("ingestion-worker pods in CrashLoopBackOff after config update",
     "DATABASE_URL environment variable was missing from the new config map",
     "Added the variable and added config validation to the CI pipeline",
     "2026-09-16T16:05:00Z"),
]

for description, cause, fix, ts in incidents:
    store_incident(description, cause, fix, timestamp=ts)

print("All seed incidents stored!")