# src/infrastructure/scrapers/newspaper_adapter.py
from newspaper import Article, Config
from src.application.ports.fetcher_port import NewsFetcherPort
from src.domain.models import NewsArticle

class NewspaperAdapter(NewsFetcherPort):
    def __init__(self):
        # Configuração para simular navegador também no Scraper
        self.config = Config()
        self.config.browser_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    def fetch_article(self, url: str) -> NewsArticle:
        article = Article(url, language='pt', config=self.config)
        
        article.download()
        
        # VERIFICAÇÃO CRÍTICA:
        if not article.html:
            raise Exception("Não foi possível obter o conteúdo (HTML vazio). O site pode estar bloqueando o acesso.")

        article.parse()
        article.nlp()

        return NewsArticle(
            title=article.title,
            content=article.summary if article.summary else article.text[:2000],
            url=url,
            image_url=article.top_image
        )