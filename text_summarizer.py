import requests
import streamlit as st

# URL for the Ollama API
OLLAMA_URL = "http://localhost:11434/api/generate"

# Function to summarize text using DeepSeek model
def summarize_text(text):
    # Prepare the payload for the API request
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text:\n\n{text}",
        "stream": False
    }
    # Make the POST request to the Ollama API
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No output generated")
    else:
        return f"Error: {response.text}"
    
# Streamlit app to summarize text
st.title("Text Summarizer with DeepSeek")
st.write("Enter text below to get a summary:")

user_input = st.text_area("Input Text", height=300)

if st.button("Summarize"):
    if user_input.strip() == "":
        st.error("Please enter some text to summarize")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(user_input)
        st.subheader("Summary:")
        st.write(summary)
    
# if __name__ == "__main__":
#     sample_text = """Artificial Intelligence is transforming industries
#     by automating tasks, analyzing large datasets, and improving 
#     decision-making. From healthcare to finance, AI applications 
#     are driving efficiency and innovation. However, ethical concerns 
#     about privacy, bias, and job displacement continue to spark 
#     global discussions."""

#     print("*** Summary ***")
#     print(summarize_text(sample_text))