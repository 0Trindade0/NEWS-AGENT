import feedparser
from urllib.parse import quote
from googlenewsdecoder import new_decoderv1
from src.application.ports.search_port import NewsSearchPort

class GoogleSearchAdapter(NewsSearchPort):
    def __init__(self):
        # Base URL do Google News RSS em Português/Brasil
        self.base_url = "https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt"

    def search_by_query(self, query: str, limit: int = 5) -> list[str]:
        """
        Busca notícias no Google News e decodifica os links reais.
        """
        encoded_query = quote(query)
        search_url = self.base_url.format(query=encoded_query)

        print(f"[*] Buscando feed: {search_url}")
        feed = feedparser.parse(search_url)
        
        # Seleciona apenas os primeiros resultados baseados no limite
        entries = feed.entries[:limit]
        print(f"[*] Processando {len(entries)} links do Google News...")

        real_urls = []
        for entry in entries:
            url = self._resolve_link(entry.link)
            if url:
                print(f"[DEBUG] URL Decodificada: {url[:60]}...")
                real_urls.append(url)
        
        return real_urls

    def _resolve_link(self, google_url: str) -> str:
        """
        Usa o decodificador para extrair a URL real sem precisar de requests.get.
        """
        try:
            # interval=None desativa o delay entre decodificações (mais rápido para poucos links)
            decoded_link = new_decoderv1(google_url, interval=None)
            
            if decoded_link and decoded_link.get("status"):
                return decoded_link.get("decoded_url")
            return None
        except Exception as e:
            print(f"[!] Erro ao decodificar link: {e}")
            return None
