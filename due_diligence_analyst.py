# due_diligence_analyst.py
from utils import AgentState, web_search
from langchain_community.chat_models import ChatOllama
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
import re

console = Console()

DUE_DILIGENCE_ANALYST_PROMPT = """
As a senior venture capital due diligence analyst, conduct an exhaustive, investment-grade due diligence analysis...
"""

def due_diligence_analyst(state: AgentState) -> AgentState:
    console.print(Panel(f"[bold yellow]Due Diligence Analyst Agent[/bold yellow] working"))
    text = state['company_profiles'][0]['description']
    company_names = re.findall(r"• Name: ([^\(\n]+)", text)
    llm = ChatOllama(model="mistral", temperature=0.1)
    prompt = DUE_DILIGENCE_ANALYST_PROMPT.format(industry=state['industry'])
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ]
    response = llm.invoke(messages)
    state['due_diligence_report'] = response.content
    state['current_agent'] = 'report_synthesizer'
    return state