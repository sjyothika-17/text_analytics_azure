!pip install openai
!pip install azure-ai-ml
!python -m pip install azure-identity
from openai import AzureOpenAI
endpoint = "https://project2016-resource.services.ai.azure.com/api/projects/project2016"
api_key = "DPSjaasjsnmsmms0vCyp1rgU7FfJdWgDOfHxl88fdxxTO8JQQJ99CKACE1PydXJ3w3AAAAACOGC6XY"
deployment_name = "gpt-5-mini"
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)


response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "indian capital "}
    ]
)

print(response.choices[0].message.content)
