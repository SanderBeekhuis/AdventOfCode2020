import day2.main as main
import pytest

@pytest.mark.parametrize(
  "test,expected",
  [
    ("1-3 a: abcde", True),
    ("1-3 b: cdefg", False),
    ("2-9 c: ccccccccc", True),
  ]
)
def test_is_valid(test, expected):
  assert main.is_valid(test) == expected