# main.py
from industry_researcher import industry_researcher
from thesis_developer import thesis_developer
from company_sourcer import company_sourcer
from due_diligence_analyst import due_diligence_analyst
from report_synthesizer import report_synthesizer
from utils import get_next_agent, create_workflow, save_report_to_file, AgentState
from rich.panel import Panel
import argparse
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="VC Agent Framework for Deal Sourcing and Due Diligence")
    parser.add_argument("--industry", type=str, required=True, help="Industry to research and analyze")
    args = parser.parse_args()

    console.print(Panel.fit(
        f"[bold]VC Agent Framework[/bold]\nIndustry: {args.industry}",
        title="Deal Sourcing and Due Diligence Automation",
        border_style="green"
    ))

    try:
        workflow = create_workflow(args.industry)
        result = workflow.invoke({
            "industry": args.industry,
            "messages": [],
            "research_data": {},
            "industry_thesis": "",
            "company_profiles": [],
            "due_diligence_report": "",
            "current_agent": "industry_researcher",
            "status": "in_progress"
        })
        filename = save_report_to_file(result["due_diligence_report"], args.industry)
        console.print(f"\n[bold green]Due Diligence Report saved to:[/bold green] {filename}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == "__main__":
    main()


# Test runner for industry_researcher.py
# Add this to the end of industry_researcher.py
if __name__ == "__main__":
    from utils import AgentState
    import json

    state = AgentState(
        industry="fintech",
        messages=[],
        research_data={},
        industry_thesis="",
        company_profiles=[],
        due_diligence_report="",
        current_agent="industry_researcher",
        status="in_progress"
    )

    state = industry_researcher(state)
    print("\n\n===== INDUSTRY RESEARCH OUTPUT =====")
    print(json.dumps(state['research_data'], indent=2))


# Test runner for thesis_developer.py
# Add this to the end of thesis_developer.py
if __name__ == "__main__":
    from utils import AgentState
    import json

    state = AgentState(
        industry="fintech",
        messages=[],
        research_data={'analysis': 'Dummy industry research summary goes here...'},
        industry_thesis="",
        company_profiles=[],
        due_diligence_report="",
        current_agent="thesis_developer",
        status="in_progress"
    )

    state = thesis_developer(state)
    print("\n\n===== THESIS OUTPUT =====")
    print(json.dumps(state['industry_thesis'], indent=2))


# Test runner for company_sourcer.py
# Add this to the end of company_sourcer.py
if __name__ == "__main__":
    from utils import AgentState
    import json

    state = AgentState(
        industry="fintech",
        messages=[],
        research_data={},
        industry_thesis="Dummy investment thesis goes here...",
        company_profiles=[],
        due_diligence_report="",
        current_agent="company_sourcer",
        status="in_progress"
    )

    state = company_sourcer(state)
    print("\n\n===== COMPANY PROFILES OUTPUT =====")
    print(json.dumps(state['company_profiles'], indent=2))


# Test runner for due_diligence_analyst.py
# Add this to the end of due_diligence_analyst.py
if __name__ == "__main__":
    from utils import AgentState
    import json

    state = AgentState(
        industry="fintech",
        messages=[],
        research_data={},
        industry_thesis="",
        company_profiles=[{
            "name": "Sample",
            "description": "• Name: Plaid Inc. (Founded: May 2013)\nMore sample profile data here..."
        }],
        due_diligence_report="",
        current_agent="due_diligence_analyst",
        status="in_progress"
    )

    state = due_diligence_analyst(state)
    print("\n\n===== DUE DILIGENCE REPORT OUTPUT =====")
    print(json.dumps(state['due_diligence_report'], indent=2))


# Test runner for report_synthesizer.py
# Add this to the end of report_synthesizer.py
if __name__ == "__main__":
    from utils import AgentState
    import json

    state = AgentState(
        industry="fintech",
        messages=[{"role": "assistant", "content": "Sample company profiles here..."}],
        research_data={"analysis": "Industry analysis content here..."},
        industry_thesis="Investment thesis content here...",
        company_profiles=[{"description": "Company details here..."}],
        due_diligence_report="Due diligence report here...",
        current_agent="report_synthesizer",
        status="in_progress"
    )

    state = report_synthesizer(state)
    print("\n\n===== FINAL REPORT OUTPUT =====")
    print(json.dumps(state['due_diligence_report'], indent=2))
