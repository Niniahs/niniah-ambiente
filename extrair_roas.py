from bs4 import BeautifulSoup

# Abra o arquivo HTML exportado da Shopee Ads
with open('shopee_ads.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Extrai todos os nomes de campanhas
nomes_campanha = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='ellipsis-content multi')]

# Extrai todos os ROAS Destino
roas_destino = [tag.get_text(strip=True) for tag in soup.find_all('span', class_='roi-value')]

# Extrai todos os ROAS Atual (aparece mais de uma vez, vamos pegar só os relevantes)
roas_atual_all = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='report-format-number')]

# Como podem haver muitos "report-format-number", normalmente os ROAS da campanha aparecem em algum padrão.
# Se for igual ao número de campanhas, já está certo.
# Senão, precisamos filtrar (me avise se sair trocado).

# Exibe os resultados juntos (ajustando pelo menor tamanho para não dar erro)
n = min(len(nomes_campanha), len(roas_destino), len(roas_atual_all))

print("Campanha | ROAS Destino | ROAS Atual")
print("-" * 50)
for i in range(n):
    print(f"{nomes_campanha[i]} | {roas_destino[i]} | {roas_atual_all[i]}")

# (Opcional) Salva em CSV para facilitar análise posterior
import csv
with open('resultado_shopee.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Campanha', 'ROAS Destino', 'ROAS Atual'])
    for i in range(n):
        writer.writerow([nomes_campanha[i], roas_destino[i], roas_atual_all[i]])

print("\nArquivo resultado_shopee.csv gerado com sucesso!")
