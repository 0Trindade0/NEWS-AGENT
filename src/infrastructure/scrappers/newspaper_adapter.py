from newspaper import Article
from src.application.ports.fetcher_port import NewsFetcherPort
from src.domain.models import NewsArticle

class NewspaperAdapter(NewsFetcherPort):
    def fetch_article(self, url: str) -> NewsArticle:
        # Cria o objeto de artigo da biblioteca
        article = Article(url, language='pt') 
        
        # Download e Processamento
        article.download()
        article.parse()
        
        # Opcional: article.nlp() -> Extrai palavras-chave e resumo automático
        
        return NewsArticle(
            title=article.title,
            content=article.text,
            url=url,
            image_url=article.top_image  # Pega a imagem principal da matéria
        )