from bs4 import BeautifulSoup

# Abra o HTML exportado da Shopee Ads
with open('shopee_ads.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

resultados = []

# Tente identificar as linhas das campanhas (ajuste conforme o seu HTML)
# Aqui está uma lógica genérica: busca por linhas de tabela (tr)
for linha in soup.find_all('tr'):
    colunas = linha.find_all('td')
    if len(colunas) > 2:
        nome_campanha = colunas[0].get_text(strip=True)
        roas_destino = colunas[1].get_text(strip=True)
        roas_atual = colunas[2].get_text(strip=True)
        resultados.append({
            'campanha': nome_campanha,
            'roas_destino': roas_destino,
            'roas_atual': roas_atual
        })

print(f"Total de campanhas encontradas: {len(resultados)}")
print('-' * 50)
for r in resultados:
    print(f"Campanha: {r['campanha']}")
