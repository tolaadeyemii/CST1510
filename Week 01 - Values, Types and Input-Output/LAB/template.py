"""
RECORD CHECK  -  my version
===========================

Name  : Adetola Adeyemi
Lane  :  AI      (delete two)
Date  : 23rd September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. 

dataset_name = input("Dataset Name: ")     
rows_loaded = int(input("Rows Loaded: ")) 
rows_expected = int(input("Rows Expected: "))    


# ================================================================== PROCESS
# 2. 

difference = rows_expected - rows_loaded   
percent = (rows_loaded / rows_expected) * 100  


# =================================================================== OUTPUT
# 3. 
print()
print("=" * 34)
print(f"  DATASET CHECK  -  {dataset_name}")
print("=" * 34)

# : your report lines go here

print("=" * 34)
print(f"Rows Loaded: {rows_loaded:>10}")
print(f"Rows Expected: {rows_expected:>10}")
print(f"Difference: {difference:>+10}")
print(f"Percent: {percent:>10.2f}%")

print("=" * 34)
print("I am really enjoying this course and learning about Python programming!")
print("=" * 34)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
