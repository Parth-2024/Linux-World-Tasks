import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib as jl
data=pd.read_csv("Competition/Machine Learning/Heart Attack Reponses - Form Responses 1.csv")
mind=LinearRegression()
y=data["Heart Attack Risk"]
x=data["Body Fat Percentage"]
x=x.values
x=x.reshape(5,1)
print(mind.fit(x,y))
query=int(input("Enter your Body Fat percentage:"))
print(mind.predict([[query]]))
jl.dump(mind,"Heart_Risk_Model")
#to use it somewhere else us model=jl.load("Heart_Risk_Model") code
