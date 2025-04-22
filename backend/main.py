from graph import create_graph
from langchain_core.messages import HumanMessage

graph = create_graph()

#TODO: Adicionar configuração do thread_id vinda do frontend
#TODO: criar uma API e colocar isso em um controller
config = {
    "configurable": {
        "thread_id": "123"
    }
}

while True:
    user_input = input("Digite uma mensagem: ")
    
    response = graph.invoke({"messages": [HumanMessage(content=user_input)]}, config)
    
    print(response["messages"][-1].content)