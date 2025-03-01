from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable

@traceable(name="initialize_llm")
def create_llm(model_name: str, temperature: float) -> ChatGroq:
    """
    Create a Groq LLM instance
    """
    llm = ChatGroq(
        model_name=model_name,
        temperature=temperature,
        max_tokens=8192,
    )
    
    return llm 