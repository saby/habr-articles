from lesson1.foreword.task import first_task


def test_add():
    assert first_task(1, 2) == 3, "Sum 1 + 2 to equal 3"
    assert first_task(2, 2) == 4, "Sum 2 + 2 to equal 4. Поменяй return"

