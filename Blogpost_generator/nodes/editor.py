from typing import Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable

editor_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an editor who ensures blog content is engaging and well-formatted. When editing:
    - Maintain and refine existing emoji usage
    - Add emojis where they would enhance the message
    - Remove excessive or inappropriate emojis
    - Ensure consistent emoji style throughout
    - Check that emojis complement rather than overwhelm the content
    Focus on clarity, flow, and engagement while keeping emoji usage natural and meaningful."""),
    ("user", "Edit and improve this blog content while optimizing emoji usage: {draft_content}")
])

@traceable(name="editor_node")
def edit_content(state: Dict[str, Any], llm) -> Dict[str, Any]:
    editor_chain = editor_prompt | llm
    
    edited_content = editor_chain.invoke({
        "draft_content": state["draft_content"]
    })
    
    state["final_content"] = edited_content
    return state 