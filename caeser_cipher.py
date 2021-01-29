# Benjamin Mercier 100745885

## Caesar Cipher

class CaesarCipher():

    def __init__(self, message):
        self._message = message
        self._decryptMessage = ""

    def encrypt(self):
        encryptStr = []
        for x in self._message:
            if x.isalpha(): # if the character is a letter convert it into ascii
                asc = ord(x)
                asc += 3
                if 97 > asc > 90:
                    asc -= 26
                    encryptStr.append(asc)
                elif  asc > 122:
                    asc -= 26
                    encryptStr.append(asc)
                else:
                    encryptStr.append(asc)

        encrypted_message = []
        for x in encryptStr: # converts ascii back into letters
            char = chr(x)
            encrypted_message.append(char)

        split_message = []
        for x in self._message: # separates each character in string
            split_message.append(x)

        i_of_encrypt = 0
        i_of_split = 0
        for x in split_message: # replaces all non encrypted letters with their encrypted versions
            if x.isalpha():
                split_message[i_of_split] = encrypted_message[i_of_encrypt]
                i_of_encrypt += 1
                i_of_split += 1
            else:
                i_of_split += 1

        final_message = ""
        for x in split_message: # adds the encrypted characters from the list into a final string
            final_message += x

        self._decryptMessage = final_message
        print(final_message)

    def decrypt(self):
        decryptStr = []
        for x in self._decryptMessage:
            if x.isalpha():  # if the character is a letter convert it into ascii
                asc = ord(x)
                asc -= 3
                if 97 > asc > 90:
                    asc += 26
                    decryptStr.append(asc)
                elif asc < 65:
                    asc += 26
                    decryptStr.append(asc)
                else:
                    decryptStr.append(asc)

        decrypted_message = []
        for x in decryptStr:  # converts ascii back into letters
            char = chr(x)
            decrypted_message.append(char)

        split_message = []
        for x in self._decryptMessage:  # separates each character in string
            split_message.append(x)

        i_of_encrypt = 0
        i_of_split = 0
        for x in split_message:  # replaces all encrypted letters with their decrypted versions
            if x.isalpha():
                split_message[i_of_split] = decrypted_message[i_of_encrypt]
                i_of_encrypt += 1
                i_of_split += 1
            else:
                i_of_split += 1

        final_message = ""
        for x in split_message:  # adds the decrypted characters from the list into a final string
            final_message += x

        print(final_message)


def Main():
    key = input("Enter a message: ")

    o = CaesarCipher(key)
    o.encrypt()
    o.decrypt()

Main()

## bonus shit

# def caser_cipher(self):
#     asciiStr = []  # holds the ascii version of the letters in the message
#     for x in self._message:  # converts letters to ascii
#         asc = ord(x)
#         asciiStr.append(asc)
#
#     encryptStr = []  # holds the encrypted ascii code
#     for i in asciiStr:  # shifts ascii code over by 3 characters
#         i += 3
#         if 90 < i < 97:
#             i -= 26
#             encryptStr.append(i)
#         elif i > 122:
#             i -= 26
#             encryptStr.append(i)
#         else:
#             encryptStr.append(i)
#
#     encrypted_message = ""  # holds the final encrypted message
#     for r in encryptStr:  # converts encrypted ascii code into letters
#         char = chr(r)
#         encrypted_message += char
#     print("Encrypted message: {}".format(encrypted_message))
#
#
# def decypt(self):
#     encrypted_message = []  # holds the ascii version of the letters in the message
#     for x in self._message:  # converts letters to ascii
#         asc = ord(x)
#         encrypted_message.append(asc)
#
#     decryptStr = []  # holds the final decrypted message
#     for i in encrypted_message:  # shifts ascii code over by 3 characters
#         i -= 3
#         if 65 > i:
#             i += 26
#             decryptStr.append(i)
#         elif 97 > i:
#             i += 26
#             decryptStr.append(i)
#         else:
#             decryptStr.append(i)
#
#     decrypted_message = ""
#     for r in decryptStr:  # converts decrypted ascii code into letters
#         char = chr(r)
#         decrypted_message += char
#     print("Decrypted message: {}".format(decrypted_message))