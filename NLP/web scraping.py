#web scraping

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Base URL
BASE_URL = "https://indianexpress.com"

# Headers for polite scraping
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}

def get_homepage_soup():
    """Fetches and parses the Indian Express homepage HTML."""
    try:
        response = requests.get(BASE_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching homepage: {e}")
        return None

def extract_article_links(soup):
    """Extracts article titles and links from homepage soup."""
    links_seen = set()
    articles = []

    # Top stories sections 
    for tag in soup.find_all('a', href=True):
        title = tag.get_text(strip=True)
        link = tag['href']

        if (title and "/article/" in link and link.startswith("https://")) and link not in links_seen:
            links_seen.add(link)
            articles.append((title, link))

        if len(articles) >= 30:
            break

    return articles[:30]

def fetch_article_text(url):
    """Fetches the full text of a news article given its URL."""
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Indian Express typically uses this class for paragraphs
        content_div = soup.find('div', class_='full-details')
        if not content_div:
            content_div = soup.find('div', class_='articles')

        if content_div:
            paragraphs = content_div.find_all('p')
            full_text = '\n'.join(p.get_text(strip=True) for p in paragraphs)
            return full_text.strip()

        return "No content found."
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article {url}: {e}")
        return "Failed to fetch article."

def main():
    print("Scraping Indian Express homepage...")
    soup = get_homepage_soup()
    if not soup:
        return

    print("Extracting article links...")
    articles = extract_article_links(soup)

    data = []
    print(f"Found {len(articles)} articles. Extracting full texts...\n")

    for idx, (title, link) in enumerate(articles, start=1):
        print(f"[{idx}] Scraping: {title}")
        full_text = fetch_article_text(link)
        data.append({
            'NEWS_TITLE': title,
            'NEWS_LINK': link,
            'FULL_SCRAPED_TEXT': full_text
        })
        time.sleep(random.uniform(1, 3))  # Polite delay

    # Create DataFrame
    df = pd.DataFrame(data, columns=["NEWS_TITLE", "NEWS_LINK", "FULL_SCRAPED_TEXT"])

    # Save to CSV
    df.to_csv("indian_express_news.csv", index=False, encoding='utf-8')
    print("\n✅ Scraping completed. Data saved to 'indian_express_news.csv'.")

if __name__ == "__main__":
    main()