# en base a una ruta remota, el progama muestra el nombre del equipo y de la ruta

# entrada de datos
ruta_remota = input('ingrese la ruta remota: ')
ruta_remota = ruta_remota.strip('//')
equipo = ruta_remota [:7]
ruta = ruta_remota [7:]
print(f'equipo = {equipo}; ruta = {ruta}')