from jar import Jar
"""
    The above code contains unit tests for a Jar class in Python.
"""
"""
    The above code contains unit tests for a Jar class in Python.
"""

def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

    j = Jar(20)
    assert j.capacity == 20
    assert j.size == 0

    try:
        j = Jar("invalid")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid capacity."

    try:
        j = Jar(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative capacity."

def test_str():
    j = Jar()
    assert str(j) == ""

    j.deposit(3)
    assert str(j) == "🍪🍪🍪"

    j.deposit(5)
    assert str(j) == "🍪🍪🍪🍪🍪🍪🍪🍪"

    j.withdraw(2)
    assert str(j) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    j = Jar()
    j.deposit(3)
    assert j.size == 3

    j.deposit(7)
    assert j.size == 10

    try:
        j.deposit(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative deposit."

    try:
        j.deposit(5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for over-capacity deposit."

def test_withdraw():
    j = Jar(10)
    j.deposit(5)
    j.withdraw(3)
    assert j.size == 2

    j.withdraw(2)
    assert j.size == 0

    try:
        j.withdraw(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative withdraw."

    try:
        j.withdraw(1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for over-withdraw."
