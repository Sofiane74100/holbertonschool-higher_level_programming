import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Open the CSV file and read the data
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON format
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
