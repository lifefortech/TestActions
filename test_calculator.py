import unittest

from calculator import add, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
