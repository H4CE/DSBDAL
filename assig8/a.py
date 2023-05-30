import pandas as pd
import numpy as np

df=pd.read_csv("Social_Network_Ads.csv")

#replacing 1 for Male and 0 for Female
df["Gender"]=df["Gender"].replace(["Male","Female"],[1,0])

x=df[["Gender","Age","Salary"]]
y=df["Purchased"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.1, random_state=8)

from sklearn.linear_model import LogisticRegression
reg=LogisticRegression()
reg.fit(x_train,y_train)

y_pred=reg.predict(x_test)
print(y_pred)