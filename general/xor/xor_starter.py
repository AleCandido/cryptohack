def get_flag(input_data):
    label = input_data[0]
    num = input_data[1]

    flag = []
    for c in label:
        flag.append(chr(ord(c) ^ num))

    return "crypto{" + "".join(flag) + "}"


input_data = ["label", 13]
