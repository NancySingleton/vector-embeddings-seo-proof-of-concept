import csv


def read(filename):
    with open(filename) as input_file:
        reader = csv.reader(input_file, delimiter='|')
        return [row for row in reader]


def write(filename, content):
    with open(filename, 'w') as output_file:
        writer = csv.writer(output_file, delimiter='|', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(content)