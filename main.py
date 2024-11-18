from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv()

# Retrieve the endpoint and subscription key from environment variables
endpoint = os.getenv("AZURE_VISION_ENDPOINT")
subscription_key = os.getenv("AZURE_VISION_SUBSCRIPTION_KEY")

# Validate that the necessary environment variables are set
if not endpoint or not subscription_key:
    raise EnvironmentError("Please set AZURE_VISION_ENDPOINT and AZURE_VISION_SUBSCRIPTION_KEY in your environment.")

# API URL and request parameters
analyze_url = f"{endpoint}/vision/v3.1/analyze"
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}
params = {
    "visualFeatures": "Categories,Description,Color"
}

# Example image URL
image_url = "https://cdn.pixabay.com/photo/2024/06/22/16/55/ai-generated-8846672_1280.jpg"
data = {"url": image_url}

# Make the request to the Azure Vision API
response = requests.post(analyze_url, headers=headers, params=params, json=data)

# Check for errors in the response
response.raise_for_status()

# Parse and display the analysis results
analysis = response.json()
print("Analysis results:", analysis)
