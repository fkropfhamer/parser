import unittest

from non_terminal import NonTerminal

class TestNonTerminal(unittest.TestCase):
    def test_init(self):
        non_terminal = NonTerminal("TEST")
        self.assertEqual(non_terminal.name, "TEST")

    def test_equals(self):
        non_terminal1 = NonTerminal("TEST")
        non_terminal2 = NonTerminal("TEST")
        non_terminal3 = NonTerminal("NOT_TEST")
        self.assertIsNot(non_terminal1, non_terminal2)
        self.assertEqual(non_terminal1, non_terminal1)
        self.assertEqual(non_terminal1, non_terminal2)
        self.assertNotEqual(non_terminal1, non_terminal3)


    def test_str(self):
        non_terminal = NonTerminal("TEST")

        self.assertEqual(str(non_terminal), 'NonTerminal ("TEST")')


if __name__ == '__main__':
    unittest.main()

