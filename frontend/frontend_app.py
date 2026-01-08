import requests
import streamlit as st

st.title = "MPPNY"


BACKEND_ADDRESS = "http://127.0.0.1:8000"


resp = requests.get(f"{BACKEND_ADDRESS}/user/get")
resp.raise_for_status()
st.table(resp.json())


name = st.text_input("Name:")
if st.button("Add"):
    res = requests.post(f"{BACKEND_ADDRESS}/user/add", json={"name": name})
