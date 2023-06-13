import textwrap
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def get_sublinks(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    html_soup = BeautifulSoup(html, "html.parser")
    anchor_tags = html_soup.find_all('a')
    sublinks = [urljoin(url, anchor['href']) for anchor in anchor_tags if 'href' in anchor.attrs]
    return sublinks

def get_text(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    html_soup = BeautifulSoup(html, "html.parser")
    text = html_soup.get_text()
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    wrapped_text = textwrap.fill(text, width=80, initial_indent="    ", subsequent_indent="    ")
    with open("output.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(wrapped_text)
        
coindesk_url = "https://www.coindesk.com/"
articles_url = get_sublinks(coindesk_url)
for article in articles_url:
    get_text(article)