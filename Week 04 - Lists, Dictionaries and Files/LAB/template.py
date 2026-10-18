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

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
   difference = value - limit
   percent = (value - limit) * 100 if limit != 0 else 0
   status = "OVER LIMIT" if value > limit else "OK"
   return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
   print(f"{label}: Value={value}, Limit={limit}, Difference={difference}, {percent:.1f}%, Status={status}")

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
  loaded_list = []
  with open(path, "r") as file:
    for line in file:
      line = line.strip()
      parts = line.split(",")

      label = parts[0]
      value = float(parts[1])
      limit = float(parts[2])

      record = {"label": label, "value": value, "limit": limit}
      loaded_list.append(record)

  return loaded_list
records = load_records("data.txt")



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit_count = 0
output_file = open("results.txt", "w")
for record in records:
  label = record["label"]
  value = record["value"]
  limit = record["limit"]
diff, pct, status = check_record(value, limit)
output_file.write(label + "," + status + "\n")

if status == "OVER LIMIT":
  over_limit_count = over_limit_count + 1
output_file.close()
print("Total records OVER LIMIT:", over_limit_count)
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
