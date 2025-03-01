from typing import Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable

content_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a blog writer who creates engaging content with appropriate emoji usage. Follow these guidelines:
    - Include relevant emojis at the start of each section/heading
    - Use emojis to emphasize key points and statistics
    - Add emojis to make important takeaways more memorable
    - Don't overuse emojis - aim for natural, meaningful placement
    - Ensure emojis enhance readability rather than distract from it"""),
    ("user", "Write an engaging blog post with appropriate emoji usage following this outline: {outline}")
])

@traceable(name="content_node")
def generate_content(state: Dict[str, Any], llm) -> Dict[str, Any]:
    content_chain = content_prompt | llm
    
    content = content_chain.invoke({
        "outline": state["outline"]
    })
    
    state["draft_content"] = content
    return state 