n = int(input())

temp = []

for i in range(0, n):
    s = input()
    temp.append(s)

for i in range(0, n):
    for j in range(0, len(temp[i]), 2):
        print(temp[i][j], end='')
    print(end=' ')
    for j in range(1, len(temp[i]), 2):
        print(temp[i][j], end='')
    print()