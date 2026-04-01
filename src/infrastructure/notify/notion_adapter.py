# src/infrastructure/notify/notion_adapter.py
from notion_client import Client
from src.application.ports.notifier_port import NotifierPort
from src.domain.models import NewsArticle

class NotionAdapter(NotifierPort):
    def __init__(self, auth_token: str, database_id: str):
        self.notion = Client(auth=auth_token)
        self.database_id = database_id

    def send(self, article: NewsArticle) -> bool:
        try:
            # 1. Criar a página (Linha na tabela)
            new_page = self.notion.pages.create(
                parent={"database_id": self.database_id},
                properties={
                    # ATENÇÃO: Os nomes abaixo devem ser IGUAIS aos do seu Notion
                    "Título": {"title": [{"text": {"content": article.title[:100]}}]},
                    "Link": {"url": article.url},
                },
                # 2. Adicionar o conteúdo dentro da página (Blocos)
                children=[
                    # Bloco de Imagem (Capa da notícia)
                    {
                        "object": "block",
                        "type": "image",
                        "image": {
                            "type": "external",
                            "external": {"url": article.image_url if article.image_url else "https://via.placeholder.com/800x400?text=Sem+Imagem"}
                        }
                    },
                    # Cabeçalho do conteúdo
                    {
                        "object": "block",
                        "type": "heading_2",
                        "heading_2": {"rich_text": [{"text": {"content": "Resumo da Matéria"}}]}
                    },
                    # Parágrafo de texto (Notion tem limite de 2000 caracteres por bloco)
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{"text": {"content": article.content[:2000]}}]
                        }
                    }
                ]
            )
            print(f"[OK] Notícia enviada ao Notion: {article.title[:50]}...")
            return True
            
        except Exception as e:
            print(f"[!] Erro crítico na API do Notion: {e}")
            return False