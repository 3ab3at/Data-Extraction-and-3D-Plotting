import pandas as pd
import sys,os
sys.path.append(os.path.realpath('..'))

# Read the three text files into separate DataFrames
df1 = pd.read_csv('data/radius_extracted.txt', header=None)
df2 = pd.read_csv('data/angle_extracted.txt', header=None)
df3 = pd.read_csv('data/DMF_extracted.txt', header=None)

# Merge the three DataFrames into a single DataFrame
merged_df = pd.concat([df1, df2, df3], axis=1)

# Write the merged DataFrame to a CSV file
merged_df.to_csv('csv/data.csv', index=False)