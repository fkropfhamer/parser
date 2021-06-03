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


    def test_str(self):
        production_rule = ProductionRule.from_string("S -> NP VP")
        self.assertEqual(str(production_rule), "S -> NP VP")


    def test_equals(self):
        production_rule1 = ProductionRule.from_string("S -> NP VP")
        production_rule2 = ProductionRule.from_string("S -> NP VP")
        production_rule3 = ProductionRule.from_string('N -> "Thomas"')

        self.assertIsNot(production_rule1, production_rule2)
        self.assertEqual(production_rule1, production_rule2)
        self.assertEqual(production_rule1, production_rule1)
        self.assertNotEqual(production_rule1, production_rule3)
        

if __name__ == '__main__':
    unittest.main()

