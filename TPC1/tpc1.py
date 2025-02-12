import re

def somador():
    texto = input("Escreva um texto: ")  # Recebe a entrada do usuário
    soma = 0
    ligado = True  # Estado inicial: ligado
    numeros = re.findall(r'\d+|[Oo][Nn]|[Oo][Ff][Ff]|=', texto)

    for item in numeros:
        item_lower = item.lower()

        if item_lower == "off":
            ligado = False
        elif item_lower == "on":
            ligado = True
        elif item == "=":
            print(f"Resultado da soma: {soma}")
        elif ligado:
            soma += int(item)

# Executa o programa
somador()