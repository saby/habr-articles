from lesson2.task5.task import task5


def test_add():
    assert task5([1, 3, 7]) == [7, 3, 1]
    assert task5([4, 5, 1, 7, 75, 2]) == [4, 5, 75, 7, 1, 2]
    assert task5([3, 2, 1]) == [1, 2, 3]
    assert task5([1, 1, 1]) == [1, 1, 1]
    assert task5([1, 2, 3, 0, 5]) == [1, 2, 3, 5, 0]
    assert task5([1, 2, 3, 5, 0]) == [1, 2, 3, 0, 5]
    assert task5([1, 2]) == [2, 1]
    assert task5([2, 1]) == [1, 2]


