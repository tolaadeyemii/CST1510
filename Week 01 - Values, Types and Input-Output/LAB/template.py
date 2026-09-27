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

label = input("Label: ")      # : replace with an input() call
first = float(input("Value 1: "))     # : replace with an input() call, converted
second = float(input("Value 2: "))    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. 

difference = second - first   
percent = (first / second) * 100  


# =================================================================== OUTPUT
# 3. 
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here

print("=" * 34)
print(f"First Value: {first:>10.2f}")
print(f"Second Value: {second:>10.2f}")
print(f"Difference: {difference:>+10.2f}")
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
