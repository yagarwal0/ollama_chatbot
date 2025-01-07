import streamlit as st
from langchain_ollama import OllamaLLM

model_name = "llama3.2"

st.title("Ollama LLM Chatbot")
st.write("Using model: llama3.2")

prompt = st.text_input("Enter your query:", placeholder="Type something here...")

if st.button("Get your Answer"):
    if prompt.strip():
        try:
            llm = OllamaLLM(model=model_name)            
            response = llm.invoke(prompt)
            st.subheader("Response:")
            st.write(response)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before clicking the button.")

st.markdown("---")
st.write("Built by [Yash](https://linkedin.com/yashcs).")
