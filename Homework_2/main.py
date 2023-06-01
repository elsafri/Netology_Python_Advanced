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
        new_pattern = r"+7(\1)\2-\3-\4 \5\6"
        contact[5] = re.sub(pattern, new_pattern, contact[5])
    return file_list


def duplicates_correction(file_list):
    result = file_list
    tmp_list = []
    for k, i in enumerate(file_list):
        for c in range(k + 1, len(file_list)):
            if i[0] == file_list[c][0] and i[1] == file_list[c][1]:
                if i[2] == '':
                    result[k][2] = file_list[c][2]
                else:
                    result[k][2] = i[2]
                if i[3] == '':
                    result[k][3] = file_list[c][3]
                else:
                    result[k][3] = i[3]
                if i[4] == '':
                    result[k][4] = file_list[c][4]
                else:
                    result[k][4] = i[4]
                if i[5] == '':
                    result[k][5] = file_list[c][5]
                else:
                    result[k][5] = i[5]
                if i[6] == '':
                    result[k][6] = file_list[c][6]
                else:
                    result[k][6] = i[6]
                tmp_list.append(c)

    for k, i in enumerate(tmp_list):
        result.pop(i - k)
    return result


def correct_file(file):
    with open(file, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=',')
        file_list = list(rows)

    names_file_list = names_correction(file_list)
    phones_file_list = phones_correction(names_file_list)
    final_file_list = duplicates_correction(phones_file_list)

    with open('phonebook.csv', 'w', encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_file_list)


if __name__ == '__main__':
    correct_file('phonebook_raw.csv')



