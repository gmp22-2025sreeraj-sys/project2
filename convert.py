# convert_mat_to_csv.py
from scipy.io import loadmat
import pandas as pd
import os

base = os.path.dirname(os.path.abspath(__file__))

# === 1. Meta ===
meta = loadmat(os.path.join(base, "cars_meta.mat"))
class_names = [c[0] for c in meta["class_names"][0]]
pd.DataFrame({
    "class_id": range(1, len(class_names)+1),
    "class_name": class_names
}).to_csv(os.path.join(base, "cars_meta.csv"), index=False)
print("cars_meta.csv created")

# === 2. Train annotations ===
train = loadmat(os.path.join(base, "cars_train_annos.mat"))
records = []
for ann in train["annotations"][0]:
    records.append({
        "bbox_x1": int(ann[0][0]),
        "bbox_y1": int(ann[1][0]),
        "bbox_x2": int(ann[2][0]),
        "bbox_y2": int(ann[3][0]),
        "class_id": int(ann[4][0]),
        "fname": str(ann[5][0])
    })
pd.DataFrame(records).to_csv(os.path.join(base, "cars_train_annos.csv"), index=False)
print("cars_train_annos.csv created")

# === 3. Test annotations ===
test = loadmat(os.path.join(base, "cars_test_annos.mat"))
records_test = []
for ann in test["annotations"][0]:
    records_test.append({
        "bbox_x1": int(ann[0][0]),
        "bbox_y1": int(ann[1][0]),
        "bbox_x2": int(ann[2][0]),
        "bbox_y2": int(ann[3][0]),
        "fname": str(ann[5][0])
    })
pd.DataFrame(records_test).to_csv(os.path.join(base, "cars_test_annos.csv"), index=False)
print("cars_test_annos.csv created")

print("\n✅ Conversion complete. CSVs are ready.")
