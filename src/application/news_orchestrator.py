import time # Importe o time para a pausa

class NewsOrchestrator:
    def __init__(self, fetcher, notifier, searcher, summarizer):
        self.fetcher = fetcher
        self.notifier = notifier
        self.searcher = searcher
        self.summarizer = summarizer

    def run_agent(self, topic: str, limit: int = 5):
        print(f"[*] Iniciando NEWS-AGENT para o tema: {topic}")
        urls = self.searcher.search_by_query(topic, limit=limit)
        
        for i, url in enumerate(urls):
            try:
                # 1. Extração
                article = self.fetcher.fetch_article(url)
                
                if article.title and "Google News" not in article.title:
                    print(f"[+] Notícia encontrada: {article.title}")
                    
                    # 2. IA - Resumo Inteligente
                    article.content = self.summarizer.summarize(article.content, topic)
                    
                    # 3. Publicação no Notion
                    self.notifier.send(article)
                    
                    # --- PAUSA ESTRATÉGICA ---
                    # Adicionamos uma pausa de 10 segundos entre as notícias
                    # para não estourar a cota do plano gratuito do Gemini.
                    if i < len(urls) - 1: # Não precisa pausar na última notícia
                        print("[*] Aguardando 10s para respeitar a cota da API...")
                        time.sleep(10)
                
                else:
                    print(f"[-] Pulando link inválido: {url}")
                    
            except Exception as e:
                print(f"[!] Falha ao processar {url}: {e}")