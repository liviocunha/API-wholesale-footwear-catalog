import random
from typing import Dict


def generate_api_key():
    """ Create API Key for using Client """
    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    size = 50
    api_key = "".join(random.sample(chars, size))
    return api_key


def modified_dict_values_title(data_dict: Dict):
    """ Convert string Values of Dictionary in .title() """
    modified_dict = {}
    for k, v in data_dict.items():
        modified_dict[k] = str(data_dict[k]).title()
    return modified_dict

