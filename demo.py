import re
import os
from datetime import datetime

import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from utils import AgentState
from industry_researcher import industry_researcher
from thesis_developer import thesis_developer
from company_sourcer import company_sourcer
from report_synthesizer import report_synthesizer

sns.set_style("whitegrid")

def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)

st.set_page_config(
    page_title="CapIntel",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stButton>button { width: 100%; }
    .report-box { background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }
    .footer { position: fixed; bottom: 0; width: 100%; background-color: #f0f2f6; padding: 1rem; text-align: center; border-top: 1px solid #e0e0e0; }
    </style>
""", unsafe_allow_html=True)

if 'report_history' not in st.session_state:
    st.session_state['report_history'] = []

st.title(":bar_chart: CapIntel")
st.markdown("### Automated venture capital (VC) deal sourcing and due diligence")

with st.sidebar:
    st.header("Report Configuration")
    report_type = st.selectbox(
        "Report Type",
        ["Full Due Diligence", "Industry Analysis", "Company Profile", "Investment Thesis"],
        help="Select the type of report you want to generate"
    )
    industry = st.text_input(
        "Industry",
        placeholder="e.g., Fintech, Healthcare, AI",
        help="Enter the industry you want to analyze"
    )
    st.subheader("Customization Options")
    report_length = st.select_slider(
        "Report Length",
        options=["Concise", "Standard", "Detailed"],
        value="Standard",
        help="Choose the level of detail in the report"
    )
    if report_type == "Full Due Diligence":
        _ = st.checkbox("Include Financial Analysis", value=True)
        _ = st.checkbox("Include Competitor Analysis", value=True)
        _ = st.checkbox("Include Risk Assessment", value=True)
    if report_type in ["Company Profile", "Full Due Diligence"]:
        _ = st.text_input("Company Name (Optional)")
        _ = st.selectbox(
            "Company Stage",
            ["Seed", "Series A", "Series B", "Series C+", "Growth"],
            help="Select the company's funding stage"
        )
    generate_button = st.button("Generate Report", type="primary", use_container_width=True)
    st.markdown("---")
    with st.expander("About CapIntel"):
        st.markdown("""
        CapIntel is an AI-powered platform for VC deal sourcing and due diligence.

        **Features:**
        - Comprehensive industry analysis
        - Detailed company profiles
        - Investment thesis development
        - Risk assessment
        - Financial analysis

        **Report Types:**
        1. **Full Due Diligence**: Complete analysis of companies and industry
        2. **Industry Analysis**: Market trends and opportunities
        3. **Company Profile**: Detailed company analysis
        4. **Investment Thesis**: Strategic investment recommendations
        """)

if generate_button:
    if not industry:
        st.error("Please enter an industry name")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Initialize state as a dict
        state = {
            "industry": industry,
            "messages": [],
            "research_data": {},
            "industry_thesis": "",
            "company_profiles": [],
            "due_diligence_report": "",
            "current_agent": "",
            "status": ""
        }

        # Industry Research
        if report_type in ["Industry Analysis", "Company Profile", "Investment Thesis", "Full Due Diligence"]:
            status_text.text("Running Industry Researcher...")
            state = industry_researcher(state)
            progress_bar.progress(25)

        # Thesis Development
        if report_type in ["Company Profile", "Investment Thesis", "Full Due Diligence"]:
            status_text.text("Running Thesis Developer...")
            state = thesis_developer(state)
            progress_bar.progress(50)

        # Company Sourcing
        if report_type in ["Company Profile", "Full Due Diligence"]:
            status_text.text("Running Company Sourcer...")
            state = company_sourcer(state)
            progress_bar.progress(75)

        # Report Synthesis
        if report_type == "Full Due Diligence":
            status_text.text("Running Report Synthesizer...")
            state = report_synthesizer(state)
            progress_bar.progress(100)

        status_text.text("Done!")

        # Display results
        if report_type == "Industry Analysis":
            raw = state["research_data"].get("analysis", "No analysis available.")
            st.markdown(strip_html(raw))

        elif report_type == "Company Profile":
            profiles = state.get("company_profiles", [])
            if profiles:
                for comp in profiles:
                    st.subheader(comp.get("name", "Unnamed"))
                    st.write(comp.get("description", "No description."))
            else:
                st.warning("No company profiles were generated.")

        elif report_type == "Investment Thesis":
            st.markdown(strip_html(state.get("industry_thesis", "No thesis available.")))

        else:  # Full Due Diligence
            rpt = strip_html(state.get("due_diligence_report", "No report available."))
            st.markdown(rpt)
            # Example chart
            sectors = ['Digital Health', 'Telemedicine', 'Biotech', 'MedTech', 'Health IT']
            allocations = [30, 20, 25, 15, 10]
            fig, ax = plt.subplots()
            ax.pie(allocations, labels=sectors, autopct='%1.1f%%')
            ax.set_title("Suggested Portfolio Allocation")
            st.pyplot(fig)

        # Record history
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        st.session_state['report_history'].append({
            "timestamp": timestamp,
            "industry": industry,
            "type": report_type
        })

# Show history at the bottom
if st.session_state['report_history']:
    st.markdown("---")
    st.subheader("Report History")
    df = pd.DataFrame(st.session_state['report_history'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%d_%H%M%S')
    df = df.sort_values('timestamp', ascending=False)
    st.table(df.rename(columns={'timestamp':'Generated'}))

st.markdown("---")
