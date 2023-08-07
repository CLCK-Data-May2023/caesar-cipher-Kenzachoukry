def encrypt(text, shift=5):
    empty_text = ""
    for character in text:
        if character.isalpha():
            is_upper_case = character.isupper()
            character = character.lower()
            encrypted_character = chr((ord(character) - ord('a') + shift) % 26 + ord('a'))
            if is_upper_case:
                encrypted_character = encrypted_character.upper()
        else:
            encrypted_character = character
        empty_text += encrypted_character
    return empty_text
