import matplotlib.pyplot as mpt
import pandas as pd

# pegando dados com o usuario
while True:
    dado = input('Insira o local, tipo de gasto, quantidade, horario separados por espaco ou escreva enter para gerar o grafico: ')
    if dado.lower() == 'enter':
        break
    else:
        confirma = input('Se os dados estiverem corretos, escreva sim, caso contrario, escreva nao: ')
        if confirma.lower() == 'sim':
            dado = dado.split()
            if len(dado) == 4:
                novos_dados = pd.DataFrame({
                    'Local': [dado[0]],
                    'Tipo': [dado[1]],
                    'Quantidade': [dado[2]],
                    'Horario': [dado[3]]
                })
            else:
                continue
        elif confirma.lower() == 'nao' or confirma.lower() == 'não':
            continue
        else:
            continue

arquivo = 'dados.csv'

novos_dados.to_csv(arquivo, mode = 'a', index=False, header=False)
