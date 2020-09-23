from Interface import menu, tarefas, usuarios  # importando os pacotes
from time import sleep


class Cliente:  # classe onde será armazenado os dados
    def __init__(self, nome, sobre, cpf, ncar, senha, limite):
        self.nome = nome  # primeiro nome do cliente
        self.sobre = sobre  # ultimo nome do cliente
        self.cpf = cpf  # cpf do cliente
        self.ncar = ncar  # número do cartão
        self.senha = senha  # senha da conta
        self.limite = limite  # limite do cartão


arq = "clientes.txt"  # nome do arquivo
if not tarefas.arquivoExiste(arq):  # se ele não existir, o programa irá criar
    tarefas.criar(arq)
fila = "fila.txt"  # nome do arquivo
if not tarefas.arquivoExiste(arq):  # se ele não existir, o programa irá criar
    tarefas.criar(arq)
user = usuarios.Users
while True:
    menu.titulo('PyBANK', 6, 42)
    sleep(1)
    user = user(input('Tipo de Usuário: ').upper().strip())
    login = user.Login()
    if login:
        while True:  # Novamente a validação do CPF
            cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
            if tarefas.validaCPF(cpf):
                break
            print("Erro! CPF inválido, por favor digite novamente!")
        s = input("Senha: ")
        if tarefas.findCliente(arq, cpf, s, z=0):
            while True:
                op = menu.menu(['Novo Pedido', 'Visualizar Inf. Conta', 'Acompanhar Operações', 'Sair'])
                if op == 1:
                    # Verifica se os dados são válidos. Se sim, continua a validação, se não, encerra a operação e
                    # volta para a tela inicial.
                    cat = input("Categoria: ").lower().strip()
                    com = float(input("Valor da Compra: R$ ").replace(',', '.'))
                    tarefas.pedido(fila, com, cat, cpf)
                elif op == 2:
                    usuarios.Mostrar(arq, cpf)
                elif op == 3:
                    tarefas.vpedidos(fila, cpf)
                elif op == 4 or op == 0:
                    break
                else:
                    print("Opção Inválida! Digite novamente!")
        else:
            menu.titulo('CLIENTE NÃO ENCONTRADO', 2, 42)
    else:
        while True:
            op = menu.menu(['Cadastrar novo cliente', 'Validar operação de crédito', 'Liberar Crédito', 'Fechar'])
            if op == 1:  # Cadastro de Novo Cliente
                cliente = Cliente  # Criação do objeto 'cliente'
                menu.titulo('OPÇÃO 1', 6, 42)
                cliente.nome = input("Nome: ")
                cliente.sobre = input("Sobrenome(Ultimo Nome): ")
                while True:  # Validação do CPF
                    # Antes de adicionar o valor, o programa irá retirar os dois pontos e o traço, se houver.
                    cliente.cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
                    if tarefas.validaCPF(cliente.cpf):
                        break
                    print("Erro! CPF inválido, por favor digite novamente!")
                cliente.ncar = menu.leiaInt("Número do Cartão: ")
                cliente.senha = menu.leiaInt("Senha(6 Digitos): ")
                cliente.limite = menu.leiaFloat("Limite de Crédito: R$ ")
                tarefas.cadastra(arq, cliente)  # Escrita dos dados dentro do arquivo cliente
                sleep(1)
            elif op == 2:  # Validação de Operação de Crédito
                menu.titulo('OPÇÃO 2', 6, 42)
                while True:  # Novamente a validação do CPF
                    cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
                    if tarefas.validaCPF(cpf):
                        break
                    print("Erro! CPF inválido, por favor digite novamente!")
                nc = menu.leiaInt("N. Cartão: ")
                if tarefas.findCliente(arq, x=cpf, z=nc, y=0):
                # Verifica se os dados são válidos. Se sim, continua a validação, se não, encerra a operação e
                # volta para a tela inicial.
                    a = open("fila.txt", 'r')
                    if tarefas.validaTrans(cpf):
                        co = 0
                        for linha in a:
                            re = linha.split(';')
                            if re[0] == cpf:
                                break
                            co += 1
                        re.pop()
                        re.append("APROVADO")
                        tarefas.alterar_linha("fila.txt", co, re)
                    else:
                        co = 0
                        for linha in a:
                            re = linha.split(';')
                            if re[0] == cpf:
                                break
                            co += 1
                        re.pop()
                        re.append("NEGADO")
                        tarefas.alterar_linha("fila.txt", co, re)
                    a.close()
                    print(f"Operação Finalizada! O pedido foi {re[3]}")
                else:
                    menu.titulo('CLIENTE NÃO ENCONTRADO', 2, 42)
                    sleep(1)
            elif op == 3:
                print('Indisponível!')
            elif op == 4 or op == 0:  # Encerrar o programa
                break
            else:
                print("\033[0;31mOpção inválida! Por favor, digite uma das opções acima.\033[m")
            sleep(1)
    break
menu.titulo('TENHA UM BOM DIA', 6, 42)
