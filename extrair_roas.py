from bs4 import BeautifulSoup
import re

with open('shopee_ads.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

nomes_campanha = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='ellipsis-content multi')]
roas_destino = [tag.get_text(strip=True) for tag in soup.find_all('span', class_='roi-value')]
roas_atual_all = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='report-format-number')]

campanhas_reais = []
for i in range(min(len(nomes_campanha), len(roas_destino), len(roas_atual_all))):
    # Limpa o ROAS destino: remove "R$", vírgulas, espaços, aspas, etc.
    roas_limpo = re.sub(r'[^\d.,]', '', roas_destino[i])
    roas_limpo = roas_limpo.replace(',', '.').replace('..', '.')
    # Considera campanha real se o ROAS for número e diferente de vazio
    if roas_limpo.replace('.', '', 1).isdigit():
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
