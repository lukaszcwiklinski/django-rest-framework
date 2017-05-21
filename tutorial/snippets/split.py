x = 'ala,ma,kota'

def split(text, delimiter=' '):
    result = []
    word = ''

    for letter in text:
        word += letter

        if delimiter == letter:
            result.append(word)
            word = ''

        result.append(word)
    return result


print split(x, ',')
