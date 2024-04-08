import csv

def modifyCSV():
    
    with open ('Airline_Delay_Cause.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open ('Airline_Delay_Cause_No_Extra_Info.csv', 'w', newline = '') as file:
            reqCol = ["arr_del15", "carrier_ct", "security_delay", "arr_flights", "carrier_delay", "arr_diverted",
                  "weather_ct", "security_ct", "nas_ct", "arr_cancelled", "late_aircraft_ct",
                  "arr_delay", "weather_delay", "nas_delay", "late_aircraft_delay"]
            csv_writer = csv.DictWriter(file, fieldnames = reqCol)
            csv_writer.writeheader()
            for line in csv_reader:
                #del line['']
                del line['month']
                del line['year']
                del line['carrier_name']
                del line['airport_name']
                del line['carrier']
                del line['airport']

                csv_writer.writerow(line)