class Users:
    def __init__(self, acesso):
        self.acesso = acesso

    def Login(self):
        if self.acesso == 'CLIENTE':
            return True
        if self.acesso == 'ROOT':
            return False
        else:
            print("Opção Inválida! Por favor, digite novamente!")


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
                itens.clear()
                break
    except Exception as erro:
        print(erro)
    finally:
        a.close()