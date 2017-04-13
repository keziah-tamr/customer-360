def create_json_files_orig(cfg, defs, datafolder):
    #Send this function a csv file with no header and a header object,
    #and the function writes a json object to disk.
    #Actually, it writes a list of json dictionaries, not a true json obj.
    for source, file_def in defs.iteritems():
        if file_def.get('local_name'):
            filepath_in=os.path.join(datafolder,file_def['file_modification_chain'][-1])
            simple_header, data=utils.import_file_from_csv(filepath_in)
            num_header_cols=len(simple_header)
            new_file_name='{0}.json'.format(file_def['local_name'])
            filepath_out=os.path.join(datafolder,new_file_name)
            with open(filepath_out, 'w') as file_handle_out:
                print 'Preparing to convert raw file {0} to json'.format(filepath_in)
                #This template is what each line of the output looks like.
                body_request_template= { "action": "CREATE", "recordId": None, "record": {} }
                for num_line,line in enumerate(data):
                    #For each line in the raw file, transform that line into a json dict.
                    record={simple_header[n]: [data] for n, data in enumerate(line) if data}
                    body_request_template['record'] = record
                    body_request_template['recordId'] = record[file_def['primary_id']][0]
                    #And write that json dict to disk.
                    json.dump(body_request_template, file_handle_out)
                    file_handle_out.write('\n')
            defs[source]['file_modification_chain'].append(new_file_name)
    return defs


def create_json_file(cfg, defs, datafolder):
    #Send this function a csv file with no header and a header object,
    #and the function writes a json object to disk.
    #Actually, it writes a list of json dictionaries, not a true json obj.
    with open('new.csv', 'w'):
        print 'Preparing to convert raw file {0} to json'.format(filepath_in)
        #This template is what each line of the output looks like.
        body_request_template= { "action": "CREATE", "recordId": None, "record": {} }
        for num_line,line in enumerate(data):
            #For each line in the raw file, transform that line into a json dict.
            record={simple_header[n]: [data] for n, data in enumerate(line) if data}
            body_request_template['record'] = record
            body_request_template['recordId'] = record[file_def['primary_id']][0]
            #And write that json dict to disk.
            json.dump(body_request_template, file_handle_out)
            file_handle_out.write('\n')
    defs[source]['file_modification_chain'].append(new_file_name)
    return defs


