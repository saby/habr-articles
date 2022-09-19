from lesson1.task2.task import task2


def test_add():
    assert task2(5234) == 14, "5234: 5 + 2 + 3 + 4 = 14. Сравниваем "
    assert task2(0) == 0, "0 = 0. Сравниваем "
    assert task2(92000) == 11, "92000: 9 + 2 + 0 + 0 + 0 = 11. Сравниваем "
    assert task2(65040) == 15, "65040: 6 + 5 + 0 + 4 + 0 = 15. Сравниваем "
