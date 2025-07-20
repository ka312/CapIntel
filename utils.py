# utils.py
from typing import List, Dict, Any, TypedDict
from datetime import datetime
from langgraph.graph import StateGraph, END
from rich.console import Console

console = Console()

class AgentState(TypedDict):
    industry: str
    messages: List[Dict[str, Any]]
    research_data: Dict[str, Any]
    industry_thesis: str
    company_profiles: List[Dict[str, Any]]
    due_diligence_report: str
    current_agent: str
    status: str

def web_search(query: str, num_results: int = 5) -> List[Dict[str, str]]:
    console.print(f"[bold blue]Searching web for:[/bold blue] {query}")
    try:
        from duckduckgo_search import DDGS
        results = DDGS().text(query, max_results=num_results)
        return [{"title": r.get("title", ""), "body": r.get("body", ""), "href": r.get("href", "")} for r in results]
    except Exception as e:
        console.print(f"[bold yellow]Warning: Rate limit hit or search error. Using fallback data.[/bold yellow]")
        return [{"title": "Search Failed", "body": str(e), "href": ""}]

def get_next_agent(state: AgentState) -> str:
    return {
        'industry_researcher': 'thesis_developer',
        'thesis_developer': 'company_sourcer',
        'company_sourcer': 'due_diligence_analyst',
        'due_diligence_analyst': 'report_synthesizer'
    }.get(state.get('current_agent', ''), END)

def create_workflow(industry: str):
    workflow = StateGraph(AgentState)
    from industry_researcher import industry_researcher
    from thesis_developer import thesis_developer
    from company_sourcer import company_sourcer
    from due_diligence_analyst import due_diligence_analyst
    from report_synthesizer import report_synthesizer
    workflow.add_node("industry_researcher", industry_researcher)
    workflow.add_node("thesis_developer", thesis_developer)
    workflow.add_node("company_sourcer", company_sourcer)
    workflow.add_node("due_diligence_analyst", due_diligence_analyst)
    workflow.add_node("report_synthesizer", report_synthesizer)
    workflow.add_edge("industry_researcher", "thesis_developer")
    workflow.add_edge("thesis_developer", "company_sourcer")
    workflow.add_edge("company_sourcer", "due_diligence_analyst")
    workflow.add_edge("due_diligence_analyst", "report_synthesizer")
    workflow.add_edge("report_synthesizer", END)
    workflow.set_entry_point("industry_researcher")
    return workflow.compile()

def save_report_to_file(report: str, industry: str) -> str:
    filename = f"{industry.replace(' ', '_').lower()}_due_diligence_report.md"
    with open(filename, "w") as f:
        f.write(report)
    return filename
