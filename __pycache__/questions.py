import csv


header = ['Question', 'Answ1', 'Answ2', 'rightAnsv']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]
with open('Questions/countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header

    # write multiple rows
    writer.writerows(data)

with open("Questions/countries.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
