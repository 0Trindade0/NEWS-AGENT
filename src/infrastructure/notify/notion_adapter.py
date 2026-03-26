from notion_client import Client
from src.application.ports.notifier_port import NotifierPort
from src.domain.models import NewsArticle

class NotionAdapter(NotifierPort):
    def __init__(self, auth_token: str, database_id: str):
        self.notion = Client(auth=auth_token)
        self.database_id = database_id

    def send(self, article: NewsArticle) -> bool:
        try:
            self.notion.pages.create(
                parent={"database_id": self.database_id},
                properties={
                    "Título": {"title": [{"text": {"content": article.title}}]},
                    "Link": {"url": article.url},
                    "Relevância": {"number": article.relevance_score}
                },
                children=[
                    {
                        "object": "block",
                        "type": "image",
                        "image": {"type": "external", "external": {"url": article.image_url}}
                    } if article.image_url else {},
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": [{"text": {"content": article.content[:2000]}}]}
                    }
                ]
            )
            return True
        except Exception as e:
            print(f"Erro ao postar no Notion: {e}")
            return False