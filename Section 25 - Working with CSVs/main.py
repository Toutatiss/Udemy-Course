DATA_PATH = "/Users/felka/Documents/Python/Udemy Course/Section 25 - Working with CSVs/weather_data.csv"


## Classic Option
# with open(DATA_PATH, "r") as weather_data_file:
#     data = weather_data_file.readlines()
# print(data)

## Using CSV library
# import csv

# with open(DATA_PATH, "r") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row)
        
# print(temperatures)

## Using Pandas

import pandas

data = pandas.read_csv(DATA_PATH)
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)

# Using pandas:
## Get the mean temperature
# print(data["temp"].mean())

## Get the max temperature
# print(data.temp.max())

## Get data in Monday row
# print(data[data.day == "Monday"])

# Get row for the day when the temperature was max
print(data[data.temp == data.temp.max()])

# Working with just monday
monday = data[data.day == "Monday"]
print(monday.condition)

# Get Monday's temperature in farenheit
monday_temp_c = monday.temp[0]
monday_temp_f = (monday_temp_c * 9/5) + 32
print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "Jack", "Angela"],
    "scores": [70, 80, 90]
}

data = pandas.DataFrame(data_dict)
print(data_dict)
data.to_csv("example_file.csv")