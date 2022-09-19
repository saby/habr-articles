from lesson1.task7.task import task7


def test_add():
    assert task7(r'C:\Documents\Newsletters\Summer2018.pdf') == 'Summer2018', r'Проверяем на C:\Documents\Newsletters\Summer2018.pdf. Сравниваем '
    assert task7(r'C:\Newsletters\winter1.jpeg') == 'winter1', r'Проверяем на C:\Newsletters\winter1.jpeg. Сравниваем '
    assert task7(r'C:\ololo3.7z') == 'ololo3', r'Проверяем на C:\ololo3.7z. Сравниваем '
