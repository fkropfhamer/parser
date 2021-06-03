import unittest

from terminal import Terminal

class TestTerminal(unittest.TestCase):
    def test_init(self):
        terminal = Terminal("test")
        self.assertEqual(terminal.symbol, "test")

    def test_equals(self):
        terminal1 = Terminal("test")
        terminal2 = Terminal("test")
        terminal3 = Terminal("123")
        self.assertIsNot(terminal1, terminal2)
        self.assertEqual(terminal1, terminal1)
        self.assertEqual(terminal1, terminal2)
        self.assertNotEqual(terminal1, terminal3)


if __name__ == '__main__':
    unittest.main()

