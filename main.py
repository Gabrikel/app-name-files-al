while True:
    print('---------------------------------------')

    name = input('Digite o nome do objeto: ')
    print('Ok!')

    def discMaker():
        global str
        str = input('Digite uma disciplina: ')
        if str[3] == 'a' or str[3] == 'e' or str[3] == 'i' or str[3] == 'o' or str[3] == 'u':
            str = str[0:4]
            return str
        if str[4] != 'a' or str[4] != 'e' or str[4] != 'i' or str[4] != 'o' or str[4] != 'u':
            str = str[0:3]
            return str
        else:
            str = str[0:4]
            return str
    discMaker()


    local = input('Qual a cidade? ')


    print('Okay, agora vou gerar o nome do arquivo pra você:')

    name = name.upper()
    str = str.upper()
    local = local.upper()

    name = name.replace(' ', '_')

    arquivo = '{DISC}-{NAME}-{LOCAL}-R00 - AL.ext'

    arquivo = arquivo.replace('{DISC}', str).replace('{NAME}', name).replace('{LOCAL}', local)

    print('  ')
    print(arquivo)
    print('  ')
    print('---------------------------------------')
    print('  ')






