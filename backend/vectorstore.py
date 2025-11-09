import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX_NAME, EMBED_MODEL
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
pc=Pinecone(api_key=PINECONE_API_KEY)
embeddings=HuggingFaceEmbeddings(model_name=EMBED_MODEL)
INDEX_NAME="rag-index"
def get_retriever():
    """Initialize and returns the Pinecone vector store retriever"""
    if INDEX_NAME not in pc.list_indexes().names():
         print("Creating Pinecone index...")
         pc.create_index(
             name=INDEX_NAME,
             dimension=384,
             metric="cosine",
             spec=ServerlessSpec(cloud='aws',region='us-east-1')
         )
         print("Created Pinecone index.")
    vectorstore=PineconeVectorStore(index_name=INDEX_NAME,embedding=embeddings)
    return vectorstore.as_retriever()
import uuid

def add_document(text_content: str):
    """Adds a single text document to the vector store
    Splits the text into chunks before embedding and upserting"""
    
    if not text_content:
        raise ValueError("Text content is empty.")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    
    # Split text into chunks
    chunks = text_splitter.split_text(text_content)  # returns list of strings
    print("Splitting document into chunks for indexing...")
    
    # Initialize vector store
    vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
    
    # Add text chunks directly
    vectorstore.add_texts(chunks)
    print("Successfully added chunks to vector store")

