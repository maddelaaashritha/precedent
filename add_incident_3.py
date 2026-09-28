from memory import store_incident

store_incident(
    description="disk full on the logging server, no space left on device",
    root_cause="Log rotation was disabled after a config change, so log files grew without limit",
    fix="Re-enabled log rotation, cleared old logs, and added a disk usage alert at 80 percent"
)

print("New incident stored!")