"""Tiny password strength checker.

Usage:
  python scripts/password_strength.py "P@ssw0rd!"
"""

from __future__ import annotations

import string
import sys


SYMBOLS = set(string.punctuation)
DIGITS = set(string.digits)


def check_strength(password: str) -> str:
    """Return weak, okay, or strong based on simple rules."""
    if not password:
        return "weak"

    length = len(password)
    has_digit = any(ch in DIGITS for ch in password)
    has_symbol = any(ch in SYMBOLS for ch in password)

    if length < 8:
        return "weak"
    if length >= 12 and has_digit and has_symbol:
        return "strong"
    return "okay"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python scripts/password_strength.py <password>")
        return 1

    password = argv[1]
    strength = check_strength(password)
    print(strength)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
