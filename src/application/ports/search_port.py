from abc import ABC, abstractmethod

class NewsSearchPort(ABC):
    @abstractmethod
    def search_by_query(self, query: str, limit: int = 5) -> list[str]:
        """Retorna uma lista de URLs baseada em um termo de busca."""
        pass