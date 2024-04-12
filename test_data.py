import random

sitzplan = {}


def generate_status():
    return random.choice(["o", "c"])


for i in range(1, 11):
    for j in range(1, 21):
        status = generate_status()
        sitzplan[f"A{i}-{j}"] = {"Preis": 50, "Status": status}


for i in range(1, 11):
    for j in range(1, 21):
        status = generate_status()
        sitzplan[f"B{i}-{j}"] = {"Preis": 40, "Status": status}


for i in range(1, 11):
    for j in range(1, 21):
        status = generate_status()
        sitzplan[f"C{i}-{j}"] = {"Preis": 30, "Status": status}


for i in range(1, 11):
    for j in range(1, 21):
        status = generate_status()
        sitzplan[f"D{i}-{j}"] = {"Preis": 20, "Status": status}


with open("test_data.txt", "w") as file:
    for sitzplatz, daten in sitzplan.items():
        file.write(f"{sitzplatz}, {daten['Preis']}, {daten['Status']}\n")
