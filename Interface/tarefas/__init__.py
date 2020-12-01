from Interface import menu

class Cliente:
    def __init__(self, bd_clientes):
        self.a = bd_clientes

    def findCliente(self, x, y=0, z=0):
        """
        -> Verifica se determinado cliente existe dentro do arquivo a(clientes.txt), procurando se o CPF(x) e a senha(y)
        existem dentro do arquivo.
        :param x: CPF
        :param y: Senha
        :param z: Número do Cartão
        :return: retorna um valor booleano referente ao fato do registro existir(True) ou não(False)
        """
        try:
            achou = False
            arq = open(self.a, 'r')
            if y != 0 and z == 0:
                for linha in arq:
                    reg = linha.split(';')
                    if str(x) == reg[2] and str(y) == reg[4]:
                        achou = True
                        break
                    if achou:
                        break
            else:
                for linha in arq:
                    reg = linha.split(';')
                    if str(x) == reg[2] and str(z) == reg[3]:
                        achou = True
                        break
                    if achou:
                        break
            arq.close()
        except:
            menu.titulo("ERRO DURANTE A BUSCA DE REGISTRO", 2, 44)
        else:
            if achou:
                return True
            else:
                return False

    def cadastra(self, c):
        """
        -> cadastra os valores do objeto(c) no arquivo de nome a
        :param a: arquivo onde será cadastrado os dados de c
        :param c: objeto que está armazenando os dados
        :return: none
        """
        try:
            arq = open(self.a, 'a')
        except:
            print(f"{menu.cor[2]}Houve um erro durante a execução do arquivo!{menu.cor[0]}")
        else:
            try:
                arq.write(f"{c.nome};{c.sobre};{c.cpf};{c.ncar};{c.senha};{c.limite}\n")
            except Exception as erro:
                print(f"{menu.cor[2]}Houve um erro de {erro.__class__} durante a inscrição dos dados!{menu.cor[0]}")
            else:
                menu.titulo(f"{c.nome.upper()} {c.sobre.upper()} ADICIONADO AOS REGISTROS", c=5)
            finally:
                arq.close()

    def redCred(self, x, r):
        contas = open(self.a, 'r+')
        achou = False
        index = encontrarString(self.a, x)
        for conta in contas:
            info = conta.split(";")
            if info[2] == str(x):
                achou = True
                break
        ns = float(info[5]) - float(r)
        alterarLinha(self.a, index, f"{info[0]};{info[1]};{info[2]};{info[3]};{info[4]};{ns}")
        contas.close()

    def libSaldo(self, x, ad):
        contas = open(self.a, 'r+')
        achou = False
        for conta in contas:
            info = conta.split(';')
            if info[2] == str(x):
                achou = True
                break
        index = encontrarString(self.a, conta)
        novosd = float(info[5]) + float(ad)
        alterarLinha(self.a, index, f"{info[0]};{info[1]};{info[2]};{info[3]};{info[4]};{novosd}")
        print(f"Operação Finalizada! Adicionado mais R$ {float(ad):.2f} a conta de {info[0]} {info[1]}!")
        contas.close()

class Movimentos:
    def __init__(self, fila):
        self.a = fila
    
    def pedido(self, x, t, y):
        try:
            arq = open(self.a, 'a')
            arq.write(f"{y};{t};{x};EM ANALISE")
            arq.close()
        except:
            menu.titulo("ERRO DURANTE A EMISSÃO DO PEDIDO", 2, 44)
        else:
            menu.titulo("PEDIDO ADICIONADO A FILA")

    def validaPedido(self, x):
        try:
            arq = open(self.a, 'r+')
            achou = False
            cliente = Cliente('clientes.txt')
            for linha in arq:
                ped = linha.replace('\n', '').split(';')
                if str(x) == ped[0] and ped[3] == "EM ANALISE":
                    achou = True
                    break
            string = ";".join(ped)
            index = encontrarString(self.a, string)
            if achou:
                if validaTrans(str(x), ped[2]):
                    alterarLinha(self.a, index, f"{ped[0]};{ped[1]};{ped[2]};APROVADO\n")
                    print(f"Operação Finalizada! O pedido foi APROVADO!")
                    cliente.redCred(ped[0], ped[2])
                else:
                    alterarLinha(self.a, index, f"{ped[0]};{ped[1]};{ped[2]};NEGADO\n")
                    print(f"Operação Finalizada! O pedido foi NEGADO!")
            else:
                print("Pedido não encontrado")
            arq.close()
        except:
            menu.titulo("ERRO DURANTE A VALIDAÇÃO DO PEDIDO", 2, 44)

    def realPag(self, x, i):
        try:
            with open(self.a, 'a') as arq:
                arq.write(f'{i};PAGAMENTO;{x};ESPERA')
            print("Pagamento Realizado! Esperando confirmação.")
        except:
            menu.titulo("ERRO DURANTE A COMPUTAÇÃO DO PAGAMENTO", 2, 44)

    def confPag(self, i):
        with open(self.a, 'r+') as arq:
            achou = False
            cliente = Cliente('clientes.txt')
            for reg in arq:
                info = reg.replace('\n', '').split(';')
                if info[0] == str(i) and info[3] == 'ESPERA':
                    achou = True
                    break
            index = encontrarString(self.a, reg)
            if achou:
                alterarLinha(self.a, index, f'{info[0]};{info[1]};{info[2]};RECEBIDO')
                cliente.libSaldo(i, info[2])
            else:
                print("Pagamento não encontrado!")

def validaCPF(x):
    """
    -> Recebe um cpf(x) e retorna uma lista com:
    - Espaço 0: CPF(x)
    -Espaço 1: Espelho de x
    -Espaço 2: Lista vazia que será usada como intermediária entre 0 e 1
    :param x: cpf digitado
    :return: lista com 3 sublistas
    """
    valida = [[], [], []]
    while True:
        try:
            valida[0] = x[:9]
            for n in valida[0]:
                converte = int(n)
                valida[1].append(converte)
            c = 2
            for num in range(0, 2):
                for i in reversed(valida[1]):
                    valida[2].append(i * c)
                    c += 1
                soma = 0
                c = 2
                for v in valida[2]:
                    soma += v
                resto = soma % 11
                if resto < 2:
                    digi = 0
                else:
                    digi = 11 - resto
                valida[1].append(digi)
                valida[2].clear()
            valida[0] = x.replace('.', '').replace('-', '')
        except:
            print(
                "Ocorreu um erro! Por favor informe o CPF no formato XXX.XXX.XXX-YY ou XXXXXXXXXYY")
            x = input("CPF: ")
            continue
        else:
            break
    final = valida
    for v in final[1]:
        final[2].append(str(v))
    final[2] = ''.join(final[2])
    if final[0] == final[2]:
        return True
    else:
        return False


def validaTrans(idem, x=0):
    """
    -> Recebe o valor da transação e imprime na tela se ela estará liberada ou não
    :param x: valor em reais da trasação
    :param idem: localizador do cliente
    :return: none
    """
    arq = open('clientes.txt', 'r')
    for linha in arq:
        reg = linha.split(";")
        if reg[2] == str(idem):
            break
    valor = float(x)
    arq.close()
    if valor == 0.0:
        return False
    elif valor <= float(reg[5].replace('\n', '')):
        return True
    else:
        return False


def arquivoExiste(x):
    """
    -> Verifica se o arquivo x existe dentro do projeto
    :param x: arquivo a ser procurado
    :return: booleano True(Existe)/False(Não Existe)
    """
    try:
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
        a = open(x, 'wt+')
        a.close()
    except:
        print(f"{menu.cor[2]}Houve um erro na criação do arquivo!{menu.cor[0]}")
    else:
        print(f"{menu.cor[4]}Arquivo {a} criado com sucesso!{menu.cor[0]}")


def encontrarString(a, string):
    with open(a, 'r') as f:
        texto = f.readlines()
    for i in texto:
        if string in i:
            return texto.index(i)
    print('String não encontrada')


def alterarLinha(a, index, nova_linha):
    with open(a, 'r') as f:
        texto = f.readlines()
    with open(a, 'w') as f:
        for i in texto:
            if texto.index(i) == index:
                f.write(nova_linha+'\n')
            else:
                f.write(i)

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
