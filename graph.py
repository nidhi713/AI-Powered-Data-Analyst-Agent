from langgraph.graph import StateGraph
from agent import AgentState, analyze_node, insight_node, qa_node

# Create graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("analyze", analyze_node)
workflow.add_node("insights", insight_node)
workflow.add_node("qa", qa_node)

# Define flow
workflow.set_entry_point("analyze")

workflow.add_edge("analyze", "insights")
workflow.add_edge("insights", "qa")

# Compile graph
graph = workflow.compile()