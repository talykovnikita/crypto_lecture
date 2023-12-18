# Все буквы, которые поддерживает алгоритм шифрования
ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper() + "!" + " "


def generate_secret_rules(offset: int) -> tuple[dict, dict]:
    """
    Функция создания правил для шифрования и расшифрования текста шифром Цезаря
    :param offset: смещение букв
    :return: 2 набора правил в виде словарей (для шифрования и расшифрования)
    """
    encrypt_rules = {}
    decrypt_rules = {}
    for i in range(0, len(ALPHABET)):
        k, v = ALPHABET[i], ALPHABET[(i + offset) % len(ALPHABET)]
        encrypt_rules[k] = v
        decrypt_rules[v] = k

    return encrypt_rules, decrypt_rules


def crypt(rules: dict, message: str) -> str:
    """
    Функция применения правил замены к тексту

    :param rules: Правила замены букв в тексте
    :param message: Текст в котором нужно заменить буквы
    :return: результат замены
    """
    result = ""
    for i in message:
        result += rules[i]

    return result


def main():
    offset = 3
    print(f"Смещение букв: {offset}")

    encrypt_rules, decrypt_rules = generate_secret_rules(offset)
    print(f"Исходный алфавит:      {list(encrypt_rules.keys())}")
    print(f"Зашифрованный алфавит: {list(encrypt_rules.values())}\n")

    print(f"Зашифрованная буква 'а' - это: '{encrypt_rules.get('а')}'")
    print(f"Расшифрованная буква 'г' - это: '{decrypt_rules.get('г')}'")


if __name__ == '__main__':
    main()
