from serpapi import GoogleSearch

def fetch_snippets(query, api_key):
    """
    Fetches search results from SerpAPI and returns snippets as a single paragraph.
    
    :param query: The search query string.
    :param api_key: SerpAPI key.
    :return: A formatted paragraph containing all snippets.
    """
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    # Extract snippets and join them into a paragraph
    snippets = [i.get("snippet", "") for i in organic_results if "snippet" in i]
    return " ".join(snippets)

api_key = "5b96d07b1e18b3024b85366d7c4ff80f95b274682bdbc328a38d6fe757d164dd"
query = "What is happenning in kerala now"
snippets_paragraph = fetch_snippets(query, api_key)

st.write(snippets_paragraph)
