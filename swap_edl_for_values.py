#convert edl_is_deleted to value

def the_conversion(file_name):
    with open(file_name) as txtfile:
        content = txtfile.readlines()
        for line_num, line in enumerate(content):
            if line_num < 6:
                print line


the_conversion("dig_prods_json.txt")
            
