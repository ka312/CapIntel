# industry_researcher.py
import re
from utils import AgentState, web_search
from langchain_community.chat_models import ChatOllama
from rich.panel import Panel
from rich.console import Console

console = Console()

INDUSTRY_RESEARCHER_PROMPT = """
You are an expert venture capital industry researcher tasked with conducting a comprehensive analysis of the {industry} industry for investment purposes.

Provide a structured and detailed industry analysis including:
1. Market size and growth metrics (with sources and exact figures)
2. Key trends and drivers shaping the industry
3. Emerging opportunities and white spaces
4. Challenges and barriers to entry
5. Funding trends and VC activity (by stage and geography)
6. Major players and competitive landscape
7. Regulatory and geopolitical environment
8. Technology adoption timelines and innovation roadmaps

Format your response in professional markdown with sections, bullet points, and data references. Cite estimated figures and sources where relevant.
"""

def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def industry_researcher(state: AgentState) -> AgentState:
    console.print(Panel(f"[bold cyan]Industry Researcher Agent[/bold cyan] working on {state['industry']}"))
    query = f"{state['industry']} industry market size growth revenue projections investment trends venture capital funding"
    results = web_search(query, num_results=15)

    if not results:
        console.print("[red]No search results returned.[/red]")
        state['research_data'] = {"analysis": "No data found."}
        state['status'] = 'completed'
        return state

    cleaned_snippets = []
    for r in results:
        title = strip_html(r.get('title', ''))
        body  = strip_html(r.get('body',  ''))
        href  = r.get('href',       '')
        cleaned_snippets.append(f"Source: {title}\nURL: {href}\n\n{body}")
    formatted = "\n\n".join(cleaned_snippets)

    llm = ChatOllama(model="mistral", temperature=0.1)
    prompt = INDUSTRY_RESEARCHER_PROMPT.format(industry=state['industry'])
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user",   "content": formatted}
    ]

    try:
        response = llm.invoke(messages)
        analysis = response.content
    except Exception as e:
        console.print(f"[red]LLM failed: {e}[/red]")
        analysis = "LLM failed to generate analysis."

    state['research_data'] = {"analysis": analysis}
    state['current_agent'] = 'thesis_developer'
    state['status'] = 'completed'
    return state