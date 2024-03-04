# Nama: Willyandie Saputra
# Email: m243d4ky1426@bangkit.academy
# ID Dicoding: willyandie_saputra

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(data_path):
    bikes_df = pd.read_csv(data_path)
    return bikes_df

def clean_data(bikes_df):
    bikes_df["dteday"] = pd.to_datetime(bikes_df["dteday"])
    bikes_df["bulan"] = bikes_df["mnth"]
    bikes_df["tahun"] = bikes_df["yr"]
    monthly_rentals = (
        bikes_df.groupby(["tahun", "bulan"])["cnt"]
        .sum()
        .reset_index()
    )
    return bikes_df, monthly_rentals


def plot_monthly_rentals(monthly_rentals):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(
        monthly_rentals["tahun"].astype(str) + "-" + monthly_rentals["bulan"].astype(str),
        monthly_rentals["cnt"],
        marker="o",
        linestyle="-",
    )
    ax.set_title("Jumlah Penyewaan Sepeda per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)
    return fig

def plot_rentals_by_weather(bikes_df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x="weathersit", y="cnt", data=bikes_df, ax=ax)
    ax.set_title("Peminjaman Sepeda Berdasarkan Cuaca")
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.set_xticks([0, 1, 2], ["Cerah", "Berawan", "Hujan/Salju"])
    ax.grid(True)
    return fig


data_path = "main_data.csv"
bikes_df = load_data(data_path)
monthly_rentals = clean_data(bikes_df)[1]

st.title("Proyek Analisis Data: Bike-sharing-dataset")
st.write(
    "Saya memilih dataset Bike-sharing-dataset file **day.csv**, karena saya ingin melihat data peminjaman sepeda perhari dengan cakupan data yang lebih mudah diakses, dan sesuai dengan kebutuhan analisa saya. Dataset yang lebih besar atau dengan tingkat detail yang lebih tinggi mungkin memerlukan lebih banyak waktu dan sumber daya untuk diproses dan dianalisis. Dengan menggunakan dataset yang telah diagregasi ke tingkat harian, saya dapat mengurangi kompleksitas analisis."
)

st.header("Jumlah Penyewaan Sepeda per Bulan")
fig = plot_monthly_rentals(monthly_rentals)
st.pyplot(fig)

st.header("Peminjaman Sepeda Berdasarkan Cuaca")
fig = plot_rentals_by_weather(bikes_df)
st.pyplot(fig)
