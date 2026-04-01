import os
from dotenv import load_dotenv

from src.infrastructure.scrapers.newspaper_adapter import NewspaperAdapter
from src.infrastructure.scrapers.google_search_adapter import GoogleSearchAdapter
from src.infrastructure.notify.notion_adapter import NotionAdapter
from src.infrastructure.ai.gemini_adapter import GeminiAdapter
from src.application.news_orchestrator import NewsOrchestrator

load_dotenv()

def main():
    # Infraestrutura
    fetcher = NewspaperAdapter()
    searcher = GoogleSearchAdapter()
    summarizer = GeminiAdapter(api_key=os.getenv("GEMINI_API_KEY"))
    notifier = NotionAdapter(
        auth_token=os.getenv("NOTION_TOKEN"),
        database_id=os.getenv("NOTION_DATABASE_ID")
    )

    # Aplicação
    agent = NewsOrchestrator(fetcher, notifier, searcher, summarizer)
    agent.run_agent("Guerra Estados Unidos e Irã", limit=3)

if __name__ == "__main__":
    main()