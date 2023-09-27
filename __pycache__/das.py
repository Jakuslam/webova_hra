import csv

with open("countries.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
