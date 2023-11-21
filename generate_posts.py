import csv
import time
from openai import OpenAI

#initialize
client = OpenAI()

# List of prompts
# prompts = [
#     "Please write a two paragraph blog post about the structure of the atom.",
#     "Please write a two paragraph blog post about global financial markets.",
#     "Please write a two paragraph blog post about how large language models work.",
#     "Please write a two paragraph blog post about geopolitics in the modern age."
# ]

# does "blog post" matter?
prompts = [
    "Please write a two paragraph explanation about the structure of the atom.",
    "Please write a two paragraph explanation about global financial markets.",
    "Please write a two paragraph explanation about how large language models work.",
    "Please write a two paragraph explanation about geopolitics in the modern age."
]

# models
models = ["gpt-3.5-turbo","gpt-4-1106-preview"]

sys_messages = [
"You are an expert blog writer who uses engaging metaphors to make sense of complex topics for your readers.",
"You are a writer who uses engaging metaphors to make sense of complex topics for your readers."
]

# Open a CSV file in write mode
with open('output.csv', mode='w', newline='') as file:
    # Create a CSV writer
    csv_writer = csv.writer(file)
    print("empty file created")

    # Write the header
    csv_writer.writerow(['prompt', 'model', 'response'])

    #Iterate over models first
    for model in models:
        # Iterate over the prompts
        for i in range(100):
            print(model, i)
            time.sleep(2)
            st= time.time()
            prompt = prompts[i % 4]
            # print("current prompt:", prompt)

            # Request a completion from the OpenAI API
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system", "content": sys_messages[1]},
                    {"role": "user", "content": prompt}
                ]
            )
            et = time.time()

            # Retrieve the response
            response = completion.choices[0].message.content
            # print("done with one")
            print(response[:50])
            print('this took', et-st)
            # Write the current prompt, model, and response to the CSV
            csv_writer.writerow([prompt, model, response])
