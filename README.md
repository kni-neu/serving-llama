# Streamlit LLM Chatbot (Llama 3)

This is a Streamlit/Ollama LLM Application in a single container. You can read more about it at [this blog post](https://medium.com/@karl.cs6220/serving-llama-3-locally-with-streamlit-dc23c4fa133f)

## How to Run

1. Clone this repository
1. Run `./docker-startup build`
1. Run `./docker-startup deploy`

## How to Run with GPUs

1. Procure GPU GCP machine with appropriate boot disk and image
1. Clone this repository
1. Run `./docker-startup build`
1. Follow [instructions](https://hub.docker.com/r/ollama/ollama) to install with apt
1. Run `./docker-startup deploy-gpu`

## References

* [RAG with PDF upload](https://github.com/vndee/local-rag-example)
* [Langchain obtaining embeddings](https://python.langchain.com/v0.1/docs/integrations/text_embedding/ollama/)
* [Ollama blog with embeddings](https://ollama.com/blog/embedding-models)

