"""este programa te da el area de un circulo en base al radio"""

radius = int(input("ingrese el radio del circulo:"))
PI = 3.1416
area = PI * (radius ** 2)
area = round(area, 1)
print("el area del circulo es:", area)
