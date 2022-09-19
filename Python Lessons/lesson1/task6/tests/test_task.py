from lesson1.task6.task import task6


def test_add():
    assert task6('Тут три слова') == 3, 'Тут три слова'
    assert task6('Тут будет четыре слова') == 4, 'Тут будет четыре слова'
    assert task6('слово') == 1, 'слово'
    assert task6('') == 0, '..пустая строка... Должно быть 0'
