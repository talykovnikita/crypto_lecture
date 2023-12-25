from сaesar_cipher_common import *


if __name__ == '__main__':
    # Полный перебор
    very_secret_text = "ИшлуёцчпилщеёдёшлйхкфЁёюпщжЕётлсэпЕёцчхёсчпцщхйчжыпЕеее"

    for i in range(0, len(ALPHABET)):
        _, decrypt_rules = generate_secret_rules(i)
        current_attempt = crypt(decrypt_rules, very_secret_text)

        print(f"Смещение {i}: {current_attempt}")
