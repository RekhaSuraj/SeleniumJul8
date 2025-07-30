import pytest


def test_m1():
    actual = "login"
    expected = "login"

    assert actual == expected


def test_m2():
    actual = 'login'
    expected = 'home'

    assert actual == expected