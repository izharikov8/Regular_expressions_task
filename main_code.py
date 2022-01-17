from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

PHONE_PATTERN = r"(\+7|8)\s?\(?(\d{3})[\s-]?\)?\s?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?(\w*\.)?\s?(\d+)?\)?"
PHONE_FORMAT = r"+7(\2)\3-\4-\5 \6\7"

final_list = []
new_list = []


def name_phone_edit(data: list):
    for contact in data:
        full_name = ' '.join(contact[:3])
        split_name = full_name.split(' ')
        result = [split_name[0], split_name[1], split_name[2],
                contact[3], contact[4],
                re.sub(PHONE_PATTERN, PHONE_FORMAT, contact[5]),
                contact[6]]
        new_list.append(result)


def remove_duplicates(data: list):
    for contact in data:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in data:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                index = 2
                while index <= 6:
                    if contact[index] == '':
                        contact[index] = new_contact[index]
                    index += 1
    for element in data:
        if element not in final_list:
            final_list.append(element)


name_phone_edit(contacts_list)

remove_duplicates(new_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(final_list)


