from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

url = f'https://brasilapi.com.br/api/cep/v1/'

NORTE = ("AC", "AP", "AM", "PA", "RO", "RR", "TO")
NORDESTE = ("AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE")
CENTRO_OESTE =  ("DF", "GO", "MT", "MS")
SUDESTE = ("SP", "RJ", "MG", "ES")
SUL = ("PR", "SC", "RS")


def limpar_input(campo):
    campolimpo = campo.replace(".","").replace("/","").replace("-","").replace(" ","").replace("(","").replace(")","").replace("R$","")
    return campolimpo


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verficar_frete', methods=['GET','POST'])
def verificar_frete():
    if request.method == 'POST':
        cep = limpar_input(request.form.get('cep'))
        peso = request.form.get('peso', type=int, default=0 )

        if cep and peso and isinstance(peso, int) and peso >= 0:

            print(cep)
            response = requests.get(url + cep)

            if response.status_code == 200:
                data = response.json()
                estado = data['state']
                cidade = data['city']

                if estado in NORTE:
                    frete = 0.1
                elif estado in NORDESTE:
                    frete = 0.08
                elif estado in CENTRO_OESTE:
                    frete = 0.07
                elif estado in SUDESTE:
                    frete = 0.05
                elif estado in SUL:
                    frete = 0.06
                else:
                    frete = 0
                
                valor_entrega = peso * frete

                return render_template('index.html', estado=estado, cidade=cidade, valor_entrega=str(f'{valor_entrega:.2f}').replace(".", ","))
            elif 400 <= response.status_code < 500:
                return render_template('index.html', erro='CEP inválido')
            else:
                return render_template('index.html', erro='Falha na API')
        else:
            return render_template('index.html', erro='Dados inválidos' )
    return redirect('/')  

if __name__ == '__main__':
    app.run(debug=True)