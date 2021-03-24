# data = input()
# hola = []
# well = []

# for i in data:
#     if i.isalpha():
#         hola.append(i)
#     elif i.isinstance(int):
#         well.append(i)

# hola.sort()
# well.sort()
# print(hola+ ''+ well)

data = input()
hola = []
value = 0

for i in data:
    if i.isalpha():
        hola.append(i)
    else:
        value += int(i)

hola.sort()
if value!=0:
    hola.append(str(value))

print(''.join(hola))


