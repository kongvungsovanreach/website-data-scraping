from urllib.parse import urljoin
from metadata import Metadata
import requests, json
from article import Article

class Engine():
    def __init__(self,
                 base_url=None,
                 keywords=[],
                 per_page=10,
                 search_path=None,
                 payload_path=None,
                 headers_path=None,
                 page_range=()): #article list url (api/web)
        self.base_url=base_url
        self.keywords=keywords
        self.per_page=per_page
        self.search_path=search_path
        self.page_range=page_range
        self.metadata = Metadata(payload_path=payload_path, headers_path=headers_path)
    
    def retrieve_articles_metadata(self):
        full_search_path = urljoin(self.base_url, self.search_path)
        headers = self.metadata.get_header_json()
        payload = self.metadata.get_payload()

        for page in range(self.page_range[0], self.page_range[1]+1):
            print(f'\n[+] scraping on page: {page}/{self.page_range[1]}')
            payload["startNo"] = str(page)
            response = requests.post(full_search_path, json=payload, headers=headers)
            found_articles = response.json()['resultList']
            self.save_search_result_json(found_articles=found_articles, page=page)
            format_articles = self.map_articles(found_articles)
            format_articles_json = [article.to_dict() for article in format_articles]
            self.save_format_result_json(format_articles=format_articles_json, page=page)
            # for article in found_articles:
            #     print(article.url)

    def map_articles(self, response_data: list) -> list:
        """Maps a list of dictionaries to a list of Article instances."""
        articles = [Article.from_dict(item) for item in response_data]
        return articles
    
    def save_format_result_json(self, format_articles, page):
        # Save found_articles as JSON to a file
        save_path=f'./results/format_articles_{page}.json'
        with open(save_path, 'w',encoding='utf-8') as f:
            json.dump(format_articles, f, ensure_ascii=False, indent=4)
        print(f'[+] save format result to JSON file: {save_path}')
    
    def save_search_result_json(self, found_articles, page):
        # Save found_articles as JSON to a file
        save_path=f'./raw_results/found_articles_{page}.json'
        with open(save_path, 'w',encoding='utf-8') as f:
            json.dump(found_articles, f, ensure_ascii=False, indent=4)
        print(f'[+] save raw result to JSON file: {save_path}')
