from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__)

# Load Azure OpenAI credentials from environment variables
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g. https://your-resource.openai.azure.com/
openai.api_version = "2024-05-01-preview"  # check your Azure OpenAI version

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # your model deployment name

@app.route("/", methods=["GET", "POST"])
def index():
    # 🔍 Debug: return raw text to confirm Flask response works
    return "<h1>Hello from Azure Flask Chatbot 🚀</h1>"
if __name__ == "__main__":
    app.run(debug=True)
