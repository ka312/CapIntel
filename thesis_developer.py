# thesis_developer.py
from utils import AgentState, web_search
from langchain_community.chat_models import ChatOllama
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown

console = Console()

THESIS_DEVELOPER_PROMPT = """
As a venture capital strategy expert, develop a comprehensive, data-driven investment thesis for the {industry} industry. Your investment thesis should include:

1. Key macroeconomic drivers
2. Market gaps or inefficiencies
3. Emerging sub-sectors or themes
4. Risk factors and barriers to entry
5. Strategic investment rationale

Include data points, growth metrics, and potential portfolio strategies.

Format your response in clear markdown with appropriate headings and bullet points.
"""

def thesis_developer(state: AgentState) -> AgentState:
    console.print(Panel(f"[bold magenta]Thesis Developer Agent[/bold magenta] working on {state['industry']}"))
    
    # Safely get research analysis with fallback
    research_analysis = state.get('research_data', {}).get('analysis', 'No research data provided.')
    
    llm = ChatOllama(model="mistral", temperature=0.1)
    prompt = THESIS_DEVELOPER_PROMPT.format(industry=state['industry'])
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": research_analysis}
    ]
    
    response = llm.invoke(messages)
    
    # Log preview of the response
    console.print(Markdown(f"**Thesis Output Preview:**\n\n{response.content[:500]}..."))
    
    # Clean and store the response
    cleaned_response = response.content.strip()
    state['industry_thesis'] = cleaned_response
    
    state['current_agent'] = 'company_sourcer'
    return state
