import unittest

from calculator import add, is_equal, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_is_equal(self) -> None:
        self.assertTrue(is_equal(2, 2))
        self.assertFalse(is_equal(3, 4))


if __name__ == "__main__":
    unittest.main()
