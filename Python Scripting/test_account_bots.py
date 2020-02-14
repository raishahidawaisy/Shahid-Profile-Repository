import csv

#final desired format > lets make it a list

test_accounts = []
with open('test_accounts.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        test_accounts.append(row)

bots_details = [["Name","Eamil","Password"]]

for row in test_accounts[1:]:
    bot_name = row[0]
    if not row[1] or not row[2]:
        continue
    bot_email = row[1]
    bot_password = row[2]
    bots_details.append([bot_name,bot_email,bot_password])

print (bots_details)
print (len(bots_details))
