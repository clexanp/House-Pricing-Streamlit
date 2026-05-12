import streamlit as st

st.set_page_config(
    page_title="Portofolio Rafi",   
    layout="wide"                    
)

st.title("House Pricing Streamlit")

st.markdown("""
Portofolio ini dibuat dengan tujuan pengerjaan tugas dari Dibimbing, detail terkait web ini bisa dilihat di bawah ini:
- `Tentang Saya             :` Berisi informasi aku yang berisi detail pengerjaan tugas portofolio ini.
- `Visualisasi Model & Data :` Informasi lengkap terkait grafik yang meliputi dataset dan performa model yang dipakai dalam pengerjaan tugas ini.
""")

st.divider()

st.header("🪐 Tentang Saya")

kolom_kiri, kolom_kanan = st.columns([1, 2])

with kolom_kiri:
    st.image("D:\Dokumen Bootcamp Dibimbing 2025\Semua Materi dan Tugas 25 April 2026\Portofolio Building with Streamlit\Tugas\Assignment Day 51\House Pricing Streamlit\gambar_proyek\Foto Santai Part 2.jpeg", width=250)

with kolom_kanan:
    st.markdown("### Nama Lengkap")
    st.text("Raihan Azhar Rafi")
    
    st.markdown("### Latar Belakang")
    st.markdown("""
    - `Pendidikan   :` S1 Teknik Komputer, Universitas Telkom Bandung (2018 – 2023)
    - `Pelatihan    :` Bootcamp Data Science dan AI Machine Learning Batch 40, Dibimbing (2025 – Masih Berlangsung)
    - `Detail Tugas :` Assignment Day 51 - Portfolio Building with Streamlit
    """)

st.divider()

from PIL import Image

st.header("📊 Visualisasi Model dan Data")

st.markdown("""
Berikut adalah visualisasi dari dataset sesuai ketentuan tugas dan performa model menggunakan XGBoost
untuk memprediksi harga rumah.
""")

pilihan = st.radio(
    "Pilih visualisasi yang ingin ditampilkan:",
    options=[
        "Distribusi Harga Rumah",
        "Korelasi Fitur terhadap Target",
        "Learning Curve Model",
        "Metrik Evaluasi Model"
    ],
    horizontal=True
)
 
if pilihan == "Distribusi Harga Rumah":
    st.markdown("### Distribusi SalePrice")
    st.markdown("Grafik Histogram ini menunjukkan persebaran harga rumah berdasarkan dataset pada tugas ini.")
    try:
        gambar = Image.open('distribusi_harga.png')
        st.image(gambar, use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Gambar belum tersedia. Jalankan `train_model.py` terlebih dahulu.")

    st.markdown("### 📝 Penjelasan Grafik")
    st.markdown("""
    Grafik di atas bernama `histogram` yang menunjukkan persebaran distribusi harga rumah 
    dalam dataset tugas. Sumbu horizontal (X) menunjukkan rentang harga rumah dalam satuan USD, 
    sedangkan sumbu vertikal (Y) menunjukkan frekuensi atau jumlah rumah yang berada di 
    rentang harga tersebut.
    """)
    
    st.markdown("### 💡 Insight yang Didapat")
    st.markdown("""
    Dari grafik distribusi di atas, didapatkan insight penting diantaranya:
    
    🔹 `1. Harga paling umum               :` Puncak histogram menunjukkan rentang harga 
    penjualan rumah, sekitar 120.000 – 160.000 USD menurut grafik tersebut. Ini menunjukkan 
    harga "pasar" pada rumah yang paling sering muncul.
    
    🔹 `2. Outlier harga tinggi            :` Terdapat batang grafik yang memanjang signifikan, menunjukkan adanya 
    rumah-rumah mewah dengan harga jauh di atas rata-rata. Outlier ini perlu diatasi 
    karena bisa mempengaruhi performa dan hasil model jika tidak ditangani dengan baik.
    
    🔹 `3. Masukkan untuk proses modelling :` Karena distribusi target tidak normal, 
    log transform sering diterapkan pada target SalePrice untuk membuat 
    distribusi lebih mendekati normal, dan membantu model regresi bekerja lebih baik.
    """)

elif pilihan == "Korelasi Fitur terhadap Target":
    st.markdown("### Top 10 Korelasi Fitur vs SalePrice Berdasarkan Dataset Tugas Ini")
    st.markdown("Hijau = korelasi positif, Merah = korelasi negatif.")
    try:
        gambar = Image.open('korelasi_fitur.png')
        st.image(gambar, use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Gambar belum tersedia. Jalankan `train_model.py` terlebih dahulu.")

    st.markdown("### 📝 Penjelasan Grafik")
    st.markdown("""
    Grafik di atas bernama `horizontal bar chart` yang menampilkan 10 fitur dengan nilai 
    korelasi tertinggi terhadap target SalePrice (harga rumah). Korelasi tersebut diukur menggunakan 
    metode (Koefisien Korelasi Pearson) yang nilainya berkisar antara -1 hingga +1.
    
    Cara membaca grafik ini:
    - `Warna hijau (nilai positif) :` Semakin besar nilai fitur nya, semakin tinggi harga rumah.
    - `Warna merah (nilai negatif) :` Semakin besar nilai fitur nya, semakin rendah harga rumah.
    - `Panjang batang              :` Menunjukkan seberapa kuat korelasinya. Semakin panjang, maka semakin 
      kuat hubungan nya dengan harga rumah.
    """)
    
    st.markdown("### 💡 Insight yang Didapat")
    st.markdown("""
    Dari grafik korelasi ini, kita bisa memperoleh insight yang sangat berharga untuk 
    memahami faktor-faktor yang mempengaruhi harga rumah:
    
    🔹 `Overall Quality (Kualitas Keseluruhan) (Korelasi Tertinggi)                   :` Fitur ini menjadi 
    indikator prediksi paling kuat di antara fitur lainnya dengan hasil korelasi 
    sekitar 0.79. Hal tersebut menunjukkan bahwa semakin tinggi kualitas material rumah 
    dan proses penyelesaian pembangunan tahap akhir pada rumah tersebut, maka semakin 
    mahal harga rumahnya. Karena kualitas sebagai faktor penting penentu harga suatu 
    properti.
    
    🔹 `Above Grade Living Area (Luas Bangunan di Atas Tanah) (Korelasi Positif Kuat) :` 
    Semakin besar luas bangunan utama, semakin mahal rumah. Hal tersebut menunjukkan 
    bahwa luas bangunan berkaitan dengan faktor biaya material, faktor harga tanah, dan 
    pastinya akan mengubah standart nilai properti tersebut.
    
    🔹 `Garage Cars (Kapasitas Garasi dalam Jumlah Mobil) (Korelasi Positif)          :` Garasi 
    rumah yang berukuran lebih besar cenderung lebih mahal. Hal tersebut menunjukkan 
    bahwa standart harga suatu properti juga diukur dari fasilitas parkir yang memadai 
    dan bisa dijadikan referensi bagi calon pembeli.
    
    🔹 `Garage Area (Luas Garasi) (Korelasinya Mirip dengan Garage Cars)              :` Fitur ini punya korelasi 
    yang mirip karena memiliki konteks yang sama dengan kapasitas garasi.
    
    🔹 `Total Basement SF (Luas Total Basement) (Korelasi Positif)                    :` Properti yang 
    memiliki fasilitas basement yang lebih luas dihargai lebih tinggi. Hal tersebut 
    menunjukkan bahwa suatu properti dapat memiliki nilai jual yang tinggi jika 
    ditunjang oleh fasilitas pendukung yang memadai.
                
    🔹 `1st Floor SF (Luas Lantai 1) (Korelasi Positif)                               :` Biasanya ukuran luas lantai 
    pertama pada rumah memberikan nilai tambah yang cukup signifikan terhadap harga 
    jual rumah.
    
    🔹 `Full Bath (Kamar Mandi Lengkap) (Korelasi Positif)                            :` Semakin banyak atau 
    lengkap nya jumlah kamar mandi suatu rumah maka semakin mahal juga harga rumah 
    tersebut, karena berhubungan dengan kemampuan fasilitas pendukung wajib yang 
    memadai.
    
    🔹 `Year Built (Tahun Dibangun) (Korelasi Positif)                                :` Rumah yang baru dan baru saja 
    dibangun, harga properti nya pasti lebih mahal. Hal tersebut menunjukkan bahwa 
    standart pembangunan nya pasti mengikuti style modern dan kekinian dan hal tersebut 
    mempengaruhi harga rumah tersebut.
    
    🔹 `Year Remodeled (Tahun Renovasi) (Korelasi Positif)                            :` Pasti secara logika jika 
    terdapat suatu rumah yang baru saja di renovasi, maka harga jualnya jauh lebih 
    mahal dibandingkan dengan rumah yang tidak di renovasi. 
    
    🔹 `Fireplaces (Jumlah Perapian) (Korelasi Positif)                               :` Meskipun perapian termasuk 
    kebutuhan tersier, tetapi fasilitas ini mendukung kenyamanan dari segi 
    menghangatkan suhu badan penghuni suatu rumah tersebut dan hal tersebut pastinya 
    mempengaruhi peningkatan harga jual properti nya.
""")

elif pilihan == "Learning Curve Model":
    st.markdown("### Learning Curve — XGBoost")
    st.markdown("""
    Grafik ini menunjukkan performa model (RMSE) seiring bertambahnya jumlah data latih.
    Jika RMSE validasi jauh di atas RMSE latih, model mengalami **overfitting**.
    """)
    try:
        gambar = Image.open('learning_curve.png')
        st.image(gambar, use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Gambar belum tersedia. Jalankan `train_model.py` terlebih dahulu.")

elif pilihan == "Metrik Evaluasi Model":
    st.markdown("### Metrik Evaluasi Model pada Data Uji")
    st.markdown("Hasil evaluasi model XGBoost setelah dilatih:")
    
    k1, k2, k3 = st.columns(3)
    k1.metric("RMSE", "$25,432.18")
    k2.metric("MAE", "$16,891.45")
    k3.metric("R² Score", "0.8924")
    
    st.info("💡 Nilai di atas adalah contoh. Jalankan `train_model.py` untuk mendapatkan nilai aktual.")
    
    with st.expander("📖 Apa arti metrik ini?"):
        st.markdown("""
        - `RMSE (Root Mean Squared Error) :` Akar rata-rata kuadrat selisih prediksi vs aktual.
          Semakin kecil, model semakin akurat. Satuan sama dengan target (USD).
        - `MAE (Mean Absolute Error)      :` Rata-rata selisih absolut prediksi vs aktual.
          Lebih tahan terhadap data ekstrem (outlier).
        - `R² Score                       :` Seberapa baik model menjelaskan variasi data. Nilai 1.0 = sempurna,
          0 = tidak lebih baik dari menebak rata-rata.
        """)

st.divider()
st.caption("© 2026 Portofolio Rafi • Dibuat dengan Streamlit & Python")

