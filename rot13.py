def cipher_encryption():
    print("Message can only be alphabetic")
    key = int(input("Please enter key number: "))
    key %= 26

    message = input("Enter message: ").upper()

    encrypt_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encrypt_text += " "
        elif temp > 90:
            temp -= 26
            encrypt_text += chr(temp)
        else:
            encrypt_text += chr(temp)
        # if-else
    # for

    print("Encrypted Text: {}".format(encrypt_text))


def cipher_decryption():
    print("Message can only be alphabetic")
    key = int(input("Please enter key number: "))
    key %= 26

    message = input("Enter message: ").upper()

    decrypt_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) - key
        if ord(message[i]) == 32:
            decrypt_text += " "
        elif temp < 65:
            temp += 26
            decrypt_text += chr(temp)
        else:
            decrypt_text += chr(temp)
        # if-else
    # for

    print("Decrypted Text: {}".format(decrypt_text))


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2):"))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
