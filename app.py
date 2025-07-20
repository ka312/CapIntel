import streamlit as st
from report_synthesizer import report_synthesizer
from industry_researcher import industry_researcher
from thesis_developer import thesis_developer
from company_sourcer import company_sourcer
from utils import AgentState
import os
from datetime import datetime
import json
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

st.set_page_config(
    page_title="CapIntel",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .report-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 1rem;
        text-align: center;
        border-top: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

if 'report_history' not in st.session_state:
    st.session_state.report_history = []

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
        include_financials = st.checkbox("Include Financial Analysis", value=True)
        include_competitors = st.checkbox("Include Competitor Analysis", value=True)
        include_risks = st.checkbox("Include Risk Assessment", value=True)

    if report_type in ["Company Profile", "Full Due Diligence"]:
        company_name = st.text_input("Company Name (Optional)")
        company_stage = st.selectbox(
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

        state = AgentState(
            industry=industry,
            messages=[],
            research_data={},
            industry_thesis="",
            company_profiles=[],
            due_diligence_report="",
            current_agent="industry_researcher",
            status="in_progress"
        )

        progress_bar.progress(10)
        status_text.text("Running industry researcher agent...")
        state = industry_researcher(state)

        progress_bar.progress(40)
        status_text.text("Running thesis developer agent...")
        state = thesis_developer(state)

        progress_bar.progress(60)
        status_text.text("Running company sourcer agent...")
        state = company_sourcer(state)

        progress_bar.progress(80)
        status_text.text("Synthesizing final report...")
        state = report_synthesizer(state)

        os.makedirs('reports', exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename_md = f'reports/venture_capital_report_{timestamp}.md'

        with open(filename_md, 'w', encoding='utf-8') as f:
            f.write(state['due_diligence_report'])

        charts_dir = 'reports/charts'
        os.makedirs(charts_dir, exist_ok=True)

        portfolio_chart = f'{charts_dir}/portfolio_{timestamp}.png'
        fig, ax = plt.subplots(figsize=(10, 6))
        sectors = ['Digital Health', 'Telemedicine', 'Biotech', 'MedTech', 'Health IT']
        allocations = [30, 20, 25, 15, 10]
        colors = sns.color_palette("husl", len(sectors))
        ax.pie(allocations, labels=sectors, autopct='%1.1f%%', colors=colors)
        ax.set_title("Suggested Portfolio Allocation", pad=20)
        plt.savefig(portfolio_chart, bbox_inches='tight', dpi=300)
        plt.close()

        growth_chart = f'{charts_dir}/growth_{timestamp}.png'
        fig, ax = plt.subplots(figsize=(10, 6))
        years = list(range(2020, 2025))
        growth_rates = [15, 18, 22, 25, 28]
        sns.lineplot(x=years, y=growth_rates, marker='o', linewidth=2)
        ax.set_title("Projected Market Growth Rate (%)")
        ax.set_xlabel("Year")
        ax.set_ylabel("Growth Rate (%)")
        plt.savefig(growth_chart, bbox_inches='tight', dpi=300)
        plt.close()

        pdf_content = state['due_diligence_report'].encode('utf-8')

        progress_bar.progress(100)
        status_text.text("Report generated successfully!")

        report_entry = {
            "timestamp": timestamp,
            "industry": industry,
            "type": report_type,
            "filename": filename_md,
            "charts": [portfolio_chart, growth_chart]
        }
        st.session_state.report_history.append(report_entry)

        st.success(f"Report generated successfully! Saved to: {filename_md}")

        st.markdown("### Generated Report")
        with st.expander("View Report", expanded=True):
            st.markdown(state['due_diligence_report'])
            col1, col2 = st.columns(2)
            with col1:
                st.image(portfolio_chart, caption="Portfolio Allocation")
            with col2:
                st.image(growth_chart, caption="Market Growth Projection")

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="Download as Markdown",
                data=state['due_diligence_report'],
                file_name=f"vc_report_{industry}_{timestamp}.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col2:
            st.download_button(
                label="Download as PDF",
                data=pdf_content,
                file_name=f"vc_report_{industry}_{timestamp}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

if st.session_state.report_history:
    st.markdown("---")
    st.subheader("Report History")
    history_df = pd.DataFrame(st.session_state.report_history)
    history_df['timestamp'] = pd.to_datetime(history_df['timestamp'], format='%Y%m%d_%H%M%S')
    history_df = history_df.sort_values('timestamp', ascending=False)

    for _, row in history_df.iterrows():
        with st.expander(f"{row['type']} - {row['industry']} ({row['timestamp'].strftime('%Y-%m-%d %H:%M')})"):
            st.markdown(f"**Industry:** {row['industry']}")
            st.markdown(f"**Type:** {row['type']}")
            st.markdown(f"**Generated:** {row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            st.markdown(f"**File:** {row['filename']}")

            if 'charts' in row and row['charts']:
                st.markdown("### Visualizations")
                cols = st.columns(len(row['charts']))
                for idx, chart in enumerate(row['charts']):
                    if os.path.exists(chart):
                        with cols[idx]:
                            st.image(chart)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("View Report", key=f"view_{row['timestamp']}"):
                    with open(row['filename'], 'r', encoding='utf-8') as f:
                        st.markdown(f.read())
            with col2:
                with open(row['filename'], 'r', encoding='utf-8') as f:
                    st.download_button(
                        "Download",
                        f.read(),
                        file_name=os.path.basename(row['filename']),
                        key=f"download_{row['timestamp']}"
                    )

st.markdown("---")
