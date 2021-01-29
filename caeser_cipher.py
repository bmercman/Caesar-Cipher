# Author - Benjamin Mercier

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
