# ============================================

# CARA INSTALL LIBRARY KE VIRTUAL ENVIRONMENT

# ============================================

## 📌 OPTION 1: Menggunakan venv (Python Built-in)

### Windows:

```powershell
# 1. Buat virtual environment baru
python -m venv myenv

# 2. Aktivasi virtual environment
myenv\Scripts\activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install dari requirements.txt
pip install -r requirements.txt

# ATAU install manual satu per satu:
pip install torch torchvision opencv-python transformers
pip install biopython scikit-learn xgboost lightgbm
pip install pandas numpy matplotlib seaborn

# 5. Verifikasi instalasi
pip list

# 6. Deactivate saat selesai
deactivate
```

### Mac/Linux:

```bash
# 1. Buat virtual environment baru
python3 -m venv myenv

# 2. Aktivasi virtual environment
source myenv/bin/activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install dari requirements.txt
pip install -r requirements.txt

# 5. Deactivate saat selesai
deactivate
```

---

## 📌 OPTION 2: Menggunakan Conda/Anaconda

```bash
# 1. Buat conda environment baru dengan Python 3.10
conda create -n myenv python=3.10 -y

# 2. Aktivasi environment
conda activate myenv

# 3. Install packages via pip (lebih lengkap untuk deep learning)
pip install torch torchvision torchaudio
pip install transformers datasets accelerate
pip install opencv-python ultralytics
pip install biopython scikit-bio

# ATAU install via conda (lebih stabil tapi kadang versi lama)
conda install -c conda-forge numpy pandas scikit-learn matplotlib -y
conda install -c pytorch pytorch torchvision torchaudio -y

# 4. Install dari requirements.txt
pip install -r requirements.txt

# 5. Verifikasi instalasi
conda list

# 6. Deactivate
conda deactivate

# 7. Hapus environment (jika perlu)
conda env remove -n myenv
```

---

## 📌 OPTION 3: VS Code + Virtual Environment

### Di VS Code:

1. Tekan `Ctrl+Shift+P` (Windows) atau `Cmd+Shift+P` (Mac)
2. Ketik: "Python: Create Environment"
3. Pilih "Venv"
4. Pilih Python interpreter
5. Centang requirements.txt (jika ada)
6. Klik Create

### Mengganti Interpreter:

1. Tekan `Ctrl+Shift+P`
2. Ketik: "Python: Select Interpreter"
3. Pilih interpreter dari virtual environment kamu

---

## 📌 OPTION 4: Google Colab (Tidak Perlu Virtual Environment)

```python
# Langsung install di Colab Notebook
!pip install torch torchvision opencv-python
!pip install transformers datasets
!pip install biopython scikit-bio
!pip install xgboost lightgbm

# Atau install semua dari requirements.txt
!pip install -r requirements.txt

# Verifikasi
import torch
import cv2
import transformers
print("✅ Semua library berhasil diimport!")
```

---

## 📌 TIPS:

### Melihat Library yang Terinstall:

```bash
pip list                    # Semua packages
pip show torch              # Detail package tertentu
pip freeze > requirements.txt  # Export ke file
```

### Uninstall Package:

```bash
pip uninstall torch -y
```

### Update Package:

```bash
pip install --upgrade torch
pip install --upgrade pip   # Update pip itu sendiri
```

### Install Versi Spesifik:

```bash
pip install torch==2.0.0
pip install numpy>=1.20.0,<2.0.0
```

### Install PyTorch dengan CUDA (untuk GPU):

```bash
# Cek CUDA version dulu: nvidia-smi
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## 📌 TROUBLESHOOTING:

### Error "pip not found":

```bash
python -m pip install --upgrade pip
```

### Error Module Not Found:

```bash
# Pastikan virtual environment sudah aktif
# Cek interpreter yang dipakai
python -c "import sys; print(sys.executable)"
```

### Slow Download:

```bash
# Gunakan mirror Indonesia
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple torch
```

### Permission Denied:

```bash
# Gunakan --user flag
pip install --user torch
```

---

## ✅ PACKAGE LIST LENGKAP:

### Deep Learning:

- torch, torchvision, torchaudio (PyTorch)
- tensorflow, keras (TensorFlow)

### Computer Vision:

- opencv-python, opencv-contrib-python
- albumentations, timm, ultralytics
- mediapipe, pillow, scikit-image

### NLP:

- transformers, datasets, accelerate
- spacy, gensim, textblob
- sentence-transformers, nltk

### Biology:

- biopython, scikit-bio
- pyensembl, pysam

### ML Traditional:

- scikit-learn, xgboost
- lightgbm, catboost

### Data Science:

- pandas, numpy, scipy
- matplotlib, seaborn, plotly

### Tools:

- gradio, streamlit, jupyter
- tqdm (progress bar)
