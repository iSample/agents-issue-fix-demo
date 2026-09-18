import unittest

from src.greeting import format_greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_has_one_space_after_comma(self):
        self.assertEqual(format_greeting("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
