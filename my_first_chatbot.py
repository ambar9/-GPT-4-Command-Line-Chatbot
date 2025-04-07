from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI()

chat_history = [SystemMessage(content = 'You are a helpful assistant.')]

while True:
    input_text = input('You: ')
    chat_history.append(HumanMessage(content = input_text))
    if input_text == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f'AI: {result.content}')