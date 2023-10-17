import time


def nested_sleep(a, b):
    time.sleep(a)
    sleep2(b)
    if a+b > 10:
        st = "Long Sleep."
    else:
        st = "Short Sleep."
    return st


def sleep2(b):
    time.sleep(b)
    return

