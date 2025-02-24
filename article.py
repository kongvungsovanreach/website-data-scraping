class Article:
    def __init__(self, title: str, category: str, url: str, date: str, provider: str, content: str):
        self.title = title
        self.category = category
        self.url = url
        self.date = date
        self.provider = provider
        self.content = content
    
    def __repr__(self):
        return f"Article(TITLE={self.title}, CATEGORY={self.category}, URL={self.url}, DATE={self.date}, PROVIDER={self.provider}, CONTENT={self.content[:50]}...)"

    @classmethod
    def from_dict(cls, data: dict):
        """Create an Article instance from a dictionary."""
        return cls(
            title=data.get("TITLE"),
            category=data.get("CATEGORY_NAMES"),
            url=f'https://www.bigkinds.or.kr/v2/news/newsDetailView.do?newsId={data.get("NEWS_ID")}',
            date=data.get("DATE"),
            provider=data.get("PROVIDER"),
            content=data.get("CONTENT")
        )
    
    def to_dict(self):
        """Converts the Article object to a dictionary (JSON-compatible)."""
        return {
            "TITLE": self.title,
            "CATEGORY_NAMES": self.category,
            "URL": self.url,
            "DATE": self.date,
            "PROVIDER": self.provider,
            "CONTENT": self.content
        }