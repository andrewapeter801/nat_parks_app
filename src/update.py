import pandas as pd
from pathlib import Path
from base import Base
from to_mongo import ToMongo

# Folder directory
folder_dir = f'{Path(__file__).parents[0]}\\data'

# Create a csv file from the dataframe that we created in the base class.
Base().df.to_csv(f'{folder_dir}\\nat_parks.csv', index= False)
print('Saved New NP Images to CSV file')

# Read in the dataframe from the csv:
df = pd.read_csv(f'{folder_dir}\\nat_parks.csv', low_memory=False)
print('Created the DataFrame object')

