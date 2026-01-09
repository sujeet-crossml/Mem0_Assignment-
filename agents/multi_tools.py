"""
Agent that intelligently selects ONE tool.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


from cred import gemini_api_key
from tool.math import math_calculator
from tool.date import future_date
from tool.text_analyzer import analyze_text
from tool.weather import get_weather
from prompts import system_prompt

# defining chat model for gemini with api key config
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_api_key,
    temperature = 0
)

# list of tools
tools = [math_calculator, future_date, analyze_text, get_weather]

# creatin agent for model calling with multiple tools
multi_tool_agent = create_agent(
    model = llm,
    tools = tools,
    system_prompt = system_prompt
)
