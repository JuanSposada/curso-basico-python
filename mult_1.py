# este programa imprime los resultados de estas 9 multiplicaciones


num = "1"

for i in range(1,10):

    num = int(num)

    print(f"{num} * {num} = ", num * num)

    num = str(num)

    num += "1"