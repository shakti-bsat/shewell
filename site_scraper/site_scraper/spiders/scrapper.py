import scrapy
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class SairamSpider(scrapy.Spider):
    name = "sairam"
    allowed_domains = ["shewellofficial.com"]
    start_urls = ["https://www.shewellofficial.com/"]

    visited_urls = set()

    def parse(self, response):
        # Avoid revisiting same URL
        if response.url in self.visited_urls:
            return

        self.visited_urls.add(response.url)

        # Remove script and style elements
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Extract clean text
        text_content = soup.get_text(separator=" ", strip=True)

        # Extract title
        title = soup.title.string if soup.title else "No Title"

        yield {
            "url": response.url,
            "title": title,
            "content": text_content
        }

        # Follow internal links only
        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(response.url, link["href"])

            if absolute_url.startswith("https://www.shewellofficial.com/"):
                yield scrapy.Request(absolute_url, callback=self.parse)