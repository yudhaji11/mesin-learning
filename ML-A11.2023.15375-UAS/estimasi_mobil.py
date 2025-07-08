import pickle
import streamlit as st

# Load model
try:
    model = pickle.load(open('estimasi_mobil.sav', 'rb'))
except FileNotFoundError:
    st.error("File model 'estimasi_mobil.sav' tidak ditemukan. Pastikan file ada di direktori yang sama.")
    st.stop()

# Judul aplikasi
st.title('Prediksi Harga Mobil Bekas')

# Input pengguna
year = st.number_input('Input Tahun Mobil', min_value=2000, max_value=2025, step=1, value=2015)
mileage = st.number_input('Input Km Mobil', min_value=0, step=1000, value=50000)
tax = st.number_input('Input Pajak Mobil (dalam GBP)', min_value=0, step=1, value=150)
mpg = st.number_input('Input Konsumsi BBM Mobil (miles per gallon)', min_value=0.0, step=0.1, value=40.0)
engineSize = st.number_input('Input Engine Size (liter)', min_value=0.0, step=0.1, value=1.6)

# Prediksi
predict = None

if st.button('Estimasi Harga'):
    try:
        # Pastikan input diubah menjadi array dua dimensi
        predict = model.predict([[year, mileage, tax, mpg, engineSize]])
        predict_price = predict[0]  # Ambil nilai dari array
        st.write(f'Estimasi harga mobil bekas dalam Ponds (GBP): £{predict_price:,.2f}')
        st.write(f'Estimasi harga mobil bekas dalam IDR (Juta): Rp{predict_price * 19000 / 1_000_000:,.2f} Juta')
    except Exception as e:
        st.error(f"Terjadi error saat menghitung estimasi: {e}")
