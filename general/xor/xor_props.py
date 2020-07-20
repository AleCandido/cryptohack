import pwn


def get_flag(input_data):
    k1 = bytes.fromhex(input_data["k1"])
    k23 = bytes.fromhex(input_data["k23"])
    fk132 = bytes.fromhex(input_data["fk132"])
    return pwn.xor(k1, k23, fk132).decode()


input_data = dict(
    k1="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313",
    k21="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e",
    k23="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1",
    fk132="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf",
)
