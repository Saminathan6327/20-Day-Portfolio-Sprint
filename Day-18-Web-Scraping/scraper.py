import requests
from bs4 import BeautifulSoup

def run_scraper():
    print("\n========================================================")
    print(" 🕷️ WEB SCRAPER: TECH NEWS EXTRACTOR")
    print("========================================================\n")

    # We will use Hacker News (Y Combinator) as it has a very clean, simple HTML structure
    url = "https://news.ycombinator.com/"
    
    print(f"Step 1: Sending HTTP GET request to {url}...")
    try:
        # Pretend to be a normal web browser so the site doesn't block us
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (HTTP Status 200)
        response.raise_for_status() 
        print("-> Connection Successful! HTML downloaded.\n")
        
    except requests.exceptions.RequestException as e:
        print(f"-> ❌ Connection Failed: {e}")
        return

    print("Step 2: Parsing HTML with BeautifulSoup...")
    # Give the raw HTML to BeautifulSoup to organize into a navigable tree
    soup = BeautifulSoup(response.text, 'html.parser')

    print("Step 3: Extracting the Top 10 Headlines...\n")
    print("---------------- TOP TECH NEWS ----------------")
    
    # On Hacker News, the titles are wrapped in a <span> with the class 'titleline'
    # We use soup.find_all() to grab every single one of them!
    story_spans = soup.find_all('span', class_='titleline', limit=10)
    
    for index, span in enumerate(story_spans, start=1):
        # Find the <a> tag inside the span to get the actual text
        link_tag = span.find('a')
        if link_tag:
            headline = link_tag.text
            # We can also grab the URL if we want it!
            # article_url = link_tag['href'] 
            
            print(f"{index}. {headline}")
            
    print("-----------------------------------------------")
    print("\n✅ Scraping Complete!")

if __name__ == "__main__":
    run_scraper()