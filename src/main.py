import os
import json
import streamlit as st
import openai

# Configuring openai - api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# Configuring streamlit page settings
st.set_page_config(
    page_title="GPT-3.5-Turbo Chat",
    page_icon="💬",
    layout="centered"
)

# Initialize Chat Session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
# Streamlit page title
st.title("🤖 GPT-3.5-Turbo")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Input field for user's message
user_prompt = st.chat_input("Ask GPT-3.5-Turbo...")

if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user",
                                          "content": user_prompt})
    
    # Send user's message to GPT-3.5-Turbo and get a response
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]
    )
    
    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    
    # Display GPT-3.5-Turbo's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)