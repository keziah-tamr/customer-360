import csv
import os
import json


def make_json(file_name, id_name):
    file_def = {}
    file_def['primary_id'] = id_name
    body_request_template= { "action": "CREATE", "recordId": None, "record": {} }
    with open(file_name) as csvfile:
        with open("dig_prods_json.txt", 'w') as file_handle_out:
            spamreader = csv.reader(csvfile)
            for num_line, line in enumerate(spamreader):
                if num_line == 0:
                    simple_header = line
                    print simple_header
                else:
                #For each line in the raw file, transform that line into a json dict.
                    record={simple_header[n]: [data] for n, data in enumerate(line) if data}

                    #swap edl to $value and remove key for $value
                    record["edl_is_deleted"] = record["value"]
                    record.pop('value', None)

                    body_request_template['record'] = record
                    body_request_template['recordId'] = record[file_def['primary_id']][0]
                    #And write that json dict to disk.
                    json.dump(body_request_template, file_handle_out)
                    file_handle_out.write('\n')

                
make_json("dig_prods.csv", "id")
print('done')
