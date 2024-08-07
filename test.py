import streamlit as st
import pandas as pd


data = {
    "Index#": [f"A{i}" for i in range(1, 21)],
    "Value": [41, 18, 21, 63, 2, 53, 5, 57, 60, 93, 28, 3, 90, 39, 80, 88, 49, 60, 26, 28]
}

df = pd.DataFrame(data)

alpha = int(df[df['Index#'] == 'A5']['Value'].values) + int(df[df['Index#'] == 'A20']['Value'].values)
beta = int(df[df['Index#'] == 'A15']['Value'].values) // int(df[df['Index#'] == 'A7']['Value'].values)
charlie = int(df[df['Index#'] == 'A13']['Value'].values) * int(df[df['Index#'] == 'A12']['Value'].values)

new_data = {
    "Category": ['Alpha', 'Beta', 'Charlie'],
    "Value": [alpha, beta, charlie]
}

df_new = pd.DataFrame(new_data)

st.title("Simple Assessment_ Table Output & Processing")

st.write("**_Table 1_**")
st.table(df)

st.write("**_Table 2_**")
st.table(df_new)
