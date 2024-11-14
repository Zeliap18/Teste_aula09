import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
# Incremente o dashboard sobre as localizações dos quilombolas informando a quantidade de comunidades 
#por estado em um gráfico de mapas. Depois, faça o deploy de sua aplicação no Streamlit. Não esqueça de atualizar 
#o arquivo requirements.txt para que o pandas seja importado e faça a limpeza dos dados!
df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")
#Insira dados sobre estatística descritiva! Informe a quantidade de municípios e de comunidades.
qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))
qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))
#Calcule o número de comunidades por estado
st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())
#Informe os dez municípios com mais comunidades através de um gráfico de barras.
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
#Crie um slider do Streamlit e receba do usuário o número de linhas a serem impressas do dataframe, 
#filtrando o número de linhas de acordo com o valor retornado pelo slider.
numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
