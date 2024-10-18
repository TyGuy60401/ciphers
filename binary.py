ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def anti_ord(val):
    for char in ALPHABET:
        if ord(char) == val:
            return char
    else:
        return '-'

def ones_zeros_vals(text):
    vals = []
    for byte in text.split():
        vals.append(eval(f"0b{byte}"))

    return vals

def vals_to_text(vals):
    text = ''
    for val in vals:
        text += anti_ord(val)
    return text

def whole_process(binary_in):
    vals = ones_zeros_vals(binary_in)
    return vals_to_text(vals)


def main():
    text = '''
1000100 1100101 1100010 1100010 1101001
1100101 0100111 1110011 0100000 1101100
1100001 1110011

1110100 0100000 1101110 1100001 1101101
1100101 0100000 1101001 1110011 0100000
1011000 1100001

1110110 1101001 1100101 1110010
    '''
    print(whole_process(text))

if __name__ == "__main__":
    main()
