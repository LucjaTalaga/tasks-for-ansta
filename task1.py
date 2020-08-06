import csv

#getting all postal codes from csv file
def get_postal_codes():
    postal_codes = []
    with open("kody.csv" , "r") as codes:
        reader = csv.DictReader(codes, delimiter=';')
        for row in reader:
            if len(postal_codes) == 0 or row['KOD POCZTOWY'] != postal_codes[-1]:
                postal_codes.append(row['KOD POCZTOWY'])
    return postal_codes

# comparing two postal codes - returns information if the first is bigger, smaller or equal that second
def compare_two_codes(code, code_to_compare):
    result = None
    num_code = int(code.replace("-",""))
    num_code_to_compare = int(code_to_compare.replace("-",""))
    if num_code > num_code_to_compare:
        result = 'bigger'
    elif num_code < num_code_to_compare:
        result = 'smaller'
    else:
        result = 'equal'
    return result

# giving back all codes between two given values
def pc_between(min_pc, max_pc):
    all_pc = get_postal_codes()
    searched_pcs = []
    smaller = True
    for code in all_pc:
        if smaller:
            comparision = compare_two_codes(code, min_pc)
            if comparision == 'bigger' or comparision == 'equal':
                smaller = False             
        if not smaller:
            comparision = compare_two_codes(code, max_pc)
            if comparision == 'smaller' or comparision == 'equal':
                searched_pcs.append(code)
            else:
                return searched_pcs
    return searched_pcs

#running the last function with two given parameters
print(pc_between("79-900", "80-155"))