from lesson2.task3.task import task3


def test_add():
    assert task3(3) == 3, 'Проверяем для 3. Сравниваем '
    assert task3(5) == 15, 'Проверяем для 15. Сравниваем '
    assert task3(2) == 2, 'Проверяем для 2. Сравниваем '
    assert task3(1) == 1, 'Проверяем для 1. Сравниваем '
    assert task3(20) == 3715891200, 'Проверяем для 20. Сравниваем '


