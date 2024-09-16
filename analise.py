import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

br24 = pd.read_excel('C:\\Users\\vinio\\OneDrive\\Área de Trabalho\\Brasileirão\\dados.xlsx')

br24['Valor de vitórias']= br24['Vitórias'] + (br24['Empates']/2)
br24['TotalVitórias'] = br24['Valor de vitórias'] / br24['Partidas Jogadas']
br24['pyth'] = br24['Gols Marcados']**2/(br24['Gols Marcados']**2 + br24['Gols Sofridos']**2)

br24 = br24.sort_values(by='pyth', ascending=False).reset_index()

sns.relplot(x='pyth', y='TotalVitórias', data=br24)
plt.xlabel('Expectativa Pitagórica')
plt.title('Expectativa Pitagórica vs % Vitórias')
plt.show()

print(br24)