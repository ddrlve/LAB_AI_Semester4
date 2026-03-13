ASSIGNMENT WEEK 5 - GSLC

MODEL SELECTION AND REGULARIZATION

Nama: Dian Rakhmawati Lestari

NIM: *(tulis NIM kamu di sini)*

---

## Part 1 – Model Diagnosis

**1. Compare the training performance and testing performance of the baseline polynomial regression model. What differences do you observe?**

Setelah menjalankan notebook dan melihat hasilnya, saya menemukan bahwa ada perbedaan yang cukup mencolok antara performa model di data training dan data testing. Model menghasilkan Training R² sebesar 0.651 dan Training RMSE sebesar 0.517, yang artinya model cukup oke dalam menjelaskan pola pada data training. Namun, ketika dievaluasi pada data testing, hasilnya justru sangat berbeda. Testing R² yang didapat adalah -0.268 dan Testing RMSE-nya 0.906.

Nilai R² testing yang negatif ini cukup mengkhawatirkan karena artinya model bahkan lebih buruk daripada sekadar menebak rata-rata. Selain itu, RMSE testing-nya hampir dua kali lipat dari RMSE training, menunjukkan bahwa error model meningkat drastis saat bertemu data baru. Secara keseluruhan, perbedaan ini mengindikasikan bahwa model terlalu menghafal data training dan tidak benar-benar menangkap pola yang sebenarnya.

**2. Based on the R² and RMSE values, how well does the model perform on unseen data?**

Kalau dilihat dari angkanya, model ini performanya kurang bagus pada unseen data. Testing R² yang bernilai -0.268 menandakan bahwa prediksi model pada data baru justru lebih buruk daripada kalau kita hanya memprediksi nilai rata-rata y untuk semua input. Ini merupakan tanda kegagalan generalisasi yang cukup jelas.

Testing RMSE (0.906) juga jauh lebih besar dibandingkan Training RMSE (0.517), yang berarti error-nya naik signifikan saat memprediksi data yang belum pernah dilihat. Ditambah lagi, hasil Cross-Validation juga menunjukkan skor yang sangat negatif (mean ≈ -3.05 × 10¹¹), yang semakin memperkuat bahwa model ini sangat tidak stabil dan tidak bisa diandalkan untuk memprediksi data baru.

**3. Observe the prediction curve produced by the model. Describe the behavior of the curve across the input range.**

Dari grafik kurva prediksinya, terlihat jelas bahwa kurva model sangat berfluktuasi dan tidak stabil. Alih-alih membentuk kurva yang halus dan mengikuti tren umum data, kurva ini justru naik-turun tajam di antara titik-titik data. Di bagian tengah rentang input (sekitar x = 1 sampai 4), kurva masih sedikit mengikuti arah data, tetapi tetap ada osilasi berlebihan yang seharusnya tidak perlu.

Yang paling mencolok adalah perilaku kurva di ujung rentang input, terutama di sekitar x = 6, di mana kurva tiba-tiba melonjak naik sangat tajam hingga jauh melampaui rentang data yang sebenarnya. Lonjakan ini terjadi karena sifat polynomial berderajat tinggi, di mana nilai pangkat besar seperti x¹⁵ akan membesar sangat cepat. Jadi bisa dikatakan, kurva ini lebih banyak mengikuti noise daripada pola fungsi sin(x) yang sebenarnya.

**4. Based on both the evaluation metrics and the visualization, identify the main issue affecting the model.**

Berdasarkan kombinasi metrik evaluasi dan visualisasi kurva, masalah utama yang dialami model ini adalah overfitting. Model polynomial degree 15 memiliki kompleksitas yang terlalu tinggi untuk dataset dengan hanya 40 sampel. Akibatnya, model cenderung menghafal setiap detail dan noise pada data training alih-alih mempelajari pola yang sesungguhnya.

Hal ini terbukti dari beberapa indikator: R² training yang cukup tinggi namun R² testing negatif, gap RMSE training dan testing yang sangat besar, kurva prediksi yang penuh osilasi dengan lonjakan ekstrem di ujungnya, serta cross-validation scores yang sangat buruk. Semua ini mengarah pada satu kesimpulan yang sama, yaitu model terlalu overfit.

---

## Part 2 – Possible Causes

Ada beberapa faktor yang menyebabkan model baseline berperilaku seperti ini:

**Model Complexity.** Model yang digunakan memiliki polynomial degree 15, yang berarti ada 16 koefisien yang perlu diestimasi. Padahal fungsi yang kita coba tangkap hanyalah sin(x), yaitu fungsi yang berbentuk sederhana dan halus. Dengan kompleksitas yang terlalu tinggi, model punya terlalu banyak kebebasan sehingga tidak hanya menangkap pola yang sesungguhnya, tetapi juga turut mempelajari noise yang ada di dalam data.

**Polynomial Feature Expansion.** Ketika kita menggunakan PolynomialFeatures dengan degree 15, fitur input X akan diperluas menjadi [1, X, X², X³, ..., X¹⁵]. Fitur-fitur berderajat tinggi seperti X¹⁰ hingga X¹⁵ nilainya akan tumbuh sangat cepat, terutama untuk nilai X yang besar. Akibatnya, model menjadi sangat sensitif terhadap perubahan kecil pada input dan menghasilkan prediksi yang sangat fluktuatif di batas-batas rentang data.

**Dataset Size.** Dataset yang digunakan hanya terdiri dari 40 sampel, yang memang tergolong kecil. Untuk model polynomial berderajat tinggi dengan banyak parameter, dibutuhkan data yang jauh lebih banyak agar koefisien-koefisiennya bisa diestimasi dengan akurat. Dengan sedikitnya data dan banyaknya parameter, model jadi underdetermined dan rentan terhadap overfitting.

**Noise in the Dataset.** Data target y dibuat dengan menambahkan noise Gaussian acak (np.random.normal(0, 0.8)) pada fungsi sin(x). Noise ini membuat titik-titik data menyimpang dari pola yang sebenarnya. Karena model terlalu kompleks, ia menganggap noise ini sebagai pola yang harus dipelajari dan berusaha mengikutinya. Model yang lebih sederhana tentunya akan cenderung mengabaikan noise ini, tetapi polynomial degree 15 justru menghafal noise tersebut secara berlebihan.

---

## Part 3 – Model Improvement

Untuk mengatasi permasalahan overfitting pada model baseline, saya mengusulkan dua metode perbaikan:

**Method 1: Reduce Polynomial Degree.** Metode pertama yang saya coba adalah mengurangi polynomial degree dari 15 menjadi 4. Alasan saya memilih degree 4 adalah karena degree ini sudah cukup fleksibel untuk menangkap pola non-linear seperti sin(x), namun tidak terlalu kompleks sehingga masih mampu melakukan generalisasi dengan baik pada data yang belum pernah dilihat.

**Method 2: Ridge Regularization.** Metode kedua adalah menerapkan Ridge Regression (L2 regularization) dengan tetap menggunakan polynomial degree 15 dan alpha = 1. Ridge Regression bekerja dengan menambahkan penalty terhadap koefisien yang terlalu besar pada loss function, sehingga model tetap terkontrol meskipun degree-nya tinggi. Saya juga menambahkan StandardScaler untuk menormalisasi fitur polynomial agar penalty regularization diterapkan secara adil pada semua koefisien.

### Implementasi

Method 1 - Reduced Polynomial Degree (Degree = 4):

```python
model_reduced = Pipeline([
    ("poly", PolynomialFeatures(degree=4)),
    ("linear", LinearRegression())
])
model_reduced.fit(X_train, y_train)
```

Method 2 - Ridge Regularization (Degree = 15, Alpha = 1):

```python
model_ridge = Pipeline([
    ("poly", PolynomialFeatures(degree=15)),
    ("scaler", StandardScaler()),
    ("ridge", Ridge(alpha=1))
])
model_ridge.fit(X_train, y_train)
```

### Perbandingan Hasil

| Model | Train R² | Test R² | Train RMSE | Test RMSE | Mean CV Score |
|-------|----------|---------|------------|-----------|---------------|
| Baseline (Degree 15) | 0.651 | -0.268 | 0.517 | 0.906 | -3.05 × 10¹¹ |
| Reduced Degree (Degree 4) | 0.411 | 0.277 | 0.672 | 0.684 | -21.70 |
| Ridge Regularization (Degree 15) | 0.329 | 0.184 | 0.717 | 0.727 | -181.77 |

### Interpretasi

Setelah membandingkan ketiga model, hasilnya cukup menarik. Model baseline jelas sekali mengalami overfitting karena Training R² yang cukup tinggi (0.651) berbanding terbalik dengan Testing R² yang negatif (-0.268). Gap antara RMSE training dan testing juga sangat besar.

Pada Method 1 (Reduce Polynomial Degree ke 4), model mengalami peningkatan yang signifikan di sisi testing. Testing R² naik dari -0.268 menjadi 0.277, yang artinya model sekarang sudah bisa memberikan prediksi yang lebih baik daripada sekadar menebak rata-rata. Yang paling bagus adalah gap antara Training RMSE (0.672) dan Testing RMSE (0.684) menjadi sangat kecil, menandakan model sudah jauh lebih stabil dan tidak lagi overfitting. Mean CV Score juga meningkat drastis dari -3.05 × 10¹¹ menjadi -21.70, yang menunjukkan kestabilan model jauh lebih baik. Kurva prediksinya pun terlihat halus dan mengikuti bentuk fungsi sin(x) dengan baik.

Pada Method 2 (Ridge Regularization), meskipun polynomial degree-nya masih 15, model tetap stabil berkat adanya L2 penalty. Testing R² menjadi positif di angka 0.184, dan Training RMSE (0.717) dengan Testing RMSE (0.727) juga sangat berdekatan dengan selisih hanya 0.01. Mean CV Score-nya -181.77, yang memang masih negatif tapi sudah jauh lebih baik dibandingkan baseline (-3.05 × 10¹¹). Ini menunjukkan bahwa Ridge Regression berhasil mengontrol koefisien-koefisien polynomial agar tidak terlalu besar dan menghasilkan model yang lebih konsisten.

### Kesimpulan

Dari eksperimen ini, saya menyimpulkan bahwa kedua metode berhasil mengatasi overfitting yang terjadi pada model baseline. Metode Reduce Polynomial Degree menghasilkan generalisasi yang paling baik dengan Test R² tertinggi (0.277), Test RMSE terendah (0.684), dan Mean CV Score terbaik (-21.70). Sementara itu, Ridge Regularization unggul dalam hal stabilitas gap antara performa training dan testing.

Secara praktis, jika tujuannya adalah mendapatkan prediksi terbaik pada data baru, maka menurunkan degree polynomial adalah pilihan paling sederhana dan efektif. Namun jika kita membutuhkan model dengan degree tinggi karena alasan tertentu, Ridge Regularization bisa menjadi solusi yang tepat untuk menjaga model tetap terkendali.

---

Visualisasi lengkap dapat dilihat pada notebook.

Google Colab Link: *(paste link Colab kamu di sini)*
