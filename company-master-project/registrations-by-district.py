"""numbe of registration in each  district"""
import datetime
import matplotlib.pyplot as plt
import main

def registrations_by_district():
    maharashtra = main.read_csv('Maharashtra.csv')
    pincode_dict = main.csv_reader('pincode.csv')
    result_dict = {}
    for company in maharashtra:
        try:
            year = datetime.datetime.strptime(company['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022:
                year = "19" + str(year)[2:]
        except ValueError:
            pass
        if year == 2015:
            code = company['Registered_Office_Address'].split(" ")[-1]
            if code in pincode_dict:
                district = pincode_dict[code]
                if district in result_dict:
                    result_dict[district] += 1
                else:
                    result_dict[district] = 1
    def plot():
        plt.bar(result_dict.keys(),result_dict.values())
        plt.show()
    plot()

registrations_by_district()