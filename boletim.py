# Média de aprovação = 7
print("=== SISTEMA ESCOLAR ===")
nota = float(input("informe a nota do aluno"))
 
if nota >= 7:
    print("APROVADO")
elif nota >= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
