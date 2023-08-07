def encrypt(text, shift=5):
    empty_text = ""
    for char in text:
        if char.isalpha():
            is_upper_case = char.isupper()
            char = char.lower()
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            if is_upper_case:
                encrypted_char = encrypted_char.upper()
        else:
            encrypted_char = char
        empty_text += encrypted_char
    return empty_text
