
import csv

def read_csv(file_name):

    file = open(file_name,'r',encoding='latin-1')
    data = csv.DictReader(file)
    return data

def csv_reader  (file_name):

    file = open(file_name,'r',encoding='latin-1')
    data = csv.DictReader(file)
    result_dict = {}
    for row in data:
        pin = row['Pin Code']
        district = row['District']
        result_dict[pin] = district
    return result_dict