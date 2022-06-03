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
    def write_message_file(cypher_key_txt: str):
        with open(f'{output_path}\\'
                  f'Cypher-Mono-{datetime.datetime.today().strftime("%H%M%S-%Y%m%d.txt")}',
                  mode='w+') as cypher_file_txt:
            for arg in cypher_key_txt:
                cypher_file_txt.writelines(arg)

    @staticmethod
    def write_pickle_file(cypher_key_pickle: dict):
        with open(f'{output_path}\\'
                  f'Cypher-Mono-{datetime.datetime.today().strftime("%H%M%S-%Y%m%d.pickle")}', 'wb')\
                as cypher_file_pickle:
            pickle.dump(cypher_key_pickle, cypher_file_pickle)

    @staticmethod
    def write_json_file(cypher_key_json: dict):
        with open(f'{output_path}\\'
                  f'Cypher-Mono-{datetime.datetime.today().strftime("%H%M%S-%Y%m%d.json")}',
                  mode='w+') as cypher_file_json:
            cypher_file_json.write(json.dumps(cypher_key_json))


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
            encrypted_list.append(cypher_dict[elm])
        elif elm == ' ':
            encrypted_list.append(' ')
    encrypted_string = ''.join(encrypted_list)
    return encrypted_string


def load_pickle_file():
    with open(f'{output_path}\\'
              f'Cypher-Mono-211839-20220603.pickle', 'rb') \
            as cypher_file_pickle:
        m = pickle.load(cypher_file_pickle)
        print(m)


if __name__ == '__main__':
    nachricht = create_message_list(get_message())
    cyphe_dict = generate_dict(generate_list(alphabet), generate_random_list(generate_list(alphabet)))
    FileWriter.write_json_file(cyphe_dict)
    FileWriter.write_pickle_file(cyphe_dict)
    code = encode_message(nachricht, cyphe_dict)
    FileWriter.write_message_file(code)
    load_pickle_file()
