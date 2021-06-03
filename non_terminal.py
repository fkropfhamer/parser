class NonTerminal:
    def __init__(self, name):
        self.name = name


    def __eq__(self, other):
        if isinstance(other, NonTerminal):
            return self.name == other.name
        return False


    def __str__(self):
        return f"NonTerminal ({self.name})"


