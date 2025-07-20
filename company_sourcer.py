# company_sourcer.py
from utils import AgentState, web_search
from langchain_community.chat_models import ChatOllama
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
import json
import re

console = Console()

COMPANY_SOURCER_PROMPT = """
You are an elite deal sourcer for venture capital with expertise in identifying high-potential companies in the {industry} industry. Your task is to identify and analyze promising companies that align with the provided investment thesis.

Your output must be a JSON array of company profiles in the following format:
[
  {{
    "name": "Company Name",
    "description": "One-line summary of what the company does, including key metrics, founding year, location, and unique value proposition"
  }},
  ...
]

Focus on companies that:
1. Have demonstrated strong market traction
2. Show innovative technology or business model
3. Have a clear path to scale
4. Align with current market trends
5. Have a strong founding team

Provide at least 5-7 high-quality company profiles that match these criteria.
"""

def company_sourcer(state: AgentState) -> AgentState:
    console.print(Panel(f"[bold green]Company Sourcer Agent[/bold green] working on {state['industry']}"))
    llm = ChatOllama(model="mistral", temperature=0.2)
    prompt = COMPANY_SOURCER_PROMPT.format(industry=state['industry'])
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": state['industry_thesis']}
    ]
    response = llm.invoke(messages)
    
    # Log raw response for debugging
    console.print(Panel(f"[bold yellow]Raw LLM response:[/bold yellow]\n{response.content[:1000]}"))
    
    try:
        # Clean the response content
        cleaned_content = re.sub(r"^```(json)?|```$", "", response.content.strip(), flags=re.MULTILINE)
        parsed = json.loads(cleaned_content)
        
        # Validate JSON structure
        for company in parsed:
            if "name" not in company or "description" not in company:
                raise ValueError(f"Missing required fields in company profile: {company}")
        
        state['company_profiles'] = parsed
    except json.JSONDecodeError as e:
        console.print(Panel(f"[bold red]Error parsing company profiles as JSON: {str(e)}[/bold red]"))
        state['company_profiles'] = [{'name': 'Parsing Error', 'description': response.content}]
    except ValueError as e:
        console.print(Panel(f"[bold red]Error validating company profiles: {str(e)}[/bold red]"))
        state['company_profiles'] = [{'name': 'Validation Error', 'description': str(e)}]
    
    state['current_agent'] = 'due_diligence_analyst'
    return state
