"""
Enterprise Training Sample: Private RAG Pipeline Implementation
Demonstrates connecting a local vector store to an Ollama-hosted LLM.
"""

from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

def build_local_rag_pipeline(file_path, query):
    # 1. Load the private document
    print("Loading document...")
    loader = TextLoader(file_path)
    documents = loader.load()

    # 2. Split document into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # 3. Create localized embeddings and store in ChromaDB
    print("Generating local embeddings...")
    embeddings = FastEmbedEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)

    # 4. Initialize the local LLM via Ollama (e.g., Qwen 2.5)
    print("Initializing local LLM...")
    llm = Ollama(model="qwen2.5")

    # 5. Build the Retrieval QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3})
    )

    # 6. Execute the secure local query
    print(f"Querying: {query}")
    response = qa_chain.invoke(query)
    
    return response['result']

if __name__ == "__main__":
    # Example usage:
    # Ensure Ollama is running locally with 'ollama run qwen2.5'
    sample_query = "What are the core features of the Global Staffing Operating System?"
    # answer = build_local_rag_pipeline("hr_requirements_doc.txt", sample_query)
    # print(answer)
