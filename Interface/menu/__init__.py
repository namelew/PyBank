cor = (
    #cores que vão ser utilizadas no programa
    '\033[m',  # 0 - sem cor
    '\033[1;30m',  # 1 - branco
    '\033[1;31m',  # 2 - vermelho
    '\033[1;32m',  # 3 - verde
    '\033[1;33m',  # 4 - amarelo
    '\033[1;34m',  # 5 - azul
    '\033[1;35m',  # 6 - roxo
    '\033[1;36m',  # 7 - magenta
    '\033[1;37m'  # 8 - cinza
)


def leiaInt(x):
    """
    -> Recebe um valor x e retorna x convertido em inteiro. Caso o valor não possa ser convertido
    a função dará erro e pedirá um novo valor.
    :param x: valor a ser convertido para inteiro
    :return: retorna o valor inteiro
    """
    while True:
        try:
            entrada = int(input(x))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Por favor digite um valor inteiro.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;34mO usuário encerrou a entrada de dados.\033[m")
            return 0
        else:
            return entrada


def leiaFloat(x):
    """
       -> Recebe um valor x e retorna x convertido em decimal. Caso o valor não possa ser convertido
       a função dará erro e pedirá um novo valor.
       :param x: valor a ser convertido para decimal
       :return: retorna o valor decimal
       """
    while True:
        try:
            entrada = float(input(x).replace(',', '.'))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Por favor digite um valor real.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;34mO usuário encerrou a entrada de dados.\033[m")
            return 0.0
        else:
            return entrada


def titulo(msg, c=0, tan=0):
    """
    -> Formata uma string em um título de tamanho e cor selecionável com uma linha em cima e outra em baixo
    e com o texto centralizado.
    :param msg: string
    :param c: cor do texto(padrão sem cor)
    :param tan: tamanho do texto(padrão len(string) + 4)
    :return: none
    """
    if tan == 0:
        tam = len(msg) + 4
    else:
        tam = tan
    print(f"{cor[c]}-"*tam)
    print(f"{msg}".center(tam))
    print(f"-{cor[c]}" * tam, end='')
    print(cor[0])


def linha(tam=42):
    """
    -> Retorna uma linha de tamanho selecionável
    :param tam: tamanho da linha(padrão 42)
    :return: retorna linha
    """
    return "-" * tam


def menu(list):
    """
    -> Recebe uma lista com n strings que representam as opções do menu, formata e exibi ela
    na tela. Depois, recebe um valor inteiro referente a opção selecionada e o retorna.
    :param list: lista com as strings das opções
    :return: opção selecionada
    """
    c = 1
    print(linha())
    for i in list:
        print(f"\033[0;33m{c} -\033[0;34m {i}\033[m")
        c += 1
    print(linha())
    o = leiaInt("Opção: ")
    return o
