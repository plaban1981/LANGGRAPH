# LANGGRAPH
Learning Agenti AI
### Blogpost Generator
<img width="1232" alt="image" src="https://github.com/user-attachments/assets/80c9bd6e-d283-49ca-9510-579370650acb" />

<img width="1274" alt="image" src="https://github.com/user-attachments/assets/d3b378ea-9ae4-480c-be86-aa8faea4f00f" />




**Blog Post Generation**


**1. Overall Architecture:**




<img width="545" alt="image" src="https://github.com/user-attachments/assets/2a02913a-2ba7-4b0a-802e-04be3c478f00" />

 
**2. Workflow Components:**

- **Research Node**: 
  - Uses SerpAPI to gather real-world data
  - Combines search results with LLM processing
  - Creates comprehensive research summary

- **Title Generator**:
  - Takes research results and topic
  - Generates SEO-friendly title with emojis
  - Ensures engaging and relevant titles

- **Outline Generator**:
  - Creates structured outline with emoji sections
  - Based on research findings
  - Provides framework for content

- **Content Generator**:
  - Writes detailed content following outline
  - Incorporates emojis naturally
  - Maintains professional tone

- **Editor Node**:
  - Polishes content
  - Optimizes emoji usage
  - Ensures readability and flow

**3. UI Structure:**
```python
# Main Components
├── Header (✨ AI Blog Generator)
├── Sidebar
│   ├── Topic Input
│   ├── Generation Tips
│   └── Generate Button
└── Main Content
    ├── Progress Indicators
    ├── Generated Blog Section
    │   ├── Blog Title
    │   └── Blog Content
    └── Download Options
```

4. Key Features:

- **Progress Tracking**:
```python
status_messages = [
    "🔍 Researching topic...",
    "✍️ Generating title...",
    "📝 Creating outline...",
    "📚 Writing content...",
    "✨ Polishing final draft..."
]
```

- **Error Handling**:
```python
try:
    # Generation logic
except Exception as e:
    st.error(f"❌ An error occurred: {str(e)}")
```

- **Data Persistence**:
```python
def save_blog(title, content):
    # Handles AIMessage objects
    title_text = title.content if hasattr(title, 'content') else str(title)
    content_text = content.content if hasattr(content, 'content') else str(content)
    # Save to JSON
```

5. Styling Approach:
```css
/* Professional UI Elements */
.output-container {
    background-color: #f0f2f6;
    border-radius: 10px;
}

/* Section Headers */
h4 {
    border-left: 4px solid #FF4B4B;  // Visual hierarchy
}

/* Content Formatting */
.blog-content {
    line-height: 1.6;  // Readability
}
```

**6. Integration Points:**

- **LangGraph**: Manages the workflow between nodes
- **Groq**: Provides LLM capabilities
- **SerpAPI**: Gathers research data
- **Streamlit**: Handles UI rendering
- **Langsmith**: Enables debugging and monitoring

**7. User Experience Flow:**
 ![image](https://github.com/user-attachments/assets/5e42a870-13d8-459e-a246-5c6cd0bf6703)

 
**This architecture ensures:**
- Modular components
- Clear separation of concerns
- Scalable workflow
- Professional output
- User-friendly interface
- Error resilience
- Consistent styling

The approach combines AI capabilities with user experience best practices to create a professional blog generation tool.
