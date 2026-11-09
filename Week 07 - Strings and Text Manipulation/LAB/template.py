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
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):

    raw_line = raw_line.strip()
    parts = raw_line.split(",")
    survey = parts[0].strip()
    record = {"survey": survey}

    for part in parts[1:]:
        key, value = part.split("=")

        key = key.strip().lower()
        value = value.strip()

        if key == "rating" or key == "age":
            value = int(value)

        record[key] = value

    return record

def status_of(record):

    rating = record["rating"]
    age = record["age"]

    if rating < 1 or rating > 5:
        return "FLAGGED"

    elif age < 0 or age > 120:
        return "FLAGGED"

    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [
    " Survey_2026 , rating=4 , age=23 ",
    "SURVEY_2025, RATING=5, AGE=31",
    " Survey_2024 , rating=3 , age=19 ",
    "survey_2023, rating=7, age=25",
    " Survey_2022 , rating=2 , age=145 "
]
with open("messy_lines.txt", "w") as file:
    for record in raw_records:
        file.write(record + "\n")

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged_count = 0
total_records = 0

with open("messy_lines.txt", "r") as file:

    for raw_record in file:

        clean_record = parse_line(raw_record)
        status = status_of(clean_record)
        print("Cleaned record:", clean_record)
        print("Status:", status)
        print("--------------------------")

        total_records += 1
        if status == "FLAGGED":
            flagged_count += 1

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
