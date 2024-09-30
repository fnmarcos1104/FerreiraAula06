import os 

os.system('cls')

# Estrutura de Repetição (While)

# login = 'Marcos'
# senha = '54321'
# leitura = ''
# leitura2 = ''

# while (leitura != senha and leitura2 != login):
#     leitura2 = input('Digite o login: ')
#     leitura = input('Digite a senha: ')
#     if leitura == senha and leitura2 == login:
#         print('Acesso liberado')
#     else:
#         print('Login ou senha incorretos')



# contador = 10
# while contador != 0:
#     print(contador)
#     contador -= 1



# s = 0 
# c = 1
# while c < 4:
#     n = int(input('Informe um número: '))
#     s += n
#     c += 1
# print('O total é ', s)


# n = ''
# resposta = 'S'
# while resposta != 'N':
#     n = input('Informe um texto: ')
#     resposta = input('QUER CONTINUAR S/N: ')[0].upper()
# print(n)


n = s = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s = s + n
print(s)