from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import Ollama

def initialize_chat():
    llm = Ollama(model="llama2") 
    memory = ConversationBufferMemory()  
    chat_chain = ConversationChain(llm=llm, memory=memory)
    return chat_chain

def chat_with_model(chat_chain, user_input):
    response = chat_chain.run(user_input)
    return response