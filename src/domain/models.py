from dataclasses import dataclass
from typing import Optional

@dataclass
class NewsArticle:
    title: str
    content: str
    url: str
    image_url: Optional[str] = None
    relevance_score: float = 0.0