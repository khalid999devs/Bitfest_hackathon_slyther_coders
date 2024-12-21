from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, CSVLoader, JSONLoader
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM  

MODEL='llama2'

def fine_tune_model(data_path, file_type):
    if file_type == 'pdf':
        loader = PyPDFLoader(data_path)
    elif file_type == 'csv':
        loader = CSVLoader(data_path)
    elif file_type == 'json':
        loader = JSONLoader(data_path)
    else:
        raise ValueError("Unsupported file type")

    docs = loader.load()

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    
    llm = OllamaLLM(model=MODEL)
    chain = LLMChain(llm=llm, vectorstore=vectorstore)

    return chain
