import streamlit as st
import requests

# Function to call Azure OpenAI API
def call_openai_api(prompt):
    api_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Your API key
    endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }
    
    response = requests.post(endpoint, headers=headers, json=data)
    return response.json()

# Streamlit UI
st.title("Financial Advisor Chatbot")
st.write("Ask me any financial question below!")

# Text input for user question with a unique key
user_input = st.text_input("Your Question:", key="user_question")

if st.button("Get Advice"):
    if user_input:
        # Call the OpenAI API
        response = call_openai_api(user_input)
        advice = response['choices'][0]['message']['content']
        st.write("**Financial Advice:**", advice)
    else:
        st.write("Please enter a question to get advice.")