#!/usr/bin/python3

from keygen import key_gen, encryptor, decyrptor
def main():
    input_text = input("Enter message: ")
    print("Your Message: {}".format(input_text))
    result_dict = encryptor(input_text)
    print("Encrypted Message: {}".format(result_dict["cipher"]))
    decrypted_text = decyrptor(result_dict)
    print("Decrypted Message: {}".format(decrypted_text))