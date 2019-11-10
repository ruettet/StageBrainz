from json import dumps
from codecs import open

with open("./catalog/fixtures/entity_and_relation_types.csv", "r", "utf-8") as f:
    lines = f.read().split("\n")

header = lines[0].split(",")

fixtures = []

for line in lines[1:]:
    print(line)
    fixture = {"fields": {}}
    for i, value in enumerate(line.split(",")):
        if len(value) > 0:
            key = header[i]
            if key in ["model", "pk"]:
                fixture[key.replace(" ", "_")] = value
            if key in ["name", "abbreviation"]:
                fixture["fields"][key.replace(" ", "_")] = value

    fixtures.append(fixture)

with open("./catalog/fixtures/entity_and_relation_types.json", "w", "utf-8") as f:
    f.write(dumps(fixtures, indent=4))
