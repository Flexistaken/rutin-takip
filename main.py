import datetime as dt
import json


gunluk = {"2026-09-15": {"journal": True, "reading": True, "workout": True, "commit": True}}

with open("veriler.JSON", "w") as dosya:
    json.dump(gunluk, dosya)

with open("veriler.JSON", "r") as dosya:
    x = json.load(dosya)
    print(x)
    print(type(x))
    print(x["2026-09-15"])
    

