import pickle
import rsa
from cryptography.fernet import Fernet
import os
import logging
import sys

file_path = os.path.join(os.path.join(__file__))
text_path = os.path.dirname(file_path)
log_path = os.path.join(text_path, "logg_file.log")
encrypt_pickled_data = " "
key = " "

logging.basicConfig(
    filename=log_path,
    # filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def stop():
    logging.error("The program was stopped forcefully!!.")
    sys.exit()


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
    global encrypt_pickled_data
    global key
    logging.info("Process is successfully started!!")
    original_dict_data = dict_data
    pickle_dict_data = pickle.dumps(original_dict_data)
    key = gen_enc_key()
    encrypt_pickled_data = key.encrypt(pickle_dict_data)
    # print(type(encrypt_pickled_data))
    text_path = os.path.join(text_path, "output.bin")
    with open(text_path, "wb") as f:
        f.write(encrypt_pickled_data)
        logging.info("Encrypted data has been stored successfully!")


def read_data():
    global encrypt_pickled_data
    global text_path
    global key
    if os.path.exists(text_path):
        logging.info(
            "Successfully verified the existence of the .bin file in the script path."
        )
    else:
        logging.error("The .bin file does not exist in the script path.")
        stop()
    with open(text_path, "rb") as f:
        read_encrypted_data = f.read()
        if encrypt_pickled_data == read_encrypted_data:
            logging.info(
                "The .bin file was read successfully, and encrypted data retrieved."
            )
            decrypt_message = key.decrypt(read_encrypted_data)
            # decrypt_message = decrypt_message.decode()
            unpickled_decrypt_message = pickle.loads(decrypt_message)
            print("The received dict message is", unpickled_decrypt_message)
            # print(unpickled_decrypt_message)
            logging.info("The decrypted data was successfully unpickled")
        else:
            logging.info(
                "The read encrypt data is mismatch with original encrypted data"
            )
            stop()

    if isinstance(unpickled_decrypt_message, dict):
        logging.info("The message was received successfully!!")
    else:
        print("The data is not dict type plese check the log for more info")
        # logging.info("The dict data is received successfully")


def gen_enc_key():
    key = Fernet.generate_key()
    fernet_key = Fernet(key)
    return fernet_key
