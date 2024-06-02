from abc import ABC, abstractmethod

from .newsletter import Newsletter


class NewsletterRepository(ABC):

    @abstractmethod
    def save(self, newsletter: Newsletter):
        pass
