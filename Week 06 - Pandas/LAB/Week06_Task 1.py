import pandas as pd
df = pd.read_csv("DATA/students.csv")
print("First 5 rows")
print(df.head(5))

print("Last 3 rows")
print(df.tail(3))

print("n-- Shape (Rows, Columns)--")
print(df.shape)
print("n-- Column names list --")
print(df.columns.tolist())