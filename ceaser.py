import pprint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
NORM_DIST = {
    'a': 73,
    'b': 9,
    'c': 30,
    'd': 44,
    'e': 130,
    'f': 28,
    'g': 16,
    'h': 35,
    'i': 74,
    'j': 2,
    'k': 3,
    'l': 35,
    'm': 25,
    'n': 78,
    'o': 74,
    'p': 27,
    'q': 3,
    'r': 77,
    's': 63,
    't': 93,
    'u': 27,
    'v': 13,
    'w': 16,
    'x': 5,
    'y': 19,
    'z': 1
}

def ceasar(text, shift, rev=False):
    """ Positive shift goes to the right. e.g. a + 1 = b

    Parameters
    ----------
    text : str
        Input text to decode
    shift : int
        Amout to shift

    Returns
    -------
    str
        Decoded text """

    output = ''
    alph = ALPHABET if not rev else ''.join(reversed(ALPHABET))
    for char in text:
        if char.lower() not in alph:
            output += char
            continue

        n = alph.index(char.lower())
        letter = alph[(n + shift) % len(alph)]
        output += letter if char == char.lower() else letter.upper()
    return output


def vigenere(text, key):
    output = ''
    for i, char in enumerate(text):
        if char.lower() not in ALPHABET:
            output += char
            continue

        shift = ALPHABET.index(key[i % len(key)].lower())

        n = ALPHABET.index(char.lower())
        letter = ALPHABET[(n + shift) % len(ALPHABET)]
        output += letter if char == char.lower() else letter.upper()
    return output

def rail_fence(text1, text2, long_first = True):
    longer_text = [text1, text2][max(len(text1), len(text2)) != len(text1)]
    shorter_text = [text1, text2][longer_text == text1]
    output = ''
    for i in range(len(longer_text)):
        if long_first:
            output += longer_text[i]
        output += shorter_text[i] if i < len(shorter_text) else ''
        if not long_first:
            output += longer_text[i]
    return output

def letter_distribution(text):
    dist = {}
    for char in set(text):
        count_char = len(text.split(char)) - 1
        dist[char] = count_char
    return sorted(dist.items(), key=lambda x: -x[1])

def manual_unscramble(text):
    while True:
        new_word = input(">> ")
        

def book():
    # print(vigenere('ATTACKATDAWN', 'LEMON'))

    with open('./book.txt', 'r') as fin:
        txt = fin.read()

    print("Original")
    print(txt)

    do_stats = False
    if do_stats:
        print("----------")
        print("SOME STATS")
        print("----------")
        print("LENGTH:", len(txt))

        print("Cipher distribution:")
        pprint.pprint(letter_distribution(txt))
        # normal distribution
        print("Normal distribution:")
        pprint.pprint(sorted(NORM_DIST.items(), key=lambda x: -x[1]))


    # ceasar cipher
    do_ceasar = False
    if do_ceasar:
        print("---------------------")
        print("CEASAR CIPHER ATTEMPT")
        print("---------------------")
        for i in range(26):
            print(i, ceasar(txt, i))

    # vigenere cipher with multiple keys
    do_vigenere = True
    if do_vigenere:
        print("-----------------------")
        print("VIGENERE CIPHER ATTEMPT")
        print("-----------------------")
        keys = ['lights',
                'heartemoji',
                'admire',
                'murder',
                'kings',
                'corner',
                'kingscorner',
                'wimmer']
        keys = ['sunroom', 'treasureisland']
        for key in keys:
            print(key)
            print(vigenere(txt, key))

    do_rail_fence = False
    if do_rail_fence:
        print('-------------------------')
        print("RAIL FENCE CIPHER ATTEMPT")
        print('-------------------------')

        # Every other from period
        print('every other split at period')
        t1, t2 = txt.split('.')
        print("Longer first")
        print(rail_fence(t1, t2))
        print("Longer second")
        print(rail_fence(t1, t2, long_first=False))

        # Every other
        print("Every other")
        t1 = txt[:int(len(txt)/2)]
        t2 = txt[int(len(txt)/2):]
        print("Longer first")
        print(rail_fence(t1, t2))
        print("Longer second")
        print(rail_fence(t1, t2, False))

    do_manual_unscramble = False
    if do_manual_unscramble:
        manual_unscramble(txt)

def hoc_loco():
    with open("./hoc_loco.txt", 'r') as fin:
        txt = fin.read()

    print("HOC LOCO")
    print("original")
    print(txt)
    pprint.pprint(letter_distribution(txt))


    print(vigenere(txt, 'hoclocoius'))
    print(vigenere(txt, 'wimmer'))
    print(vigenere(txt, 'fequalse'))



    print("CEASAR CIPHER")
    for i in range(27):
        print(i, ceasar(txt[:-1], i, rev=False))
        print(i, ceasar(txt[:-1], i, rev=True))
        print()

def main():
    book()
    # hoc_loco()

if __name__ == "__main__":
    main()
