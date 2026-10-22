
dna = input().strip().upper()
procurada = input().strip().upper()

encontrada = False

for i in range(len(dna) - len(procurada) + 1):
    if dna[i:i + len(procurada)] == procurada:
        print(f"Sequência encontrada na posição {i}")
        encontrada = True
        break

if not encontrada:
    print("Sequência não encontrada")
