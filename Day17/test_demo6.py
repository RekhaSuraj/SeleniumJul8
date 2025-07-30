import pytest

@pytest.mark.run(order=5)
def test_m1():
    print('logout')


@pytest.mark.run(order=1)
def test_m2():
    print('login')


@pytest.mark.run(order=2)
def test_m3():
    print('Create user')


@pytest.mark.run(order=4)
def test_m4():
    print('delete user')


@pytest.mark.run(order=3)
def test_m5():
    print('edit user')