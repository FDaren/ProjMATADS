import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

# Definindo as configurações iniciais do aplicativo Streamlit
st.title('Stock History App')
st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# Baixando os dados para o primeiro gráfico
data = yf.download(ticker_symbol, start='2020-01-01', end='2023-06-26')

# Exibindo os dados em forma de tabela
st.subheader('Histórico')
st.dataframe(data)

# Criando o primeiro gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Fechamento'))
fig.update_layout(title=f'{ticker_symbol}', xaxis_title='Data', yaxis_title='Preço')
st.plotly_chart(fig)

# Baixando os dados para o segundo gráfico
data2 = yf.download(ticker_symbol, start='2020-01-01', end='2023-06-26')

# Criando o segundo gráfico
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data2.index, y=data2['Volume'], name='Volume'))
fig2.update_layout(title=f'{ticker_symbol} - Volume', xaxis_title='Data', yaxis_title='Volume')
st.plotly_chart(fig2)
