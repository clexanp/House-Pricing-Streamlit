import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor
import joblib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

print("=" * 50)
print("MULAI PELATIHAN MODEL")
print("=" * 50)

print("\n[1/5] Memuat dataset train.csv...")
df = pd.read_csv('train.csv')
print(f"      Dataset berhasil dimuat: {df.shape[0]} baris, {df.shape[1]} kolom")

print("\n[2/5] Memisahkan fitur (X) dan target (y)...")
X = df.drop(columns=['Id', 'SalePrice'])
y = df['SalePrice']
print(f"      Jumlah fitur: {X.shape[1]}")
print(f"      Target: SalePrice")

print("\n[3/5] Membagi data latih (80%) dan data uji (20%)...")
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"      Data latih: {X_latih.shape[0]} baris")
print(f"      Data uji  : {X_uji.shape[0]} baris")

kolom_numerik = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
kolom_kategorikal = X.select_dtypes(include=['object']).columns.tolist()
print(f"      Kolom numerik   : {len(kolom_numerik)}")
print(f"      Kolom kategorikal: {len(kolom_kategorikal)}")

print("\n[4/5] Membangun pipeline preprocessing dan model XGBoost...")

pipa_numerik = Pipeline(steps=[
    ('isi_kosong', SimpleImputer(strategy='median')),
    ('skala', StandardScaler())
])

pipa_kategorikal = Pipeline(steps=[
    ('isi_kosong', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

praproses = ColumnTransformer(transformers=[
    ('numerik', pipa_numerik, kolom_numerik),
    ('kategorikal', pipa_kategorikal, kolom_kategorikal)
])

pipa_utama = Pipeline(steps=[
    ('praproses', praproses),
    ('model', XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    ))
])

print("\n[5/5] Melatih model (mungkin butuh waktu beberapa detik)...")
pipa_utama.fit(X_latih, y_latih)
print("      Pelatihan selesai!")

print("\n" + "=" * 50)
print("EVALUASI MODEL")
print("=" * 50)

prediksi_uji = pipa_utama.predict(X_uji)
rmse = np.sqrt(mean_squared_error(y_uji, prediksi_uji))
mae = mean_absolute_error(y_uji, prediksi_uji)
r2 = r2_score(y_uji, prediksi_uji)

print(f"RMSE : ${rmse:,.2f}")
print(f"MAE  : ${mae:,.2f}")
print(f"R²   : {r2:.4f}")

print("\nMenyimpan model ke 'model_rumah.pkl'...")
joblib.dump(pipa_utama, 'model_rumah.pkl')
print("Model berhasil disimpan!")

print("\n" + "=" * 50)
print("MEMBUAT VISUALISASI")
print("=" * 50)

print("\n[1/3] Membuat grafik distribusi harga rumah...")
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(y, bins=50, color='cornflowerblue', edgecolor='white', alpha=0.85)
ax.set_title('Distribusi Harga Rumah (SalePrice)', fontsize=14, fontweight='bold')
ax.set_xlabel('Harga (USD)', fontsize=12)
ax.set_ylabel('Frekuensi', fontsize=12)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
fig.savefig('distribusi_harga.png', dpi=150, bbox_inches='tight')
plt.close()
print("      Disimpan: distribusi_harga.png")

print("\n[2/3] Membuat grafik korelasi fitur...")
korelasi = df.select_dtypes(include=['int64', 'float64']).corr()['SalePrice'].drop('SalePrice')
korelasi_10 = korelasi.abs().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(8, 6))
warna = ['#2ecc71' if korelasi[idx] > 0 else '#e74c3c' for idx in korelasi_10.index]
ax.barh(korelasi_10.index, korelasi[korelasi_10.index], color=warna, edgecolor='white')
ax.set_title('10 Fitur dengan Korelasi Tertinggi terhadap SalePrice', fontsize=14, fontweight='bold')
ax.set_xlabel('Koefisien Korelasi', fontsize=12)
ax.axvline(0, color='black', linewidth=0.8)
plt.tight_layout()
fig.savefig('korelasi_fitur.png', dpi=150, bbox_inches='tight')
plt.close()
print("      Disimpan: korelasi_fitur.png")

print("\n[3/3] Membuat grafik learning curve...")
ukuran, skor_latih, skor_val = learning_curve(
    pipa_utama, X_latih, y_latih,
    cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='neg_mean_squared_error',
    random_state=42
)

rmse_latih = np.sqrt(-skor_latih.mean(axis=1))
rmse_val = np.sqrt(-skor_val.mean(axis=1))

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(ukuran, rmse_latih, 'o-', color='#3498db', label='RMSE Data Latih', linewidth=2)
ax.plot(ukuran, rmse_val, 'o-', color='#e67e22', label='RMSE Data Validasi', linewidth=2)
ax.set_title('Learning Curve — Model XGBoost', fontsize=14, fontweight='bold')
ax.set_xlabel('Jumlah Data Latih', fontsize=12)
ax.set_ylabel('RMSE', fontsize=12)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)
plt.tight_layout()
fig.savefig('learning_curve.png', dpi=150, bbox_inches='tight')
plt.close()
print("      Disimpan: learning_curve.png")

print("\n" + "=" * 50)
print("SEMUA SELESAI! File yang dihasilkan:")
print("  - model_rumah.pkl")
print("  - distribusi_harga.png")
print("  - korelasi_fitur.png")
print("  - learning_curve.png")
print("=" * 50)