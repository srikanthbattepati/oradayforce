
import datetime
import matplotlib.pyplot as plt
import main

def number_of_registrations_per_year():
    result_dict = {}
    maharashtra = main.read_csv('Maharashtra.csv')
    for company in maharashtra:
        try:
            year = datetime.datetime.strptime(company['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022: # Dataset is last updated in 2021
                year = "19" + str(year)[2:]
            if year in result_dict:
                result_dict[str(year)] += 1
            else:
                result_dict[str(year)] = 1
        except ValueError:
            pass
        
    #     try:
    #         year = int(datetime.datetime.strptime(company['DATE_OF_REGISTRATION'],"%d-%m-%y").year)
    #         # print(year)
            
    
    #     except ValueError:
    #         continue
    #     if(year>2022):
    #         str_year=str(year)
    #         year=int('19'+(str_year[2:]))

    #     if year in result_dict:
    #         result_dict[str(year)] += 1
    #     else:
    #         result_dict[str(year)] = 1
    # print(result_dict)
        
    # sorted_dict = dict(sorted(result_dict.items(),key=lambda x : x[0]))
    def plot():
        year = result_dict.keys() 
        registrations= result_dict.values()
        plt.bar(year,registrations)
        plt.xlabel("Year")
        plt.ylabel("Number of registrations")
        plt.title("Number of registrations per year")
        plt.xticks(rotation=90)
        plt.show()
    plot()

number_of_registrations_per_year()