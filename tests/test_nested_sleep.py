import nested_sleep

def test_short_sleep():
    a = 0.01
    b = 0.01
    expected = "Short Sleep."
    result = nested_sleep(a, b)

    assert expected == result

def test_long_sleep():
    a = 4
    b = 7
    expected = "Long Sleep."
    result = nested_sleep(a, b)

    assert expected == result

