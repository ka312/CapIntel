# report_synthesizer.py
import re
from langchain_community.chat_models import ChatOllama
from rich.console import Console
from rich.panel import Panel
from utils import AgentState

console = Console()

def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def report_synthesizer(state: AgentState) -> AgentState:
    console.print(Panel("[bold cyan]Report Synthesizer Agent[/bold cyan] assembling the full due diligence report..."))

    # Prepare contexts, stripping any HTML
    industry = state.get('industry', 'N/A')
    research_raw = state.get('research_data', {}).get('analysis', '')
    research = strip_html(research_raw)
    thesis_raw = state.get('industry_thesis', '')
    thesis = strip_html(thesis_raw)
    companies = state.get('company_profiles', [])
    # Build a clean companies context
    comps_context = "\n".join(
        [f"{strip_html(c.get('name',''))}: {strip_html(c.get('description',''))}" for c in companies]
    )

    llm = ChatOllama(model="mistral", temperature=0.1)
    def ask_llm(title: str, context: str) -> str:
        prompt = f"You're a VC analyst. Given the following context, generate a detailed {title} section in markdown.\n\nContext:\n{context}\n\nOutput:"""
        messages = [{"role": "system", "content": prompt}]
        try:
            resp = llm.invoke(messages)
            return resp.content.strip()
        except Exception:
            return f"Error generating {title}."

    fin = ask_llm("Financial Analysis", comps_context)
    op  = ask_llm("Operational Analysis", comps_context)
    mk  = ask_llm("Market Analysis", research)
    ca  = ask_llm("Competitive Analysis", comps_context)
    lc  = ask_llm("Legal and Regulatory Compliance", research)
    ra  = ask_llm("Risk Assessment", f"{thesis}\n{comps_context}")
    rec = ask_llm("Investment Recommendations", f"{thesis}\n{comps_context}")

    # Combine into report
    report = f"""# Executive Summary
This report presents an investment analysis of the **{industry}** industry using automated agents.

# Industry Analysis
{research}

# Investment Thesis
{thesis}

# Company Profiles
"""
    for c in companies:
        report += f"### {strip_html(c.get('name',''))}\n{strip_html(c.get('description',''))}\n\n"
    report += f"""# Due Diligence Analysis

## Financial Analysis
{fin}

## Operational Analysis
{op}

## Market Analysis
{mk}

## Competitive Analysis
{ca}

## Legal and Regulatory Compliance
{lc}

## Risk Assessment
{ra}

# Investment Recommendations
{rec}

# Appendices
**Glossary**  
VC: Venture Capital  
TAM: Total Addressable Market  
CAC: Customer Acquisition Cost  
LTV: Lifetime Value
"""

    state['due_diligence_report'] = report
    state['current_agent'] = 'done'
    return state
