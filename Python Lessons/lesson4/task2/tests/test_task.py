from lesson4.task2.task import get_kinetic_energy


def test_add():
    assert get_kinetic_energy(5, 2), (10.0, {(5, 2): 10.0})
    assert get_kinetic_energy(5, 3), (22.5, {(5, 2): 10.0, (5, 3): 22.5})
    assert get_kinetic_energy(5, 3), (22.5, {(5, 2): 10.0, (5, 3): 22.5})
    assert get_kinetic_energy(5, 4), (40.0, {(5, 2): 10.0, (5, 3): 22.5, (5, 4): 40.0})
    assert get_kinetic_energy(5, 2), (10.0, {(5, 2): 10.0, (5, 3): 22.5, (5, 4): 40.0})
