import json

with open(r'C:\Users\1\django\backend\fixtures\animals\animals.json') as f:
    json_file = json.load(f)

breed_list = []

for el in json_file:
    breed_list.append(el["fields"]['breed'])

age_list = [i for i in range(1, 9)]

limit_list = [i for i in range(1, 21)]

offset_list = [i for i in range(0, 20)]

gender_list = ['female', 'male']

type_list = ['cat', 'dog']

id_list = [i for i in range(1, 6)]