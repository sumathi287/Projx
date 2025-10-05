import pickle
import rsa
from cryptography.fernet import Fernet
import os
import logging

file_path = os.path.join(os.path.join(__file__))
print(file_path)
text_path = os.path.dirname(file_path)
log_path = os.path.join(text_path, "logg_file.log")

logging.basicConfig(
    filemode=log_path,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def save_dict(dict_data):
    """
    Serialize (pickle), encrypt, and save a dictionary to a binary file.
    Args:
        dict_data (dict): The dictionary data to be saved.
    Returns:
        True(log data): If the binary data is successfully stored in .bin file
        False(log data): If the non-binary data is stored in .bin file
    """
    global text_path
    original_dict_data = dict_data
    pickle_dict_data = pickle.dumps(original_dict_data)
    key = gen_enc_key()
    encrypt_pickled_data = key.encrypt(pickle_dict_data)
    text_path = os.path.join(text_path, "output.bin")

    try:
        with open(text_path, "wb") as f:
            f.write(encrypt_pickled_data)
            logging.info("Contact storage was successful!")
    except TypeError:
        # print("TypeError: a bytes-like object is required, not 'str'")
        logging.info("TypeError: a bytes-like object is required, not 'str'")


def read_data():
    pass


def gen_enc_key():
    key = Fernet.generate_key()
    fernet_key = Fernet(key)
    return fernet_key
