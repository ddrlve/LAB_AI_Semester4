# ============================================
# DEMO: Test All Installed Libraries
# ============================================
# Run this script to verify all packages are working

import sys
print(f"Python: {sys.version}\n")
print("="*60)
print("Testing Installed Libraries...")
print("="*60 + "\n")

# Test imports
tests = []

# Deep Learning
try:
    import torch
    print(f"✅ PyTorch: {torch.__version__}")
    print(f"   CUDA Available: {torch.cuda.is_available()}")
    tests.append(("PyTorch", True))
except Exception as e:
    print(f"❌ PyTorch: {e}")
    tests.append(("PyTorch", False))

try:
    import tensorflow as tf
    print(f"✅ TensorFlow: {tf.__version__}")
    tests.append(("TensorFlow", True))
except Exception as e:
    print(f"❌ TensorFlow: {e}")
    tests.append(("TensorFlow", False))

# Computer Vision
try:
    import cv2
    print(f"✅ OpenCV: {cv2.__version__}")
    tests.append(("OpenCV", True))
except Exception as e:
    print(f"❌ OpenCV: {e}")
    tests.append(("OpenCV", False))

try:
    import albumentations
    print(f"✅ Albumentations: {albumentations.__version__}")
    tests.append(("Albumentations", True))
except Exception as e:
    print(f"❌ Albumentations: {e}")
    tests.append(("Albumentations", False))

try:
    import mediapipe
    print(f"✅ MediaPipe: {mediapipe.__version__}")
    tests.append(("MediaPipe", True))
except Exception as e:
    print(f"❌ MediaPipe: {e}")
    tests.append(("MediaPipe", False))

# NLP
try:
    import transformers
    print(f"✅ Transformers: {transformers.__version__}")
    tests.append(("Transformers", True))
except Exception as e:
    print(f"❌ Transformers: {e}")
    tests.append(("Transformers", False))

try:
    import spacy
    print(f"✅ spaCy: {spacy.__version__}")
    tests.append(("spaCy", True))
except Exception as e:
    print(f"❌ spaCy: {e}")
    tests.append(("spaCy", False))

try:
    import gensim
    print(f"✅ Gensim: {gensim.__version__}")
    tests.append(("Gensim", True))
except Exception as e:
    print(f"❌ Gensim: {e}")
    tests.append(("Gensim", False))

# Biology
try:
    import Bio
    print(f"✅ BioPython: {Bio.__version__}")
    tests.append(("BioPython", True))
except Exception as e:
    print(f"❌ BioPython: {e}")
    tests.append(("BioPython", False))

try:
    import skbio
    print(f"✅ scikit-bio: {skbio.__version__}")
    tests.append(("scikit-bio", True))
except Exception as e:
    print(f"❌ scikit-bio: {e}")
    tests.append(("scikit-bio", False))

# ML Libraries
try:
    import sklearn
    print(f"✅ scikit-learn: {sklearn.__version__}")
    tests.append(("scikit-learn", True))
except Exception as e:
    print(f"❌ scikit-learn: {e}")
    tests.append(("scikit-learn", False))

try:
    import xgboost
    print(f"✅ XGBoost: {xgboost.__version__}")
    tests.append(("XGBoost", True))
except Exception as e:
    print(f"❌ XGBoost: {e}")
    tests.append(("XGBoost", False))

try:
    import lightgbm
    print(f"✅ LightGBM: {lightgbm.__version__}")
    tests.append(("LightGBM", True))
except Exception as e:
    print(f"❌ LightGBM: {e}")
    tests.append(("LightGBM", False))

# Data Science
try:
    import pandas as pd
    print(f"✅ Pandas: {pd.__version__}")
    tests.append(("Pandas", True))
except Exception as e:
    print(f"❌ Pandas: {e}")
    tests.append(("Pandas", False))

try:
    import numpy as np
    print(f"✅ NumPy: {np.__version__}")
    tests.append(("NumPy", True))
except Exception as e:
    print(f"❌ NumPy: {e}")
    tests.append(("NumPy", False))

try:
    import matplotlib
    print(f"✅ Matplotlib: {matplotlib.__version__}")
    tests.append(("Matplotlib", True))
except Exception as e:
    print(f"❌ Matplotlib: {e}")
    tests.append(("Matplotlib", False))

# Summary
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
passed = sum(1 for _, result in tests if result)
total = len(tests)
print(f"✅ Passed: {passed}/{total}")
print(f"❌ Failed: {total-passed}/{total}")

if passed == total:
    print("\n🎉 All libraries installed successfully!")
else:
    print("\n⚠️ Some libraries failed to install.")
    print("\nFailed libraries:")
    for name, result in tests:
        if not result:
            print(f"  • {name}")
    print("\nRun: pip install <library-name> to fix")
