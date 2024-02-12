import csv
from time import sleep

with open ('Airline_Delay_Cause.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
        sleep(1)