t=str(input('Исходный текст:'))
c=str()
r=str()
m=[]
n=[]

for i, q in enumerate(t, start=1):
    m.append(ord(q))

for i, q in enumerate(m, start=1):
    a=chr(q+3)
    c+=a
print('Шифр:',c)


for i, q in enumerate(c, start=1):
    n.append(ord(q)-3)


for i, q in enumerate(n, start=1):
    a=chr(q)
    r+=a
print('Дешифровка:',r)
