<h1 >Задача 2</h1>
<h2>Напишите декоратор memorize, который запоминает в словаре в виде: ключ - аргументы функции,
    а значение - это результат функции.
    Если функция с такими аргументами уже вызывалась, то берется значение словаря, если нет, то в словарь добавляется.
    Проще говоря, необходимо организовать механизм кэширования.
</h2>
<p><i>Входные данные:</i></p>
<ul><li>Два аргумента. weight <strong>(int)</strong>, speed <strong>(int)</strong></li></ul>
<p><i>Выходные данные:</i></p>
<ul><li><strong>tuple</strong> с двумя аргументами: результат вычисления кинетической энергии <strong>(float)</strong> и словарь "кэша" <strong>(dict)</strong></li></ul>
<p><i>Пример:</i></p>
<div class="example">
    <code>@memorize</code> <br>
    <code>def get_kinetic_energy():</code> <br>
    <div style="margin-left: 20px"><code>return (weight * speed ** 2)/2</code> </div> <br>
    >>> <strong>(22.5, {(5, 2): 10.0, (5, 3): 22.5})</strong>
</div>
<p>Подсказки:</p>
<div class="hint">
    <div>НЕ изменяйте ничего в get_kinetic_energy()</div>
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
