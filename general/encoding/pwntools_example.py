# NOTE: activate connection with `nc socket.cryptohack.org 13377`
# `nc` is netcat

import json

from pwn import *  # pip install pwntools
from Crypto.Util.number import long_to_bytes
import codecs
import base64
from rich import console

out = console.Console()

r = remote("socket.cryptohack.org", 13377, level="debug")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(encoded, encoding):
    # TODO: mv encoding steps into decoding
    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(encoded, "rot_13")
    elif encoding == "bigint":
        decoded = bytes.fromhex(encoded[2:]).decode()
    elif encoding == "utf-8":
        decoded = "".join([chr(c) for c in encoded])

    return decoded


received = json_recv()

while "flag" not in received:
    out.print("[i]Received type:[/i]")
    out.print(received["type"])
    out.print("[i]Received encoded value:[/i]")
    out.print(received["encoded"])

    to_send = {"decoded": decode(received["encoded"], received["type"])}
    json_send(to_send)

    received = json_recv()

out.print(f"[u]flag[/u]: {received['flag']}")
