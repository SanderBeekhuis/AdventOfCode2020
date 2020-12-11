import main
import pytest

def test_run():
  assert main.run(file='test_input.txt') == 2

def test_run_invalid():
  assert main.run(file='input_invalid.txt') == 0