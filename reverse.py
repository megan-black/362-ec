def rev():
    sentence = input("Give me a sentence: ")
    sentence = sentence.split(' ')
    ret = ''
    for word in sentence[::-1]:
        ret += word + ' '
    return ret


print(rev())