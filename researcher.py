import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

INTERNAL_NOTES = """
- Marketing: We ran an unscheduled 'Flash Sale' campaign in June that cost $15,000.
- Cloud Infrastructure: AWS increased prices for GPU instances by 25% starting this month.
- Travel: The Sales team attended an unplanned conference in Dubai.
"""

class ResearchAgent:
    def __init__(self, api_key):
        # Using Llama 3.3 70B on Groq for high-speed, intelligent reasoning
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile", 
            groq_api_key=api_key,
            temperature=0
        )

    def explain_variance(self, category, amount):
        prompt = ChatPromptTemplate.from_template("""
        You are a Corporate Finance Researcher. 
        Category: {category}
        Over-budget Amount: ${amount}
        
        Reference the internal notes below to find the specific reason:
        {notes}
        
        Provide a concise, professional explanation for the CFO.
        """)
        
        chain = prompt | self.llm
        response = chain.invoke({"category": category, "amount": amount, "notes": INTERNAL_NOTES})
        return response.content