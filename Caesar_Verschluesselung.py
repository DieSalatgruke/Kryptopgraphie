import sys
import datetime

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
output_path = r"C:\MaHo\Python\Python_Output"


def file_writer(cypher):
    with open(f'{output_path}\\'
              f'Cypher-CaeVer-{datetime.datetime.today().strftime("%H-%M-%S_%Y-%m-%d.txt")}', mode='w+') as cypher_file:
        for arg in cypher:
            cypher_file.writelines(arg)
    print('finished')


def get_msg():
    msg = str(input('Nachricht hier eintragen: '))
    return msg


def create_listmsg(message: str):
    list_msg = []
    msg = message.upper()
    list_msg[:0] = msg
    return list_msg


def create_listnum(msg_list: list):
    list_numbers = []
    for elm in msg_list:
        if elm in Index_Crypto.keys():
            list_numbers.append(Index_Crypto[elm])
        elif elm == ' ':
            list_numbers.append(' ')
    return list_numbers


def get_key(val):
    for key, value in Index_Crypto.items():
        if val == value:
            return key


def encode_string(encod_list: list):
    list_cypher = []
    for i in encod_list:
        if i in Index_Crypto.values():
            list_cypher.append(get_key(i))
        elif i == ' ':
            list_cypher.append(' ')
    cypher_msg = ''.join(list_cypher)
    return cypher_msg


class Encoder:

    @staticmethod
    def create_listencode(num_list: list):
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


class Decoder:

    @staticmethod
    def create_listencode(num_list: list):
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


def coding(task):
    if task == 'E' or task == 'e':
        msg = create_listmsg(get_msg())
        list_of_msg = create_listnum(msg)
        en_cyper = encode_string(encoding(list_of_msg))
        file_writer(en_cyper)
    elif task == 'D' or task == 'd':
        msg = create_listmsg(get_msg())
        list_of_msg = create_listnum(msg)
        de_cyper = encode_string(decoding(list_of_msg))
        file_writer(de_cyper)
    else:
        sys.exit()


def encoding(list_of_message):
    list_of_encoding = Encoder.create_listencode(list_of_message)
    return list_of_encoding


def decoding(list_of_message):
    list_of_decoding = Decoder.create_listencode(list_of_message)
    return list_of_decoding


def caesar_verschluesselung():
    task = str(input(f'Cäsar-Verschlüsselung \n'
                     f'E - Verschlüsseln \n'
                     f'D - Entschlüsseln \n'
                     f'Hier eintragen: '))
    return task


if __name__ == '__main__':
    coding(caesar_verschluesselung())
