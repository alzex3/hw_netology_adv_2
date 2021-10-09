import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


for contact in contacts_list[1:]:
    name_join = ' '.join(contact[:3])
    name_split = name_join.strip().split(' ')

    for i, name in enumerate(name_split):
        contact[i] = name_split[i]


for contact in contacts_list[1:]:
    number = contact[5]
    result1 = re.sub(r'^8', '+7', number)
    result2 = re.sub(r'\+7\s*\D*495\D*\s*', '+7(495)', result1)
    result3 = re.sub(r'(\)\d{3})(\s|-)*(\d{2})(\s|-)*(\d+)', r'\1-\3-\5', result2)
    result4 = re.sub(r'\s*\(*доб.\s*(\d+)\)*', r' доб.\1', result3)
    contact[5] = result4


names = []
duplicates = []
for contact in contacts_list[1:]:
    if ' '.join(contact[0:2]) not in names:
        names.append(' '.join(contact[0:2]))
    else:
        for element in contacts_list[1:]:
            if contact == element:
                duplicates.append(contact)
                contacts_list.remove(element)

for duplicate in duplicates:
    for element in contacts_list:
        if duplicate[0] == element[0]:
            for i, n in enumerate(element):
                if duplicate[i] != '':
                    element[i] = duplicate[i]


with open("phonebook.csv", "w") as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerows(contacts_list)
