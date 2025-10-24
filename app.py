import streamlit as st
import google.generativeai as genai

# --- Streamlit setup ---
st.set_page_config(page_title="📄 Gemini PDF Q&A", page_icon="🤖")
st.title("📄 Gemini PDF Q&A Chatbot")
st.write("Upload a PDF and ask questions — Gemini will read it directly!")

# --- Gemini API Key Input ---
api_key = st.text_input("🔑 Enter your Gemini API key:", type="password")
if api_key:
    genai.configure(api_key=api_key)

# --- Upload PDF ---
uploaded_file = st.file_uploader("📂 Upload a PDF file", type=["pdf"])

if uploaded_file and api_key:
    st.success("✅ PDF uploaded successfully!")
    
    # Load Gemini model
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    # Convert uploaded file to Gemini-compatible object
    pdf_data = {
        "mime_type": "application/pdf",
        "data": uploaded_file.getvalue()
    }

    # Ask questions about the PDF
    st.subheader("💬 Ask a question about your PDF")
    user_question = st.text_input("Type your question here")

    if st.button("Get Answer"):
        if not user_question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                response = model.generate_content(
                    [user_question, pdf_data]
                )
            st.write("### 🧠 Answer:")
            st.write(response.text)
else:
    st.info("Please upload a PDF and enter your API key to begin.")

