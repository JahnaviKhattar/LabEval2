import requests
import pymongo

import pandas as pd
data = pd.read_csv("Medical_Equipment_Suppliers.csv")
print(data.head())

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['medical_db']
collection = db['suppliers']

collection.insert_many(data)
print("Data inserted successfully!")

providers_in_ca = data[data['practicestate'] == 'CA']
print(providers_in_ca[['provider_id','practicename', 'practicestate']])

providers_in_ny = data[(data['practicestate'] == 'NY') & (data['specialitieslist'] == 'Medical Supply Company Other') & (data['supplies_list'].str.contains('OXYGEN & EQUIPMENT'))]

print(providers_in_ny[['provider_id', 'practicestate', 'specialitieslist', 'providertypelist']])

data.loc[data['provider_id'] == 20506619, 'telephonenumber'] = '123123123'

print(data[data['provider_id'] == 20506619][['provider_ID', 'telephonenumber']])

supplies_in_tx = data[data['practicestate'] == 'TX']['supplieslist']
