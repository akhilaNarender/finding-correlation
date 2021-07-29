import plotly.express as px
import csv
import numpy as np

with open("./data/Ice-cream vs Cold-Drink vs Temparature - Ice Cream.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cool_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Marks In Percentage"]))
            cool_drink_sales.append(float(row["Days Present"]))

    return {"x" : ice_cream_sales, "y": cool_drink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/XXXXXXXXXXXXXX.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
   # plotFigure(data_path)

setup()
