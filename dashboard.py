import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

#import Dataset
def import_data():
    return pd.read_csv("CleanData_bsH.csv")

df = import_data()

st.set_option('deprecation.showPyplotGlobalUse', False)

#Mengganti nilai weather
df.weathersit.replace({
    1 : 'Clear',
    2 : 'Mist',
    3 : 'Light Snow',
    4 : 'Heavy Rain'
}, inplace = True)

#Melengkapi Dashboard 
st.header('Bike Sharing Dashboard :sparkles:')

#Membuat Sidebar
with st.sidebar:
    #Menambahkan logo
    st.image("Logo.png", width= 200)
    st.sidebar.title("Choose The Visualization")
    choose_date = st.selectbox("Choose Year", df["yr"].unique())
    choose_visual = st.sidebar.radio("The Visual", ("Kondisi Total Rental Berdasrkan Cuaca dan Musim", "Kondisi Total Rental Berdasrkan Weekday dan Bulanan"))

# Kondisi Total Rental Berdasrkan Cuaca dan Musim
if choose_visual == "Kondisi Total Rental Berdasrkan Cuaca dan Musim":
    filter_date = df[df["yr"] == choose_date]
    filter_season = filter_date.groupby('season')['cnt'].sum()
    filter_wheater = filter_date.groupby('weathersit')['cnt'].sum()


    st.subheader("Kondisi Total Rental Berdasrkan Musim")

    fig, ax = plt.subplots(figsize = (10,6))
    sns.barplot(
    data = filter_season,
    ax = ax
    )
    plt.title('Kondisi Total Rental Berdasrkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Total Rental Sepeda')
    st.pyplot(fig)

    st.subheader("Kondisi Total Rental Berdasrkan Cuaca")

    fig, ax = plt.subplots(figsize = (10,6))
    sns.barplot(
    data = filter_wheater,
    ax = ax
    )
    plt.title('Kondisi Total Rental Berdasrkan Cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Total Rental Sepeda')
    st.pyplot()
    st.write("Hasil visualisasi boxplot di atas dapat disimpulkan bahwa season dan cuaca setiap tahunnya sangat berpengaruh pada total rental sepeda, faktanya setiap season Spring memiliki tingkat total rental sepeda paling sedikit, berbeda dengan season Fall yang memiliki tingkat total rental sepeda paling banyak. Walupun di tahun berikutnya yaitu 2012 terdapat kenaikan total rental sepeda di season Spring maupun Fall")

#Kondisi Total Rental Berdasrkan Weekday dan Bulanan
elif choose_visual == "Kondisi Total Rental Berdasrkan Weekday dan Bulanan":
    filter_date = df[df["yr"] == choose_date]
    filter_mnth = filter_date.groupby('mnth')['cnt'].sum()
    filter_weekday = filter_date.groupby('weekday')['cnt'].sum()

    st.subheader("Kondisi Total Rental Berdasrkan Bulanan")

    fig, ax = plt.subplots(figsize = (10,6))
    sns.barplot(
    data = filter_mnth,
    ax = ax
    )
    plt.title('Kondisi Total Rental Berdasrkan Bulanan')
    plt.xlabel('Bulan')
    plt.ylabel('Total Rental Sepeda')
    st.pyplot(fig)

    st.subheader("Kondisi Total Rental Berdasrkan Weekday")

    fig, ax = plt.subplots(figsize = (10,6))
    sns.barplot(
    data = filter_weekday,
    ax = ax
    )
    plt.title('Kondisi Total Rental Berdasrkan Weekday')
    plt.xlabel('Weekday')
    plt.ylabel('Total Rental Sepeda')
    st.pyplot()
    st.write("Hasil visualisasi boxplot di atas dapat disimpulkan bahwa season dan cuaca setiap tahunnya sangat berpengaruh pada total rental sepeda, faktanya setiap season Spring memiliki tingkat total rental sepeda paling sedikit, berbeda dengan season Fall yang memiliki tingkat total rental sepeda paling banyak. Walupun di tahun berikutnya yaitu 2012 terdapat kenaikan total rental sepeda di season Spring maupun Fall")

# Tren Total Rental
filter_date = df[df["yr"] == choose_date]
st.subheader(f"Tren Total Rental Berdasrkan Bulanan Pada Tahun 2011 dan 2012")
df['mnth'] = pd.Categorical(df['mnth'], categories = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des'], ordered = True)

total_mnth = df.groupby(by = ['mnth', 'yr']).agg({
    'cnt' : 'sum'
}).reset_index()

sns.lineplot(
    x = 'mnth',
    y = 'cnt',
    hue = 'yr',
    marker = "o", 
    data = total_mnth
)

plt.title("Pola Total Rental Sepeda Setiap Bulan Pada Tahun 2011 dan 2012")
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title = "Year", loc ="lower right")
plt.tight_layout()
st.pyplot()
st.write("Hasil visualisasi line chart di atas menunjukan pola fluaktif setiap bulannya pada tahun 2011 dan 2012. Ini dapat dilihat dari lonjakan kenaikan total rental sepeda pada bulan mei tahun 2011 kemudian lonjakan penurunan terjadi di bulan desember setelah itu terjadi lonjakan kenaikan pada bulan Maret tahun 2012 dan penurunan kembali pada bulan desember tahun 2012. Penurunan di bulan-bulan tersebut juga disebabkan karena peralihan musim Winter-Spring yang faktanya di visualiasi pertanyaan 1. Namun dampak postifnya total rental sepeda mengalam kenaikan pada tahun 2012")
