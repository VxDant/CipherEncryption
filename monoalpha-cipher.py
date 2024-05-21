import string

key = "zebraiscongthqulxypdjkmfvw"

plain_text = open("alice_input.txt", encoding="utf8")
message = plain_text.read()
plain_text.close()
plain_text_2 = ""
cipher_text = ""

for c in message.lower():
    if c in string.ascii_lowercase:
        z = ord(c) - ord('a')
        cipher_text += key[z]
    elif c == " ":
        cipher_text += " "

print(cipher_text)

for c in cipher_text:
    if c in string.ascii_lowercase:
        index = key.index(c)
        index = index + ord('a')
        plain_text_2 += chr(index)
    else:
        plain_text_2 += " "

print(plain_text_2)







