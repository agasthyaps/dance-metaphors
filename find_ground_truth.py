from googlesearch import search
import requests
from bs4 import BeautifulSoup
import pandas as pd

# queries
queries_blog = [
"structure of atom explanation",
"global financial markets explanation",
"how large language models work explanation",
"geopolitics in the modern age explanation"
]

# List of dance related words
dance_words = ["dance", "dances", "dancing", "danced", "waltz", "waltzes", "waltzing", "waltzed", "ballet"]

# get the urls to the top ten hits
def get_urls(query_list, n_urls = 10):
    links = []
    topics = []
    for query in query_list:
        for result in search(query, num=n_urls, stop=n_urls,pause=2):
            links.append(result)
            topics.append(query)
    link_df = pd.DataFrame({'topic':topics,'url':links})
    return link_df

# Function to fetch and parse content from a URL
def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Function to count dance related words in text
def count_key_words(content, key_words):
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator=' ').lower().strip()
    print(text)
    return sum(any(word in text for word in key_words) for word in key_words)

# Function to count dance related words in text
def raw_text(content):
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator=' ').lower().strip()
    # print(text)
    return text


# DO IT
found_links = get_urls(queries_blog, n_urls=100)
print("got urls")

raws = []
for url in found_links.loc[:,'url']:
    content = fetch_url_content(url)
    if content:
        raw_txt = raw_text(content)
    else:
        raw_txt = "ERROR"
    raws.append(raw_txt)

found_links['raw_text'] = raws
found_links.to_csv('raw_text.csv', index=False)
