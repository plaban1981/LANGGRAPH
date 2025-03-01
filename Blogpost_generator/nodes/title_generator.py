from typing import Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable

title_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative title generator. Create an engaging, SEO-friendly title for a blog post. Include 1-2 relevant emojis in the title to make it more engaging."),
    ("user", "Generate a compelling title with emojis for a blog post about: {topic}\n\nResearch context: {research_results} STRICTLY WITHIN 35 WORDS")
])

@traceable(name="title_node")
def generate_title(state: Dict[str, Any], llm) -> Dict[str, Any]:
    title_chain = title_prompt | llm
    
    title = title_chain.invoke({
        "topic": state["topic"],
        "research_results": state["research_results"]
    })
    
    state["title"] = title
    return state 