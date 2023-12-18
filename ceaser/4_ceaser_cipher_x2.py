from сaesar_cipher_common import *

# Пример шифрования и расшифрования
if __name__ == '__main__':
    # Сообщение, которое хотим зашифровать
    message = "Всем привет! Я сегодня читаю лекцию про криптографию!!!"

    # Выбираем первое смещение
    print("Первый раунд:")
    offset = 3

    # Создаём правила замены букв для шифрования и расшифрования
    encrypt_rules, _ = generate_secret_rules(offset)
    print(f"Исходный алфавит:      {list(encrypt_rules.keys())}")
    print(f"Зашифрованный алфавит: {list(encrypt_rules.values())}")

    encrypted_text_1 = crypt(encrypt_rules, message)
    print(f"Зашифрованное первый раз сообщение: {encrypted_text_1}")

    # Выбираем второе смещение
    print("\nВторой раунд:")
    offset = 4

    # Создаём правила замены букв для шифрования и расшифрования
    encrypt_rules, _ = generate_secret_rules(offset)
    print(f"Исходный алфавит:      {list(encrypt_rules.keys())}")
    print(f"Зашифрованный алфавит: {list(encrypt_rules.values())}")

    encrypted_text_2 = crypt(encrypt_rules, encrypted_text_1)
    print(f"Зашифрованное второй раз сообщение: {encrypted_text_2}")

    print("\nРезультаты:")
    print(f"Исходное сообщение:                  {message}")
    print(f"Зашифрованное первый раз сообщение:  {encrypted_text_1}")
    print(f"Зашифрованное второй раз сообщение:  {encrypted_text_2}")


