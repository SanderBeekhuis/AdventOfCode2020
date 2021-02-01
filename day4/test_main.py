import day4.main as main

def test_run():
  assert main.run(file='day4/test_input.txt') == 2

def test_run_invalid():
  assert main.run(file='day4/input_invalid.txt') == 0