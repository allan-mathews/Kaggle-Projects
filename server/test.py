import json

f = open('server/artifacts/columns.json', "r")

# Reading from file
data = json.loads(f.read())
