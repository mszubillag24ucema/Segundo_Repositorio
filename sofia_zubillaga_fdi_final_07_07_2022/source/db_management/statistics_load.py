import csv
from source.models.brazalete import Brazalete


def load_statistics(): # traer la informacion que hay en el archivo statistics.csv
    stats = []
    with open('source/db_management/statistics.csv', 'r') as statistics_file:
        rows = csv.DictReader(statistics_file)
        for row in rows:
            stats.append(Brazalete(
                row['date'],
                row['dna'],
                row['blod_sugar_level'],
                row['emotion_level'],


            ))
    return stats


def save_statistics(stats): # agregar los datos que se cargan desde postman
    with open('source/db_management/statistics.csv', 'a') as statistics_file:
        header = ["date", "dna", "blod_sugar_level", "emotion_level"]
        writer = csv.DictWriter(statistics_file, fieldnames=header)

        if statistics_file.tell() == 0: # para que el header aparezca solo al principio del db
            writer.writeheader()

        writer.writerow(stats)
