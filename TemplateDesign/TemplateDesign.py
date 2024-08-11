
from abc import ABC, abstractmethod


class TemplateDesign(ABC):

    @abstractmethod
    def get_books(self):
        pass

    @abstractmethod
    def create_notes(self):
        pass

    @abstractmethod
    def practice(self):
        pass

    def create_formula(self):
        print('Create Formula List')

    def study(self):
        self.get_books()
        self.create_notes()
        self.create_formula()
        self.practice()

