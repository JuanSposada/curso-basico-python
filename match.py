# este programa calcula operaciones introduciendo dos valores y un operador

# Entrada de variables

valor_1 = int(input("ingrese el primer valor: "))
valor_2 = int(input("ingrese el segundo valor: "))
operador = input("ingrese el operador: ")

# implementacion de match case
match operador:
    case '+':
        print(f' 💻{valor_1} + {valor_2} = ', valor_1 + valor_2)
    case '-':
        print(f'🍨{valor_1} - {valor_2} =', valor_1 - valor_2)
    case '*':
        print(f'🌞{valor_1} * {valor_2} =', valor_1 * valor_2)
    case '/': 
        print(f'☘️ {valor_1} / {valor_2} =', valor_1 / valor_2)
    case _:
        print(f'😞 error!! operador no valido')


