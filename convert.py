import requests
from langchain.prompts import PromptTemplate
API_URL = "https://api-inference.huggingface.co/models/codellama/CodeLlama-13b-hf" #better results wrt 7b-hf
# API_URL = "https://api-inference.huggingface.co/models/codellama/CodeLlama-7b-hf"
# API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"
headers = {"Authorization": "Bearer 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"}
 
 
def query(payload):
    # response = requests.post(API_URL, headers=headers, json=payload)
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()
 
 
with open('chefrecipe.rb', 'r') as file: #Recipe1.rb  Recipe2.rb Recipe3.rb Recipe4.rb chefrecipe.rb
    code = file.read()
 
 
 
template = """[INST] <<SYS>> Convert the following chef recipe into an Ansible playbook: <</SYS>>
{code}
 
 
Here are some additional instructions to enhance the conversion:
1. Make sure to include the necessary Ansible modules for each task.
2. Use Ansible best practices for variable names and playbook structure.
3. Consider any specific requirements or constraints for the Ansible environment.
 
[/INST]"""
 
prompt= PromptTemplate.from_template(template)
prompt=prompt.format(code=code)
# print(prompt)
   
 
output = query({
    "inputs": prompt,
    "parameters": {'min_length': 200, 'max_length': 500, 'max_time':120}
})
# print(output)
print(output[0]['generated_text'])
# Extracting the generated_text field
# texts = [item['generated_text'] for item in output]
 
# # extract the part after "[/INST]\n: Like this:"
# answers = [text.split('[/INST]\n')[1] for text in texts if '[/INST]\n' in text]
 
 
# for answer in answers:
# print(answer)
# Extracting the generated_text field
texts = [item['generated_text'] for item in output]
 
# # extract the part after "[/INST]\n: Like this:"
answers = [text.split('[/INST]\n')[1] for text in texts if '[/INST]\n' in text]
 
 
# for answer in answers:
print(answers)
 
# Open the file in write mode ('w')
with open('output.yaml', 'w') as file:
    # Write the generated text to the file
    file.write(answers[0])
 
 
 
 
 
