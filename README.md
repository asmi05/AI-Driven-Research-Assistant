#The following environment is selected: \.venv\Scripts\python.exe
#pip install requests beautifulsoup4 scrapy transformers torch sentence-transformers faiss-cpu bibtexparser
#pip install scholarly
#pip install huggingface_hub[hf_xet]
# In a file test_setup.py
#pip install streamlit requests beautifulsoup4 scrapy transformers torch sentence-transformers faiss-cpu bibtexparser

import requests
from bs4 import BeautifulSoup
from transformers import pipeline

print("Libraries imported successfully!")
