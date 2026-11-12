
import csv
import os

def save_result(strategy, score, winner):
    filename = "results.csv"
    exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not exists:
            writer.writerow([
                "strategie",
                "score",
                "victoire"
            ])

        writer.writerow([
            strategy,
            score,
            int(winner)
        ])
