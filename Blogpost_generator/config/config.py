import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith configuration
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_PROJECT"] = "blog_generator"

# API Keys
os.environ["GROQ_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "6409ba77b2520ac169496f6fe7d0060c0b10ef58b0748ec8084fb28cba313ce1"
# Model configurations
MODEL_NAME = "mixtral-8x7b-32768"

# Temperature settings
TITLE_TEMP = 0.7
RESEARCH_TEMP = 0.7
OUTLINE_TEMP = 0.5
CONTENT_TEMP = 0.7
EDITOR_TEMP = 0.3 