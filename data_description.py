import numpy as np
import pandas as pd

#LOAD DATA
df = pd.read_csv('WalmartSalesData.csv', na_values='?')

#DATASET OVERVIEW
df.head() #previewing a sample
# Invoice ID Branch       City  ... gross margin percentage gross income Rating
#0  750-67-8428      A     Yangon  ...                4.761905      26.1415    9.1
#1  226-31-3081      C  Naypyitaw  ...                4.761905       3.8200    9.6
#2  631-41-3108      A     Yangon  ...                4.761905      16.2155    7.4
#3  123-19-1176      A     Yangon  ...                4.761905      23.2880    8.4
#4  373-73-7910      A     Yangon  ...                4.761905      30.2085    5.3

#[5 rows x 17 columns]

df.shape #number of observations
#(1000, 17)

df.dtypes #data types
#Invoice ID                  object
#Branch                      object
#City                        object
#Customer type               object
#Gender                      object
#Product line                object
#Unit price                 float64
#Quantity                     int64
#Tax 5%                     float64
#Total                      float64
#Date                        object
#Time                        object
#Payment                     object
#cogs                       float64
#gross margin percentage    float64
#gross income               float64
#Rating                     float64
#dtype: object

df[df.duplicated()] #check duplicated rows
#Empty DataFrame
#Columns: [Invoice ID, Branch, City, Customer type, Gender, Product line, Unit price, Quantity, Tax 5%, Total, Date, Time, Payment, cogs, gross margin percentage, gross income, Rating]
#Index: []

df.isna().sum() #missing values per features
#Invoice ID                 0
#Branch                     0
#City                       0
#Customer type              0
#Gender                     0
#Product line               0
#Unit price                 0
#Quantity                   0
#Tax 5%                     0
#Total                      0
#Date                       0
#Time                       0
#Payment                    0
#cogs                       0
#gross margin percentage    0
#gross income               0
#Rating                     0
#dtype: int64

df.isna().sum().sum() #number of missing cells
#0

round(df.isna().sum().sum())/df.size*100,1) #percentage of missing cells
#0
