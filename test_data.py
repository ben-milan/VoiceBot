import pandas as pd
import random

def generate_data():
    return random.choice(["o", "c"])

columns = ["Sektor", "Reihe", "Platz", "Preis", "Status"]
sitzplan_df = pd.DataFrame(columns=columns)

for sektor in ["A", "B", "C", "D"]:
    for reihe in range(1, 11):
        for platz in range(1, 21):
            preis = 50 if sektor == "A" else 40 if sektor == "B" else 30 if sektor == "C" else 20
            status = generate_data()
            sitzplan_df = sitzplan_df._append({
                                              "Sektor": sektor,
                                              "Reihe": reihe,
                                              "Platz": platz,
                                              "Preis": preis,
                                              "Status": status}, ignore_index=True)

sitzplan_df.to_csv("test_data.csv", index=False)


