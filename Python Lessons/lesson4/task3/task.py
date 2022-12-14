class Name:
    """Класс для работы с ФИО"""

    def __init__(self):
        pass

    def _check(self):
        """
        Проверка правильности переданого формат ФИО
        :return:
        """
        pass

    def strfname(self, str_format):
        """Преобразует переданный формат в строку
        %Ф - фамилия, %ф - первая буква фамилии
        %И - имя, %и - первая буква имени
        %О - отчество, %о - первая буква отчества
        """
        pass

    @property
    def brief_name(self):
        """Сокращенное имя (без отчества)
        :return: Возвращает строку вида Петров Иван
        """
        pass

    @property
    def initials(self):
        """Инициалы
        :return: Возвращает строку вида Петров И.С.
        """
        pass
