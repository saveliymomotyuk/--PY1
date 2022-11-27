import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    listdik = []
    rowslist = []
    with open(filename, 'r') as f:
        result = f.readlines()
        headers = result[0].rstrip().split(sep=',')
        for row in result[1:]:
            rowslist.append(row.strip().split(sep=','))
        for x in rowslist:
            a = {k:v for k, v in zip(headers, x)}
            listdik.append(a)

    return listdik
    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
