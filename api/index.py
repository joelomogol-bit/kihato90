 import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from collections import Counter

app = Flask(__name__)

def run_scraper_and_analyze():
    """Scrapes data and performs basic analysis using lightweight native Python."""
    url = "https://toscrape.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # 1. Fetch data
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 2. Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")
        quotes_data = []
        authors_list = []
        quote_elements = soup.find_all("div", class_="quote")
        
        for element in quote_elements:
            text = element.find("span", class_="text").text.strip()
            author = element.find("small", class_="author").text.strip()
            tags = [tag.text for tag in element.find_all("a", class_="tag")]
            
            authors_list.append(author)
            quotes_data.append({
                "Quote": text,
                "Author": author,
                "Tags": tags
            })
            
        # 3. Analyze Data without Pandas (Lightweight & Vercel Friendly)
        unique_authors = set(authors_list)
        author_counts = dict(Counter(authors_list))
        
        analysis = {
            "total_quotes_scraped": len(quotes_data),
            "unique_authors_found": len(unique_authors),
            "top_authors": author_counts
        }
        
        return {
            "status": "success",
            "analytics": analysis,
            "data": quotes_data
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Web route that triggers when someone visits your Vercel URL
@app.route('/')
def home():
    result = run_scraper_and_analyze()
    return jsonify(result)

# For testing locally on your computer
if __name__ == "__main__":
    app.run(debug=True)
