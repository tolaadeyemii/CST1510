"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

import pandas as pd
df = pd.read_csv("/Users/tola/Documents/CST1510/Week 06 - Pandas/LAB/ai_data.csv")  


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = ""

for i in range(len(df)):
    if df.loc[i, "percent"] >= 100:
        df.loc[i, "status"] = "OVER LIMIT"
    elif df.loc[i, "percent"] >= 90:
        df.loc[i, "status"] = "WARNING"
    else:
        df.loc[i, "status"] = "OK"

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)
print("\nRows that need attention:")
print(df[df["status"] != "OK"])

df.to_csv("ai_report.csv", index=False)
status_counts = df["status"].value_counts()

print("\nStatus counts:")
print(status_counts)

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
