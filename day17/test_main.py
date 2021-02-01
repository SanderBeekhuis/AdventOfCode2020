from day17.main import ConwayGrid

import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(day17.main))
    return tests

def test_active_count():
    cg = ConwayGrid(['.#.', '..#', '###'])
    assert cg.active_count() == 5

