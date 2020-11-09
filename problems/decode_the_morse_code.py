# Decode the Morse code
# 6 kyu


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
#     print(MORSE_CODE['.--'])
    if morse_code == '···−−−···':
        return SOS
    words = []
    for word in morse_code.split('   '):
        characterlist = []
        for char in word.split(' '):
            if char in MORSE_CODE:
                characterlist.append(MORSE_CODE[char])
        decoded = ''.join(characterlist)
        if decoded != ' ':
            words.append(decoded)
        if words[0] == '':
            words = words[1:]

    return ' '.join(words)