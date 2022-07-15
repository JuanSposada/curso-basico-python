# este programa transforma la fecha en otro formato

 

 

fecha = "12/22/21"

print(fecha)

fecha= fecha.split("/")

n= fecha.pop(0)

fecha.insert(1,n)

fecha[2] = "20" + fecha[2]

fecha = '-'.join(fecha)

print(fecha)

 