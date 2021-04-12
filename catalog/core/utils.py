import random
import base64
import requests
import sys
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


# Replace with your API key
api_key = 'e9ba762472ed0b259ca49bb9f9892a6a'


def upload_image(photo, code):
    try:
        with open(photo, "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": api_key,
                "image": base64.b64encode(file.read()),
                "name": code,
            }
            res = requests.post(url, payload)
        if res.status_code == 200:
            # print("Server Response: " + str(res.status_code))
            # print("Image Successfully Uploaded")
            return res
        else:
            print("ERROR")
            print("Server Response: " + str(res.status_code))
            return res
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
        sys.exit()
    except OSError as e:
        print("OSError:", e)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()
