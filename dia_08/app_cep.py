import streamlit as st
import pandas as pd

import requests

URL = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

cep = st.text_input("Busque seu cep")

if cep != "":
    
    try:
        resp = requests.get(URL.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index=True)

    except Exception as err:
        st.error("Entre com um cep válido!")