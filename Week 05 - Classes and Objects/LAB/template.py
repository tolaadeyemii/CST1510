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

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record label, value and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Return the warning level based on the value-to-limit ratio."""
        ratio = self.value / self.limit

        if ratio >= 1.0:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif ratio >= 0.9:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.


def load_records(path):
    records_list = []

    try:
        with open(path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                dataset_name, rows_loaded, rows_expected = parts

                new_record = Record(dataset_name, rows_loaded, rows_expected)
                records_list.append(new_record)
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found. Please create it first")

    return records_list
records = load_records("datasets.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

over_limit_count = 0
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

current_status = record.status()
if current_status == "OVER LIMIT":
    over_limit_count += 1

print(f"Value  :{record.value}")
print(f"Limit  :{record.limit}")
print(f"Status :{current_status}")
print("=" * 34)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
