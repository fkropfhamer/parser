import unittest

from production_rule import ProductionRule
from non_terminal import NonTerminal
from terminal import Terminal

class TestProductionRule(unittest.TestCase):

    def test_init(self):
        production_rule = ProductionRule("left_side", "right_side")
        self.assertEqual(production_rule.left_side, "left_side")
        self.assertEqual(production_rule.right_side, "right_side")

    def test_from_string(self):
        production_rule = ProductionRule.from_string("S -> NP VP")
        self.assertEqual(production_rule.left_side, NonTerminal("S"))
        self.assertEqual(production_rule.right_side, [NonTerminal("NP"), NonTerminal("VP")])

        production_rule = ProductionRule.from_string('N -> "Thomas"')
        self.assertEqual(production_rule.left_side, NonTerminal("N"))
        self.assertEqual(production_rule.right_side, [Terminal("Thomas")])


if __name__ == '__main__':
    unittest.main()

