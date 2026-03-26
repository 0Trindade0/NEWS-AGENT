# No seu main.py ou orchestrator.py
def run_agent(url_da_noticia: str):
    # 1. Instancia os adaptadores (As ferramentas)
    scraper = NewspaperAdapter()
    notion = NotionAdapter(auth_token="seu_token", database_id="seu_id")
    
    # 2. Executa a extração (Entrada)
    print(f"Buscando notícia em: {url_da_noticia}")
    noticia_extraida = scraper.fetch_article(url_da_noticia)
    
    # 3. Lógica de Negócio (Filtro)
    # Aqui você poderia colocar sua IA para decidir se é relevante
    if "Guerra" in noticia_extraida.title:
        print(f"Notícia relevante encontrada: {noticia_extraida.title}")
        
        # 4. Envia para o Notion (Saída)
        sucesso = notion.send(noticia_extraida)
        
        if sucesso:
            print("Postado no Notion com sucesso!")