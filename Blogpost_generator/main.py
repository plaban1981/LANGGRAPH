from typing import Dict, Any
from langgraph.graph import Graph, END,START,StateGraph
from config.config import *
from utils.llm_utils import create_llm
from nodes.research import research
from nodes.title_generator import generate_title
from nodes.outline_generator import create_outline
from nodes.content_generator import generate_content
from nodes.editor import edit_content
from typing_extensions import TypedDict,TypeVar, Annotated, Sequence, List, Tuple, Dict, Optional

class state(TypedDict):
    topic:str
    draft_content:str
    title:str
    research_results:str
    final_content:str
    outline:str
    

def create_blog_workflow() -> Graph:
    # Initialize LLMs with Groq
    research_llm = create_llm(MODEL_NAME, RESEARCH_TEMP)
    title_llm = create_llm(MODEL_NAME, TITLE_TEMP)
    outline_llm = create_llm(MODEL_NAME, OUTLINE_TEMP)
    content_llm = create_llm(MODEL_NAME, CONTENT_TEMP)
    editor_llm = create_llm(MODEL_NAME, EDITOR_TEMP)
    
    # Create workflow
    workflow = StateGraph(state)
    
    # Add nodes
    workflow.add_node("research", lambda state: research(state, research_llm))
    workflow.add_node("titles", lambda state: generate_title(state, title_llm))
    workflow.add_node("outlines", lambda state: create_outline(state, outline_llm))
    workflow.add_node("content", lambda state: generate_content(state, content_llm))
    workflow.add_node("editor", lambda state: edit_content(state, editor_llm))
    
    # Define edges
    workflow.add_edge(START,"research")
    workflow.add_edge("research", "titles")
    workflow.add_edge("titles", "outlines")
    workflow.add_edge("outlines", "content")
    workflow.add_edge("content", "editor")
    workflow.add_edge("editor", END)
    
    return workflow.compile()

def generate_blog(topic: str) -> Dict[str, Any]:
    workflow = create_blog_workflow()
    
    # Initialize state
    initial_state = {"topic": topic}
    
    # Execute workflow
    final_state = workflow.invoke(initial_state)
    
    return final_state

if __name__ == "__main__":
    topic = "All About Deepseek-R1"
    result = generate_blog(topic)
    print("Blog Title:")
    print(result["title"].content)
    print("\nFinal Blog Post:")
    print(result["final_content"].content) 
    #geerate .MD report
    with open("blogpost_content.md","w",encoding="utf-8") as f:
        f.write(result["title"].content)
        f.write("\n\n")
        f.write(result["final_content"].content)