n = int(input())

phone_book = {}

for i in range(0, n):
    a = input().strip().split(' ')
    phone_book[a[0]] = a[1]
try:
    while True:
        a = input()
        if len(a)> 0:
            print(a,'=',phone_book[a])
        else:
            print("Not found")
except EOFError:
    pass

