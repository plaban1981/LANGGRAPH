from typing import Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable

outline_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an outline creator. Based on the research provided, create a structured outline for a blog post. Include a relevant emoji for each main section to make the outline more engaging."),
    ("user", "Create an outline with section emojis based on this research: {research_results}")
])

@traceable(name="outline_node")
def create_outline(state: Dict[str, Any], llm) -> Dict[str, Any]:
    outline_chain = outline_prompt | llm
    
    outline = outline_chain.invoke({
        "research_results": state["research_results"]
    })
    
    state["outline"] = outline
    return state 