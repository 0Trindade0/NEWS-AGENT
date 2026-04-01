from abc import ABC, abstractmethod

class SummarizerPort(ABC):
    @abstractmethod
    def summarize(self, text: str, topic: str) -> str:
        """
        Takes raw news content and returns a refined summary focused on the topic.
        """
        pass