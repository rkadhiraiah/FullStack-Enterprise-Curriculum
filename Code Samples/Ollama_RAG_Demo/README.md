# 🧠 Local AI: Retrieval-Augmented Generation (RAG) Pipeline

**Objective:** A capstone code sample for the Local AI Infrastructure module.

This repository demonstrates how to build a fully private, offline RAG pipeline. It utilizes the Ollama framework to run local Large Language Models (like Qwen 2.5) and vector databases to query private documents without sending data to external cloud providers.

## 🛠️ Infrastructure
* **LLM Engine:** Ollama 
* **Models:** Qwen 2.5 (optimized for standard local hardware/GPUs)
* **Orchestration:** LangChain (Python)
* **Vector Store:** ChromaDB

## 🚀 How It Works
1. **Ingestion:** Reads local text documents and splits them into chunks.
2. **Embedding:** Converts text into vector embeddings using a local embedding model.
3. **Retrieval:** Performs similarity search against the vector database based on the user prompt.
4. **Generation:** Passes the retrieved context to the local Ollama model to generate a secure, hallucination-free response.
