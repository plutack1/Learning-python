import pandas
# with open("weather_data .csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for column in list(data)[1:]:
#         temperatures.append(int(column[1]))
#     print(temperatures)
data = pandas.read_csv("weather_data .csv")
temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# avg_temp = data["temp"].mean()
# max_value = data["temp"].max()
# print(avg_temp, max_value)
print(data[data.temp == data.temp.max()])

