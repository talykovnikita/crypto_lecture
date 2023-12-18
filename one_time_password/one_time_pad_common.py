def crypt(message: str, key: str) -> str:
    result = ""
    for i in range(0, len(message)):
        message_symbol_code = ord(message[i])
        key_symbol_code = ord(key[i % len(key)])

        encrypted_symbol_code = message_symbol_code ^ key_symbol_code

        result += chr(encrypted_symbol_code)

    return result


def main():
    my_message = "2024 год будет високосным! Yes, it's true ☻..."
    my_key = "пароль"
    print(my_message)
    print(my_key * 10, end="")
    print()
    print()

    encrypted_message = crypt(my_message, my_key)

    print(f"Исходное сообщение:      {my_message}")
    print(f"Зашифрованное сообщение: {encrypted_message}")
    print(f"Байты зашифрованного сообщения: {encrypted_message.encode('utf-8')}")

    decrypted_message = crypt(encrypted_message, my_key)

    print()
    print()
    print(f"Расшифрованное сообщение: {decrypted_message}")


if __name__ == "__main__":
    main()
