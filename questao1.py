codigosEquipamentos = [101, 102, 103, 104, 105, 106, 107, 108]
statusManutencao = [0, 1, 0, 1, 0, 1, 1, 0]

def separarEquipamentos(codigosEquipamentos, statusManutencao):
    pendente = []
    concluido = []
    for i in range(len(codigosEquipamentos)):
        if statusManutencao[i] == 1:
            concluido.append(codigosEquipamentos[i])
        else:
            pendente.append(codigosEquipamentos[i])
    return pendente, concluido

pendente, concluido = separarEquipamentos(codigosEquipamentos, statusManutencao)
print("Pendentes: ", pendente)
print("Concluidos:", concluido)