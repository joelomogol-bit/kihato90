# Web Scraper & Data Analyzer

A lightweight, clean Python automation tool that extracts data from web pages, processes it using Pandas, and structures it into a CSV file.

## Features
- Safe web parsing utilizing `BeautifulSoup`.
- Robust error handling for HTTP timeouts and failures.
- Automated data structuring and analytics reports with `Pandas`.
- Built-in directory protection to safely output data locally.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python scraper.py
   ```

## Output
The script saves a processed dataset to `data/scraped_quotes.csv` containing fields for text contents, specific authors, and categories.
