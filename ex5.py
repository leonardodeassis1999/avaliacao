presentes = []

for i in range(5):
    item = input(f"Cadastre o {i+1}° item: ")
    presentes.append(item)
print("\nLista de Presentes:")
for indice, item in enumerate(presentes, start=1):
    print(f"{indice}. {item}")
print(f"\nTotal de itens cadastrados: {len(presentes)}")