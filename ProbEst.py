# -*- coding: utf-8 -*-

#mporting pandas library to read the csv file
import pandas as pd

#Reading the csv file and storing it in a pandas dataframe
cars_df = pd.read_csv("cars.csv")

#Creating lists for the unique values of make and aspiration to avoid repetition and increase efficiency.
make_list = cars_df['make'].unique().tolist()
aspiration_list = cars_df['aspiration'].unique().tolist()

#calculating the conditional probability for aspiration and make
for make_type in make_list:
    for aspiration_type in aspiration_list:
       match_count = len(cars_df[(cars_df['aspiration'] == aspiration_type) & (cars_df['make'] == make_type)])
       total_count = len(cars_df[cars_df['make'] == make_type])
       conditional_prob = match_count / total_count
       print(f"Prob(aspiration = {aspiration_type} | make = {make_type}) = {conditional_prob * 100:.2f}%")
print("")

#Calculating the probability of each make
for make_type in make_list: 
    probability_calc = len(cars_df[cars_df['make'] == make_type])/ len(cars_df)
    print(f"Prob(make = {make_type}) = {probability_calc * 100:.2f}%")
    
    