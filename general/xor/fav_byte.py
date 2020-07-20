import pwn


def get_flag(input_data):
    crypto = b"crypto"
    bytes_input = bytes.fromhex(input_data)
    for byte in range(260):
        candidate = pwn.xor(bytes_input, chr(byte).encode())
        if crypto in candidate:
            return candidate.decode()


input_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
