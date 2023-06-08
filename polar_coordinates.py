import cmath
n = input()
symbol = []
x1 = []
y1 = []

if n[0] == '-':
    x1.append(n[0])
    n = n[1:]
for i in range(len(n)):
    if n[i].isdigit() == False:
        symbol.append(i)
for i in range(len(n)):
    if i<symbol[0]:
        x1.append(n[i])
    elif  i<symbol[1]:
        y1.append(n[i])
x = int(''.join(x1))
y = int(''.join(y1))

print(abs(complex(x,y)))
print(cmath.phase(complex(x,y)))
