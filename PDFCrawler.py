from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import validators

class PDFURLCrawler:
    def __init__(self) -> None:
        print("initializing Crawler")
        self.pdfs = set()
        self.hrefs = set()
        self.parsed_urls = set()
    def crawl(self,url, limit, base_url):
            if limit <= 0:
                return self.pdfs
            if validators.url(url):
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                anchor_tags = soup.find_all('a')
                for anchor in anchor_tags:
                    
                    href = anchor.get('href') 
                    # Check if the anchor is not None
                    if href is not None:
                        if '.pdf' in href:
                            if href.startswith('https://'):
                                # print("PDF Found: " + href)
                                self.pdfs.add(href)
                            else:
                                abs_link = urljoin(base_url, href)
                                self.pdfs.add(abs_link)
                                # print("PDF Found without https " + abs_link)
                        if not href.startswith('https://'):
                            if href not in self.hrefs:
                                self.hrefs.add(href)
                                #print("Reference Links:", href)
                                absolute_link = urljoin(base_url, href)
                                self.crawl(absolute_link, limit - 1, base_url)
                        if href.startswith('https://'):
                            self.crawl(href, limit - 1, base_url)
            else:
                print("Stopped because invalid URL")
                print("Problematic URL: ", url)
            return list(set(self.pdfs))

if __name__ == "__main__":
    crawler = PDFURLCrawler()
    pdfs = crawler.crawl(url = "https://www.gmo.com/asia/product-index-page/multi-asset-class/benchmark-free-allocation-strategy/", limit=3, base_url="https://www.gmo.com/")
    print(pdfs)
    
 