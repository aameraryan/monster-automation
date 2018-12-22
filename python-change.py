import csv
csv_file = open('tobechanged.csv', 'r')
new_csv_file = open('changed.csv', 'a')

fieldnames = ['name', 'link', 'exp', 'location', 'nationality', 'info', 'extra_info', 'phone', 'email', 'extra_details', 'industry', 'heading', 'new_email']


reader = csv.DictReader(csv_file)
writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)

writer.writeheader()

for row in reader:
    old_email = row['email']
    # if '\n' in str(old_email):
    #     ll = old_email.split('\n')
    #     new_email = ll[-1]
    place = old_email.strip().rfind(' ')
    new_email = old_email[place-1:]

    new_row = dict(row)
    new_row.update({'new_email': new_email})
    writer.writerow(new_row)
    print(new_row)
