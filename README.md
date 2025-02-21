# 🚚 Calculadora de Frete

Este projeto é um aplicativo web para calcular o frete de uma encomenda com base no **CEP** de destino e no **peso** informado. Ele utiliza a **BrasilAPI** para obter informações do CEP e aplica uma taxa de frete baseada na região do Brasil.

## 📌 Funcionalidades

- Interface amigável para inserir **CEP** e **peso da encomenda**.
- Consulta a **BrasilAPI** para obter informações do local.
- Cálculo automático do valor do frete baseado na região.
- Exibição do resultado diretamente na interface.
- Tratamento de erros para CEPs inválidos ou falhas na API.

## 🛠️ Tecnologias Utilizadas

- **Flask** (Backend)
- **BrasilAPI** (Consulta de CEP)
- **HTML + Bootstrap** (Frontend)
- **JavaScript** (Melhoria na experiência do usuário)

## 📂 Estrutura do Projeto

```plaintext
📁 projeto_frete/
│-- 📄 app.py          # Código principal do servidor Flask
│-- 📄 index.html      # Interface web do projeto
│-- 📁 templates/      # Diretório onde ficam os arquivos HTML (se necessário)
│-- 📁 static/         # Diretório para arquivos CSS e JS (caso adicione estilos)
```

## 🚀 Como Rodar o Projeto

### 📌 Pré-requisitos

- Python 3 instalado
- Biblioteca Flask instalada (`pip install flask`)
- Conexão com a internet (para consultar a BrasilAPI)

### 📌 Passo a passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto_frete.git
   cd projeto_frete
   ```

2. Instale as dependências:
   ```bash
   pip install flask requests
   ```

3. Execute o servidor:
   ```bash
   python app.py
   ```

4. Acesse no navegador:
   ```
   http://127.0.0.1:5000
   ```

## 🎯 Como Funciona?

1. O usuário informa o **CEP** e o **peso** da encomenda.
2. O backend consulta a **BrasilAPI** para identificar o **estado** e a **cidade** do CEP informado.
3. O sistema aplica uma taxa de frete de acordo com a região:
   - Norte: **R$ 0,10 por grama**
   - Nordeste: **R$ 0,08 por grama**
   - Centro-Oeste: **R$ 0,07 por grama**
   - Sudeste: **R$ 0,05 por grama**
   - Sul: **R$ 0,06 por grama**
4. O resultado do cálculo é exibido para o usuário.

## 🔧 Melhorias Futuras

- Implementação de um design personalizado com **CSS**.
- Adição de um banco de dados para armazenar cálculos realizados.
- Melhorias na **validação do CEP** e tratamento de erros.
- Opção para calcular o prazo estimado de entrega.

## 📜 Licença

Este projeto está licenciado sob a **Licença MIT** - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

👨‍💻 **Desenvolvido por Pedro Vitor**

