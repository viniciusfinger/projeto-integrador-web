from state import State
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

def attendance_agent(state: State):
    """Agent responsible for attending to the studio's clients"""
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    tools = [tool_get_client_info]
    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", """
                Você é um funcionário do estúdio Passione Tattoo e atende os clientes em seu primeiro contato para agendar uma tatuagem.
        
                Para isso, você deve utilizar as seguinte ferramenta disponíveis para coletar as informações necessárias para agendar a tatuagem:
                
                1. **tool_get_client_info**  :
                    Utilize esta ferramenta para coletar informações básicas do cliente, como nome, telefone e dados sobre a arte que o cliente quer tatuar.
                    - **Argumentos:**  
                        - `client_name`: (Opcional): Nome do cliente.
                        - `client_phone`: (Opcional): O telefone do cliente.
                        - `client_has_art_ready`: (Opcional): Se a arte que o cliente quer tatuar está pronta ou precisará ser criada.
                        
                        - **Comportamento esperado:**  
                        Se solicitado, a ferramenta pode retornar mensagens para pedir mais informações ou fornecer as informações já obtidas.
                        
                        Caso necessário, peça mais informações para extrair um entendimento robusto e adequado. 
                        Seja claro, direto e gentil.
                    
                        Responda na língua portuguesa do Brasil.
            """),
            ("placeholder", "{messages}")
        ]
    )
    
    agent = create_react_agent(model=llm, tools=tools, state_modifier=prompt_template, checkpointer=False)
    
    return agent.invoke({"messages": state["messages"]})


def tool_get_client_info(
    client_name: Optional[str] = None,
    client_phone: Optional[str] = None,
    client_has_art_ready: Optional[bool] = None,
) -> str:
    """
    Utilize esta ferramenta para obter informações sobre o cliente.
    
    Args:
        client_name: Optional[str] - Nome do cliente
        client_phone: Optional[str] - Telefone do cliente
        client_has_art_ready: Optional[bool] - Se a arte que o cliente quer tatuar está pronta ou precisará ser criada
    Returns:
        Retorna as informações do cliente agrupadas.
    """
    
    if client_name == None:
        return "Por favor, informe qual é o seu nome"
    if client_phone == None:
        return "Por favor, informe qual é o seu telefone para contato"
    if client_has_art_ready == None:
        return "Por favor, informe se a arte que o cliente quer tatuar está pronta ou precisará ser criada"

    return f"""
    Os dados foram coletados com sucesso:
    
    O nome do cliente é: {client_name}
    O telefone do cliente é: {client_phone}
    A arte que o cliente quer tatuar está pronta? {client_has_art_ready}
    """
