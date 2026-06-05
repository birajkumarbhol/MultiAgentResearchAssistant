
import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.researcher import ResearchAgent
from agents.analyst import AnalystAgent
from agents.writer import WriterAgent
from agents.memory_agent import MemoryAgent
from agents.reviewer import ReviewerAgent   # ✅ ADDED

st.title("🤖 Multi-Agent Research Assistant")

query = st.text_input("Enter your research topic")

if st.button("Run Research"):

    if not query:
        st.warning("Please enter a topic")
        st.stop()

    # ---------------- INIT AGENTS ----------------
    planner = PlannerAgent()
    search_agent = SearchAgent()
    researcher = ResearchAgent()
    analyst = AnalystAgent()
    writer = WriterAgent()
    reviewer = ReviewerAgent()
    memory = MemoryAgent()

    # ---------------- STEP 1 ----------------
    st.write("🚀 Step 1: Creating plan...")
    plan = planner.create_plan(query)
    st.subheader("📌 Plan")
    st.write(plan)

    # ---------------- STEP 2 ----------------
    st.write("🔍 Step 2: Searching...")
    search_results = search_agent.search(query)
    st.subheader("Search Results")
    st.write(search_results)

    # ---------------- STEP 3 ----------------
    st.write("🧠 Step 3: Researching...")
    research_output = researcher.analyze_search_results(query, search_results)
    st.subheader("Research Output")
    st.write(research_output)

    # ---------------- STEP 4 ----------------
    st.write("📊 Step 4: Analysis...")
    analysis = analyst.analyze(research_output)
    st.subheader("Analysis")
    st.write(analysis)

    # ---------------- STEP 5 ----------------
    st.write("✍️ Step 5: Writing report...")
    report = writer.write_report(analysis)
    st.subheader("Report")
    st.write(report)

    # ---------------- STEP 6 ----------------
    st.write("🧪 Step 6: Reviewing report...")
    final_report = reviewer.review(report)
    st.subheader("Final Reviewed Report")
    st.write(final_report)

    # ---------------- STEP 7 ----------------
    st.write("💾 Step 7: Saving memory...")
    save_msg = memory.save_memory(query, final_report)
    st.success(save_msg)