import streamlit as st
from serpapi import GoogleSearch

def fetch_snippets_with_linked_sources(query, api_key):
    params = {"engine": "google", "q": query, "api_key": api_key}
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])
    
    snippets_with_sources = []
    
    for i in organic_results:
        snippet = i.get("snippet", "")
        source = i.get("source", "Unknown Source")
        link = i.get("link", "#")
        
        if snippet:
            # Format the source as a clickable link (Markdown format)
            linked_source = f"[{source}]({link})"
            snippets_with_sources.append(f"{snippet} ({linked_source})")

    return " ".join(snippets_with_sources)
    
api_key = st.secrets["API_KEY"]
query = "What is the latest improvements in Tesla Bots?"
snippets_paragraph = fetch_snippets_with_sources(query, api_key)

st.write(snippets_paragraph)
