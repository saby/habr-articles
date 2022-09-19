from lesson2.task2.task import task2


def test_add():
    assert task2(3) == ['1 *', '2 **', '3 ***']
    assert task2(5) == ['1 *', '2 **', '3 ***', '4 ****', '5 *****']
    assert task2(0) == []

