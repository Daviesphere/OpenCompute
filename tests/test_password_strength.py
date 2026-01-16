import unittest

from scripts.password_strength import check_strength


class TestPasswordStrength(unittest.TestCase):
    def test_empty_is_weak(self) -> None:
        self.assertEqual(check_strength(""), "weak")

    def test_short_is_weak(self) -> None:
        self.assertEqual(check_strength("abc"), "weak")

    def test_length_only_is_okay(self) -> None:
        self.assertEqual(check_strength("longenough"), "okay")

    def test_length_and_number_is_okay(self) -> None:
        self.assertEqual(check_strength("longenough1"), "okay")

    def test_strong_needs_length_digits_symbols(self) -> None:
        self.assertEqual(check_strength("LongerPass1!"), "strong")


if __name__ == "__main__":
    unittest.main()
