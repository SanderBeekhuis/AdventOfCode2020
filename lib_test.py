import lib

def test_split_on_empty():
    assert lib.split_on_empty(['a', 'b', '', 'c']) == [['a', 'b'], ['c']]