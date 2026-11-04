df['Result'] = df['Grade'].apply(lambda g: 'Pass' if g >= 60 else 'Fail')

df['Combined_Score'] = (df['Grade'] * 0.7 + df['Attendance'] * 0.3).round(1)

print("--- First 10 Rows with New Columns ---")
print(df[['Name', 'Grade', 'Attendance', 'Result', 'Combined_Score']].head(10))

print("\n--- Result Counts ---")
print(df['Result'].value_counts())