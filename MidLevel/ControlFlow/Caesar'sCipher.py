def caesarCipher(text, shift):
    encrypted_text = ""
    text = text.replace(" ", "")
    for char in text:
        if char.isalpha():  # アルファベットの文字のみを対象にする
            if char.islower():  # 小文字の場合
                shifted = ord('a') + (ord(char) - ord('a') + shift) % 26
                encrypted_text += chr(shifted)
            elif char.isupper():  # 大文字の場合
                shifted = ord('A') + (ord(char) - ord('A') + shift) % 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # アルファベット以外の文字はそのまま追加

    return encrypted_text
