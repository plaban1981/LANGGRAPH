import streamlit as st
from main import generate_blog
import json
from datetime import datetime
import os

# Set page configuration
st.set_page_config(
    page_title="✨ AI Blog Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .output-container {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .title-section {
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
    }
    .status-message {
        text-align: center;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 10px;
        background-color: #e8f0fe;
    }
    .blog-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #1f1f1f;
    }
</style>
""", unsafe_allow_html=True)

def save_blog(title, content):
    """Save blog to a JSON file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_blogs/blog_{timestamp}.json"
    
    os.makedirs("generated_blogs", exist_ok=True)
    
    # Extract the content from AIMessage objects
    title_text = title.content if hasattr(title, 'content') else str(title)
    content_text = content.content if hasattr(content, 'content') else str(content)
    
    blog_data = {
        "title": title_text,
        "content": content_text,
        "generated_at": timestamp
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(blog_data, f, ensure_ascii=False, indent=4)
    
    return filename

def main():
    # Title Section
    st.markdown("""
    <div class="title-section">
        <h1>✨ AI Blog Generator ✨</h1>
        <p>Create engaging blog posts with AI-powered content generation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎯 Blog Settings")
        topic = st.text_area(
            "Enter your blog topic",
            placeholder="e.g., The Future of Artificial Intelligence",
            height=100
        )
        
        st.markdown("### 💡 Tips")
        st.info("""
        - Be specific with your topic
        - Include target audience if relevant
        - Mention specific aspects you want to cover
        """)
        
        generate_button = st.button("🚀 Generate Blog", type="primary")
    
    # Main content area
    if generate_button and topic:
        with st.spinner("🎨 Crafting your blog post..."):
            try:
                # Progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulate progress for better UX
                for i in range(5):
                    status_messages = [
                        "🔍 Researching topic...",
                        "✍️ Generating title...",
                        "📝 Creating outline...",
                        "📚 Writing content...",
                        "✨ Polishing final draft..."
                    ]
                    status_text.markdown(f"""
                    <div class="status-message">
                        {status_messages[i]}
                    </div>
                    """, unsafe_allow_html=True)
                    progress_bar.progress((i + 1) * 20)
                
                # Generate blog
                result = generate_blog(topic)
                
                # Display results
                st.markdown("### 📝 Generated Blog")
                
                # Title Section
                st.markdown("#### ✨ Blog Title")
                st.markdown(f"""
                <div class="output-container">
                    <div class="blog-title">{result['title'].content}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Content Section
                st.markdown("#### 📄 Blog Content")
                st.markdown("""
                <div class="output-container">
                    <div class="blog-content">
                """, unsafe_allow_html=True)
                st.markdown(result['final_content'].content)
                st.markdown("</div></div>", unsafe_allow_html=True)
                
                # Save blog
                title_text = result['title'].content if hasattr(result['title'], 'content') else str(result['title'])
                content_text = result['final_content'].content if hasattr(result['final_content'], 'content') else str(result['final_content'])
                filename = save_blog(title_text, content_text)
                
                # Download button
                with open(filename, 'r', encoding='utf-8') as f:
                    blog_json = f.read()
                    
                st.download_button(
                    label="📥 Download Blog",
                    data=blog_json,
                    file_name=f"blog_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    
    elif generate_button and not topic:
        st.warning("⚠️ Please enter a topic first!")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; margin-top: 2rem; padding: 1rem; background-color: #f0f2f6; border-radius: 10px;'>
        <p>Made with ❤️ using LangGraph and Groq</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 