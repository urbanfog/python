import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = df.groupby("Primary Fur Color").size()

fur_color.to_csv("./squirrel_color.csv")
# create csv
