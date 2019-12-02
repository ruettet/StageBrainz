from json import dumps
from codecs import open

with open("./catalog/fixtures/productions.csv", "r", "utf-8") as f:
    lines = f.read().split("\n")

header = lines[0].strip().split("\t")
print(header)

fixtures = []

for line in lines[1:]:
    fixture = {"fields": {}}
    print(line.split("\t"))
    for i, value in enumerate(line.strip().split("\t")):
        if len(value) > 0:
            key = header[i]
            print(key, value)
            if key in ["model", "pk"]:
                fixture[key.replace(" ", "_")] = value
            if key in ["name", "sort_name", "disambiguation"]:
                fixture["fields"][key.replace(" ", "_")] = value

    fixtures.append(fixture)

with open("./catalog/fixtures/productions.json", "w", "utf-8") as f:
    f.write(dumps(fixtures, indent=4))
