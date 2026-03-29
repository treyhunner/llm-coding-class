import csv

csv_filename = "expenses.csv"

with open(csv_filename) as csv_file:
    reader = csv.DictReader(csv_file)
    total = sum(
        float(row["Cost"])
        for row in reader
        if row["Category"] == "Air Travel"
    )

print(total)
