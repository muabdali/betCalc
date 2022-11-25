import csv
import glob


#creates combined standings

def combinedStandings():
    csv_files = {}      # (header as tuple) : csv.writer()
    header_type_count = 1
    for filename in glob.glob('*.csv'):
        with open(filename, newline='') as f_input:
            csv_input = csv.reader(f_input)
            header = tuple(next(csv_input))

            try:
                csv_files[header].writerows(csv_input)
            except KeyError:
                f_output = open(f'combinedStandings{header_type_count:02}.csv', 'w', newline='')
                header_type_count += 1
                csv_output = csv.writer(f_output)
                csv_files[header] = csv_output
                csv_output.writerow(header)
                csv_output.writerows(csv_input)
