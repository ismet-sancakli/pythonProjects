alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v',
           'y', 'z']
bigAlphabet = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü',
               'V', 'Y', 'Z']


def letter_dictionary(int_number):
    encrypted_message = ""
    for i in message:
        if i == " ":
            encrypted_message += i
        elif i.isupper():
            encrypted_message += bigAlphabet[(bigAlphabet.index(i) + int_number) % len(bigAlphabet)]
        else:
            encrypted_message += alphabet[(alphabet.index(i) + int_number) % len(alphabet)]

    print(f"Encrypted message : {encrypted_message}")

    return encrypted_message


def decode(int_val, string):
    decoded_message = ""
    for i in string:
        if i == " ":
            decoded_message += i
        elif i.isupper():
            decoded_message += bigAlphabet[(bigAlphabet.index(i) - int_val) % len(bigAlphabet)]
        else:
            decoded_message += alphabet[(alphabet.index(i)  - int_val) % len(alphabet)]

    print(f"Decoded message {decoded_message}")
    return decoded_message


message = "merhaba dünya"
number = int(input("Enter the number between 0 to 29 : "))
enc_message = letter_dictionary(number)
print("-----------------------------------------------------")
decode(number, enc_message)



