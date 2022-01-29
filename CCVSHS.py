from turtle import color
import plotly.express as px
import csv 
import numpy as np

def plotfigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()
def getDataSource(data_path):
    sleep_in_hours=[]
    Coffee_in_ml=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sleep_in_hours.append(float(row["sleep in hours"]))
            Coffee_in_ml.append(float(row["Coffee in ml"]))

    return {"x":Coffee_in_ml,"y":sleep_in_hours}

def FindCorelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("corelation between Coffee in ml and sleep in hours: \n",correlation[0,1])

def Setup():
    data_path="CCvsHS.csv"
    data_source=getDataSource(data_path)
    FindCorelation(data_source)
    plotfigure(data_path)

Setup()