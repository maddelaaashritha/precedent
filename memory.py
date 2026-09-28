from memory_setup import hindsight, BANK_ID

def store_incident(description, root_cause, fix, timestamp=None):
    content = (
        f"Incident: {description}\n"
        f"Root cause: {root_cause}\n"
        f"Fix that worked: {fix}"
    )
    if timestamp:
        hindsight.retain(bank_id=BANK_ID, content=content,
                         context="production incident", timestamp=timestamp)
    else:
        hindsight.retain(bank_id=BANK_ID, content=content,
                         context="production incident")
    print("Incident stored successfully!")

def recall_similar_incidents(new_incident_text):
    results = hindsight.recall(bank_id=BANK_ID, query=new_incident_text, budget="low")
    return results