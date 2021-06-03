class Terminal:
    def __init__(self, symbol):
        self.symbol = symbol
    

    def __eq__(self, other):
        if isinstance(other, Terminal):
            return self.symbol == other.symbol

        return False


    def __str__(self):
        return f"Terminal ({self.symbol})"

