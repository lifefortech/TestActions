import unittest

<<<<<<< HEAD
from calculator import add, is_equal, multiply, subtract
=======
from calculator import add, divide, multiply, subtract
>>>>>>> origin/main


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

<<<<<<< HEAD
    def test_is_equal(self) -> None:
        self.assertTrue(is_equal(2, 2))
        self.assertFalse(is_equal(3, 4))
=======
    def test_divide(self) -> None:
        self.assertEqual(divide(2, 1), 2)
        self.assertEqual(divide(6, 3), 2)
>>>>>>> origin/main


if __name__ == "__main__":
    unittest.main()
