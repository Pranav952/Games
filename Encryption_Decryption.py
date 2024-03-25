alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
encrypt_text = []
decrypt_text = []


def encode(shift, text):
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypt_index = (index + shift) % 26
            encrypt_text.append(alphabet[encrypt_index])
        else:
            encrypt_text.append(char)


def decode(shift, text):
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_index = (index - shift) % 26
            decrypt_text.append(alphabet[decrypted_index])
        else:
            decrypt_text.append(char)


print("Welcome to data encrypt and decrypt")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit:\n")
while (direction.lower() != "exit"):
    if (direction.lower() == "encode") or (direction.lower() == "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction.lower() == "encode":
            encode(shift, text)
            print(f"Your encrypted message is {encrypt_text}")
            encrypt_text = []
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit:\n")
        elif direction.lower() == "decode":
            decode(shift, text)
            print(f"Your Decoded Message is {decrypt_text}")
            decrypt_text = []
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit:\n")
    else:
        print("Invalid choice,please chose again")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit:\n")
print("program closed successfully")