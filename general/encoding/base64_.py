import base64


def get_flag(hex_string):
    bytes_ = bytearray.fromhex(hex_string)
    return base64.b64encode(bytes_)


input_data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
