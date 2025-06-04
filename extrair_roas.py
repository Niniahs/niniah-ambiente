from bs4 import BeautifulSoup
import re

with open('shopee_ads.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

nomes_campanha = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='ellipsis-content multi')]
roas_destino = [tag.get_text(strip=True) for tag in soup.find_all('span', class_='roi-value')]
roas_atual_all = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='report-format-number')]

# Palavras típicas de banners/shopee, customize se necessário
palavras_banners = [
    "Quais", "Saiba", "Ative", "Seu saldo", "Anúncio GMV Max",
    "Melhore", "Aprenda", "Anúncio Automático de Produto", "Anúncio de Loja"
]

campanhas_reais = []
for i in range(min(len(nomes_campanha), len(roas_destino), len(roas_atual_all))):
    nome = nomes_campanha[i]
    # Verifica se o nome não começa com nenhuma palavra de banner
    if not any(nome.startswith(p) for p in palavras_banners):
        campanhas_reais.append((nome, roas_destino[i], roas_atual_all[i]))

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
