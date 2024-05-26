#!/bin/bash

# Start the Ollama server at port 11434
echo "Starting the Ollama Server"
ollama serve &

# Check to see if the Llama3 LLM is available
echo "Waiting for Facebook's Open Source Llama3 downloads"
sleep 5 # Necessary if server is not yet up
ollama pull llama3

# Start the streamlit server, blocking exit
echo "Starting the Streamlit server"
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
