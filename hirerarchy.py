import pandas as pd
df=pd.read_csv("cars_meta.csv")
def split_name(n):
    parts=n.rsplit(' ',1)
    year=parts[-1] if parts[-1].isdigit() else ''
    core=parts[0] if year else n
    brand=core.split()[0]
    model=core.replace(brand,'').strip()
    return pd.Series([brand, model, year])
df[['brand','model','year']]=df['class_name'].apply(split_name)
df.to_csv("class_hierarchy.csv", index=False)
print("class_hierarchy.csv created")
