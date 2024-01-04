from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/consulta_nfce', methods=['POST'])
def consulta_nfce():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'A URL não foi fornecida'}), 400

    url = data['url']

    pagina = requests.get(url)

    if pagina.status_code == 200:
        site = BeautifulSoup(pagina.content, 'html.parser')

        div_cnpj = site.find('div', string=lambda t: t and 'CNPJ:' in t)

        if div_cnpj:
            cnpj = div_cnpj.text.replace('CNPJ:', '').strip()
        else:
            cnpj = 'CNPJ não encontrado no HTML.'

        div_linhashade = site.find('div', {'class': 'linhaShade'})

        if div_linhashade:
            span_valor_total = div_linhashade.find('span', {'class': 'totalNumb txtMax'})

            if span_valor_total:
                valor_total = span_valor_total.text.strip()
            else:
                valor_total = 'Span com classe "totalNumb txtMax" não encontrado dentro da div com classe "linhaShade".'
        else:
            valor_total = 'Div com classe "linhaShade" não encontrada.'

        return jsonify({'CNPJ': cnpj, 'Valor Total': valor_total}), 200
    else:
        return jsonify({'error': f'Erro ao acessar a página. Código de status: {pagina.status_code}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
