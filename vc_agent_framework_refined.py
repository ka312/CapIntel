"""
VC Agent Framework for Deal Sourcing and Due Diligence

This script implements an agentic framework for automating venture capital 
deal sourcing and due diligence processes using open-source LLMs.
"""

import os
import json
import requests  # Used indirectly by dependencies
import argparse
from typing import List, Dict, Any, TypedDict, Annotated, Optional
from datetime import datetime
import time

# Try to import markdown, or install it if missing
try:
    import markdown
except ImportError:
    print("Installing markdown package...")
    import subprocess
    subprocess.check_call(["pip", "install", "markdown"])
    import markdown

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

# For LangGraph components
try:
    from langgraph.graph import StateGraph, END
    try:
        from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
    except ImportError:
        print("Installing langchain_core...")
        import subprocess
        subprocess.check_call(["pip", "install", "langchain_core"])
        from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(["pip", "install", "langgraph", "langchain", "langchain_core"])
    from langgraph.graph import StateGraph, END
    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# For Ollama integration
try:
    from langchain_community.llms import Ollama
    from langchain_community.chat_models import ChatOllama
except ImportError:
    print("Installing Ollama integration...")
    import subprocess
    subprocess.check_call(["pip", "install", "langchain_community"])
    from langchain_community.llms import Ollama
    from langchain_community.chat_models import ChatOllama

# Web search integration
try:
    import duckduckgo_search
except ImportError:
    print("Installing web search capabilities...")
    import subprocess
    subprocess.check_call(["pip", "install", "duckduckgo-search"])
    import duckduckgo_search

# Initialize console for rich output
console = Console()

# Create simple memory storage
# Note: langgraph 0.3+ uses a different mechanism for state persistence
# For this script, we're using a simple dictionary for memory
memory = {}

# State definitions
class AgentState(TypedDict):
    """Define the state for our agent system"""
    industry: str
    messages: List[Dict[str, Any]]
    research_data: Dict[str, Any]
    industry_thesis: str
    company_profiles: List[Dict[str, Any]]
    due_diligence_report: str
    current_agent: str
    status: str
    ollama_url: str

# Agent prompts
INDUSTRY_RESEARCHER_PROMPT = """
You are an expert venture capital industry researcher tasked with conducting a comprehensive analysis of the {industry} industry for investment purposes.

Conduct in-depth research covering:
1. Industry Definition and Market Structure
   - Precise market size with specific numerical data (current and forecasted for 5-10 years)
   - Historical and projected CAGR with exact percentages
   - Key geographic markets with breakdown by region/country (North America, Europe, Asia-Pacific, etc.)
   - Market segmentation (specific sub-sectors and their relative sizes)

2. Competitive Landscape
   - Top 10 companies by market share with exact percentages when available
   - Emerging players and potential disruptors
   - Recent M&A activity with specific transaction values
   - Competitive intensity metrics (HHI index if available)

3. Investment Activity
   - VC funding trends with exact dollar amounts by year/quarter
   - Number of deals by stage (Seed, Series A, B, C+)
   - Average deal sizes with specific figures
   - Most active VC firms in the space with number of investments

4. Technology Trends
   - Key technological developments with expected timeframes for mainstream adoption
   - Patents and IP landscape (number of patents filed by major players)
   - Breakthrough technologies and their projected impact on the market
   - Technology readiness levels for emerging innovations

5. Regulatory Environment
   - Specific regulations affecting the industry by region
   - Pending legislation with potential impacts
   - Compliance costs and regulatory barriers to entry

Use only factual, verifiable data from reputable sources. For all metrics, provide specific numerical values, dates, percentages, and growth rates. Source attribution is essential.

Your analysis must be data-driven, detailed, and include specific companies, technologies, funding amounts, and market metrics. Avoid general statements without supporting data.
"""

THESIS_DEVELOPER_PROMPT = """
As a venture capital strategy expert, develop a comprehensive, data-driven investment thesis for the {industry} industry that would guide a $100M+ fund's investment strategy.

Your investment thesis must include:

1. Market Opportunity Assessment
   - Addressable market size with TAM, SAM, and SOM figures in exact dollar amounts
   - 5-year and 10-year market projections with specific CAGR percentages
   - Detailed analysis of market inflection points with timeline predictions
   - Specific demand drivers with quantifiable impact metrics

2. Value Chain Analysis
   - Complete mapping of the industry value chain with key players at each stage
   - Value distribution analysis (percentage of value captured at each stage)
   - Margin analysis across the value chain with exact percentage figures
   - Identification of bottlenecks and high-value positions

3. Investment Strategy Recommendations
   - Ideal company stage for investment (with specific criteria for each stage)
   - Optimal check size ranges with specific dollar amounts
   - Expected holding periods with specific year ranges
   - Target ROI thresholds with exact multiples and IRR percentages
   - Exit strategy options with historical exit multiple data

4. Sub-Sector Prioritization
   - Ranking of sub-sectors by investment attractiveness with specific scoring criteria
   - Growth rate comparisons with exact CAGR figures
   - Competitive intensity assessment with specific metrics
   - Technological disruption probability by sub-sector

5. Risk Assessment Framework
   - Detailed risk factors with probability and impact matrices
   - Industry-specific risk metrics and KPIs to monitor
   - Sensitivity analysis for key market variables
   - Potential black swan events with mitigation strategies

6. Success Criteria for Portfolio Companies
   - Key technical milestones with specific metrics
   - Financial performance thresholds (revenue growth rates, gross margins, CAC/LTV ratios)
   - Team composition requirements with specific expertise areas
   - Strategic partnership opportunities with named potential partners

Your thesis must be extremely specific, data-driven, and actionable. Include exact figures, percentages, timelines, and named examples throughout. This thesis will be used for actual investment decisions, so it must be comprehensive, detailed and based on robust industry analysis.
"""

COMPANY_SOURCER_PROMPT = """
You are an elite deal sourcer for venture capital with expertise in identifying high-potential companies in the {industry} industry. Based on the industry research and investment thesis, identify 3-5 REAL, SPECIFIC companies that represent prime investment opportunities.

For each company, provide a comprehensive profile including:

1. Company Overview
   - Full legal name and date founded (exact year)
   - Headquarters location and any secondary offices
   - Number of employees (specific range or exact figure)
   - Notable founders and key executives with relevant background details
   - Company website URL

2. Product/Technology Details
   - Detailed technical description of core products/services
   - Key technological differentiators with specific technical advantages
   - Intellectual property position (number of patents, key IP assets)
   - Product development roadmap with specific milestone dates
   - Technical architecture and stack details where relevant

3. Market Position
   - Specific customer segments and use cases
   - Named key clients or customers (at least 3-5 examples)
   - Market share percentage if available
   - Competitive positioning with direct named competitors
   - Growth rate compared to industry average (specific percentage)

4. Financial Profile
   - Total funding raised to date (exact amount)
   - Detailed funding history by round (dates, amounts, lead investors)
   - Revenue figures or estimates (specific ranges at minimum)
   - Burn rate and runway estimates (in months)
   - Unit economics (CAC, LTV, margins) with specific metrics
   - Valuation at last round and valuation methodology

5. Traction and Growth Metrics
   - User/customer growth rates with specific percentages
   - Retention rates with exact figures
   - Revenue growth trajectory with year-over-year percentages
   - Other relevant KPIs specific to their business model with actual metrics

6. Strategic Alignment
   - Specific alignment with investment thesis (reference exact points)
   - Market timing rationale with specific market indicators
   - Potential synergies with existing portfolio companies
   - Clear competitive advantages with quantifiable metrics

Only profile REAL companies that actually exist in this industry, using accurate and specific data. Avoid generic descriptions or hypothetical examples. Each profile should be detailed, data-rich, and demonstrate deep knowledge of the company and its position in the market.
"""

DUE_DILIGENCE_ANALYST_PROMPT = """
As a senior venture capital due diligence analyst, conduct an exhaustive, investment-grade due diligence analysis of each identified company in the {industry} industry. Your analysis must be comprehensive, data-driven, and meet institutional investor standards.

For each company, provide a structured analysis covering:

1. Business Model Analysis
   - Detailed revenue model breakdown with specific revenue streams and their percentage contribution
   - Customer acquisition strategy with specific CAC metrics and channel performance data
   - Unit economics analysis including specific contribution margins, LTV/CAC ratios, and payback periods
   - Operational efficiency metrics (revenue per employee, etc.) compared to industry benchmarks
   - Pricing strategy analysis with specific price points and comparison to competitors

2. Financial Assessment
   - Detailed analysis of financial statements with specific metrics (if available)
   - Revenue growth rates with YoY comparisons and forward projections
   - Gross and net margin analysis with exact percentages
   - Cash flow analysis including burn rate in specific dollar amounts per month
   - Detailed cap table analysis including ownership percentages and dilution scenarios
   - Financing history with specific round sizes, valuations, and investor participation
   - Future funding requirements with specific amounts and timing

3. Market and Competitive Analysis
   - Detailed TAM, SAM, SOM calculations with specific dollar amounts
   - Market penetration percentage and growth potential
   - Competitive landscape mapping with specific market share data where available
   - SWOT analysis with quantifiable metrics for each factor
   - Barriers to entry and company's defensibility with specific examples
   - Customer concentration risk with percentage of revenue from top clients

4. Technology and Product Assessment
   - Technical architecture evaluation with specific strengths and weaknesses
   - Technology stack assessment and scalability analysis
   - Product roadmap evaluation with specific milestone analysis
   - IP portfolio assessment (patents, trade secrets, etc.) with specific counts and quality analysis
   - Technical debt assessment with specific areas of concern
   - R&D efficiency metrics compared to industry standards

5. Team Evaluation
   - Detailed founder background analysis including relevant domain expertise
   - Key executive assessment with specific experience metrics
   - Team composition analysis (technical vs. business, experience distribution)
   - Talent density metrics compared to industry standards
   - Organizational structure analysis and hiring roadmap evaluation
   - Compensation structure analysis relative to market standards
   - Cultural assessment based on specific observable behaviors and practices

6. Risk Assessment and Mitigation
   - Comprehensive risk matrix with probability and impact ratings for each risk
   - Market risks with specific scenario planning
   - Technology risks with detailed technical assessment
   - Team risks with specific gaps or dependencies
   - Regulatory risks with specific regulatory requirements and compliance status
   - Financial risks with detailed runway analysis
   - Competition risks with specific threat assessment from named competitors
   - Detailed mitigation strategies for each identified risk

7. Exit Potential Analysis
   - Specific potential acquirers with strategic rationale for each
   - Historical M&A transactions in the space with specific multiples and deal structures
   - IPO readiness assessment with specific metrics and timeline
   - Comparable exit valuations with detailed multiple analysis
   - Potential exit valuation range with specific methodologies (DCF, comparable transactions, etc.)

8. Investment Recommendation
   - Deal structure recommendation with specific terms
   - Valuation assessment with detailed methodology
   - Investment thesis validation against specific criteria
   - Expected returns calculation with detailed assumptions
   - Ownership target with anti-dilution considerations
   - Board seat and governance recommendations
   - Specific conditions and milestones for investment

Your analysis must be extraordinarily detailed, data-rich, and specifically tailored to each company. Include actual figures, percentages, and metrics throughout. This analysis will be used for actual investment decisions, so it must meet institutional investment standards.
"""

REPORT_SYNTHESIZER_PROMPT = """
As a venture capital investment report synthesizer, create a comprehensive, investment-grade due diligence report for the {industry} industry. This report must be exceptionally detailed, data-driven, and meet the standards expected by institutional investors and investment committees.

Your report must include:

1. Executive Summary (2-3 pages)
   - Industry highlights with specific market size and growth figures
   - Key investment thesis points with specific metrics
   - Top investment opportunities with brief company overviews
   - Summary of due diligence findings with specific strengths/risks
   - Clear investment recommendations with specific expected returns

2. Industry Analysis (5-7 pages)
   - Comprehensive market size and growth metrics with exact figures and sources
   - Detailed competitive landscape with market share data
   - Regulatory environment analysis with specific regulations by region
   - Technology trend analysis with adoption timelines
   - Investment activity metrics with specific funding data by stage and quarter
   - Value chain analysis with margin distribution data

3. Investment Thesis (3-5 pages)
   - Detailed market opportunity assessment with TAM, SAM, SOM figures
   - Value chain positioning strategy with specific target segments
   - Exit landscape analysis with specific potential acquirers and IPO scenarios
   - Risk/return profile with specific metrics and benchmarks
   - Investment criteria with specific thresholds and requirements
   - Portfolio construction recommendations with specific allocation percentages

4. Company Profiles (4-6 pages per company)
   - Comprehensive company overview with founding date, location, team size
   - Founder and key executive backgrounds with relevant experience
   - Detailed product/technology description with specific differentiators
   - Market positioning with specific customer segments and named competitors
   - Traction metrics with specific growth rates, customer counts, retention figures
   - Financial profile with detailed funding history, revenue metrics, burn rate
   - Strategic alignment with investment thesis (specific points of alignment)

5. Due Diligence Analysis (6-8 pages per company)
   - Business model analysis with revenue streams, unit economics, pricing strategy
   - Detailed financial assessment with growth rates, margins, cash flow analysis
   - Market and competitive analysis with TAM calculations and market share data
   - Technology assessment with architecture evaluation, scalability analysis, IP portfolio
   - Team evaluation with domain expertise assessment, organizational structure
   - Comprehensive risk assessment with probability/impact ratings and mitigation strategies
   - Exit potential analysis with specific potential acquirers and valuation ranges

6. Investment Recommendations (3-4 pages)
   - Deal prioritization with specific ranking methodology
   - Recommended deal structures with specific terms
   - Valuation assessment with detailed methodologies and comparable transactions
   - Expected returns with multiple scenarios (base, upside, downside)
   - Portfolio impact analysis with diversification considerations
   - Ownership and governance recommendations
   - Specific conditions and milestones for investment

7. Risk Factors and Mitigation (3-4 pages)
   - Comprehensive risk matrix with impact and probability ratings
   - Industry-specific risks with detailed analysis
   - Company-specific risks with individual assessments
   - Macroeconomic and geopolitical risk factors
   - Detailed mitigation strategies for each key risk
   - Key risk indicators to monitor with specific thresholds

8. Appendices
   - Detailed market data with source attribution
   - Competitive landscape maps and detailed competitor profiles
   - Detailed financial models and projections
   - Technical due diligence deep dives
   - Team assessment details
   - Reference checks summary (if applicable)

Format the report with proper sections, subsections, tables, and data visualization elements. Include specific data points, metrics, figures, percentages, and dollar amounts throughout. The report must be extremely detailed, data-rich, and professional enough to present to an investment committee making multi-million dollar decisions.
"""

# Web search functionality
def web_search(query: str, num_results: int = 5) -> List[Dict[str, str]]:
    """Perform a web search using DuckDuckGo and return results"""
    console.print(f"[bold blue]Searching web for:[/bold blue] {query}")
    
    try:
        # Add delay between requests to avoid rate limiting
        time.sleep(2)  # 2 second delay between requests
        
        results = duckduckgo_search.DDGS().text(query, max_results=num_results)
        return [{"title": r.get("title", ""), "body": r.get("body", ""), "href": r.get("href", "")} 
                for r in results]
    except Exception as e:
        console.print(f"[bold yellow]Warning:[/bold yellow] Rate limit hit or search error. Using fallback data.")
        # Return some fallback data instead of empty results
        return [{
            "title": "Fallback Data",
            "body": f"Using fallback data for query: {query}. Please try again later.",
            "href": ""
        }]

# Agent functions
def industry_researcher(state: AgentState) -> AgentState:
    """Research agent that gathers information about the industry"""
    console.print(Panel(f"[bold cyan]Industry Researcher Agent[/bold cyan] working on {state['industry']}"))
    
    # Perform web search for industry information
    search_query = f"{state['industry']} industry market size growth revenue projections investment trends venture capital funding"
    search_results = web_search(search_query, num_results=15)
    
    # Additional searches for specific data
    market_search = web_search(f"{state['industry']} industry market share top companies competitors", num_results=10)
    funding_search = web_search(f"{state['industry']} venture capital funding deals investment rounds", num_results=10)
    tech_search = web_search(f"{state['industry']} technology trends innovations patents breakthroughs", num_results=10)
    
    # Combine all search results
    all_results = search_results + market_search + funding_search + tech_search
    
    # Format search results
    formatted_results = "\n\n".join([
        f"Source: {result['title']}\nURL: {result['href']}\n\n{result['body']}" 
        for result in all_results
    ])
    
    # Get LLM to analyze the industry based on search results
    prompt = INDUSTRY_RESEARCHER_PROMPT.format(industry=state['industry'])
    
    # Initialize the Ollama model with custom URL
    llm = ChatOllama(
        model="mistral",
        temperature=0.1,
        base_url=state.get('ollama_url', 'http://localhost:11434')
    )
    
    # Generate research analysis
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"Here are web search results about the {state['industry']} industry:\n\n{formatted_results}\n\nBased on these results, provide a comprehensive industry research analysis with specific data, metrics, and figures.")
    ]
    
    response = llm.invoke(messages)
    research_analysis = response.content
    
    # Update state
    state['research_data'] = {
        'raw_search_results': all_results,
        'analysis': research_analysis,
        'timestamp': datetime.now().isoformat()
    }
    
    state['messages'].append({
        "role": "system",
        "content": f"Industry Researcher completed analysis of {state['industry']}"
    })
    
    state['messages'].append({
        "role": "assistant",
        "content": research_analysis
    })
    
    console.print(Markdown("## Industry Research Completed"))
    console.print(Markdown(research_analysis[:500] + "..."))
    
    state['current_agent'] = 'thesis_developer'
    return state

def thesis_developer(state: AgentState) -> AgentState:
    """Develops an investment thesis based on the research"""
    console.print(Panel(f"[bold magenta]Thesis Developer Agent[/bold magenta] working on {state['industry']}"))
    
    research_analysis = state['research_data']['analysis']
    
    # Perform additional searches for thesis development
    investment_search = web_search(f"{state['industry']} industry investment strategy venture capital thesis", num_results=10)
    exit_search = web_search(f"{state['industry']} exit strategies IPO acquisition multiples M&A", num_results=10)
    risk_search = web_search(f"{state['industry']} investment risks challenges regulatory barriers", num_results=10)
    
    # Format additional search results
    additional_info = "\n\n".join([
        f"Source: {result['title']}\nURL: {result['href']}\n\n{result['body']}" 
        for result in investment_search + exit_search + risk_search
    ])
    
    # Initialize the Ollama model
    llm = ChatOllama(model="mistral", temperature=0.1)
    
    # Generate investment thesis
    prompt = THESIS_DEVELOPER_PROMPT.format(industry=state['industry'])
    
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"""
Here is the comprehensive research analysis for the {state['industry']} industry:

{research_analysis}

Additional investment strategy and exit information:

{additional_info}

Based on this information, develop a detailed, data-driven investment thesis for the {state['industry']} industry. 
Include specific metrics, figures, timelines, and actionable investment criteria.
""")
    ]
    
    response = llm.invoke(messages)
    thesis = response.content
    
    # Update state
    state['industry_thesis'] = thesis
    
    state['messages'].append({
        "role": "system",
        "content": f"Thesis Developer completed investment thesis for {state['industry']}"
    })
    
    state['messages'].append({
        "role": "assistant",
        "content": thesis
    })
    
    console.print(Markdown("## Investment Thesis Developed"))
    console.print(Markdown(thesis[:500] + "..."))
    
    state['current_agent'] = 'company_sourcer'
    return state

def company_sourcer(state: AgentState) -> AgentState:
    """Sources potential companies based on the thesis"""
    console.print(Panel(f"[bold green]Company Sourcer Agent[/bold green] working on {state['industry']}"))
    
    # Get necessary information from state
    industry = state['industry']
    thesis = state['industry_thesis']
    
    # Perform web search for companies in the industry
    search_query = f"top {industry} startups companies venture capital funding recent rounds"
    company_results = web_search(search_query, num_results=15)
    
    # Additional targeted searches
    emerging_search = web_search(f"emerging {industry} startups innovative disruptive", num_results=10)
    funding_search = web_search(f"{industry} recent funding rounds series A B C", num_results=10)
    acquisition_search = web_search(f"{industry} startups acquisition targets potential exits", num_results=10)
    
    # Get specific company names from search results
    all_results = company_results + emerging_search + funding_search + acquisition_search
    
    # Extract potential company names from search results
    companies_mentioned = set()
    for result in all_results:
        # This is a simple extraction - in a real system, you'd use NER or similar techniques
        title_words = result['title'].split()
        for i in range(len(title_words) - 1):
            if title_words[i][0].isupper() and title_words[i+1][0].isupper():
                companies_mentioned.add(f"{title_words[i]} {title_words[i+1]}")
    
    # Search for specific details on top companies
    company_details = []
    for company in list(companies_mentioned)[:10]:  # Limit to top 10 mentioned companies
        details = web_search(f"{company} {industry} funding revenue business model", num_results=5)
        company_details.extend(details)
    
    # Format all search results
    formatted_results = "\n\n".join([
        f"Source: {result['title']}\nURL: {result['href']}\n\n{result['body']}" 
        for result in all_results + company_details
    ])
    
    # Initialize the Ollama model
    llm = ChatOllama(model="mistral", temperature=0.2)
    
    # Generate company profiles
    prompt = COMPANY_SOURCER_PROMPT.format(industry=industry)
    
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"""
Industry: {industry}

Investment Thesis:
{thesis}

Web Search Results on Companies:
{formatted_results}

Based on this comprehensive information, identify and profile 3-5 real, specific companies that represent 
strong investment opportunities in the {industry} industry. Provide detailed information on each company 
including founding date, location, funding history, key products, market position, and financial metrics.
""")
    ]
    
    response = llm.invoke(messages)
    company_profiles_text = response.content
    
    # Update state
    company_profiles = [
        {"name": "Detailed Company Profiles", "description": company_profiles_text}
    ]
    
    state['company_profiles'] = company_profiles
    
    state['messages'].append({
        "role": "system",
        "content": f"Company Sourcer identified potential investment targets in {state['industry']}"
    })
    
    state['messages'].append({
        "role": "assistant",
        "content": company_profiles_text
    })
    
    console.print(Markdown("## Company Sourcing Completed"))
    console.print(Markdown(company_profiles_text[:500] + "..."))
    
    state['current_agent'] = 'due_diligence_analyst'
    return state

def due_diligence_analyst(state: AgentState) -> AgentState:
    """Performs due diligence on the sourced companies"""
    console.print(Panel(f"[bold yellow]Due Diligence Analyst Agent[/bold yellow] working"))
    
    # Get necessary information from state
    industry = state['industry']
    thesis = state['industry_thesis']
    company_profiles_text = state['messages'][-1]['content']  # Get the full text from previous step
    
    # Parse company names from the profiles (simple extraction)
    company_names = []
    lines = company_profiles_text.split('\n')
    for line in lines:
        if line.startswith('##') or line.startswith('# '):
            potential_name = line.replace('#', '').strip()
            if len(potential_name) > 0 and potential_name[0].isupper():
                company_names.append(potential_name)
    
    # If no companies were found with the method above, try a different approach
    if not company_names:
        import re
        company_pattern = re.compile(r'(?:Company|1\.|2\.|3\.|4\.|5\.)\s*[:|-]\s*([A-Z][A-Za-z0-9\s]+)')
        matches = company_pattern.findall(company_profiles_text)
        if matches:
            company_names = [match.strip() for match in matches]
    
    # If still no companies found, use some default extraction
    if not company_names:
        # Extract words that start with uppercase letters and are followed by more text
        words = company_profiles_text.split()
        for i in range(len(words) - 1):
            if (len(words[i]) > 1 and words[i][0].isupper() and words[i].lower() not in 
                ['the', 'a', 'an', 'in', 'for', 'of', 'company', 'profile']):
                if i+1 < len(words) and not words[i+1].startswith((':', '-', '.')):
                    potential_name = words[i]
                    if potential_name not in company_names:
                        company_names.append(potential_name)
    
    # Limit to 5 companies
    company_names = company_names[:5]
    
    # Perform detailed research on each company
    company_research = {}
    for company in company_names:
        console.print(f"[bold blue]Researching company:[/bold blue] {company}")
        
        # Business model and products
        business_results = web_search(f"{company} business model revenue products services", num_results=5)
        
        # Financial information
        financial_results = web_search(f"{company} funding financials revenue growth", num_results=5)
        
        # Team information
        team_results = web_search(f"{company} founders CEO executives team leadership", num_results=5)
        
        # Technology information
        tech_results = web_search(f"{company} technology platform architecture patents", num_results=5)
        
        # Market position
        market_results = web_search(f"{company} market share competitors position industry", num_results=5)
        
        # Combine all company research
        all_company_results = business_results + financial_results + team_results + tech_results + market_results
        
        # Format the company research
        company_research[company] = "\n\n".join([
            f"Source: {result['title']}\nURL: {result['href']}\n\n{result['body']}" 
            for result in all_company_results
        ])
    
    # Combine all the research into a structured document
    combined_research = f"# Due Diligence Research for Companies in the {industry} Industry\n\n"
    
    for company, research in company_research.items():
        combined_research += f"## {company}\n\n{research}\n\n---\n\n"
    
    # Initialize the Ollama model
    llm = ChatOllama(model="mistral", temperature=0.1)
    
    # Generate due diligence analysis
    prompt = DUE_DILIGENCE_ANALYST_PROMPT.format(industry=industry)
    
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"""
Industry: {industry}

Investment Thesis:
{thesis[:3000]}... (truncated for brevity)

Company Profiles:
{company_profiles_text}

Additional Company Research:
{combined_research[:15000]}... (truncated for brevity)

Based on all this information, conduct a comprehensive investment-grade due diligence analysis on each company. 
Your analysis should be extremely detailed, with specific metrics, figures, and data-points throughout.
""")
    ]
    
    response = llm.invoke(messages)
    due_diligence_analysis = response.content
    
    # Update state
    state['due_diligence_analysis'] = due_diligence_analysis
    
    state['messages'].append({
        "role": "system",
        "content": f"Due Diligence Analyst completed analysis"
    })
    
    state['messages'].append({
        "role": "assistant",
        "content": due_diligence_analysis
    })
    
    console.print(Markdown("## Due Diligence Analysis Completed"))
    console.print(Markdown(due_diligence_analysis[:500] + "..."))
    
    state['current_agent'] = 'report_synthesizer'
    return state

def report_synthesizer(state: AgentState) -> AgentState:
    """Creates the final due diligence report"""
    console.print(Panel(f"[bold purple]Report Synthesizer Agent[/bold purple] working"))
    
    # Get necessary information from state
    industry = state['industry']
    research_analysis = state['research_data']['analysis']
    thesis = state['industry_thesis']
    company_profiles_text = state['messages'][-3]['content']  # Get company profiles
    due_diligence_analysis = state['messages'][-1]['content']  # Get due diligence analysis
    
    # Perform additional searches for market trends and exit opportunities
    recent_trends = web_search(f"latest {industry} industry trends 2023 2024 forecast", num_results=10)
    exit_opportunities = web_search(f"{industry} M&A activity IPO exits recent acquisitions", num_results=10)
    comparable_deals = web_search(f"{industry} comparable transactions deal multiples valuations", num_results=10)
    
    # Format additional context
    additional_context = "\n\n".join([
        f"Source: {result['title']}\nURL: {result['href']}\n\n{result['body']}" 
        for result in recent_trends + exit_opportunities + comparable_deals
    ])
    
    # Initialize the Ollama model
    llm = ChatOllama(model="mistral", temperature=0.1)
    
    # Generate final report
    prompt = REPORT_SYNTHESIZER_PROMPT.format(industry=industry)
    
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"""
Industry: {industry}

Research Analysis:
{research_analysis[:3000]}... (truncated for brevity)

Investment Thesis:
{thesis[:3000]}... (truncated for brevity)

Company Profiles:
{company_profiles_text[:3000]}... (truncated for brevity)

Due Diligence Analysis:
{due_diligence_analysis[:5000]}... (truncated for brevity)

Additional Market Context:
{additional_context[:3000]}... (truncated for brevity)

Based on all this comprehensive information, synthesize a detailed, investment-grade due diligence report 
that would meet the standards of a professional venture capital firm. Your report should be extremely detailed,
data-rich, and follow the structure outlined in the prompt.
""")
    ]
    
    response = llm.invoke(messages)
    final_report = response.content
    
    # Update state
    state['due_diligence_report'] = final_report
    
    state['messages'].append({
        "role": "system",
        "content": f"Report Synthesizer completed the final due diligence report"
    })
    
    state['messages'].append({
        "role": "assistant",
        "content": final_report
    })
    
    console.print(Markdown("## Final Due Diligence Report Completed"))
    console.print(Markdown(final_report[:1000] + "..."))
    
    state['status'] = 'completed'
    return state

# Set up the LangGraph
def get_next_agent(state: AgentState) -> str:
    """Determine which agent should run next based on current state"""
    current_agent = state.get('current_agent', 'industry_researcher')
    
    if current_agent == 'industry_researcher':
        return 'thesis_developer'
    elif current_agent == 'thesis_developer':
        return 'company_sourcer'
    elif current_agent == 'company_sourcer':
        return 'due_diligence_analyst'
    elif current_agent == 'due_diligence_analyst':
        return 'report_synthesizer'
    else:
        return END

def create_workflow(industry: str, ollama_url: str = 'http://localhost:11434') -> Any:
    """Create the workflow graph for the agent system"""
    # Define the initial state
    initial_state = AgentState(
        industry=industry,
        messages=[],
        research_data={},
        industry_thesis="",
        company_profiles=[],
        due_diligence_report="",
        current_agent="industry_researcher",
        status="in_progress",
        ollama_url=ollama_url
    )
    
    # Create the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("industry_researcher", industry_researcher)
    workflow.add_node("thesis_developer", thesis_developer)
    workflow.add_node("company_sourcer", company_sourcer)
    workflow.add_node("due_diligence_analyst", due_diligence_analyst)
    workflow.add_node("report_synthesizer", report_synthesizer)
    
    # Add edges
    workflow.add_edge("industry_researcher", "thesis_developer")
    workflow.add_edge("thesis_developer", "company_sourcer")
    workflow.add_edge("company_sourcer", "due_diligence_analyst")
    workflow.add_edge("due_diligence_analyst", "report_synthesizer")
    workflow.add_edge("report_synthesizer", END)
    
    # Set the entry point
    workflow.set_entry_point("industry_researcher")
    
    # Compile the workflow
    return workflow.compile()

def save_report_to_file(report: str, industry: str) -> str:
    """Save the due diligence report to a file"""
    filename = f"{industry.replace(' ', '_').lower()}_due_diligence_report.md"
    
    with open(filename, "w") as f:
        f.write(report)
    
    return filename

def main():
    """Main function to run the VC agent framework"""
    parser = argparse.ArgumentParser(description="VC Agent Framework for Deal Sourcing and Due Diligence")
    parser.add_argument("--industry", type=str, required=True, help="Industry to research and analyze")
    parser.add_argument("--ollama-url", type=str, default="http://localhost:11434", 
                       help="URL for Ollama API (default: http://localhost:11434)")
    args = parser.parse_args()
    
    console.print(Panel.fit(
        f"[bold]VC Agent Framework[/bold]\nIndustry: {args.industry}",
        title="Deal Sourcing and Due Diligence Automation",
        border_style="green"
    ))
    
    try:
        # Check if Ollama is running
        try:
            response = requests.get(f"{args.ollama_url}/api/tags")
            if response.status_code != 200:
                raise Exception("Ollama API not responding correctly")
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] Could not connect to Ollama at {args.ollama_url}")
            console.print("Please make sure Ollama is installed and running. You can install it from https://ollama.ai")
            console.print("After installation, run 'ollama serve' in a terminal to start the server.")
            return
        
        # Create the workflow with Ollama URL
        workflow = create_workflow(args.industry, args.ollama_url)
        
        # Execute the workflow
        result = workflow.invoke({
            "industry": args.industry,
            "messages": [],
            "research_data": {},
            "industry_thesis": "",
            "company_profiles": [],
            "due_diligence_report": "",
            "current_agent": "industry_researcher",
            "status": "in_progress",
            "ollama_url": args.ollama_url
        })
        
        # Save the report to a file
        filename = save_report_to_file(result["due_diligence_report"], args.industry)
        
        console.print(f"\n[bold green]Due Diligence Report saved to:[/bold green] {filename}")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        import traceback
        console.print(traceback.format_exc())

if __name__ == "__main__":
    main() 