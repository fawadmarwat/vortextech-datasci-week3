##### Build an Interactive Dashboard for Retail Sales Data using Streamlit ####
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#####LOAD DATA ######
df =pd.read_csv(r"C:\Users\MHK\Downloads\data.csv\data.csv",
encoding="latin1")
# Dashboard Title#

st.title("Retail Sales Dashboard")
st.write(" Dataset Preview")
st.dataframe(df.head())

st.title("Retail Sales Dashboard")
st.subheader("Dataset Preview")
st.dataframe(df.head())
##TITLE DASHBOARD##
st.title("Retail Sales Dashboard")
st.subheader("Dataset Preview")
st.dataframe(df.head())

###Filter (Country)
country = st.selectbox("select country",df["Country"].unique())
# Filter unitprice
price_range = st.slider(
    "Select Unit Price Range",
    float(df["UnitPrice"].min()),
    float(df["UnitPrice"].max()),
    (
        float(df["UnitPrice"].min()),
        float(df["UnitPrice"].max())
    )
)
filtered_df = df[
    (df["Country"] == country) &
    (df["UnitPrice"] >= price_range[0]) &
    (df["UnitPrice"] <= price_range[1])
]

st.subheader("Filtered Data")
st.dataframe(filtered_df)
## ALL GRAPHS AND PLOTS
# ===========================
# BAR CHART
# ===========================
st.subheader("Top 5 Countries by Orders")

top_countries = (
    filtered_df["Country"]
    .value_counts()
    .head(5)
    .reset_index()
)

top_countries.columns = ["Country", "Count"]

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(top_countries["Country"], top_countries["Count"], color="blue")
plt.xticks(rotation=20)
plt.title("Top 5 Countries")
st.pyplot(fig)


# ===========================
# PIE CHART
# ===========================
st.subheader("Country Distribution")

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(
    top_countries["Count"],
    labels=top_countries["Country"],
    autopct="%1.1f%%"
)
plt.title("Country Distribution")
st.pyplot(fig)


# ===========================
# SCATTER PLOT
# ===========================
st.subheader("Unit Price vs Quantity")

fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(
    filtered_df["UnitPrice"],
    filtered_df["Quantity"],
    color="red"
)
plt.xlabel("Unit Price")
plt.ylabel("Quantity")
plt.title("Unit Price vs Quantity")
st.pyplot(fig)

st.success("Dashboard Created Successfully")
