import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith configuration
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "Your API Key"
os.environ["LANGCHAIN_PROJECT"] = "blog_generator"

# API Keys
os.environ["GROQ_API_KEY"] = "Your Api Key"
os.environ["SERPAPI_API_KEY"] = "Your Api Key"
# Model configurations
MODEL_NAME = "mixtral-8x7b-32768"

# Temperature settings
TITLE_TEMP = 0.7
RESEARCH_TEMP = 0.7
OUTLINE_TEMP = 0.5
CONTENT_TEMP = 0.7
EDITOR_TEMP = 0.3 
