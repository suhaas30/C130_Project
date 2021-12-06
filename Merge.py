import pandas as pd
import csv

dataset_1 = []
dataset_2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)
with open("unit_converted_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers1 = dataset_1[0]
headers2 = dataset_2[0]
stars_data1 = dataset_1[1:]
stars_data2 = dataset_2[1:]

stars_data = []

headers = headers1 + headers2

for index, datarow in enumerate(stars_data1):
    stars_data.append(stars_data1[index] + stars_data2[index])
    

with open("final_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)