import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


data = pd.read_csv("amazon.csv", encoding = "iso-8859-1", parse_dates= ["date"])

shape = data.shape
print("Number of Rows:", shape[0])
print("Number of Columns:", shape[1])

dup_data = data.duplicated().any()
print("Are there any duplicated values in the data", dup_data)
data =data.drop_duplicates()
print(data.shape)

print(data.isnull().sum())

print(data.describe(include = "all", datetime_is_numeric=True))

data['month'].replace({"Janeiro":"Jan","Fevereiro": "Feb","Março": "March","Abril":"April","Maio":"May","Junho":"June","Julho":"July","Agosto":"Aug","Setembro":"Sep","Outubro":"Oct","Novembro":"Nov","Dezembro":"Dec"},inplace=True)

data1 = data.groupby("month")["number"].sum().reset_index()
sns.barplot(x="month", y="number", data=data1)
plt.show()

data2 = data.groupby("year")["number"].sum().reset_index()
sns.barplot(x="year", y="number", data=data2)
plt.show()

data3 = data.groupby("state")["number"].sum().reset_index()
sns.barplot(x="state", y="number", data=data3)
plt.xticks(rotation=75)
plt.show()

data4 = data.groupby("state")["number"].mean().sort_values(ascending=False).reset_index()
sns.barplot(x="state", y="number", data=data4)
plt.xticks(rotation=75)
plt.show()