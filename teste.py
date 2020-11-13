# arquivo de teste para funções
from Interface import menu
a = 'fila.txt'
idem = "03044618223"
try:
    arq = open(a, 'r')
    categoria = []
    totalcat = []
    for linha in arq:
        registro = linha.split(";")
        if registro[0] == idem:
            categoria.append(registro[1])
    for c in range(0, len(categoria)):
        arq = open(a, 'r')
        soma = 0
        for line in arq:
            mark = line.split(";")
            if categoria[c] == mark[1]:
                soma += float(mark[2])
        totalcat.append(soma)
        arq.close()
    menu.titulo("Total de Gasto Por Categoria", tan=44)
    for cont in range(0, len(categoria)):
        print(f"{categoria[cont]:^22} {totalcat[cont]:^22}")
        print(menu.linha(44))
except Exception as erro:
    print(f"Ocorreu um erro de {erro} durante a procura do registro")
finally:
    # arq.close()
    print("Acabou")
