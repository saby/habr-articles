<h1 >Задача 3</h1>
<h2>Опишите класс Name. Экземпляр класса создается одной строкой, состоящей из 2-3 слов (на это должна быть проверка).</h2>
<div class="example">
Среди свойств/методов этого класса должны быть:<br>
<strong>brief_name</strong> Возвращает строку вида ‘Фамилия Имя’ (без отчества)<br>
<strong>initials</strong> Возвращает строку вида ‘Фамилия И.О.’ (фамилия и инициалы)<br>
<strong>strfname(format)</strong> Преобразует по переданному формату format строку, где
%Ф - фамилия, %ф – первая буква фамилии,
    %И - имя, %и - первая буква имени
    %О - отчество, %о - первая буква отчества<br>
</div>
<p><i>Входные данные:</i></p>
<ul><li> ФИО в виде строки <strong>(str)</strong></li></ul>
<p><i>Примеры:</i></p>
<div class="example">
    <code>name = Name(‘Иванов Иван’):</code> <br>
    или <br>
    <code>fullname = Name(‘Иванов Иван Иванович’)</code> <br>
    Как работают свойства/методы класса: <br>
    <code>fullname.brief_name return 'Иванов Иван'</code> <br>
    <code>name.initials return 'Иванов И.'</code> <br>
    <code>fullname.strfname('%И %О %ф.')  return 'Иван Иванович И.'</code> <br>

</div>
<p>Подсказки:</p>
<div class="hint">
    <a href="https://pythonru.com/osnovy/klass-i-obekt-v-python">Классы и объекты</a>
</div>
<p>Ссылки:</p>
<a href="https://online.sbis.ru/shared/disk/cc167bcb-96f1-4238-914c-c9023f65851a">Вебинар</a>
<br>
<a href="https://youtu.be/1dpEusFf_xI">Курс МФТИ по Python 3 Лекция 8</a>
<br>
<a href="https://pythonru.com/osnovy/klass-i-obekt-v-python">Классы и объекты</a>
<br>
<a href="https://python-scripts.com/object-oriented-programming-in-python">Основы ООП</a>
<br>
<a href="https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html">Подключение модулей</a>
<br>
<a href="https://python-scripts.com/scope">Области видимости</a>
<br>
<a href="https://pythonworld.ru/osnovy/dekoratory.html">Декораторы</a>
