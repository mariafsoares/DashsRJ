import streamlit as st
import pandas as pd
from PIL import Image

DATA_URL = ("./PE9_streamlit_data.xlsx")

st.set_page_config(page_title="VOAs PE9",
                   layout="centered",
                   initial_sidebar_state="auto")

# External CSS
main_external_css = """
        <style>
            .sidebar.sidebar-content{
            background-image: linear-gradient(#0E1117,#0E1117);
            color: #0E1117}
        </style>"""
st.markdown(main_external_css, unsafe_allow_html=True)

icon = Image.open("./Imagem2.png") #braskem_logo
st.sidebar.image(icon, use_column_width=True,) #caption="VOAs Entregues"

st.title("ANALISADORES VIRTUAIS PE9 📈")
st.sidebar.title("PRODUTOS APTOS PARA UTILIZAÇÃO")

@st.cache(persist=True)
def load_data():
    data = pd.read_excel(DATA_URL)
    return data

data = load_data()

#st.dataframe(data)

select = st.sidebar.selectbox('LINHA DE PRODUÇÃO', ['LINHA 1', 'LINHA 2'], key='1')
st.markdown("#### Dashboard de Acompanhamento dos Modelos entregues por Produto")

if select == 'LINHA 1':    
    st.write("## LINHA 1")
    df = data.loc[data['LINHA']=='LINHA 1']
    select_pr = st.sidebar.selectbox('PROCESSO', ['REAÇÃO','EXTRUSÃO'], key='1')

    if select_pr == 'REAÇÃO':
        df = df.loc[df['PROCESSO']=='REAÇÃO']
        select_ana = st.sidebar.selectbox('ANÁLISE', ['ÍNDICE DE FLUIDEZ','DENSIDADE'], key='1')

        if select_ana == 'DENSIDADE':
            df = df.loc[df['ANÁLISE']=='DENSIDADE', 'PRODUTO'].reset_index().drop(columns=['index'])
            st.subheader("PRODUTOS ENTREGUES PARA DENSIDADE REAÇÃO 👇 ")
            st.table(df)

        else:
            df = df.loc[df['ANÁLISE']=='ÍNDICE DE FLUIDEZ', 'PRODUTO'].reset_index().drop(columns=['index'])    
            st.subheader("PRODUTOS ENTREGUES PARA IF REAÇÃO 👇 ")
            st.table(df)
    else:
        df = df.loc[df['PROCESSO']=='EXTRUSÃO']
        select_ana = st.sidebar.selectbox('ANÁLISE', ['ÍNDICE DE FLUIDEZ','DENSIDADE'], key='1')

        #if select_ana == 'DENSIDADE':
        #    df = df.loc[df['ANÁLISE']=='DENSIDADE', 'PRODUTO'].reset_index().drop(columns=['index'])
        #    st.subheader("PRODUTOS ENTREGUES PARA DENSIDADE EXTRUSÃO 👇 ")
        #    st.table(df)

        if select_ana == 'ÍNDICE DE FLUIDEZ':
            df = df.loc[df['ANÁLISE']=='ÍNDICE DE FLUIDEZ', 'PRODUTO'].reset_index().drop(columns=['index'])    
            st.subheader("PRODUTOS ENTREGUES PARA IF EXTRUSÃO 👇 ")
            st.table(df)

        else:
            st.write('Não há analisadores para Densidade Extrusão.')                
else:
    st.write("## LINHA 2")
    df = data.loc[data['LINHA']=='LINHA 2']
    select_pr = st.sidebar.selectbox('PROCESSO', ['REAÇÃO','EXTRUSÃO'], key='1')

    if select_pr == 'REAÇÃO':
        df = df.loc[df['PROCESSO']=='REAÇÃO']
        select_ana = st.sidebar.selectbox('ANÁLISE', ['ÍNDICE DE FLUIDEZ','DENSIDADE'], key='1')

        if select_ana == 'DENSIDADE':
            df = df.loc[df['ANÁLISE']=='DENSIDADE', 'PRODUTO'].reset_index().drop(columns=['index'])
            st.subheader("PRODUTOS ENTREGUES PARA DENSIDADE REAÇÃO 👇 ")
            st.table(df)

        else:
            df = df.loc[df['ANÁLISE']=='ÍNDICE DE FLUIDEZ', 'PRODUTO'].reset_index().drop(columns=['index'])    
            st.subheader("PRODUTOS ENTREGUES PARA IF REAÇÃO 👇 ")
            st.table(df)
    else:
        df = df.loc[df['PROCESSO']=='EXTRUSÃO']
        select_ana = st.sidebar.selectbox('ANÁLISE', ['ÍNDICE DE FLUIDEZ','DENSIDADE'], key='1')

        #if select_ana == 'DENSIDADE':
        #    df = df.loc[df['ANÁLISE']=='DENSIDADE', 'PRODUTO'].reset_index().drop(columns=['index'])
        #    st.subheader("PRODUTOS ENTREGUES PARA DENSIDADE EXTRUSÃO 👇 ")
        #    st.table(df)

        if select_ana == 'ÍNDICE DE FLUIDEZ':
            df = df.loc[df['ANÁLISE']=='ÍNDICE DE FLUIDEZ', 'PRODUTO'].reset_index().drop(columns=['index'])    
            st.subheader("PRODUTOS ENTREGUES PARA IF EXTRUSÃO 👇 ")
            st.table(df)   

        else:
            st.write('Não há analisadores para Densidade Extrusão.')


