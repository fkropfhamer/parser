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

    def __str__(self):
        right_side_string = ' '.join([f'"{x.symbol}"' if isinstance(x, Terminal) else x.name for x in self.right_side])

        return f'{self.left_side.name} -> {right_side_string}'


    def __eq__(self, other):
        if isinstance(other, ProductionRule):
            return (self.left_side == other.left_side) and (self.right_side == other.right_side)

        return False
