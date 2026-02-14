import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compare_time(df):
    #Trail Width by Year
    #------------------
    plt.figure()
    sns.lineplot(data=df, x='date_collected',y = 'width_ft')
    plt.xticks()
    plt.title("Year and Width of Trails")
    plt.xlabel("Year")
    plt.ylabel("Width")
    plt.show()



def compare_bar(df):
    #Trail Surface by Difficulty (Bar)
    #---------------------------- 
    order = ["1: Flat and smooth",
            "2: Slightly uneven", 
            "3: Moderate and rough", 
            "4: Strenuous climbs"]
    plt.figure()
    sns.countplot(data=df, x='difficulty', hue='surface',order=order)
    plt.xticks()
    plt.title("Surface and Difficulty")
    plt.xlabel("Difficulty")
    plt.ylabel("Count")
    plt.yscale('log')
    plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter())
    plt.gca().yaxis.set_minor_formatter(ticker.NullFormatter())
    plt.show()

def compare_box(df): 
    #Trail Width by Difficulty (Box Plot)
    #----------------------------
    order = ["1: Flat and smooth",
             "2: Slightly uneven", 
             "3: Moderate and rough", 
             "4: Strenuous climbs"]

    sns.boxplot(x='difficulty', y='width_ft', data=df, order=order)
    plt.title("Trail Width by Difficulty")
    plt.xlabel("Difficulty")
    plt.ylabel("Width (ft)")
    plt.show()

    #Trail Width by Development (Box Plot)
    #----------------------------
    order = ["Class I : Minimal/Undeveloped",
             "Class II : Simple/Minor Developed", 
             "Class III : Developed/Improved", 
             "Class V : Fully Developed",
             "Class IV : Highly Developed"]

    sns.boxplot(x='class', y='width_ft', data=df, order=order)
    plt.title("Trail Development by Width")
    plt.xlabel("Development")
    plt.ylabel("Width (ft)")
    plt.show()

def main():
    df = pd.read_csv("Park_Trails_Clean.csv")
    #compare_bar(df)
    #compare_box(df)
    compare_time(df)

main()
