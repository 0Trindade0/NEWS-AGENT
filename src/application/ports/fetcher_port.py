from abc import ABC, abstractmethod
from src.domain.models import NewsArticle

class NewsFetcherPort(ABC):
    @abstractmethod
    def fetch_article(self, url: str) -> NewsArticle:
        """Extrai conteúdo e imagem de uma URL específica."""
        pass