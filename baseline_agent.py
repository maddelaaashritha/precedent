import os, sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

incident = " ".join(sys.argv[1:]) or "redis timeouts again during a traffic spike"
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are an on-call SRE assistant."},
        {"role": "user", "content": f"New incident:\n{incident}\n\nWhat should I do?"}
    ]
)
print(response.choices[0].message.content)