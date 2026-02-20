import pandas as pd

#Summary of quantitative variables
def quant_summ(df):
    print("Quantitative Summary:")
    for col in df.columns: 
        print("")
        print(f"Column: {col}")
        print("Max:",df[col].max())
        print("Min:",df[col].min())
        print("Mean:",df[col].mean().round(0))
        print("Median:",df[col].median())
        print("Q1:",df[col].quantile(0.25))
        print("Q3:",df[col].quantile(0.75))
        print("")

#Summary of frequency for ordinal, counts values 
def ordin_summ(df):
    print("Ordinal Summary:")
    for col in df.columns: 
        print("")
        print("Most frequent:", df[col].value_counts())

#Summary of frequency for categorical, counts values 
def categ_summ(df):
    print("Categorical Sumamry")
    for col in df.columns: 
        print("")
        print("Most frequent:", df[col].value_counts())

def main():
    df = pd.read_csv("P1_EDA/Park_Trails_Clean.csv")

    quant_cols = ['width_ft', 'date_collected']
    quant_df = df[quant_cols]
    quant_summ(quant_df)

    ordin_cols = ['class', 'difficulty']
    ordin_df = df[ordin_cols]
    ordin_summ(ordin_df)

    categ_cols = ['surface','park_name']
    categ_df = df[categ_cols]
    categ_summ(categ_df)

main()