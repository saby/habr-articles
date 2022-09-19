from lesson2.task7.task import task7


def test_add():
    assert task7([{'Наименование': "Чай", 'Цена': 320},
                  {'Наименование': "Хлеб", 'Цена': 120},
                  {'Наименование': "Молоко", 'Цена': 220},
                  {'Наименование': "Икра", 'Цена': 350}]) == \
        [{'Наименование': "Икра", 'Цена': 350},
         {'Наименование': "Чай", 'Цена': 320}]

    assert task7([{'Наименование': "Чай", 'Цена': 350},
                  {'Наименование': "Икра", 'Цена': 350}]) == \
        [{'Наименование': "Чай", 'Цена': 350},
         {'Наименование': "Икра", 'Цена': 350}]
    assert task7([{'Наименование': "Чай", 'Цена': 360},
                  {'Наименование': "Хлеб", 'Цена': 220},
                  {'Наименование': "Молоко", 'Цена': 220},
                  {'Наименование': "Икра", 'Цена': 350}]) == \
           [{'Наименование': "Чай", 'Цена': 360},
            {'Наименование': "Икра", 'Цена': 350}]
