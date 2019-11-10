from json import dumps
from codecs import open

with open("./catalog/fixtures/locale.csv", "r", "utf-8") as f:
    lines = f.read().split("\n")

header = lines[0].strip().split(",")
print(header)

fixtures = []

for line in lines[1:]:
    fixture = {"fields": {}}
    print(line.split(","))
    for i, value in enumerate(line.split(",")):
        if len(value) > 0:
            key = header[i]
            print(key, value)
            if key in ["model", "pk"]:
                fixture[key.replace(" ", "_")] = value
            if key in ["name", "abbreviation"]:
                fixture["fields"][key.replace(" ", "_")] = value

    fixtures.append(fixture)

with open("./catalog/fixtures/locale.json", "w", "utf-8") as f:
    f.write(dumps(fixtures, indent=4))
