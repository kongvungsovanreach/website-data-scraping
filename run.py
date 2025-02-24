from engine import Engine

#scrapping metadata
base_url = 'https://www.bigkinds.or.kr'
keywords = [] #not yet implement
per_page = 50
search_path = 'api/news/search.do'
payload_path='./meta/payload.json'
headers_path='./meta/headers.txt'
page_range=(301,400)

if __name__ == '__main__':
    #engine declaration
    engine = Engine(
        base_url=base_url,
        keywords=keywords,
        per_page=per_page,
        search_path=search_path,
        payload_path=payload_path,
        headers_path=headers_path,
        page_range=page_range
    )

    engine.retrieve_articles_metadata()