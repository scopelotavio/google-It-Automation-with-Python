## DictReader - read
## DictReader() allows us to convert the data in a CSV file into a standard dictionary

import csv

with open("software.csv") as software:
    csv_file = csv.DictReader(software)
    for row in csv_file:
        print(("{} has {} readers").format(row["name"], row["users"]))
     