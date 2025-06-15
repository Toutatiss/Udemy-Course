# TASK: Make a new dataframe and csv with how many squirrels of each color.
DATA_PATH = "/Users/felka/Documents/Python/Udemy Course/Section 25 - Working with CSVs/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

import pandas

data = pandas.read_csv(DATA_PATH)

fur_colours_data = data["Primary Fur Color"]
fur_counts = fur_colours_data.value_counts()
print(fur_counts)

fur_counts.to_csv("Fur_Counts.csv")