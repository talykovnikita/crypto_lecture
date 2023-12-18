from сaesar_cipher_common import *


def main():
    """
    Пример шифрования и расшифрования
    :return:
    """
    # Выбираем смещение
    offset = 3

    # Создаём правила замены букв для шифрования и расшифрования
    encrypt_rules, decrypt_rules = generate_secret_rules(offset)
    print(f"Исходный алфавит:      {list(encrypt_rules.keys())}")
    print(f"Зашифрованный алфавит: {list(encrypt_rules.values())}\n")

    # Сообщение, которое хотим зашифровать
    message = "Всем привет! Я сегодня читаю лекцию про криптографию!!!"

    encrypted_text = crypt(encrypt_rules, message)
    print(f"Зашифрованное сообщение:  {encrypted_text}")

    decrypted_text = crypt(decrypt_rules, encrypted_text)
    print(f"Расшифрованное сообщение: {decrypted_text}")


if __name__ == '__main__':
    main()

