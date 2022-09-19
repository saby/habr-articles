import unittest

from lesson2.task4.task import task4


class TestCase(unittest.TestCase):
    def test_add(self):
        assert task4(64) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60], 'Проверяем для 64. Сравниваем '
        assert task4(17) == [5, 10, 15], 'Проверяем для 17. Сравниваем '
        assert task4(0) == [], 'Проверяем для 0. Сравниваем '
        assert task4(1) == [], 'Проверяем для 1. Сравниваем '
        assert task4(55) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55], 'Проверяем для 55. Сравниваем '
