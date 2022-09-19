from lesson3.task2.task import task2


def test_add():
    assert task2(1331) == True, 'Проверяем для 1331'
    assert task2(131) == True, 'Проверяем для 131'
    assert task2(1361) == False, 'Проверяем для 1361'
    assert task2(12345678987654321) == True, 'Проверяем для 12345678987654321'
    assert task2(0) == True, 'Проверяем для 0'
    assert task2(22) == True, 'Проверяем для 22'
    assert task2(220) == False, 'Проверяем для 220'




