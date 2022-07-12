f = [0,1]

print("estos son los numeros de la serie de fibonacci")
print(f[0])
print(f[1])
for i in range(2, 100):
    f.append(f[i-1] + f[i-2])
    print(f[i])