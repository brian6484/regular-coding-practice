
n = int(input())
hola = list(map(int, input().split()))
hola.sort()
#number of members in group
count = 0
#number of groups
group = 0

for i in hola:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group) 

#use list to sort

