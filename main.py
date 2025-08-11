from searcher import search_arxiv
from summarizer import summarize_text
from vector_db import build_vector_db, suggest_related
from citer import generate_citation

def run_research_agent(query):
    papers = search_arxiv(query)
    for p in papers:
        p['short_summary'] = summarize_text(p['summary'])
        p['citation'] = generate_citation(p)
    
    index, embeddings, _ = build_vector_db(papers)
    suggestions = suggest_related(query + " related topics", index, embeddings, papers)
    
    output = {
        'results': papers,
        'suggestions': suggestions
    }
    return output

# Run: result = run_research_agent("agentic AI applications")
# Print or display results