from abc import ABC, abstractmethod
from src.domain.models import NewsArticle

class NotifierPort(ABC):
    @abstractmethod
    def send(self, article: NewsArticle) -> bool:
        """Envia uma notícia para um destino externo."""
        pass