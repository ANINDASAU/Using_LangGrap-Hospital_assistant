import os
import streamlit as st
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="AS Hospital Assistant", page_icon="🏥")
st.title("🏥 AS Hospital Symptom Assistant")
st.markdown("This agent uses **Gemini 2.5 Flash** and **LangGraph** to route medical inquiries.")

# --- SIDEBAR: API KEY ---
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your Google API Key", type="password")
    st.info("Your key is used only for this session.")

# Check if API key is provided
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    
    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

    # --- LANGGRAPH NODES ---

    def get_symptom_node(state: dict) -> dict:
        # In the UI version, we just pass the state through
        # because the input is captured by the Streamlit text_input
        return state

    def classify_symptom(state: dict) -> dict:
        prompt = (
            "You are a helpful medical assistant, classify the symptom below into one of the categories \n "
            "-General\n -Emergency\n -Nerve Problem\n"
            f"Symptom: {state['symptom']}\n"
            "Respond only with one word: General, Emergency or Nerve Problem"
        )
        response = llm.invoke([HumanMessage(content=prompt)])
        category = response.content.strip()
        state["category"] = category
        return state

    def symptom_router(state: dict) -> dict:
        cat = state["category"].lower()
        if "general" in cat:
            return "general"
        elif "emergency" in cat:
            return "emergency"
        elif "nerve problem" in cat:
            return "nerve_problem"
        else:
            return "general"

    def general_node(state: dict) -> dict:
        state["answer"] = f"'{state['symptom']}' seems general: directing you to the general ward for consulting a doctor."
        return state

    def emergency_node(state: dict) -> dict:
        state["answer"] = f"'{state['symptom']}' is a MEDICAL EMERGENCY: seeking immediate help."
        return state

    def nerve_problem_node(state: dict) -> dict:
        state["answer"] = f"'{state['symptom']}' seems like a nerve health issue: talk to our counselor."
        return state

    # --- BUILD LANGGRAPH ---
    builder = StateGraph(dict)
    builder.set_entry_point("get_symptom")

    builder.add_node("get_symptom", get_symptom_node)
    builder.add_node("classify", classify_symptom)
    builder.add_node("general", general_node)
    builder.add_node("emergency", emergency_node)
    builder.add_node("nerve_problem", nerve_problem_node)

    builder.add_edge("get_symptom", "classify")
    builder.add_conditional_edges("classify", symptom_router, {
        "general": "general",
        "emergency": "emergency",
        "nerve_problem": "nerve_problem"
    })

    builder.add_edge("general", END)
    builder.add_edge("emergency", END)
    builder.add_edge("nerve_problem", END)

    graph = builder.compile()

    # --- UI INTERACTION ---
    user_input = st.text_input("Describe your symptom:", placeholder="e.g., I have a sharp pain in my chest")

    if st.button("Check Symptom"):
        if user_input:
            with st.spinner("Analyzing with LangGraph..."):
                # We invoke the graph with the user input already in the state
                final_state = graph.invoke({"symptom": user_input})
                
                # Display results in the UI
                st.divider()
                st.subheader("Agent Evaluation")
                st.write(f"**Classification:** {final_state.get('category')}")
                
                if "emergency" in final_state.get('category', '').lower():
                    st.error(final_state["answer"])
                else:
                    st.success(final_state["answer"])
        else:
            st.warning("Please enter a symptom first.")

else:
    st.warning("Please enter your API Key in the sidebar to activate the agent.")