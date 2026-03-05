# Quick Start - Install Libraries

## Install di Notebook

Jalankan cell 3 di notebook.

## Install di Virtual Environment

### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

### Mac/Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## Install di Conda

```bash
conda create -n myenv python=3.10
conda activate myenv
pip install -r requirements.txt
```

## Test

```python
import torch, cv2, transformers
print("✅ Done!")
```
