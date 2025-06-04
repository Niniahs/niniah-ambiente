from bs4 import BeautifulSoup

with open('shopee_ads.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

nomes_campanha = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='ellipsis-content multi')]
roas_destino = [tag.get_text(strip=True) for tag in soup.find_all('span', class_='roi-value')]
roas_atual_all = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='report-format-number')]

import re
# Apenas campanhas que possuem ROAS Destino numérico
campanhas_reais = []
for i in range(min(len(nomes_campanha), len(roas_destino), len(roas_atual_all))):
    # Se o ROAS Destino é um número (exclui banners e propagandas)
    if re.match(r'^\d+(\.\d+)?$', roas_destino[i].replace(',', '.').strip()):
        campanhas_reais.append((nomes_campanha[i], roas_destino[i], roas_atual_all[i]))

print("Campanha | ROAS Destino | ROAS Atual")
print("-" * 50)
for c in campanhas_reais:
    print(f"{c[0]} | {c[1]} | {c[2]}")

import csv
with open('resultado_shopee.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Campanha', 'ROAS Destino', 'ROAS Atual'])
    for c in campanhas_reais:
        writer.writerow([c[0], c[1], c[2]])

print("\nArquivo resultado_shopee.csv gerado só com campanhas reais!")
