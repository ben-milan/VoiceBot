sitzplan = {}


for i in range(1, 11):
    for j in range(1, 21):
        sitzplan[f"A{i}-{j}"] = {"Preis": 50}


for i in range(1, 11):
    for j in range(1, 21):
        sitzplan[f"B{i}-{j}"] = {"Preis": 40}


for i in range(1, 11):
    for j in range(1, 21):
        sitzplan[f"C{i}-{j}"] = {"Preis": 30}


for i in range(1, 11):
    for j in range(1, 21):
        sitzplan[f"D{i}-{j}"] = {"Preis": 20}

print(sitzplan)
with open("test_data.txt", "w") as file:
    for sitzplatz, daten in sitzplan.items():
        file.write(f"{sitzplatz}, {daten['Preis']}\n")
