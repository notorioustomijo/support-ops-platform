import csv

with open("tickets.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"].strip().lower() == "open":
            print(f"{row['id']}. {row['subject']}")