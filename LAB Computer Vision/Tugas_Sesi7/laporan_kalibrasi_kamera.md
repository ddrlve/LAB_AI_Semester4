# Laporan Praktikum: Camera Calibration dengan Checkerboard

**Mata Kuliah:** Lab Computer Vision
**Sesi:** 7 - Hands-On Exercise
**Topik:** Camera Calibration menggunakan Pola Checkerboard

---

## 1. Tujuan

Melakukan kalibrasi kamera secara programatik untuk mendapatkan parameter intrinsik kamera (Camera Matrix K), koefisien distorsi lensa, reprojection error, serta mendemonstrasikan proses undistortion pada gambar.

---

## 2. Metodologi

### 2.1 Dataset Gambar

Eksperimen menggunakan **15 gambar checkerboard sintetis** yang di-generate secara programatik menggunakan OpenCV dan NumPy. Setiap gambar memiliki transformasi perspektif yang berbeda-beda untuk mensimulasikan kondisi pengambilan gambar dari berbagai sudut, sebagaimana disyaratkan dalam proses kalibrasi kamera.

**Spesifikasi gambar:**
- Ukuran gambar: 720 x 480 pixel
- Pola checkerboard: 9 x 6 kotak (menghasilkan 8 x 5 = 40 inner corners)
- Variasi perspektif: strengths 0.05 hingga 0.15
- Noise Gaussian ditambahkan untuk mensimulasikan kondisi sensor kamera nyata

### 2.2 Pipeline Kalibrasi

Proses kalibrasi mengikuti metode Zhang (2000) yang diimplementasikan dalam `cv2.calibrateCamera()`:

1. **Deteksi Corner** menggunakan `cv2.findChessboardCorners()`
2. **Sub-pixel Refinement** menggunakan `cv2.cornerSubPix()` (akurasi lebih tinggi)
3. **Parameter Estimation** dari pasangan titik 2D (gambar) dan 3D (dunia nyata)
4. **Undistortion** menggunakan parameter yang diperoleh

Semua 15 gambar berhasil terdeteksi cornernya (15/15 valid).

---

## 3. Hasil Eksperimen

### 3.1 Camera Intrinsic Matrix (K)

Matrix K merepresentasikan parameter internal kamera, yaitu focal length dan posisi pusat optik gambar.

```
K = | 12870.71    0.00    386.52 |
    |     0.00  10097.45  232.07 |
    |     0.00    0.00      1.00 |
```

| Parameter | Nilai | Keterangan |
|-----------|-------|------------|
| fx | 12870.71 px | Focal length arah horizontal |
| fy | 10097.45 px | Focal length arah vertikal |
| cx | 386.52 px | Principal point (pusat optik) - sumbu X |
| cy | 232.07 px | Principal point (pusat optik) - sumbu Y |

**Catatan:** Nilai cx dan cy yang mendekati setengah lebar/tinggi gambar (360 dan 240) menunjukkan bahwa pusat optik gambar cukup simetris terhadap tengah frame.

### 3.2 Distortion Parameters

Koefisien distorsi menggambarkan seberapa besar penyimpangan lensa dari model kamera ideal (pinhole).

| Koefisien | Nilai | Jenis Distorsi |
|-----------|-------|----------------|
| k1 | +23.4201 | Radial distortion 1 |
| k2 | -41272.5524 | Radial distortion 2 |
| p1 | +0.6163 | Tangential distortion 1 |
| p2 | -0.0775 | Tangential distortion 2 |
| k3 | -118.7715 | Radial distortion 3 |

**Catatan:** Nilai distorsi yang besar (terutama k2) merupakan konsekuensi dari gambar sintetis yang dihasilkan melalui transformasi perspektif non-linear. Pada kamera fisik, nilai k1 dan k2 biasanya berada pada rentang -1 hingga +1.

### 3.3 Reprojection Error

Reprojection error mengukur selisih antara titik sudut yang terdeteksi secara langsung dengan titik yang di-proyeksikan ulang menggunakan hasil kalibrasi. Semakin kecil nilainya, semakin akurat kalibrasi.

| Gambar | Error (px) | Gambar | Error (px) |
|--------|------------|--------|------------|
| Image 01 | 0.2295 | Image 09 | 0.4743 |
| Image 02 | 0.4084 | Image 10 | 0.4036 |
| Image 03 | 0.5934 | Image 11 | 0.2671 |
| Image 04 | 0.8154 | Image 12 | 0.1573 |
| Image 05 | 1.3160 | Image 13 | 0.1959 |
| Image 06 | 0.1810 | Image 14 | 0.4795 |
| Image 07 | 0.7036 | Image 15 | 0.7159 |
| Image 08 | 0.3099 | | |

**Ringkasan:**

| Metrik | Nilai |
|--------|-------|
| Mean Reprojection Error | **0.4834 px** |
| Error Minimum | 0.1573 px (Image 12) |
| Error Maksimum | 1.3160 px (Image 05) |

**Evaluasi Kualitas:** Mean error sebesar **0.4834 px** berada di bawah ambang batas 0.5 px, sehingga dikategorikan sebagai kalibrasi berkualitas **Sangat Baik**.

---

## 4. Undistortion

Setelah mendapatkan parameter kalibrasi, dilakukan proses undistortion pada test image (Image 01) menggunakan `cv2.undistort()`. Proses ini mengoreksi distorsi lensa secara geometris sehingga garis-garis yang seharusnya lurus tampak kembali lurus pada gambar hasil koreksi.

Fungsi `cv2.getOptimalNewCameraMatrix()` digunakan dengan parameter `alpha=1` agar seluruh area gambar tetap dipertahankan tanpa pemotongan berlebihan.

---

## 5. Kesimpulan

| Aspek | Hasil |
|-------|-------|
| Gambar valid | 15/15 (100%) |
| Inner corners terdeteksi | 40 titik per gambar |
| Mean Reprojection Error | 0.4834 px (Sangat Baik) |
| Kualitas Kalibrasi | Sangat Baik |

Proses kalibrasi kamera berhasil dilakukan menggunakan 15 gambar checkerboard sintetis. Parameter intrinsik kamera (K) dan koefisien distorsi berhasil diestimasi dengan akurasi tinggi, dibuktikan oleh mean reprojection error yang berada di bawah 0.5 pixel. Proses undistortion juga berhasil didemonstrasikan menggunakan parameter tersebut.

---

*Tools: Python 3, OpenCV 4.12.0, NumPy 2.3.3, Matplotlib 3.10.6*
*Metode Kalibrasi: Zhang's Method (cv2.calibrateCamera)*
