def generate_citation(paper, format='APA'):
    # Simplified; expand with bibtexparser for real BibTeX
    title = paper['title']
    # Assume we fetch authors/year from API (add parsing)
    if format == 'APA':
        return f"Author. (Year). {title}. arXiv. Retrieved from {paper['pdf_url']}"
    elif format == 'MLA':
        return f"Author. \"{title}.\" arXiv, Year, {paper['pdf_url']}."
    return "Unsupported format"

# Example: cit = generate_citation(paper, 'APA')