import sys

Index_Crypto = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
    "Ä": 27,
    "Ö": 28,
    "Ü": 29,
}


secretnumber = 3


class Encoder:

    @staticmethod
    def get_msg():
        msg = str(input('Hier eintragen zum verschlüsseln: '))
        return msg

    @staticmethod
    def create_listmsg(message: str):
        list_msg = []
        msg = message.upper()
        list_msg[:0] = msg
        return list_msg

    @staticmethod
    def create_listnum(msg_list: list):
        list_numbers = []
        for elm in msg_list:
            if elm in Index_Crypto.keys():
                list_numbers.append(Index_Crypto[elm])
            elif elm == ' ':
                list_numbers.append(' ')
        return list_numbers

    @staticmethod
    def create_listencod(num_list: list):
        encod_list = []
        for num in num_list:
            if num == 27:
                encod_list.append(1)
            elif num == 28:
                encod_list.append(2)
            elif num == 29:
                encod_list.append(3)
            elif num == ' ':
                encod_list.append(' ')
            else:
                num += secretnumber
                encod_list.append(num)
        return encod_list

    @staticmethod
    def get_key(val):
        for key, value in Index_Crypto.items():
            if val == value:
                return key

    @staticmethod
    def encode_string(encod_list: list):
        list_cypher = []
        for i in encod_list:
            if i in Index_Crypto.values():
                list_cypher.append(Encoder.get_key(i))
            elif i == ' ':
                list_cypher.append(' ')
        cypher_msg = ''.join(list_cypher)
        return cypher_msg


class Decoder:

    @staticmethod
    def get_msg():
        msg = str(input('Hier eintragen zum entschlüsseln: '))
        return msg

    @staticmethod
    def create_listmsg(message: str):
        list_msg = []
        msg = message.upper()
        list_msg[:0] = msg
        return list_msg

    @staticmethod
    def create_listnum(msg_list: list):
        list_numbers = []
        for elm in msg_list:
            if elm in Index_Crypto.keys():
                list_numbers.append(Index_Crypto[elm])
            elif elm == ' ':
                list_numbers.append(' ')
        return list_numbers

    @staticmethod
    def create_listencod(num_list: list):
        encod_list = []
        for num in num_list:
            if num == 1:
                encod_list.append(27)
            elif num == 2:
                encod_list.append(28)
            elif num == 3:
                encod_list.append(29)
            elif num == ' ':
                encod_list.append(' ')
            else:
                num -= secretnumber
                encod_list.append(num)
        return encod_list

    @staticmethod
    def get_key(val):
        for key, value in Index_Crypto.items():
            if val == value:
                return key

    @staticmethod
    def encode_string(encod_list: list):
        list_cypher = []
        for i in encod_list:
            if i in Index_Crypto.values():
                list_cypher.append(Decoder.get_key(i))
            elif i == ' ':
                list_cypher.append(' ')
        cypher_msg = ''.join(list_cypher)
        return cypher_msg


def encoding():
    msg = Encoder.create_listmsg(Encoder.get_msg())
    listofmsg = Encoder.create_listnum(msg)
    listofencode = Encoder.create_listencod(listofmsg)
    en_cyper = Encoder.encode_string(listofencode)
    return en_cyper


def decoding():
    msg = Decoder.create_listmsg(Decoder.get_msg())
    listofmsg = Decoder.create_listnum(msg)
    listofencode = Decoder.create_listencod(listofmsg)
    de_cyper = Decoder.encode_string(listofencode)
    return de_cyper


if __name__ == '__main__':
    task = str(input(f'Was soll gemacht werden? \n'
                     f'E - Verschlüsseln \n'
                     f'D - Entschlüsseln \n'
                     f'Hier eintragen: '))
    if task == 'E' or task == 'e':
        print(encoding())
    elif task == 'D' or task == 'd':
        print(decoding())
    else:
        sys.exit()
