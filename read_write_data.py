import csv

def modifyCSV(orginfilename, newfilename):
    with open (orginfilename + '.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open (newfilename + '.csv', 'w', newline = '') as file:
            reqCol = ["arr_flights", "security_ct", "carrier_ct", "arr_cancelled", "arr_diverted",
                  "arr_del15", "weather_ct", "nas_ct", "late_aircraft_ct"]
            csv_writer = csv.DictWriter(file, fieldnames = reqCol)
            csv_writer.writeheader()
            for line in csv_reader:
                del line['month']
                del line['year']
                del line['carrier_name']
                del line['airport_name']
                del line['carrier']
                del line['airport']
                del line['arr_delay']
                del line['carrier_delay']
                del line['weather_delay']
                del line['security_delay']
                del line['nas_delay']
                del line ['late_aircraft_delay']
                csv_writer.writerow(line)