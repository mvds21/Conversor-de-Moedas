# Conversor-de-Moedas

# 💱 Conversor de Moedas com Gráfico Histórico (Currency Converter with Historical Chart)

Este é um aplicativo web construído com Streamlit que permite aos usuários converter valores entre diferentes moedas e visualizar o histórico da taxa de câmbio entre duas moedas selecionadas.

## 📜 Descrição (Description)

O aplicativo oferece uma interface simples para:
1.  Selecionar uma moeda de origem e uma moeda de destino.
2.  Inserir um valor a ser convertido.
3.  Visualizar o valor convertido.
4.  Inverter rapidamente as moedas de origem e destino.
5.  (Funcionalidade implícita no código, mas não visível na UI fornecida - Adicionar se implementado) Visualizar um gráfico com o histórico da taxa de câmbio para o último mês entre as moedas selecionadas.

Ele utiliza a API da [ExchangeRate-Host](https://exchangerate.host/) para obter as taxas de câmbio em tempo real e dados históricos.

## ✨ Funcionalidades (Features)

* **Conversão de Moedas:** Converte valores entre as seguintes moedas:
    * USD (Dólar Americano)
    * EUR (Euro)
    * BRL (Real Brasileiro)
    * JPY (Iene Japonês)
    * GBP (Libra Esterlina)
* **Seleção Intuitiva:** Dropdowns fáceis de usar para selecionar as moedas.
* **Entrada de Valor:** Campo numérico para inserir o valor a ser convertido.
* **Inversão Rápida:** Botão para inverter as moedas de origem e destino com um clique.
* **Tratamento de Erros:** Exibe mensagens de erro caso a conversão ou a busca de dados da API falhe.
* **(Opcional - se implementado) Gráfico Histórico:** Exibe um gráfico de linha com a variação da taxa de câmbio entre as duas moedas selecionadas nos últimos 30 dias.

## 🚀 Como Executar (How to Run)

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    Certifique-se de ter um arquivo `requirements.txt` com o seguinte conteúdo:
    ```txt
    streamlit
    pandas
    plotly
    requests
    ```
    E então execute:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Defina sua Chave da API:**
    O código utiliza uma chave da API da `exchangerate.host`. Você precisará obter a sua própria chave gratuita no site [ExchangeRate-Host](https://exchangerate.host/) e substituir o valor da variável `API_KEY` no arquivo Python:
    ```python
    API_KEY = "SUA_CHAVE_API_AQUI"
    ```

5.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run seu_arquivo_python.py
    ```
    (Substitua `seu_arquivo_python.py` pelo nome do seu arquivo Python principal).

O aplicativo deverá abrir automaticamente no seu navegador padrão.

## 🛠️ Tecnologias Utilizadas (Technologies Used)

* **Python:** Linguagem de programação principal.
* **Streamlit:** Framework para criação de aplicativos web interativos com Python.
* **Pandas:** Biblioteca para manipulação e análise de dados (usada para o gráfico histórico).
* **Plotly:** Biblioteca para criação de gráficos interativos.
* **Requests:** Biblioteca para fazer requisições HTTP à API.

## 🌐 API Utilizada (API Used)

* **ExchangeRate-Host API:** Fornece dados de taxas de câmbio em tempo real e históricas.
    * Site: [https://exchangerate.host/](https://exchangerate.host/)

## 🖼️ Screenshots (Screenshots)

*(Adicione aqui screenshots da sua aplicação. Por exemplo:*

*Tela Principal:*
`![Tela Principal](link_para_sua_imagem_tela_principal.png)`

*Gráfico Histórico (se implementado):*
`![Gráfico Histórico](link_para_sua_imagem_grafico.png)`
*)*

## 🔮 Possíveis Melhorias Futuras (Potential Future Improvements)

* Permitir que o usuário selecione o período para o gráfico histórico.
* Adicionar mais moedas à lista.
* Salvar moedas favoritas do usuário.
* Melhorar a interface do usuário com mais elementos visuais.
* Internacionalização (suporte a múltiplos idiomas).
