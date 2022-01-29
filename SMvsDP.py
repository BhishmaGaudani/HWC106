from turtle import color
import plotly.express as px
import csv 
import numpy as np

def plotfigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
        fig.show()
def getDataSource(data_path):
    MarksInPercentage=[]
    DaysPresent=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))

    return {"x":DaysPresent,"y":MarksInPercentage}

def FindCorelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("corelation between Days Present and Marks In Percentage: \n",correlation[0,1])

def Setup():
    data_path="SMvsDP.csv"
    data_source=getDataSource(data_path)
    FindCorelation(data_source)
    plotfigure(data_path)

Setup()