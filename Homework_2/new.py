import csv
import re


def names_correction(file_list):
    for contact in file_list[1:]:
        full_name = f'{contact[0]} {contact[1]} {contact[2]}'.strip()
        full_name_list = full_name.split(' ')
        if len(full_name_list) == 3:
            contact[0], contact[1], contact[2] = full_name_list[0], full_name_list[1], full_name_list[2]
        elif len(full_name_list) == 2:
            contact[0], contact[1] = full_name_list[0], full_name_list[1]
    return file_list


def phones_correction(file_list):
    for contact in file_list:
        pattern = r"(?:\+7|8)?[-\s]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(?:\s\(?(доб\.)\s(\d+)\)?)?"
        substitution = r"+7(\1)\2-\3-\4 \5\6"
        contact[5] = re.sub(pattern, substitution, contact[5])
    return file_list


def duplicates_erase(file_list):
    count = 1
    contacts_list = file_list[1:]
    for contact in file_list[1:]:
        for contact_check in contacts_list[count:]:
            if contact[0] == contact_check[0] and contact[1] == contact_check[1]:
                if contact[2] == '':
                    contact[2] = contact_check[2]
                if contact[3] == '':
                    contact[3] = contact_check[3]
                if contact[4] == '':
                    contact[4] = contact_check[4]
                if contact[5] == '':
                    contact[5] = contact_check[5]
                if contact[6] == '':
                    contact[6] = contact_check[6]
                file_list.remove(contact_check)
        count += 1
    return file_list


def correct_file(file):
    with open(file) as f:
        rows = csv.reader(f, delimiter=',')
        file_list = list(rows)

    names_final_list = names_correction(file_list)
    phones_final_list = phones_correction(names_final_list)
    final_file = duplicates_erase(phones_final_list)

    with open('phonebook.csv', 'w') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_file)


if __name__ == '__main__':
    correct_file('phonebook_raw.csv')