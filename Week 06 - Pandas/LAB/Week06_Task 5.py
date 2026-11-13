import pandas as pd
df = pd.read_csv('01 - Series and DataFrame/examples/servers.csv')

print("Top 5 students by grade")
top_grades = df.sort_values(by="grade", ascending=False)
print(top_grades.head(5))
print("\n-- Sorted by city (A-Z) and grade (Low-High) --")
sorted_city_grade = df.sort_values(by=["City", "grade"], ascending=[True, True])
print(sorted_city_grade.head(10))