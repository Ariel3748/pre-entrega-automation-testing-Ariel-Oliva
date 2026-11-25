import csv
import json

def reader_users_csv():
    with open("data/users.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
     
    