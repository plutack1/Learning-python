import pandas as pd
full_table = pd.read_csv(
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = full_table["Primary Fur Color"]
gray = full_table[fur_colors == "Gray"]
gray_count = len(gray.index)

Cinnamon = full_table[fur_colors == "Cinnamon"]
Cinnamon_count = len(Cinnamon.index)

Black = full_table[fur_colors == "Black"]
Black_count = len(Black.index)

new_table_dict = {
    "fur color":["Gray", "Black", "Cinnamon"],
    "count":[gray_count, Black_count, Cinnamon_count]
}
new_table = pd.DataFrame(new_table_dict)
new_table.to_csv("new_table.csv")

