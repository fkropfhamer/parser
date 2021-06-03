from non_terminal import NonTerminal
from terminal import Terminal


class ProductionRule:
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side
    
    @classmethod
    def from_string(cls, string):
        left_side, right_side = string.split("->")

        left_side = left_side.split()

        if len(left_side) > 1:
            raise Exception("rules of type < 2 are not allowed!")

        left_side = NonTerminal(left_side[0])

        right_side = right_side.split()

        right_side = [Terminal(x.replace("'", "").replace('"', "")) if ("'" in x or '"' in x) else NonTerminal(x) for x in right_side]

        return cls(left_side, right_side)



