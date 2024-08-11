

from Composite import Composite
from Leaf import Leaf


a = Composite()
b = Composite()
c = Composite()
leaf2 = Leaf()
b.add(leaf2)
a.add(b)
leaf1 = Leaf()
a.add(leaf1)
a.operation()
