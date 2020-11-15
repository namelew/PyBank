# arquivo de teste para funções
from Interface import tarefas
a = 'fila.txt'
i = "03044618223"
ad = '2000.0'
try:
    with open(a, 'r+') as arq:
        achou = False
        for reg in arq:
            info = reg.split(';')
            if info[0] == str(i) and info[3] == "ESPERA":
                achou = True
                break
        index = tarefas.encontrar_string(a, reg)
        if achou:
            tarefas.alterar_linha(a, index, f'{info[0]};{info[1]};{info[2]};RECEBIDO')
            tarefas.libSaldo('clientes.txt', i, info[2])
        else:
            print("Pagamento não encontrado!")
except Exception as erro:
    print(f"Ocorreu um erro de {erro} durante a procura do registro")
finally:
    # arq.close()
    print("Acabou")
