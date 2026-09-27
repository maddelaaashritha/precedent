from memory_setup import hindsight, BANK_ID

def diagnose_with_memory(incident_text):
    answer = hindsight.reflect(
        bank_id=BANK_ID,
        query=f"A new incident just happened: {incident_text}. Have we seen anything similar before? If so, what was the root cause and the fix? If not, say clearly that this is a new type of incident."
    )
    return answer

if __name__ == "__main__":
    result = diagnose_with_memory("checkout service throwing 500s, pool exhausted")
    print(result.text)