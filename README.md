# PyBank
Um pseudo-aplicativo de um aplicativo de um banco escrito em python(A pseudo app off a bank application made in python).  

Funcionalidades:  

    * Cadastro de Clientes(Disponível) * Solicitação de Compras(Disponível) * Realização de Pagamentos(Disponével) * Validação de Transações(Disponível) * Histórico de Movimentações separado por categorias(Disponível) * Interface Gráfica(Indisponível)  
## Arquivos  
### Códigos Python  
   Ao todo foram criados 4 códigos em python que trabalham em conjunto e um arquivo de teste para funções que serão implementadas e correções de bugs. São eles:
### Main.py  
   Este é o arquivo principal do projeto, nele serão executadas as funções dos outros modulos. Ele é responsável por passar os dados as funções onde serão processados, fazer a chamada destas e garantir que todas trabalhem em conjunto.  
### Módulo Interface  
   Este modulo é responsável por trabalhar com todo o processamento de informações do sistema, sendo subdivido em três submódulos: menu, tarefas e usuarios.  
#### Submódulo "menu"  
   Este é responsável pela parte visual do sistema, garantindo que o usuário seja capaz de navegar de forma intuitiva pelo mesmo, além de garantir que o próprio designer do sistema seja agradável aos olhos.  
#### Submódulo "tarefas"
   Esse, por outro lado, cuída das requisições e tarefas que serão executadas pelo sistema. É o maior arquivo python e o que possui mais funções. Também cuida das redundâncias do sistema e sua integração com o *bando de dados*, o qual é simulado pelos arquivos .txt.
#### Submódulo "usuario"
   Por fim, esse é responsável por garantir a segurança e o acesso de ambos os tipos de usuário, root e cliente.
### Arquivos .txt 
