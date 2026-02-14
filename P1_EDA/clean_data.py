import pandas as pd

df = pd.read_csv("Parks_Trails_20260213.csv")
df = df.drop_duplicates()
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

df['width_ft'] = df['width_ft'].map(width_map)

#Clean dates 
df['date_collected'] = pd.to_datetime(df["date_collected"], errors='coerce').dt.year


#Clean ordinal variables for x-labels. 
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

