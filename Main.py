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
    menu.titulo('PyBANK', 6, 44)
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
                op = menu.menu(['Novo Pedido',
                                "Realizar Pagamento",
                                'Visualizar Inf. Conta',
                                'Extrato da Conta',
                                'Sair'])
                if op == 1:
                    menu.titulo('NOVO PEDIDO', 6, 44)
                    print("- Se o valor da compra for 0 ou nulo, a ope_\nração será cancelada.")
                    cat = input("Categoria: ").upper().strip()
                    com = tarefas.leiaFloat("Valor da Compra: R$ ")
                    if com == 0.0:
                        menu.titulo("OPERAÇÃO CANCELADA", 2, 44)
                    else:
                        tarefas.pedido(fila, com, cat, cpf)
                elif op == 2:
                    menu.titulo('REAZLIZANDO PAGAMENTO', 6, 44)
                    print("- Se o valor do depósito for 0 ou nulo, a\noperação será cancelada.")
                    pag = tarefas.leiaFloat("Valor: R$ ")
                    if pag == 0.0:
                        menu.titulo("OPERAÇÃO CANCELADA", 2, 44)
                    else:
                        tarefas.realPag(fila, pag, cpf)
                elif op == 3:
                    menu.titulo('INFORMAÇÕES DA CONTA', 6, 44)
                    menu.Mostrar(arq, cpf)
                elif op == 4:
                    menu.titulo('EXTRATO', 6, 44)
                    op = menu.menu(['Histórico de Transações', 'Resumo do Extrato', 'Ambos', 'Sair'])
                    if op == 1:
                        menu.vpedidos(fila, cpf)
                    elif op == 2:
                        menu.listarMovimento(fila, cpf)
                    elif op == 3:
                        menu.titulo("Resumo", 5, 44)
                        menu.listarMovimento(fila, cpf)
                        menu.titulo("Histórico", 5, 44)
                        menu.vpedidos(fila, cpf)
                    elif op == 4:
                        menu.titulo("OPERAÇÃO FINALIZADA", tan=44)
                    else:
                        menu.titulo("OPÇÃO INVÁLIDA", 2, 44)
                elif op == 5 or op == 0:
                    break
                else:
                    print("Opção Inválida! Digite novamente!")
        else:
            menu.titulo('CLIENTE NÃO ENCONTRADO', 2, 44)
    else:
        senhaRT = input("Senha: ").lower()
        if senhaRT == "root":
            while True:
                op = menu.menu(['Cadastrar novo cliente', 'Validar operação de crédito', 'Validar Pagamento', 'Fechar'])
                if op == 1:
                    cliente = Cliente
                    menu.titulo('CADASTRO DE USUÁRIO', 6, 44)
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
                    menu.titulo('VALIDAÇÃO DE PEDIDO', 6, 44)
                    while True:
                        cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
                        if tarefas.validaCPF(cpf):
                            break
                        print("Erro! CPF inválido, por favor digite novamente!")
                    tarefas.validaPedido(fila, cpf)
                    sleep(1)
                elif op == 3:
                    menu.titulo('CONFIRMAÇÃO DE PAGAMENTO', 6, 44)
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
        else:
            menu.titulo("ACESSO NEGADO", 2, 44)
    break
menu.titulo('TENHA UM BOM DIA', 6, 44)
