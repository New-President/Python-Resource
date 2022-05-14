# A python program to illustrate Caesar Cipher Technique
def caesarEncrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = 'HELLOWORLDTHESECRETISOUT'
s = 5
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + caesarEncrypt(text, s))
