
import matplotlib.pylab as plt
import main

def authorized_capital():
    lables = ["<= 1L",  "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", "> 10Cr"]
    auth_cap = {
        "<= 1L" : 0,
        "1L to 10L" : 0,
        "10L to 1Cr" : 0,
        "1Cr to 10Cr":  0 ,
        "> 10 cr" : 0   
    }
    maharashtra = main.read_csv('Maharashtra.csv')
    for company in maharashtra:
        current_cap = float(company['AUTHORIZED_CAP'])
        if current_cap <= 100000:
            auth_cap["<= 1L"] += 1
        elif current_cap <= 1000000:
            auth_cap["1L to 10L"] += 1
        elif current_cap <= 10000000:
            auth_cap["10L to 1Cr"] += 1
        elif current_cap <= 100000000:
            auth_cap["1Cr to 10Cr"] += 1
        else:
            auth_cap["> 10 cr"] += 1
    def plot():
        weight = list(auth_cap.values())
        plt.hist(lables,bins=5,weights=weight)
        plt.xlabel("Capital range")
        plt.ylabel("Number of companies ")
        plt.title("Authorised Capital ")
        plt.show()
    plot()

authorized_capital()