from Interface.menu import *
from time import sleep as slp


def calculaCpf(x):
    """
    -> Recebe um cpf(x) e retorna uma lista com:
    - Espaço 0: CPF(x)
    -Espaço 1: Espelho de x
    -Espaço 2: Lista vazia que será usada como intermediária entre 0 e 1
    :param x: cpf digitado
    :return: lista com 3 sublistas
    """
    import re
    valida = [[], [], []]
    while True:
        try:
            valida[0] = x[:9]   # Pega os 9 primeiros digitos do cpf
            for n in valida[0]:
                converte = int(n)
                # Converte  cada um para int e adiciona a segunda sublista
                valida[1].append(converte)
            c = 2
            for num in range(0, 2):
                # Multiplica eles por c e adiciona na terceira sublista
                for i in reversed(valida[1]):
                    valida[2].append(i * c)
                    c += 1
                soma = 0
                c = 2
                for v in valida[2]:
                    soma += v   # soma todos os valores da terceira lista
                resto = soma % 11   # tira o resto da divisão da soma por 11
                if resto < 2:  # Se o resto da divisão for menor que dois, o digito que será adicionado será 0
                    digi = 0
                else:  # Senão, será 11 - o resto da divisão
                    digi = 11 - resto
                # por fim, adiciona o digito na segunda lista
                valida[1].append(digi)
                # apaga o que tiver na lista 3, e repete o processo mais uma vez
                valida[2].clear()
            valida[0] = x.replace('.', '').replace('-', '')
        except:
            print(
                "Ocorreu um erro! Por favor informe o CPF no formato XXX.XXX.XXX-YY ou XXXXXXXXXYY")
            x = input("CPF: ")
            continue
        else:
            break
    return valida  # retorna a lista interia para continuar o processo


def validaCPF(y):
    """
    -> Recebe um cpf e o joga em CalculaCpf(), depois compara o CPF original com seu espelho e retorna se ele
    é valida(True) ou não(False)
    :param y: CPF que vai ser jogado em CalculaCpf()
    :return: Booleano(True/False)
    """
    final = calculaCpf(y)
    for v in final[1]:
        # tranforma o que estava em int pra str de novo
        final[2].append(str(v))
    final[2] = ''.join(final[2])    # junta em uma única string
    if final[0] == final[2]:  # Compara o resultado para ver se ambos são iguais
        return True  # Se sim, o CPF é válido
    else:
        return False  # Senão, ele é inválido


def findCliente(a, x, y=0, z=0):
    """
    -> Verifica se determinado cliente existe dentro do arquivo a(clientes.txt), procurando se o CPF(x) e a senha(y)
    existem dentro do arquivo.
    :param a: Arquivo onde ocorrerá a validação
    :param x: CPF
    :param y: Senha
    :param z: Número do Cartão
    :return: retorna um valor booleano referente ao fato do registro existir(True) ou não(False)
    """
    try:
        achou = False  # inicia a flag
        arq = open(a, 'r')  # abri o arquivo
        if y != 0 and z == 0:
            for linha in arq:
                # Transforma reg em uma variável de escopo global
                # transforma uma linha do arquivo em uma lista, separando pelo ';'
                reg = linha.split(';')
                if str(x) == reg[2] and str(y) == reg[4]:
                    achou = True  # caso ache, muda a flag para True e encerra o loop
                    break
                if achou:
                    break  # também encerra o loop de fora
        else:
            for linha in arq:
                # Transforma reg em uma variável de escopo global
                # transforma uma linha do arquivo em uma lista, separando pelo ';'
                reg = linha.split(';')
                if str(x) == reg[2] and str(z) == reg[3]:
                    achou = True  # caso ache, muda a flag para True e encerra o loop
                    break
                if achou:
                    break
    except Exception as erro:
        print(f"Ocorreu um erro de {erro} durante a procura do registro")
    else:
        if achou:
            return True  # Se achar vai retorna que achou(True)
        else:
            return False  # Se não achar vai retorna que não(False)
    finally:
        arq.close()


def validaTrans(i, x):
    """
    -> Recebe o valor da transação e imprime na tela se ela estará liberada ou não
    :param x: valor em reais da trasação
    :return: none
    """
    arq = open('clientes.txt', 'r')
    for linha in arq:
        reg = linha.split(";")
        if reg[2] == str(i):
            break
    valor  = float(x)
    if valor <= float(reg[5].replace('\n', '')):  # retira a quebra de linha para reg[5] poder ser convertido em int
        # pega reg(especificamente o elemento 5), que foi declarada global anteriormente, e compara com o valor da com_
        # pra para dizer se ela pode ser feita ou não.
        return True
    else:
        return False
    arq.close()


def arquivoExiste(x):
    """
    -> Verifica se o arquivo x existe dentro do projeto
    :param x: arquivo a ser procurado
    :return: booleano True(Existe)/False(Não Existe)
    """
    try:  # tenta ler o arquivo x, se não conseguir, retorna que ele não existi e viceversa
        a = open(x, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(x):
    """
    -> Cria um arquivo de nome x
    :param x: nome do arquivo
    :return: none
    """
    try:
        # Cria o arquivo x depois o fecha
        a = open(x, 'wt+')
        a.close()
    except:
        print(f"{cor[2]}Houve um erro na criação do arquivo!{cor[[0]]}")
    else:
        print(f"{cor[4]}Arquivo {a} criado com sucesso!{cor[0]}")


def cadastra(a, c):
    """
    -> cadastra os valores do objeto(c) no arquivo de nome a
    :param a: arquivo onde será cadastrado os dados de c
    :param c: objeto que está armazenando os dados
    :return: none
    """
    try:
        arq = open(a, 'a')  # Abri o arquivo em "modo de adição"
    except:
        print(f"{cor[2]}Houve um erro durante a execução do arquivo!{cor[0]}")
    else:
        try:
            # adiciona os elementos do objeto nele
            arq.write(f"{c.nome};{c.sobre};{c.cpf};{c.ncar};{c.senha};{c.limite}\n")
        except Exception as erro:
            # se ouver um erro, ele dirá que houve um erro em vez de encerrar
            print(f"{cor[2]}Houve um erro de {erro} durante a inscrição dos dados!{cor[0]}")
        else:
            # se tudo der certo, essa mensagem aparecerá
            titulo(f"{c.nome.upper()} {c.sobre.upper()} ADICIONADO AOS REGISTROS", c=5)
        finally:
            # e por fim, o arquivo será fechado
            arq.close()


def pedido(a, x, t, y):
    try:
        arq = open(a, 'a')
        arq.write(f"{y};{t};{x};EM ANALISE\n")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        titulo("PEDIDO ADICIONADO A FILA")
    finally:
        arq.close()


def vpedidos(a, x):
    try:
        arq = open(a, 'r')
        achou = False  # inicia a flag
        for linha in arq:
            # Transforma reg em uma variável de escopo global
            # transforma uma linha do arquivo em uma lista, separando pelo ';'
            ped = linha.split(';')
            if str(x) == ped[0]:
                achou = True  # caso ache, muda a flag para True e encerra o loop
                break
        if achou:
            print(
                f"Index: {ped[0]}\nCat: {ped[1]}\nValor: R$ {ped[2].replace('.',',')}\nEstado: {ped[3]}")
        else:
            titulo("PEDIDO NÃO ENCONTRADO!")
    except Exception as erro:
        print(f"Erro: {erro}")
    finally:
        arq.close()


def validaPedido(a, x):
    try:
        arq = open(a, 'r+')
        achou = False
        for linha in arq:
            ped = linha.split(';')
            if str(x) == ped[0] and ped[3] == "EM ANALISE\n":
                achou = True
                break
        string = ";".join(ped)
        index = encontrar_string(a, string)
        if achou:
            if validaTrans(str(x), ped[2]):
                alterar_linha(a, index, f"{ped[0]};{ped[1]};{ped[2]};APROVADO\n")
                print(f"Operação Finalizada! O pedido foi APROVADO!")
                redCred("clientes.txt", ped[0], ped[2])
            else:
                alterar_linha(a, index, f"{ped[0]};{ped[1]};{ped[2]};NEGADO\n")
                print(f"Operação Finalizada! O pedido foi NEGADO!")
        else:
            print("Pedido não encontrado")
        arq.close()
    except Exception as erro:
        print(f"Erro: {erro}")


def encontrar_string(path,string):
    with open(path,'r') as f:
        texto=f.readlines()
    for i in texto:
        if string in i:
            return texto.index(i)
    print('String não encontrada')


def alterar_linha(path,index_linha,nova_linha):
    with open(path,'r') as f:
        texto=f.readlines()
    with open(path,'w') as f:
        for i in texto:
            if texto.index(i)==index_linha:
                f.write(nova_linha+'\n')
            else:
                f.write(i)


def redCred(a, x, r):
    contas = open(a, 'r+')
    achou = False
    index = encontrar_string(a, x)
    for conta in contas:
        info = conta.split(";")
        if info[2] == str(x):
            achou = True
            break
    ns = float(info[5]) - float(r)
    alterar_linha(a, index, f"{info[0]};{info[1]};{info[2]};{info[3]};{info[4]};{ns}")
    contas.close()


def libSaldo(a, x, ad):
    contas = open(a,'r+')
    achou = False
    for conta in contas:
        info = conta.split(';')
        if info[2] == str(x):
            achou = True
            break
    index = encontrar_string(a, conta)
    novosd = float(info[5]) + float(ad)
    alterar_linha(a, index, f"{info[0]};{info[1]};{info[2]};{info[3]};{info[4]};{novosd}")
    print(f"Operação Finalizada! Adicionado mais R$ {float(ad):.2f} a conta de {info[0]} {info[1]}!")
    contas.close()


def verifCart(a, x):
    with open(a, 'r') as arq:
        achou = False
        for reg in arq:
            valor = reg.replace('\n','')
            if valor == str(x):
                achou = True
                break
    if achou:
        return False
    else:
        with open(a, 'a') as arq:
            arq.write(str(x)+'\n')
        return True


def realPag(a, x, i):
    with open(a, 'a') as arq:
        arq.write(f'{i};PAGAMENTO;{x};ESPERA')
    print("Pagamento Realizado! Esperando confirmação.")

def confPag(a, i):
    with open(a, 'r+') as arq:
        achou = False
        for reg in arq:
            info = reg.split(';')
            if info[0] == str(i) and info[3] == 'ESPERA\n':
                achou = True
                break
        index = encontrar_string(a, reg)
        if achou:
            alterar_linha(a, index, f'{info[0]};{info[1]};{info[2]};RECEBIDO')
            libSaldo('clientes.txt', i, info[2])
        else:
            print("Pagamento não encontrado!")