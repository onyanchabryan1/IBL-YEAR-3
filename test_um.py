def test_count_no_um():
    assert count("Hello world!") == 0

def test_count_one_um():
    assert count("Um, let me think...") == 1

def test_count_multiple_um():
    assert count("I don't know, um, um, um...") == 3
