def aplicar_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    valor_final = preco - desconto
    return valor_final
    
testes = [
    (100.0, 10),
    (250.50, 15),
    (89.90, 5)
]

for preco, desc in testes:
    resultado = aplicar_desconto(preco, desc)
    print(f"Preço: R$ {preco:.2f} | Desconto: {desc}% | Valor Final {resultado:.2f}")