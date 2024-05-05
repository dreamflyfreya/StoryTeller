from openai import OpenAI


client = OpenAI()

prompts = ["a cat with prompts "]
for scene in scenes:
  response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="256x256",
    quality="standard",
    n=1,
  )
