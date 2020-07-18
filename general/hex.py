def get_flag(hex_string):
    return bytearray.fromhex(hex_string).decode()


input_data = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print(get_flag(input_data))
