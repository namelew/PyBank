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
##### 2. linha()
##### 3. menu()
#### Submódulo "tarefas"
   Esse, por outro lado, cuída das requisições e tarefas que serão executadas pelo sistema. É o maior arquivo python e o que possui mais funções. Também cuida das redundâncias do sistema e sua integração com o *bando de dados*, o qual é simulado pelos arquivos .txt.
##### 1. calcularCpf()
##### 2. validaCPF()
##### 3. findCliente()
##### 4. validaTrans()
##### 5. arquivoExiste()
##### 6. criar()
##### 7. cadastra()
##### 8. pedido()
##### 9. vpedidos()
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
### Arquivos ".txt"  
#### clientes.txt
#### cartoes.txt
#### fila.txt
