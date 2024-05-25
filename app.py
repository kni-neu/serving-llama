from langchain_community.llms import Ollama
import streamlit as st
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# llm = Ollama(model="phi:latest", base_url="http://ollama-container:11434", verbose=True)
llm = Ollama(model="llama3", base_url="http://ollama-container:11434", verbose=True)

def sendPrompt(prompt):
    global llm
    response = llm.invoke(prompt)
    return response

st.set_page_config(page_title='My Little LLM', layout = 'wide', page_icon = 'https://media.licdn.com/dms/image/C5603AQFFBPEfIzXcgg/profile-displayphoto-shrink_200_200/0/1604552403158?e=2147483647&v=beta&t=mWcPkWfIc4XZ17UBffkKw8Q9D9P0RweCfhExkb_JQAM', initial_sidebar_state = 'auto')
st.title("Karl's Little Chatbot")
if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question !"}
    ]

if prompt := st.chat_input("Your question"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = sendPrompt(prompt)
            print(response)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message) 
