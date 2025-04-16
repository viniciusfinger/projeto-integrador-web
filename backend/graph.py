from langgraph.graph import StateGraph, END, START
from agent.attendance_agent import attendance_agent
from langgraph.checkpoint.memory import MemorySaver
from state import State

def create_graph():
    
    checkpointer = MemorySaver()
    
    graph = StateGraph(State)
    
    graph.add_node("attendance_agent", attendance_agent)
    
    graph.add_edge(START, "attendance_agent")
    graph.add_edge("attendance_agent", END)
    
    return graph.compile(checkpointer=checkpointer)
    