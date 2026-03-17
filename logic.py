import os
from google import genai
from ddgs import DDGS  
import streamlit as st


def get_gemini_client():
    api_key = st.secrets['GEMINI_API_KEY']
    if not api_key:
        raise ValueError("Missing API Key! Check your .env file.")
    return genai.Client(api_key=api_key)

def verify_news_with_gemini(news_text):
   
    client = get_gemini_client()
    
    print(f"Searching for: {news_text[:30]}...")
    search_results = []
    
    try:
        ddgs = DDGS()
        results = list(ddgs.text(f"{news_text} fact check", max_results=5))
        
        if not results:
            results = list(ddgs.text(news_text, max_results=5))
            
        if results:
            for i, res in enumerate(results, 1):
                title = res.get('title', 'Unknown')
                href = res.get('href', '#')
                body = res.get('body', '')
                search_results.append(f"SOURCE {i}: {title}\nURL: {href}\nTEXT: {body}\n")
        else:
            search_results.append("No direct web results found. Analyze based on general knowledge.")
            
        search_context = "\n".join(search_results)
        
    except Exception as e:
        print(f"Search failed: {e}")
        search_context = f"Search tool error: {str(e)}"

    prompt = f"""
    You are an expert fact-checker for Indian news.
    
    USER CLAIM: "{news_text}"
    
    EVIDENCE FROM WEB:
    {search_context}
    
    INSTRUCTIONS:
    1. Compare the claim against the evidence.
    2. If the user input is in Hindi/Tamil/etc, REPLY IN THAT SAME LANGUAGE.
    3. Output Format:
       - **VERDICT:** (Fake / Real / Misleading)
       - **EXPLANATION:** (Short summary of why)
       - **EVIDENCE:** (Cite the Source numbers)
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt
        )
        return response.text, search_results

    except Exception as e:
        return f"API Error: {str(e)}", []