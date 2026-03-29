import csv

def sum_track_times(file_path):
    total_minutes = 0
    total_seconds = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            minutes, seconds = map(int, row['Time'].split(':'))
            total_minutes += minutes
            total_seconds += seconds

    # Convert total seconds to minutes and seconds
    total_minutes += total_seconds // 60
    total_seconds %= 60

    return f"{total_minutes}:{total_seconds:02}"

# Example usage
csv_file_path = "music.csv"  # Replace with the path to your CSV file
print(sum_track_times(csv_file_path))
