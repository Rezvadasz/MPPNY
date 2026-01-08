import requests
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from bs4 import BeautifulSoup



BACKEND_ADDRESS = "http://127.0.0.1:8000"
NEWS_URL = "https://www.techpowerup.com/news-tags/AMD"

st.header("AMD CPU Benchmarks") 

st.subheader("List CPU")


resp = requests.get(f"{BACKEND_ADDRESS}/cpu/get")
resp.raise_for_status()
data = resp.json()
df = pd.DataFrame(data["cpu"])

st.dataframe(df, hide_index=True)


##hozzaadas

st.subheader("Add CPU")

model = st.text_input("Model:")
pts1 = st.number_input("PTS1:")
pts2 = st.number_input("PTS2:")
pts4 = st.number_input("PTS4:")
pts8 = st.number_input("PTS8:")
pts64 = st.number_input("PTS64:")
sample = st.number_input("Sample:")
if st.button("Add"):
    res = requests.post(f"{BACKEND_ADDRESS}/cpu/add", json={"model":model, "PTS1":pts1, "PTS2":pts2, "PTS4":pts4, "PTS8":pts8, "PTS64":pts64, "samples":sample})
    


#torles

st.subheader("Remove CPU")
 
cpu_id = st.number_input("CPU ID:")
if st.button("Delete"):
    res = requests.delete(f"{BACKEND_ADDRESS}/cpu/delete/{cpu_id}")
    st.write(res.json())




#grafikon
fig = go.Figure()
colors = ['#8b5cf6', '#ef4444']
labels = ['Single-Core', 'Multi-Core']

for i, (col, label) in enumerate(zip(['PTS1', 'PTS64'], labels)):
    fig.add_trace(go.Bar( name=label, x=df['Model'], y=df[col], marker_color=colors[i]))

fig.update_layout(
    title='CPU Benchmark Scores: Single-Core vs Multi-Core Performance',
    barmode='group',
    height=600,
    xaxis_title='CPU Model',
    yaxis_title='Performance Score'
)
st.plotly_chart(fig)


page = requests.get(NEWS_URL)
soup = BeautifulSoup(page.text, "html.parser") 
articles = soup.find_all("article")


st.subheader("AMD new from TechPowerUp")

for article in articles[:5]:
    #title
    title_elem = article.find('h1') or article.find('a', class_='newslink')
    title = title_elem.get_text(strip=True)
    st.write(title)
    
    #link
    link_elem = title_elem.find('a') if title_elem else article.find('a')
    link = link_elem['href'] if link_elem and 'href' in link_elem.attrs else ""
    if link and not link.startswith('http'):
        link = f"https://www.techpowerup.com{link}"
    st.write(link)



