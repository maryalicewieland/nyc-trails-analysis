import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
surface_colors = {
    'Dirt': 'brown',
    'Paved': 'grey',
    'Gravel': 'black',
    'Wood Chips': 'peru',
    'Sand': 'yellow',
    'Boardwalk': 'teal',
    'Concrete': 'blue',
    'Grasses': 'green'
}

def compare_time(df):
    #Trail Width by Year
    #------------------
    plt.figure(figsize=(8,5))
    sns.lineplot(
        data=df,
        x='date_collected',
        y='width_ft',
        color='forestgreen'   # <- add this
    )
    plt.title("Average Width of Trails Over Time")
    plt.xlabel("Year")
    plt.ylabel("Width")
    #plt.show()
    
    #Surfaces by Year
    #-----------------
    # Count surface observations per year
    surf_counts = df.groupby(['date_collected', 'surface']).size().reset_index(name='count')
    # Normalize within each year
    surf_counts['proportion'] = surf_counts.groupby('date_collected')['count'].transform(lambda x: x / x.sum())
    # Filter only Dirt and Paved
    filtered = surf_counts[surf_counts['surface'].isin(['Dirt', 'Paved'])]

    plt.figure(figsize=(8,5))

    surface_colors = {
        'Dirt': 'sienna',
        'Paved': 'slategray'
    }

    for surface in ['Dirt', 'Paved']:
        subset = filtered[filtered['surface'] == surface]
        plt.plot(
            subset['date_collected'],
            subset['proportion'],
            label=surface,
            color=surface_colors[surface],
            linewidth=5
        )
    plt.title("Proportion of Dirt vs Paved Trails Over Time")
    plt.xlabel("Year")
    plt.ylabel("Proportion")
    plt.legend()
    plt.show()
        
    #Development by Year (Line Graph)
    #-------------------
    plt.figure(figsize=(8,5))

    class_order = [
        "Class I : Minimal/Undeveloped",
        "Class II : Simple/Minor Developed",
        "Class III : Developed/Improved",
        "Class IV : Highly Developed",
        "Class V : Fully Developed"
    ]

    # Group by year and class
    dev_counts = df.groupby(['date_collected', 'class']).size().reset_index(name='count')

    # Normalize within each year
    dev_counts['proportion'] = dev_counts.groupby('date_collected')['count'].transform(lambda x: x / x.sum())

    # Keep only ordered classes
    dev_counts = dev_counts[dev_counts['class'].isin(class_order)]

    palette = sns.color_palette("Greens", n_colors=len(class_order))

    for i, cls in enumerate(class_order):
        subset = dev_counts[dev_counts['class'] == cls]
        plt.plot(
            subset['date_collected'],
            subset['proportion'],
            label=cls,
            color=palette[i],
            linewidth=2
        )

    plt.title("Development Class Distribution Over Time")
    plt.xlabel("Year")
    plt.ylabel("Proportion of Trails")
    plt.legend()
    plt.show()

    #Development by Year (Stacked Bars)
    #-------------------
    dev_counts['date_collected'] = dev_counts['date_collected'].astype(int)
    pivot = dev_counts.pivot(index='date_collected', columns='class', values='proportion')

    pivot.plot(kind='bar', stacked=True, colormap="Greens", figsize=(8,5))

    plt.title("Development Class Composition by Year")
    plt.ylabel("Proportion of Trails")
    plt.xlabel("Year")
    plt.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, -0.15),
        ncol=3
    )
    plt.tight_layout()
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
    df = pd.read_csv("P1_EDA/Park_Trails_Clean.csv")
    #compare_bar(df)
    #compare_box(df)
    compare_time(df)

main()
