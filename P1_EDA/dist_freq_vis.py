import pandas as pd
import matplotlib.pyplot as plt

def quant_vis(df, col):

    #Boxplot
    #----------
    plt.figure()
    plt.boxplot(df.dropna())
    plt.title(f"Boxplot of {col}")
    plt.ylabel(col)
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

    #Histogram 
    #---------
    plt.figure()
    plt.hist(df.dropna(), bins=10, color='forestgreen')
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.ticklabel_format(style='plain', axis='x')
    plt.show()

def ordin_vis(df, col): 

    counts = df.value_counts()
    
    #Bar Chart
    #---------
    plt.figure()
    #Finds position, value, and sets color
    plt.bar(counts.index, counts.values, color='forestgreen')
    plt.title(f"Frequency of Development")
    plt.xlabel("Development Class")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()    

def categ_vis(df, col): 

    counts = df.value_counts()
    #Bar Chart
    #---------
    plt.figure()
    plt.bar(counts.index, counts.values, color='olive')
    plt.title(f"Bar Chart of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()


def main():
    df = pd.read_csv("P1_EDA/Park_Trails_Clean.csv")
    quant_cols = ['width_ft', 'date_collected']
    for col in quant_cols:
        quant_vis(df[col], col)

    ordin_cols = ['class', 'difficulty']
    for col in ordin_cols:
        ordin_vis(df[col], col)
    
    categ_cols = ['surface','park_name']
    for col in categ_cols: 
        categ_vis(df[col], col)

main()