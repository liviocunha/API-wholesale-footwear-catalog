import random


def generate_api_key():
    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    size = 50
    api_key = "".join(random.sample(chars, size))
    return api_key


def str_upper(string):
    return string.upper()


def str_title(string):
    return string.title()
