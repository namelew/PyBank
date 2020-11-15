from Interface import menu, tarefas, usuarios
from time import sleep


class Cliente:
    def __init__(self, nome, sobre, cpf, ncar, senha, limite):
        self.nome = nome
        self.sobre = sobre
        self.cpf = cpf
        self.ncar = ncar
        self.senha = senha
        self.limite = limite


arq = "clientes.txt"
if not tarefas.arquivoExiste(arq):
    tarefas.criar(arq)
fila = "fila.txt"
if not tarefas.arquivoExiste(arq):
    tarefas.criar(arq)
cart = "cartoes.txt"
if not tarefas.arquivoExiste(cart):
    tarefas.criar(cart)
user = usuarios.Users
while True:
    menu.titulo('PyBANK', 6, 42)
    sleep(1)
    user = user(input('Tipo de Usuário: ').upper().strip())
    login = user.Login()
    if login:
        while True:
            cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
            if tarefas.validaCPF(cpf):
                break
            print("Erro! CPF inválido, por favor digite novamente!")
        s = input("Senha: ")
        if tarefas.findCliente(arq, cpf, s, z=0):
            while True:
                op = menu.menu(['Novo Pedido', "Realizar Pagamento", 'Visualizar Inf. Conta', 'Extrato da Conta', 'Sair'])
                if op == 1:
                    cat = input("Categoria: ").upper().strip()
                    com = float(input("Valor da Compra: R$ ").replace(',', '.'))
                    tarefas.pedido(fila, com, cat, cpf)
                elif op == 2:
                    pag = float(input("Pagamento: R$ ").replace(',', '.'))
                    tarefas.realPag(fila, pag, cpf)
                elif op == 3:
                    usuarios.Mostrar(arq, cpf)
                elif op == 4:
                    tarefas.vpedidos(fila, cpf)
                    tarefas.listarMovimento(fila, cpf)
                elif op == 5 or op == 0:
                    break
                else:
                    print("Opção Inválida! Digite novamente!")
        else:
            menu.titulo('CLIENTE NÃO ENCONTRADO', 2, 42)
    else:
        while True:
            op = menu.menu(['Cadastrar novo cliente', 'Validar operação de crédito', 'Validar Pagamento', 'Fechar'])
            if op == 1:
                cliente = Cliente
                menu.titulo('OPÇÃO 1', 6, 42)
                cliente.nome = input("Nome: ")
                cliente.sobre = input("Sobrenome(Ultimo Nome): ")
                while True:
                    cliente.cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
                    if tarefas.validaCPF(cliente.cpf):
                        break
                    print("Erro! CPF inválido, por favor digite novamente!")
                while True:
                    cliente.ncar = menu.leiaInt("Número do Cartão: ")
                    if tarefas.verifCart(cart, cliente.ncar):
                        break
                    print("Número já existente! Por favor, digite novamente!")
                cliente.senha = menu.leiaInt("Senha(6 Digitos): ")
                cliente.limite = menu.leiaFloat("Limite de Crédito: R$ ")
                tarefas.cadastra(arq, cliente)
                sleep(1)
            elif op == 2:
                menu.titulo('OPÇÃO 2', 6, 42)
                while True:
                    cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
                    if tarefas.validaCPF(cpf):
                        break
                    print("Erro! CPF inválido, por favor digite novamente!")
                tarefas.validaPedido(fila, cpf)
                sleep(1)
            elif op == 3:
                while True:
                    cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
                    if tarefas.validaCPF(cpf):
                        break
                    print("Erro! CPF inválido, por favor digite novamente!")
                tarefas.confPag(fila, cpf)
            elif op == 4 or op == 0:
                break
            else:
                print("\033[0;31mOpção inválida! Por favor, digite uma das opções acima.\033[m")
            sleep(1)
    break
menu.titulo('TENHA UM BOM DIA', 6, 42)
