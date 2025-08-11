import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote

def search_arxiv(query, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=all:{quote(query)}&start=0&max_results={max_results}"
    response = requests.get(base_url + search_query)
    root = ET.fromstring(response.content)
    
    results = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        pdf_url = [link.get('href') for link in entry.findall('{http://www.w3.org/2005/Atom}link') if link.get('title') == 'pdf'][0]
        results.append({'title': title, 'summary': summary, 'pdf_url': pdf_url})
    return results

# Example: papers = search_arxiv("agentic AI")