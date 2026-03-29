import csv

def reconcile_transactions(file1, file2):
  """
  Reconciles two CSV files of financial transactions.

  Args:
    file1: Path to the first CSV file.
    file2: Path to the second CSV file.

  Returns:
    A list of tuples, where each tuple represents a transaction that was
    removed from file1, added to file2, or has a difference in amount.
  """

  with open(file1, 'r') as f1, open(file2, 'r') as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    header1 = next(reader1)  # Skip the header row
    header2 = next(reader2)

    # Check if headers are the same
    if header1 != header2:
      raise ValueError("Headers in the two files do not match.")

    transactions1 = set(tuple(row) for row in reader1)
    transactions2 = set(tuple(row) for row in reader2)

    removed = transactions1 - transactions2
    added = transactions2 - transactions1

    # Check for differences in amount
    differences = []
    for t1 in transactions1:
      for t2 in transactions2:
        if t1[:3] == t2[:3] and t1[3] != t2[3]:  # Compare date, department, amount
          differences.append(f"Amount mismatch: {t1} vs. {t2}")

    return list(removed), list(added), differences

if __name__ == "__main__":
  import sys

  if len(sys.argv) != 3:
    print("Usage: python reconcile.py <file1> <file2>")
    sys.exit(1)

  file1 = sys.argv[1]
  file2 = sys.argv[2]

  removed, added, differences = reconcile_transactions(file1, file2)

  if removed:
    print("Removed:")
    for transaction in removed:
      print(f"  {', '.join(transaction)}")

  if added:
    print("Added:")
    for transaction in added:
      print(f"  {', '.join(transaction)}")

  if differences:
    print("Amount Mismatches:")
    for difference in differences:
      print(f"  {difference}")
