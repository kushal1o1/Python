# This code is for v1 of the openai package: pypi.org/project/openai
import openai

# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI(api_key='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')

response = client.completions.create(
  model="text-davinci-003",
  prompt="write an letter to friend ",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
text_only = response.choices[0].text

print(text_only)

