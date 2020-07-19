import Crypto.Util.number


def get_flag(long_string):
    return Crypto.Util.number.long_to_bytes(long_string)


input_data = (
    "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
)
