# House Pricing Streamlit

## Requirement

Pastikan menggunakan Python 3.10 atau lebih baru.

Instal dependensi yang dibutuhkan:

```bash
pip install streamlit pandas numpy scikit-learn xgboost joblib matplotlib pillow
```

## Cara Menjalankan

1. Unduh proyek ini atau ekstrak file zip ke folder lokal di komputer Anda.
2. Buka terminal atau PowerShell, lalu masuk ke folder proyek yang sudah berisi file `app.py`, `train_model.py`, dan `train.csv`.

Contoh pada Windows:

```bash
cd "C:\path\ke\folder\House Pricing Streamlit"
```

3. Instal paket yang dibutuhkan jika belum terpasang:

```bash
pip install streamlit pandas numpy scikit-learn xgboost joblib matplotlib pillow
```

4. Jalankan pelatihan model dan buat visualisasi:

```bash
python train_model.py
```

Skrip ini akan:
- memuat dataset `train.csv`
- melatih model XGBoost
- menyimpan model ke `model_rumah.pkl`
- membuat file `distribusi_harga.png`, `korelasi_fitur.png`, dan `learning_curve.png`

5. Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

6. Buka browser dan akses URL yang ditampilkan oleh Streamlit, biasanya `http://localhost:8501`.

## Catatan

- Jika `distribusi_harga.png`, `korelasi_fitur.png`, dan `learning_curve.png` belum ada, jalankan `train_model.py` terlebih dahulu.
- `app.py` menggunakan gambar profil dari folder `gambar_proyek/`.
- Jika ingin memperbarui model atau visualisasi, jalankan ulang `train_model.py`.

---

## Lisensi

File dan kode dalam proyek ini dibuat untuk keperluan belajar dan pengembangan portofolio. Silakan digunakan, dimodifikasi, dan dibagikan kembali selama tetap mencantumkan sumber aslinya dan tetap digunakan untuk tujuan edukasi.

© 2026 Portofolio Raihan Azhar Rafi