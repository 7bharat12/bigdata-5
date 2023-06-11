# -*- coding: utf-8 -*-
"""
Created on Wed May 24 00:22:44 2023

@author: bharat
"""

import pandas as pd

# Read the dataset
dataset = pd.read_csv(r'C:\Users\bhara\Desktop\BharatChandra_AWSBigData5\videogamesales.csv')

# Replace "N/A" values with None (NULL)
dataset.replace('N/A', None, inplace=True)

# Display the cleaned dataset
print(dataset)

dataset.to_csv(r'C:\Users\bhara\Desktop\BharatChandra_AWSBigData5\output.csv', index=False)