import streamlit as st
import time
import random

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="20-Day Sprint Finale", page_icon="🚀", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("🚀 My AI Portfolio")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate to:", ["Sprint Overview", "RAG Chatbot Showcase", "Text Analyzer", "Data Dashboard"])

# 3. Page 1: The Overview (A summary of your journey)
if page == "Sprint Overview":
    st.title("🎉 The 20-Day Portfolio Sprint")
    st.markdown("### Welcome to my Grand Finale Web App!")
    st.write("Over the last 20 days, I have leveled up from basic scripts to Cloud APIs and AI models.")
    
    # Create 3 columns for a nice visual layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("💻 Python Foundations")
        st.write("✅ Object-Oriented Programming\n✅ Data Structures\n✅ Terminal Apps")
        
    with col2:
        st.success("🤖 Artificial Intelligence")
        st.write("✅ Machine Learning\n✅ Neural Networks\n✅ Computer Vision")
        
    with col3:
        st.warning("🌐 Cloud & Web")
        st.write("✅ Web Scraping\n✅ FastAPI Servers\n✅ Cloud Deployment")
        
    # Trigger a celebration animation!
    st.balloons()

# 3b. Page 1b: RAG Chatbot Showcase
elif page == "RAG Chatbot Showcase":
    st.title("🤖 RAG Chatbot Showcase")
    st.markdown("### AI-Powered Document Knowledge Assistant")
    st.write("An intelligent Retrieval-Augmented Generation (RAG) system built to query unstructured data in real-time.")
    
    # Showcase Columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💡 What is RAG?")
        st.markdown("""
        **Retrieval-Augmented Generation (RAG)** is an AI architecture that enhances the capabilities of a Large Language Model (LLM) by retrieving relevant data from an external knowledge base (like uploaded documents) before generating a response.
        
        This prevents AI hallucinations and allows for highly accurate, domain-specific answers.
        """)
        
        st.subheader("🚀 Tech Stack")
        st.info("⚡ **FastAPI & Uvicorn:** Async backend serving API endpoints.")
        st.success("🧠 **Gemini API:** Generates text embeddings and processes context-aware prompt instructions.")
        st.warning("🌲 **Pinecone:** Serverless vector search engine for real-time similarity querying.")
        st.error("🎨 **Glassmorphism UI:** Vanilla HTML/CSS/JS frontend with modern visual layouts.")
        
    with col2:
        st.subheader("⚙️ System Architecture Flow")
        st.markdown("""
        1. **Document Upload:** User drops a PDF/TXT file into the glassmorphic frontend UI.
        2. **Ingestion & Parsing:** FastAPI reads document pages and extracts text using `pdfplumber`.
        3. **Embedding:** Text chunks are transformed into 768-dimensional vector representations using `gemini-embedding-2`.
        4. **Vector Storage:** Embeddings are indexed and stored inside Pinecone.
        5. **Semantic Retrieval:** When a user asks a question, the query is embedded and Pinecone retrieves the most mathematically similar text chunks.
        6. **Contextual Answer:** Gemini synthesizes the question and matching contexts to generate a precise, markdown-formatted response.
        """)
        
        # Link button to repo
        st.markdown("---")
        st.link_button("📂 View RAG Chatbot Repository", "https://github.com/Saminathan6327/rag-chatbot")

# 4. Page 2: Interactive Text Analyzer (Like our Day 16 API, but graphical!)
elif page == "Text Analyzer":
    st.title("📝 Interactive Text Analyzer")
    st.write("Type some text below and let Python process it in real-time.")
    
    # An interactive text box for the user
    user_input = st.text_area("Enter your text here:", "Streamlit makes building web apps incredibly easy.")
    
    # A clickable button
    if st.button("Analyze Text"):
        # Show a loading spinner while "processing"
        with st.spinner("Analyzing data..."):
            time.sleep(1) # Fake delay to make it look like heavy computation!
            
            word_count = len(user_input.split())
            char_count = len(user_input)
            
            st.subheader("Analysis Results:")
            
            # Streamlit "Metrics" look like professional dashboards
            metric_col1, metric_col2 = st.columns(2)
            metric_col1.metric("Word Count", word_count)
            metric_col2.metric("Character Count", char_count)
            
            st.markdown("**Uppercased Version:**")
            st.code(user_input.upper())

# 5. Page 3: Live Data Simulator (Visualizing data like Data Scientists do)
elif page == "Data Dashboard":
    st.title("📊 Live Data Simulator")
    st.write("Streamlit can render charts and data visuals instantly with just one line of code.")
    
    if st.button("Generate Random Data"):
        with st.spinner("Connecting to data source..."):
            time.sleep(0.5)
            # Generate a list of 20 random numbers
            data = [random.randint(10, 100) for _ in range(20)]
            
            # Instantly draw charts
            st.line_chart(data)
            st.bar_chart(data)
            
            st.success("Data visualized successfully!")