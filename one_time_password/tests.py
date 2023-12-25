from one_time_pad_common import crypt


def test_0():
    msg: str = "HELLOWORLD"
    key: str = "helloworld"

    result_1: str = crypt(msg, key)

    assert result_1 != msg, f"Нулевой тест не пройден. Функция crypt ничего не делает."


def test_1():
    msg: str = "HELLOWORLD"
    key: str = "helloworld"

    result: str = crypt(crypt(msg, key), key)

    assert msg == result, f"Первый тест не пройден. Ожидали {msg}, а получили {result}"


def test_2():
    msg: str = "HELLOWORLD"
    key: str = "hello"

    result: str = crypt(crypt(msg, key), key)

    assert msg == result, f"Второй тест не пройден. Ожидали {msg}, а получили {result}"


def test_3():
    msg: str = "HELLOWORLD"
    key: str = "hellohellohellohellohellohello"

    result: str = crypt(crypt(msg, key), key)

    assert msg == result, f"Третий тест не пройден. Ожидали {msg}, а получили {result}"


def test_4():
    msg: str = "♥☻§-◘E"
    key: str = "123"

    result: str = crypt(crypt(msg, key), key)

    assert msg == result, f"Четвёртый тест не пройден. Ожидали {msg}, а получили {result}"


TESTS = [test_0, test_1, test_2, test_3, test_4]


def main():
    for test in TESTS:
        test.__call__()


if __name__ == "__main__":
    main()
