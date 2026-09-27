from memory import store_incident

store_incident(
    description="checkout-api service returning 500 errors, logs show 'connection pool exhausted'",
    root_cause="Database connection pool size was set too low for peak traffic load",
    fix="Increased the connection pool size from 10 to 50 and added pool usage monitoring"
)

store_incident(
    description="payment-service pods getting OOMKilled repeatedly during high load",
    root_cause="Memory limit set too low for the service's actual usage under load",
    fix="Increased memory limit from 512Mi to 1Gi and added a memory usage alert"
)

store_incident(
    description="cache-layer showing intermittent timeouts connecting to Redis",
    root_cause="Redis instance was undersized and hitting max connections limit",
    fix="Upgraded Redis instance tier and increased max connections setting"
)

print("All fake incidents stored!")