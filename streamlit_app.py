import streamlit as st
from serpapi import GoogleSearch

def fetch_snippets_with_sources(query, api_key):
    params = {"engine": "google", "q": query, "api_key": api_key}
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])
    
    snippets = [i.get("snippet", "") for i in organic_results if "snippet" in i]
    sources = [i.get("source", "Unknown Source") for i in organic_results if "source" in i]

    snippets_text = " ".join(snippets)
    sources_text = "Sources: " + ", ".join(set(sources)) if sources else "Sources: None"

    return f"{snippets_text}\n\n{sources_text}"

api_key = st.secrets["API_KEY"]
query = "What is the latest improvements in Tesla Bots?"
snippets_paragraph = fetch_snippets(query, api_key)

st.write(snippets_paragraph)
