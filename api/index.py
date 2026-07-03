import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

def run_scraper_and_analyze():
    """Scrapes data and uses Pandas to perform basic analysis in memory."""
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
        quote_elements = soup.find_all("div", class_="quote")
        
        for element in quote_elements:
            text = element.find("span", class_="text").text.strip()
            author = element.find("small", class_="author").text.strip()
            tags = [tag.text for tag in element.find_all("a", class_="tag")]
            
            quotes_data.append({
                "Quote": text,
                "Author": author,
                "Tags": tags
            })
            
        # 3. Analyze Data with Pandas (Cloud-safe: No saving to hard drive)
        df = pd.DataFrame(quotes_data)
        
        analysis = {
            "total_quotes_scraped": int(len(df)),
            "unique_authors_found": int(df['Author'].nunique()),
            "top_authors": df['Author'].value_counts().to_dict()
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
