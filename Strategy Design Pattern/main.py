from Fielders import Fielder

import CatchingStartegy as catching_strategy

fielder1 = Fielder(catching_strategy.KangarooCatchingStrategy())
fielder2 = Fielder(catching_strategy.ReverseCupCatchingStrategy())
fielder3 = Fielder(catching_strategy.CupHandCatchingStrategy())
fielder4 = Fielder(catching_strategy.KangarooCatchingStrategy())
fielders = [fielder2, fielder1, fielder3,fielder4]

for fielder in fielders:
    fielder.catch()
