def get_flag(encoded_list):
    flag = []
    for c in encoded_list:
        flag.append(chr(c))

    return "".join(flag)


input_data = [
    99,
    114,
    121,
    112,
    116,
    111,
    123,
    65,
    83,
    67,
    73,
    73,
    95,
    112,
    114,
    49,
    110,
    116,
    52,
    98,
    108,
    51,
    125,
]

print(get_flag(input_data))
