import csv

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    print(type(reader))
    for line in reader:
        print(line)

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file)
    csv_list = list(reader)
    print(csv_list)

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

    for line in reader:
        print(line)

    print(reader.line_num)

with open('test1.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader:
        print(line)
