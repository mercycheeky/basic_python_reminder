from openai import OpenAI, OpenAIError

api_key = "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"
client = OpenAI(api_key=api_key)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)