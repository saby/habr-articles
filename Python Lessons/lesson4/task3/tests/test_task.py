from lesson4.task3.task import Name

staff_fi = Name('Иванов Иван')
staff_fio = Name('Иванов Иван Иванович')


def test_add():
    assert staff_fio.brief_name == 'Иванов Иван', 'Провеяем brief_name'
    assert staff_fi.brief_name == 'Иванов Иван', 'Провеяем brief_name'
    assert staff_fio.initials == 'Иванов И.И.', 'Провеяем initials'
    assert staff_fi.initials == 'Иванов И.', 'Провеяем initials'
    assert staff_fio.strfname('%И %О %ф.') == 'Иван Иванович И.', "Провеяем strfname('%И %О %ф.')"
    assert staff_fi.strfname('%и.%ф.') == 'И.И.', "Провеяем strfname('%и.%ф.')"
    assert staff_fio.strfname('%и.%ф.%о.') == 'И.И.И.', "Провеяем strfname('%и.%ф.%о.')"
    assert staff_fio.strfname('%Ф %и. %о.') == 'Иванов И. И.', "Провеяем strfname('%Ф %и. %о.')"
