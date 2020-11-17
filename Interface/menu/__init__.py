from Interface.tarefas import *
from time import sleep as slp
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


def linha(tam=44):
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


def vpedidos(a, x):
    try:
        arq = open(a, 'r')
        for linha in arq:
            op = linha.replace("\n", '').split(';')
            if op[0] == str(x):
                print("-" * 44)
                print(f"{op[0]:^11}{op[1]:^11}{op[2]:^10}{op[3]:^10}")
        print("-" * 44)
        arq.close()
    except Exception as erro:
        print(f"Erro: {erro}")
    finally:
        slp(1)


def listarMovimento(a, idem):
    arq = open(a, 'r')
    categoria = []
    totalcat = []
    for linha in arq:
        registro = linha.split(";")
        if registro[0] == idem and registro[1] not in categoria:
            categoria.append(registro[1])
    for c in range(0, len(categoria)):
        arq = open(a, 'r')
        soma = 0
        for line in arq:
            mark = line.split(";")
            if categoria[c] == mark[1] and mark[0] == idem:
                soma += float(mark[2])
        totalcat.append(soma)
        arq.close()
    titulo("Total Por Categoria", tan=44)
    for cont in range(0, len(categoria)):
        print(f"{categoria[cont]:^22} {totalcat[cont]:^22}")
        print("-" * 44)
    slp(1)


def Mostrar(arq, cpf):
    try:
        itens = {}
        a = open(arq, 'r')
        for linha in a:
            inf = linha.split(';')
            if inf[2] == cpf:
                itens['Nome'] = inf[0]
                itens['Sobrenome'] = inf[1]
                itens['CPF'] = inf[2]
                itens['N.Cartão'] = inf[3]
                itens['Senha'] = inf[4]
                itens['Limite'] = inf[5]
                for k, v in itens.items():
                    print(f"{k}: {v}")
                    slp(0.5)
                itens.clear()
                break
    except Exception as erro:
        print(erro)
    finally:
        a.close()
        slp(1)
