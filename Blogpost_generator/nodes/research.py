from typing import Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable
from langchain_community.utilities import SerpAPIWrapper

research_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant. Based on the search results and topic provided, create a comprehensive research summary for a blog post. Include key facts, statistics, and relevant information."),
    ("user", """Research the following topic: {topic}

Search Results:
{search_results}

Provide a well-organized research summary that covers the main aspects of the topic.""")
])

@traceable(name="research_node")
def research(state: Dict[str, Any], llm) -> Dict[str, Any]:
    # Initialize SerpAPI
    search = SerpAPIWrapper()
    
    # Perform search
    search_results = search.run(f"{state['topic']} latest research facts statistics")
    
    # Add search results to state
    state["search_results"] = search_results
    
    # Create and run research chain
    research_chain = research_prompt | llm
    
    research_results = research_chain.invoke({
        "topic": state["topic"],
        "search_results": search_results
    })
    
    state["research_results"] = research_results
    return state 