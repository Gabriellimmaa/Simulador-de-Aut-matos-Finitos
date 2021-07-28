
with open('automato1.txt', 'r') as f:
    lines = [line.rstrip() for line in f]
print(f"inicial: {lines[0]}")
print(f"finais: {lines[1]}")
print(f"transicoes: {lines[2]}")

# manipulando as transicoes e adicionando na lista
transicoes = lines[2].split(',')
t = []
for x in transicoes:
    itemString = x.replace('(', '')
    itemString = itemString.replace(')', '')
    item = itemString.split("|")
    t.append(item)

# pegando os simbolos utilizados apartir das transicoes
simbolos = []
for x in t:
    if x[1] not in simbolos:
        simbolos.append(x[1])
aceitacao = list(map(int, "0"))   # transformando estados de aceitação em inteiros

# pegando as entradas para testes
with open('automato1_entrada.txt', 'r') as f:
    entradas = [line.rstrip() for line in f]
c = 0
cadeias = []
for entrada in entradas:
    c+=1
    cad = list(entrada)
    cadeias.append(cad)
f.close()

def percorreCadeia(cadeiaAtual, estadoAtual):
    # analisa a cadeia vazia
    if(cadeiaAtual == ['$']):
        if(estadoAtual in aceitacao):
            return True
        return False

    # verifica se o estado final da cadeia é um de aceitação
    if(cadeiaAtual == []):
        if(estadoAtual in aceitacao):
            return True
        return False

    # compara o primeiro símbolo da cadeia com todas as transições possíveis
    simboloAtual = cadeiaAtual[0]
    for i in range(len(t)):
        transicaoAtual = t[i]
        estadoInicialT = int(transicaoAtual[0])
        simboloT = transicaoAtual[1]
        if((estadoInicialT == estadoAtual) and (simboloT == simboloAtual)):
            # muda o estado atual
            estado = int(transicaoAtual[2])
            # passa para o próximo símbolo da cadeia
            cadeiaNova = cadeiaAtual[1:]
            # recursividade (com próximo símbolo e novo estado atual)
            if(percorreCadeia(cadeiaNova,estado)):
                return True
    return False

print("")
with open('automato3_resultado.txt', 'w') as f:
    # aceitação ou rejeição de cada cadeia de entrada
    for j in range(int(c)):
        cadeiaAtual = cadeias[j]
        # percorre cada cadeia (o estado 0 é sempre o estado inicial)
        if(percorreCadeia(cadeiaAtual,0)):
            print("aceita")
            f.writelines("aceita\n")
        else:
            print("rejeita")
            f.writelines("rejeita\n")

print("\nResultado registrado em 'automato1_resultado.txt'")
input()
