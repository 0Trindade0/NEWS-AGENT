class NewsOrchestrator:
    def __init__(self, notifier: NotifierPort):
        self.notifier = notifier # Aqui injetamos qualquer Notifier

    def execute(self, news_list: list[NewsArticle]):
        for news in news_list:
            if news.relevance_score > 0.7: # Exemplo de regra de negócio
                self.notifier.send(news)