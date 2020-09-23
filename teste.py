#arquivo de teste para funções
a = 'clientes.txt'
x = "03044618223"
y = 122452
z = 0
try:
    achou = False  # inicia a flag
    arq = open(a, 'r')  # abri o arquivo
    if int(y) != 0 and int(z) == 0:
        for linha in arq:
            # Transforma reg em uma variável de escopo global
            reg = linha.split(';')  # transforma uma linha do arquivo em uma lista, separando pelo ';'
            if str(x) == reg[2] and str(y) == reg[4]:
                achou = True  # caso ache, muda a flag para True e encerra o loop
                break
            if achou:
                break  # também encerra o loop de fora
    else:
        for linha in arq:
            # Transforma reg em uma variável de escopo global
            reg = linha.split(';')  # transforma uma linha do arquivo em uma lista, separando pelo ';'
            if str(x) == reg[2] and str(z) == reg[3]:
                achou = True  # caso ache, muda a flag para True e encerra o loop
                break
            if achou:
                break
except Exception as erro:
    print(f"Ocorreu um erro de {erro} durante a procura do registro")
else:
    if achou:
        print(True)   # Se achar vai retorna que achou(True)
    else:
        print(False)  # Se não achar vai retorna que não(False)
finally:
    arq.close()
