def rev(sentence):
    sentence = sentence.split(' ')
    ret = ''
    for word in sentence[::-1]:
        ret += word + ' '
    return ret[:len(ret)-1]
