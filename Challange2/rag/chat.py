from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import Ollama

def initialize_chat():
    llm = Ollama(model="llama2") 
    memory = ConversationBufferMemory()  
    chat_chain = ConversationChain(llm=llm, memory=memory)
    return chat_chain

def chat_with_model(chat_chain, user_input):
    complex_prompt = f"""
    You are an assistant designed to engage in thoughtful and insightful conversations. Your responses should be clear, detailed, and considerate of the context of the previous messages.
    The conversation context will be stored, so always refer to previous exchanges for coherence. 
    User input: {user_input}
    Respond as though you are engaging in an interactive dialogue with the user, considering their interests and goals.
    """
    response = chat_chain.run(complex_prompt)
    return response