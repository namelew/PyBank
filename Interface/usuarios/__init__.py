# cria dois usuários
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
