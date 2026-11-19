!pip install openai
!pip install azure-ai-ml
!python -m pip install azure-identity
from openai import AzureOpenAI
endpoint = "https://project2016-resource.services.ai.azure.com/api/projects/project2016"
api_key = "DPSAotdfscQz0Ihv4SdoU0vCyp1rgU7FfJdWgDOfHxl88fdxxTO8JQQJ99CKACE1PydXJ3w3AAAAACOGC6XY"
deployment_name = "gpt-5-mini"
# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)


response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a named entity recognition assistant. Extract all person names, organization names, and locations from the user's text, and return them in JSON format with keys 'persons', 'organizations', 'locations'."},
        {"role": "user", "content": "Satya Nadella, CEO of Microsoft, announced a new partnership with the University of Washington in Seattle."}
    ]
)

print(response.choices[0].message.content)