import os

os.system('cls')

# for e in range(10, 0, -1):
#     print(e)

n = int(input('Digite um número: '))


for e in range(1, n+1):
    if n % e == 0:
        print(e)
    # print(e)


