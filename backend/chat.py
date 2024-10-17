import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

# Initialize the language model
llm = ChatOllama(
    model="KolekarPramod/hrbot",
    temperature=0,
    # other params...
)

# Set up the Streamlit app
st.title("Chatbot Interface")
st.write("Talk to the chatbot!")

# Create a text input for user messages
user_input = st.text_input("You:", "")

# When the user submits a message
if st.button("Send"):
    if user_input:
        # Generate a response from the model
        ai_msg = llm.invoke(user_input)
        # Display the AI's response
        st.text_area("Bot:", ai_msg.content, height=200)

# Optional: Display chat history
if 'history' not in st.session_state:
    st.session_state.history = []

if user_input:
    st.session_state.history.append(f"You: {user_input}")
    st.session_state.history.append(f"Bot: {ai_msg.content}")

# Display the chat history
st.write("### Chat History:")
for message in st.session_state.history:
    st.write(message)
