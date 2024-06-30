import csv

with open('test1.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([12, 'Valik', 33])
    writer.writerow([43, 'Bogdan', 1])
    writer.writerow([789, 'Alice', 33])
    writer.writerow([5260, 'Mike', 178])
