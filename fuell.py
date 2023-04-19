from fuel import convert, gauge
    """
    The code contains two test functions, one for converting fuel gauge readings and another for
    displaying the gauge level.
    """

# Test convert function
def test_convert():
    assert convert("50/100") == 50
    assert convert("1/2") == 50
    assert convert("25/100") == 25
    assert convert("75/100") == 75
    assert convert("0/100") == 0
    assert convert("100/100") == 100

    # Test invalid input
    try:
        convert("1/0")
    except ZeroDivisionError as e:
        assert str(e) == "Y cannot be 0."

    try:
        convert("a/b")
    except ValueError as e:
        assert str(e) == "Invalid fraction format. Please provide a fraction in X/Y format where X and Y are integers."

    try:
        convert("5/3")
    except ValueError as e:
        assert str(e) == "X cannot be greater than Y."


# Test gauge function
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "99%"
    assert gauge(100) == "F"

