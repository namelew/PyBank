#arquivo de teste para funções
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
