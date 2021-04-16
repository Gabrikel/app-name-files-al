
def discMaker():
    global str
    str = input('Digite uma disciplina: ')
    if str[3] == 'a' or str[4] == 'e' or str[4] == 'i' or str[4] == 'o' or str[4] == 'u':
        str = str[0:3]
        return str
    else:
        str = str[0:4]
        return str
