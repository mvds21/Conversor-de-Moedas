import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests

API_KEY = "c8cb9fbc02940d91a6880304f83085aa"

def convert_currency(base, target, amount):
    url = f"https://api.exchangerate.host/convert?from={base}&to={target}&amount={amount}&access_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("success", False):
        return data['result']
    else:
        raise Exception(f"Erro da API: {data.get('error', {}).get('info', 'Erro desconhecido')}")

def get_exchange_rate(base_currency, target_currency, date):
    url = f"https://api.exchangerate.host/{date}?base={base_currency}&symbols={target_currency}&access_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("success", False):
        return data['rates'][target_currency]
    else:
        return None

st.title("💱 Conversor de Moedas com Gráfico Histórico")

# Moedas
moedas = {
    "USD": "US - Dólar Americano",
    "EUR": "EU -  Euro",
    "BRL": "BR -  Real Brasileiro",
    "JPY": "JP -  Iene Japonês",
    "GBP": "GB -  Libra Esterlina"
}
moeda_codes = list(moedas.keys())

if "base" not in st.session_state:
    st.session_state.base = "USD"
if "target" not in st.session_state:
    st.session_state.target = "BRL"

base = st.selectbox("Moeda de origem", moeda_codes, index=moeda_codes.index(st.session_state.base), format_func=lambda x: moedas[x])
target = st.selectbox("Moeda de destino", moeda_codes, index=moeda_codes.index(st.session_state.target), format_func=lambda x: moedas[x])

st.session_state.base = base
st.session_state.target = target

amount = st.number_input(f"Valor em {base}:", min_value=0.0, value=100.0)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Converter", key="btn_converter"):
        try:
            converted = convert_currency(base, target, amount)
            st.success(f"{amount:.2f} {base} = {converted:.2f} {target}")
        except Exception as e:
            st.error("Erro ao converter moedas. Verifique a conexão com a internet ou a API.")

with col2:
    if st.button("🔁 Inverter moedas", key="btn_inverter"):
        st.session_state.base, st.session_state.target = st.session_state.target, st.session_state.base
        st.rerun()