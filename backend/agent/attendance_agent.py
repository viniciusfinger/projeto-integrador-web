from state import State
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

def attendance_agent(state: State):
    """Agent responsible for attending to the studio's clients"""
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))
    tools = [tool_get_client_info]

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", """
                Você é um funcionário do estúdio Passione Tattoo Studio e atende os clientes em seu primeiro contato para agendar uma tatuagem.
                
                O estúdio fica localizado no centro de Canoas, Rio Grande do Sul. Na rua Rua dr barcelos, 2451, sala 501.
                O telefone de contato é (51)98989-7802
                
                Os tatuadores disponíveis são:
                    - Jean Szimanski, especialista em Geek, blackwork e Fullcolor. Instagram: @Jeanzink_
                    - Maria Quelipe, especialista em Geek, whipshading e delicadas. Instagram: @Marye.ink
                    - Gustavo Campos, especialista em Geek, whipshading e dark. Instagram: @guszink
                    
                Tire possíveis dúvidas sobre os tatuadores e suas especialidades, além de explicar os estilos de tatuagem, caso o usuário solicite.
                
                Para isso, você deve utilizar as seguinte ferramenta disponíveis para coletar as informações necessárias para agendar a tatuagem:
                
                1. **tool_get_client_info**:
                    Utilize esta ferramenta para coletar informações básicas do cliente, como nome, telefone e dados sobre a arte que o cliente quer tatuar.
                    - **Argumentos:**  
                        - `client_name`: (Opcional): Nome do cliente.
                        - `client_phone`: (Opcional): O telefone do cliente.
                        - `client_has_art_ready`: (Opcional): Se a arte que o cliente quer tatuar está pronta ou precisará ser criada.
                        - `tattoo_artist`: (Opcional): Nome do tatuador que o cliente quer agendar.
                        
                        - **Comportamento esperado:**  
                        Se solicitado, a ferramenta pode retornar mensagens para pedir mais informações ou fornecer as informações já obtidas.
                        
                        Caso necessário, peça mais informações para extrair um entendimento robusto e adequado. 
                        
                        Seja claro, legal e gentil. Use uma linguagem informal, jovial e descontraída com o usuário.
                    
                        Responda na língua portuguesa do Brasil, não use markdown.
                        Qualquer pergunta que não seja sobre o estúdio, tatuadores ou o contexto de tattoo, deve ser respondida com "Desculpe, não posso te ajudar com isso, estou aqui para te atender sobre o estúdio e os tatuadores."
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
    tattoo_artist: Optional[str] = None,
) -> str:
    """
    Utilize esta ferramenta para obter informações sobre o cliente.
    
    Args:
        client_name: Optional[str] - Nome do cliente
        client_phone: Optional[str] - Telefone do cliente
        client_has_art_ready: Optional[bool] - Se a arte que o cliente quer tatuar está pronta ou precisará ser criada
        tattoo_artist: Optional[str] - Nome do tatuador que o cliente quer agendar
    Returns:
        Retorna as informações do cliente agrupadas.
    """
    
    if client_name == None:
        return "Por favor, informe qual é o seu nome"
    if client_phone == None:
        return "Por favor, informe qual é o seu telefone para contato"
    if client_has_art_ready == None:
        return "Por favor, informe se a arte que o cliente quer tatuar está pronta ou precisará ser criada"
    if tattoo_artist == None:
        return "Por favor, informe qual é o tatuador que o cliente quer agendar"

    return f"""
    Os dados foram coletados com sucesso:
    
    O nome do cliente é: {client_name}
    O telefone do cliente é: {client_phone}
    A arte que o cliente quer tatuar está pronta? {client_has_art_ready}
    O tatuador que o cliente quer agendar é: {tattoo_artist}
    """

def tool_persist_client_info(client_info: str):
    """
    Utilize esta ferramenta para persistir as informações do cliente.
    """
    #TODO: Implementar a persistência das informações do cliente no DB
    
    return f"Informações do cliente persistidas com sucesso: {client_info}"