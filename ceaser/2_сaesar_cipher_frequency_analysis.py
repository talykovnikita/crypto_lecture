from сaesar_cipher_common import *
"""
Пример применения частотного анализа для взлома шифротекста
"""


def count_statistic(text: str) -> dict[str, int]:
    """
    Функция подсчитывает, сколько раз встречается каждый символ в шифротексте

    :param text: Зашифрованное сообщение
    :return: Словарь, в котором:
     - ключ - буква из шифротекста,
     - значение - количество раз, которое эта буква появилась в шифротексте
    """
    result: dict[str, int] = {}

    for i in text:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1

    return result


def main():
    # Перехваченное зашифрованное сообщение
    very_secret_text = "тйдмеёАчБдпшфнчБдпехчуэпшдтедтужАодзуи"
    print(f"Перехваченное зашифрованное сообщение: {very_secret_text}")

    statistic = sorted(count_statistic(very_secret_text).items(), key=lambda x: x[1], reverse=True)
    print(f"Количество по каждой букве в тексте: {statistic}")

    print(f"'{ALPHABET}'")
    # offset = 0
    # _, current_secret = generate_secret_rules(offset)
    # decrypted_text = crypt(current_secret, very_secret_text)
    #
    # print(f"Расшифрованное сообщение: {decrypted_text}")


if __name__ == '__main__':
    main()
