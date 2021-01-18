import day11.main

def test_run():
    assert day11.main.run('day11/test_input.txt') == 37

def test_seated_neighbours():
    lines = [['#']  * 3]* 3 

    assert day11.main.seated_neighbours(lines, 1, 1) == 8
    assert day11.main.seated_neighbours(lines, 0, 0) == 3 
    assert day11.main.seated_neighbours(lines, 1, 0) == 5
    assert day11.main.seated_neighbours(lines, 2, 2) == 3
    assert day11.main.seated_neighbours(lines, 2, 1) == 5
    