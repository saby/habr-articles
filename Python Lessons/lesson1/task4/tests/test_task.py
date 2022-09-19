from lesson1.task4.task import task4


def test_add():
    assert task4('answer') == ('nswer', 1)
    assert task4('hello') == ('hello', 0)
    assert task4('abcadeaa') == ('bcde', 4)
    assert task4('арбуз') == ('арбуз', 0)
    assert task4('') == ('', 0)
    assert task4('aaaaa') == ('', 5)
