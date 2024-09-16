from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Configurar o Selenium para usar o Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem interface gráfica)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessar a página
driver.get('https://ge.globo.com/futebol/brasileirao-serie-a/')

# Esperar um pouco para garantir que o JavaScript tenha carregado o conteúdo
time.sleep(5)  

# Obter o HTML da página
html_content = driver.page_source
driver.quit()

# Analisar o HTML com BeautifulSoup
site = BeautifulSoup(html_content, 'html.parser')

# Salvar o HTML para análise
with open('pagina.html', 'w', encoding='utf-8') as file:
    file.write(site.prettify())

# Encontrar e imprimir as linhas da tabela
tabelaTimesLinhas = site.find_all('tr', class_='classificacao__tabela--linha')

# Listas 
times = []
pontos = []
partidasJogadas = []
vitorias = []
empates = []
derrotas = []
golsMarcados = []
golsSofridos = []
saldoDeGols = []


# Adicionar o nome do time para a lista
for linha in tabelaTimesLinhas:
    nome_time = linha.find('strong', class_='classificacao__equipes classificacao__equipes--nome')


    if nome_time:
        nome_time_text = nome_time.text.strip()
        times.append(nome_time_text)  # Adicionar o nome do time à lista
        print(f'Time: {nome_time_text}')
    else:
        print("Nome do time não encontrado em:", linha.prettify())

# Coletar dados de cada time
for linha in tabelaTimesLinhas:
    celulas = linha.find_all('td')

    if len(celulas) >= 8:
        pontos.append(celulas[0].text.strip())
        partidasJogadas.append(celulas[1].text.strip())
        vitorias.append(celulas[2].text.strip())
        empates.append(celulas[3].text.strip())
        derrotas.append(celulas[4].text.strip())
        golsMarcados.append(celulas[5].text.strip())
        golsSofridos.append(celulas[6].text.strip())
        saldoDeGols.append(celulas[7].text.strip())


# Criar o DataFrame com os dados coletados
df = pd.DataFrame({
    'Times': times,
    'Pontos': pontos,
    'Partidas Jogadas': partidasJogadas,
    'Vitórias': vitorias,
    'Empates': empates,
    'Derrotas': derrotas,
    'Gols Marcados': golsMarcados,
    'Gols Sofridos': golsSofridos,
    'Saldo de Gols': saldoDeGols
})

# Salvar o DataFrame em um arquivo Excel
df.to_excel('dados.xlsx', index=False, engine='openpyxl')

#Se tudo deu certo, isso aparece no fim do terminal
print("fim")
