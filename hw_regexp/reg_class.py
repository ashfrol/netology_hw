import re
from pprint import pprint
import csv
from os.path import join

with open(join('input', 'phonebook_raw.csv')) as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)

new_contacts_list = []
temp_dict_of_info = {}
count = 0
# pprint(contacts_list)
for contact in contacts_list:
    # print(contact)
    temp_lastname = contact[0].split()
    temp_firstname = contact[1].split()
    temp_surname = contact[2].split()
    organization = contact[3]
    position = contact[4]
    phone = contact[5]
    email = contact[6]
    if len(temp_lastname) == 3:
        lastname = temp_lastname[0]
        firstname = temp_lastname[1]
        surname = temp_lastname[2]
    elif len(temp_lastname) == 2:
        lastname = temp_lastname[0]
        firstname = temp_lastname[1]
    elif len(temp_lastname) == 1:
        lastname = temp_lastname[0]
    if len(temp_firstname) == 2:
        firstname = temp_firstname[0]
        surname = temp_firstname[1]
    elif len(temp_firstname) == 1:
        firstname = temp_firstname[0]
    if len(temp_surname) == 1:
        surname = temp_surname[0]

    regexp = '(\+7|8)?\s*\(*(\d+)\)*\s*(\d*)\-*(\d*)\-*(\d*)\s*\(*(\w*\.)*\s*(\d*)\)*'
    substitute = '+7\\2\\3\\4\\5 \\6\\7'
    phone = re.sub(regexp, substitute, phone).rstrip()


    new_contact = [lastname, firstname, surname, organization, position, phone, email]

    if temp_dict_of_info.get(lastname) is None:
        temp_dict_of_info[lastname] = count
        new_contacts_list.append(new_contact)
        count += 1
    else:
        temp_count = temp_dict_of_info[lastname]
        # print(temp_count)
        if not new_contacts_list[temp_count][0]:
            new_contacts_list[temp_count][0] = lastname
        if not new_contacts_list[temp_count][1]:
            new_contacts_list[temp_count][1] = firstname
        if not new_contacts_list[temp_count][2]:
            new_contacts_list[temp_count][2] = surname
        if not new_contacts_list[temp_count][3]:
            new_contacts_list[temp_count][3] = organization
        if not new_contacts_list[temp_count][4]:
            new_contacts_list[temp_count][4] = position
        if not new_contacts_list[temp_count][5]:
            new_contacts_list[temp_count][5] = phone
        if not new_contacts_list[temp_count][6]:
            new_contacts_list[temp_count][6] = email

with open(join('output', 'phonebook.csv'), 'w') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
