from BaseComponent import BaseComponent


class Composite(BaseComponent):


    def add(self, child):
        self.child_components.append(child)

    def remove(self, child):
        self.child_components.remove(child)

    def operation(self):
        # print(len(self.child_components))
        for child in self.child_components:
            child.operation()
