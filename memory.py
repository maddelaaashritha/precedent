from memory_setup import hindsight, BANK_ID

def store_incident(description, root_cause, fix):
    content = (
        f"Incident: {description}\n"
        f"Root cause: {root_cause}\n"
        f"Fix that worked: {fix}"
    )
    hindsight.retain(bank_id=BANK_ID, content=content)
    print("Incident stored successfully!")

def recall_similar_incidents(new_incident_text):
    results = hindsight.recall(bank_id=BANK_ID, query=new_incident_text, budget="low")
    return results