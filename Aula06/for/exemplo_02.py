import os

os.system('cls')

lista_previsoes = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']

PREVISAO_BOA = 'Ensolarado'


for e in lista_previsoes:
    if e == 'PREVISAO_BOA':
        print(f'{e}, Aproveite o dia para passear.')
    else:
        print(f'{e}, Não esqueça o guarda-chuva.')




