from lesson1.task1.task import task1


def test_add():
    assert task1(123) == 136, "Проверяем на 136: 1 + 12 + 123 = 136. Сравниваем "
    assert task1(300) == 333, "Проверяем на 300: 3 + 30 + 300 = 333. Сравниваем "
    assert task1(935) == 1037, "Проверяем на 935: 9 + 93 + 935 = 1037. Сравниваем "
