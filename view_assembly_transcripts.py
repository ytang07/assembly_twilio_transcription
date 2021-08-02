import json

files = ['pmo31a8t2-7778-4e20-bf0d-baff7fbaf72f_categories.json',
'pmojwgqta-8cc3-4a6c-a881-c8b83e3a9cce_categories.json',
'pmem7j6cw-4552-4baf-b5b8-4b90dc39f508_categories.json']
for _file in files:
    f = open(_file,'r')
    json_obj = json.load(f)
    text = json_obj['results'][0]['text']
    print(text)