from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# model setup
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_retries=3,
    timeout=60
)

# 1st agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools= [web_search]
    )

#2nd agent 
def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [web_search, scrape_url]      
    )

# writer chain 
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer, Write clear, structured and insigtful reports."),
    ("human", """Write a detailed research report on the topic below.
    
    Topic: {topic}
    Research Gathered:
     {research}

     Structure the report as:
     - Introduction
     - Key Finding (minimum 3 well-explained points)
     - Conclusion
     - Source (list all URLs found in the research)

     Be detailed, factual and professional."""),    
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evluate it strictly.
     
    Report:
    {report}
    Respond in this exact formats:
     
    Score: X/10
    
    Strengths:
    - ...
    - ...
    Areas to Improve:
    - ...
    - ...
    
    One line verdict:
    ..."""),        
])

critic_chain = critic_prompt | llm | StrOutputParser()

