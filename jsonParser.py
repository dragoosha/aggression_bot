import json


def getAllData():
    with open("cnfg.json", "r") as jin:
        return json.load(jin)


def changeData(data, indent):
    with open("cnfg.json", "w") as jout:
        json.dump(data, jout, indent=indent)
