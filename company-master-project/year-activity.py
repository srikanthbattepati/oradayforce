
import datetime
import matplotlib.pyplot as plt
import main

def principal_business_over_years():

    result_dict = {}
   
    maharashtra = main.read_csv('Maharashtra.csv')
    for company in maharashtra:
        try:
            year = datetime.datetime.strptime(company['DATE_OF_REGISTRATION'],"%d-%m-%y").year
            if int(year) >= 2022: 
                year = "19" + str(year)[2:]
            if  int(year) >= 2012:
                principal_activity = company['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']
                if year in result_dict and principal_activity != 'Unclassified':
                    if principal_activity in result_dict[year]:
                        result_dict[year][principal_activity] += 1
                    else:
                        result_dict[year][principal_activity] = 1
                else:
                    result_dict[year] = {principal_activity: 1}
        except ValueError:
            pass
    
    sorted_result_dict = {
        year : dict(sorted(principal_activity.items(),key=lambda x : x[1],reverse=True))
        for year,principal_activity in result_dict.items()
    }
    
    sorted_plot_dict = dict(
        sorted(sorted_result_dict.items(),key = lambda x : x [0])
    )

    top_five_activities = list(sorted_plot_dict[2012].keys())[:5]
    
    years = list(sorted_plot_dict.keys())
    width = 0.1  
    year_range = range(len(years))
    color_codes = [
        "#FF5733",  
        "#33FF57",  
        "#FFFF33", 
        "#FF33FF", 
        "#33FFFF", 
    ]
    for index , value in enumerate(top_five_activities):
        
        values = [data.get(value) for data in list(sorted_plot_dict.values())]
        plt.bar(
            [val + index * width for val in year_range],
            values,
            width=width,
            label = value,
            color = color_codes[index]
        )
    def plot():
        plt.xlabel('Year')
        plt.ylabel('Number of Activities')
        plt.title('Principal Business Activities')
        plt.xticks([val + width * (len(top_five_activities)) for val in year_range], years)
        plt.legend()
        plt.show()
    plot()

principal_business_over_years()