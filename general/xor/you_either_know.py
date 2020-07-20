from rich import print
import pwn


def get_flag(input_data):
    flag_pattern = b"crypto{"
    input_encoded = bytes.fromhex(input_data)
    key_retrieved = pwn.xor(flag_pattern, input_encoded)[: len(flag_pattern)]
    print(f"retrieved part of the key: [b]{key_retrieved}[/b]")

    # since key_retrieved = "myXORke" guess the last one is a "y"
    key = key_retrieved + b"y"
    return pwn.xor(input_encoded, key)


input_data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
