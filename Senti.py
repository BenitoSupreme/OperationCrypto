import os
import openai

openai.api_key = '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'

def process_files_in_directory(directory_path, analyze):

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            analyze(file_path)

prompt = 'What is the meaning of life?'

response = openai.Completion.create(
  engine='text-davinci-003',
  prompt=prompt,
  max_tokens=50
)

output = response.choices[0].text.strip()

print(output)
