from groq import Groq

GROQ_API_KEY = "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"

llm = Groq(api_key=GROQ_API_KEY)
while True:
    user_input=input("Enter your question: ")
    if user_input.lower() == "exit":
        break

    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    print(response.choices[0].message.content)