from memory import store_incident

store_incident(
    description="authentication service returning 401 errors for all users after deployment",
    root_cause="A misconfigured JWT secret key was deployed, causing all existing tokens to fail validation",
    fix="Rolled back the deployment and re-deployed with the correct JWT secret key from the secrets manager"
)

print("New incident stored!")