import pandas as pd

df = pd.read_csv("P1_EDA/Park_Trails_Clean.csv")
#Drop duplicate lines
df = df.drop_duplicates()
#Change columns to lower case
df.columns = df.columns.str.lower()

#Clean quantatative variables to approximates. 
#------------
#Clean widths
width_map = {
    "less than 2 feet": 1,
    "2 feet to less than 4 feet": 3,
    "4 feet to less than 6 feet": 5,
    "6 feet to less than 8 feet": 7,
    "Over 8 feet": 9
}
#Create a map that changes text to numeric from width_map
df['width_ft'] = df['width_ft'].map(width_map)

#Clean dates to just year. (For purposes of this high-level exploration)
df['date_collected'] = pd.to_datetime(df["date_collected"], errors='coerce').dt.year


#Clean ordinal variables for x-labels. (Did not end up using in Phase: 1)
#----------------
#Clean difficulty
difficulty_map = {
    "4: strenuous climbs of moderate duration, short but steep climbs": "v",
    "3: moderate elevation change, welll-graded trail, flat trail with rough treadway": "3: Moderate and rough",
    "2: flat terrain, uneven treadway, slight elevation change": "2: Slightly uneven",
    "1: flat and smooth": "1: Flat and smooth"
}

df['difficulty'] = df['difficulty'].map(difficulty_map)

#Make new clean csv 
df.to_csv("Park_Trails_Clean.csv", index = False)

