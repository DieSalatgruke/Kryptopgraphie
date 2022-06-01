import json
import pickle
import datetime
import secrets


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ'
output_path = r"C:\MaHo\Python\Python_Output"


def generate_list(alphabet_str: str):
    alpha_list = []
    alpha_list[:0] = alphabet_str
    return alpha_list


def generate_random_list(alphabet_list: list):
    trash_list = alphabet_list
    random_alpha_list = []
    for _ in range(len(alphabet_list)):
        var = secrets.choice(trash_list)
        random_alpha_list.append(var)
        trash_list.remove(var)
    return random_alpha_list


def generate_dict(alphabet_list: list, random_list: list):
    random_cypher_dic = {}
    for alph, rand in zip(alphabet_list, random_list):
        random_cypher_dic.update({alph: rand})
    return random_cypher_dic


class FileWriter:

    @staticmethod
    def write_message_file(cypher):
        with open(f'{output_path}\\'
                  f'Cypher-CaeVer-{datetime.datetime.today().strftime("%H-%M-%S_%Y-%m-%d.txt")}',
                  mode='w+') as cypher_file:
            cypher_file.write('-' * 45 + '\n')
            cypher_file.write('Zeitstempel ' + datetime.datetime.today().strftime('%A, the %d %B %Y') +
                              datetime.datetime.today().strftime('%X'))
            cypher_file.write('-' * 45 + '\n')
            for arg in cypher:
                cypher_file.writelines(arg)

    @staticmethod
    def write_pickle_file():
        pass

    @staticmethod
    def write_json_file():
        pass


def get_message():
    message = str(input('Nachricht hier eintragen: '))
    return message


def create_message_list(message: str):
    list_message = []
    message = message.upper()
    list_message[:0] = message
    return list_message


def encode_message(message_list: list, cypher_dict: dict):
    encrypted_list = []
    for elm in message_list:
        if elm in cypher_dict.keys():
            encrypted_list.append(cypher_dict.)
    pass


if __name__ == '__main__':
    cyphe_dict = generate_dict(generate_list(alphabet), generate_random_list(generate_list(alphabet)))
    print(cyphe_dict)
