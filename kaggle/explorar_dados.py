import os
import pandas as pd

caminho = r"C:\Users\Matheus\.cache\kagglehub\datasets\bharatnatrayn\movies-dataset-for-feature-extracion-prediction\versions\1"

arquivo_csv = os.path.join(caminho, "movies.csv")

df = pd.read_csv(arquivo_csv)

print("Primeiras linhas do dataset: ")
print(df.head())