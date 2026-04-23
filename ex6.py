def classificar_idade(idade):
    if idade < 12:
        return"Criança"
    elif 13 <= idade <= 17:
        return"Adolescente"
    elif 18 <= idade <= 59:
        return"Adulto"
    else:
        idade >60
        return"Idoso"
idades_teste = [6, 14, 30, 61]
for i in idades_teste:
    print(f"Idade {i}: {classificar_idade(i)}")