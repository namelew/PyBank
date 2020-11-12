# PyBank
Um pseudo-aplicativo de um aplicativo de um banco escrito em python(A pseudo app off a bank application made in python).  

## Funcionalidades  

 * Cadastro de Clientes(Disponível)
 * Solicitação de Compras(Disponível)
 * Realização de Pagamentos(Disponével)
 * Validação de Transações(Disponível)
 * Histórico de Movimentações separado por categorias(Disponível)
 * Interface Gráfica(Indisponível)  
## Arquivos  
### Códigos Python  
   Ao todo foram criados 4 códigos em python que trabalham em conjunto e um arquivo de teste para funções que serão implementadas e correções de bugs. São eles:
### Main.py  
   Este é o arquivo principal do projeto, nele serão executadas as funções dos outros modulos. Ele é responsável por passar os dados as funções onde serão processados, fazer a chamada destas e garantir que todas trabalhem em conjunto.  
 * Um pedaço do código Main.py, utilizando as funções vpedidos(), validaCPF(), realPagamento() e Mostrar():
 ```
elif op == 2:
    while True:
      cpf = input("CPF: ").replace('.', '').replace('.', '').replace('-', '')
      if tarefas.validaCPF(cpf):
         break
      print("Erro! CPF inválido, por favor digite novamente!")
    pag = float(input("Pagamento: R$ ").replace(',', '.'))
    tarefas.realPag(fila, pag, cpf)
elif op == 3:
    usuarios.Mostrar(arq, cpf)
elif op == 4:
    tarefas.vpedidos(fila, cpf)
 ```
### teste.py
Este é um arquivo exclusivo para debuging e teste de funções que serão implementadas nos módulos do projeto.   
 * Exemplo do pré código da função vpedidos():
```
a = 'fila.txt' 
try:
    arq = open(a, 'r')
    for linha in arq:
        op = linha.replace("\n", '').split(';')
        print("-"*44)
        print(f"{op[0]:^11}{op[1]:^11}{op[2]:^10}{op[3]:^10}")
    print("-" * 44)
except Exception as erro:
    print(f"Ocorreu um erro de {erro} durante a procura do registro")
finally:
    arq.close()
 ```
 * Função implementada no submódulo "tarefas":
 ```
 def vpedidos(a, x):
    try:
        arq = open(a, 'r')
        for linha in arq:
            op = linha.replace("\n", '').split(';')
            print("-" * 44)
            print(f"{op[0]:^11}{op[1]:^11}{op[2]:^10}{op[3]:^10}")
        print("-" * 44)
    except Exception as erro:
        print(f"Erro: {erro}")
    finally:
        arq.close()
```
### Módulo Interface  
   Este modulo é responsável por trabalhar com todo o processamento de informações do sistema, sendo subdivido em três submódulos: menu, tarefas e usuarios.  
#### Submódulo "menu"  
   Este é responsável pela parte visual do sistema, garantindo que o usuário seja capaz de navegar de forma intuitiva pelo mesmo, além de garantir que o próprio designer do sistema seja agradável aos olhos. Possue as seguintes funções:
##### 1. titulo()
Esta função é responsável por imprimir na tela, uma mensagem com formatação de título. Desta forma, é responsável "por receber e orientar" o usuário dentro do programa.
 * Código da Função dentro do módulo "menu":
 ```
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
 ```
##### 2. linha()
Basicamente, imprime uma linha na tela de tamanho manipulável. Usada para simular "multiplas páginas" dentro do programa.
 * Código da Função dentro do módulo "menu":
 ```
def linha(tam=42):
    """
    -> Retorna uma linha de tamanho selecionável
    :param tam: tamanho da linha(padrão 42)
    :return: retorna linha
    """
    return "-" * tam
 ```
##### 3. menu()
Recebe uma lista de strings que armazena as opções do programa. Ajuda o usuário a visualizar as funcionalidades do sistema e tomar decisões baseadas nelas.
 * Código da Função dentro do módulo "menu":
 ```
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
 ```
#### Submódulo "tarefas"
   Esse, por outro lado, cuída das requisições e tarefas que serão executadas pelo sistema. É o maior arquivo python e o que possui mais funções. Também cuida das redundâncias do sistema e sua integração com o *bando de dados*, o qual é simulado pelos arquivos .txt.
##### 1. calcularCpf()
Utilizada durante o processo de cadastro de clientes. Essa função recebe um valor que é considerado como cpf e gera um espelho desse que será lido como o cpf verdadeiro. No fim, retorna a lista com ambos os cpf's que será comparada por outra função.
 * Código da Função dentro do módulo "tarefas":
 ```
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
                else:o
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
    return valida
 ```
##### 2. validaCPF()
Recebe um valor que é identificado como cpf e retorna um valor booleano referente ao caso do cpf ser válido ou não.
 * Código da Função dentro do módulo de "tarefas":
 ```
 def validaCPF(y):
    """
    -> Recebe um cpf e o joga em CalculaCpf(), depois compara o CPF original com seu espelho e retorna se ele
    é valida(True) ou não(False)
    :param y: CPF que vai ser jogado em CalculaCpf()
    :return: Booleano(True/False)
    """
    final = calculaCpf(y)
    for v in final[1]:
        final[2].append(str(v))
    final[2] = ''.join(final[2])
    if final[0] == final[2]:
        return True
    else:
        return False
 ```
##### 3. findCliente()
Determina se um cliente existe ou não dentro do banco, buscando ele pelo cpf, ou o número do cartão, e a sua senha.
 * Código da Função dentro do módulo "tarefas":
 ```
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
        achou = False
        arq = open(a, 'r')
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
    except Exception as erro:
        print(f"Ocorreu um erro de {erro} durante a procura do registro")
    else:
        if achou:
            return True
        else:
            return False
    finally:
        arq.close()
 ```
##### 4. validaTrans()
Define se uma transição será liberada ou não através de um retorno booleano.
 * Código da Função dentro do módulo "tarefas":
 ```
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
    if valor <= float(reg[5].replace('\n', '')):
        return True
    else:
        return False
    arq.close()
 ```
##### 5. arquivoExiste()
Verifica se determinado arquivo existe dentro do projeto. É usado dentro do Main.py para criar os arquivos .txt, caso eles não existão.
 * Código da Função dentro do módulo "tarefas":
 ```
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
 ```
 * Uso dentro do arquivo "Main.py":
 ```
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
 ```
##### 6. criar()
Cria um arquivo .txt de nome selecionável. É usado para criar os arquivos necessários para o projeto funcionar.
 * Código da Função dentro do módulo "tarefas":
 ```
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
        print(f"{cor[2]}Houve um erro na criação do arquivo!{cor[[0]]}")
    else:
        print(f"{cor[4]}Arquivo {a} criado com sucesso!{cor[0]}")
 ```
  * Uso da função dentro de Main.py:
  ```
arq = "clientes.txt"
if not tarefas.arquivoExiste(arq):
    tarefas.criar(arq)
  ```
##### 7. cadastra()
Função responsável por cadastrar os clientes no sistema. Ela recebe os dados e os insere no arquivo .txt que simula a entidade "cliente".
 * Código da Função dentro do módulo "tarefas":
 ```
 def cadastra(a, c):
    """
    -> cadastra os valores do objeto(c) no arquivo de nome a
    :param a: arquivo onde será cadastrado os dados de c
    :param c: objeto que está armazenando os dados
    :return: none
    """
    try:
        arq = open(a, 'a')
    except:
        print(f"{cor[2]}Houve um erro durante a execução do arquivo!{cor[0]}")
    else:
        try:
            arq.write(f"{c.nome};{c.sobre};{c.cpf};{c.ncar};{c.senha};{c.limite}\n")
        except Exception as erro:
            print(f"{cor[2]}Houve um erro de {erro} durante a inscrição dos dados!{cor[0]}")
        else:
            titulo(f"{c.nome.upper()} {c.sobre.upper()} ADICIONADO AOS REGISTROS", c=5)
        finally:
            arq.close()
 ```
##### 8. pedido()
Cria um pedido e o insere na entidade "fila", onde ficam salvos todas as movimentações feitas no sistema.
 * Código da Função do módulo "tarefas":
 ```
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
 ```
##### 9. vpedidos()
Abre uma tabela que mostra ao usuário, o identificador da movimentação, a sua categoria, o valor da movimentação e o seu estado atual.
 * Código da Função no módulo "tarefas":
 ```
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
 ```
##### 10. validaPedido()
##### 11. encontrar_string()
##### 12. alterar_linha()
##### 13. redCred()
##### 14. libSaldo()
##### 15. verifCart()
##### 16. realPag()
##### 17. confPag()
#### Submódulo "usuario"
   Por fim, esse é responsável por garantir a segurança e o acesso de ambos os tipos de usuário, root e cliente. Possue apenas a classe Users que possue e atributos funções que realizam essas funções.
##### Class Users
### Arquivos ".txt"  
#### clientes.txt
#### cartoes.txt
#### fila.txt
