import pytest


@pytest.mark.skip
def test_m1():
    print('m1 Hi')


@pytest.mark.skip(reason="this has a known issue")
def test_m2():
    print('m2 Hi')



a = 10
@pytest.mark.skipif(a>10, reason='a is more than 10')
def test_m3():
    print('m3 Hi')