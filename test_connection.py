from memory_setup import hindsight, BANK_ID

hindsight.retain(bank_id=BANK_ID, content="This is a test memory to confirm the connection works.")
print("Success! Memory stored.")