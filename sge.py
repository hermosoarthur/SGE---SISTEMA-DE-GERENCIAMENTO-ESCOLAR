print("==================================================")
print("   SGE - SISTEMA DE GERENCIAMENTO ESCOLAR")
print("==================================================")

nome_aluno = input("Digite o Nome do Aluno: ")
codigo_disciplina = input("Digite o Código da Disciplina (CÓD. DISC.): ") 

notas = []
avaliacoes = ["P1", "P2", "PD", "Pp1", "Pp2", "Pp3"] 

print("\n--- Preenchimento de Notas ---")


for prova in avaliacoes:

    while True:
        try:
            entrada_nota = input(f"Informe a nota da {prova} (0.0 a 10.0): ")
            nota = float(entrada_nota.replace(',', '.'))
            
            
            if nota >= 0.0 and nota <= 10.0:
                notas.append(nota)
                break 
            else:
                print(" -> AVISO: Nota inválida! O valor deve ser entre 0.0 e 10.0. Tente novamente.")
        except ValueError:
            print(" -> ERRO: Formato incorreto. Digite apenas números.")


p1 = notas[0]
p2 = notas[1]
pd = notas[2]
pp1 = notas[3]
pp2 = notas[4]
pp3 = notas[5]


media_final = (p1 + p2 + pd + pp1 + pp2 + pp3) / 6 


print("\n==================================================")
print("                 STATUS FINAL")
print("==================================================")
print(f"Nome do Aluno: {nome_aluno}")
print(f"Código da Disciplina: {codigo_disciplina}") 
print(f"Média Final: {media_final:.2f}")


if media_final >= 6.0: 
    print("Status: Aluno Aprovado")
elif media_final >= 4.0 and media_final <= 5.9: 
    print("Status: Aluno em Recuperação") 
else: 
    print("Status: Aluno Reprovado") 
print("==================================================")