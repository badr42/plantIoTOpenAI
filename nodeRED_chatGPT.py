import os
import openai
import sys

#openai.api_key = os.getenv("OPENAI_API_KEY")


humidity = sys.argv[1]

plant= sys.argv[2]

prompt= "the current soil humidity is " + humidity + "% is this enough for a " +plant+" plant, tell me if the water humidity is enough or not and what i should do, and then share some trivia about this plant"
# print(prompt)


response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)



# {
# "plant": "mint",
# "humidity": 30
# }