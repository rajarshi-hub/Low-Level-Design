from abc import ABC, abstractmethod

class BaseComponent(ABC):

    def __init__(self):
        self.child_components = []

    @abstractmethod
    def operation(self):
        pass

    def add(self, child):
        NotImplementedError('Function not implemented')
