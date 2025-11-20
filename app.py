from google import genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") 

# Create a client
client = genai.Client(api_key=api_key)

# Define the model you are going to use
model_id =  "gemini-2.5-flash"



# Define the prompt
prompt = "get the table data from given pdf file. return the data in a table format. "
file_path = "files/sample.pdf"

_pdf = client.files.upload(file="files/sample.pdf", config={'display_name': 'pdf'})

file_size = client.models.count_tokens(model=model_id,contents=_pdf)
print(f'File: {_pdf.display_name} equals to {file_size.total_tokens} tokens')

file = client.files.upload(file=file_path, config={'display_name': file_path.split('/')[-1].split('.')[0]})

# Generate a response 
start_time = time.time()
response = client.models.generate_content(model=model_id, contents=[prompt, file], config={'response_mime_type': 'text/plain'})
end_time = time.time()

# Calculate and print the time taken
elapsed_time = end_time - start_time
print(f"\nTime taken to get response: {elapsed_time:.2f} seconds")

# print the response
print(response.text)

