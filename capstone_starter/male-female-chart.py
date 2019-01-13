#!/usr/bin/python3

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing

data = pd.read_csv('profiles.csv') ## Create DataFrame
min_max_scaler = preprocessing.MinMaxScaler()

counter = 0
gender_map = {}

genders = data.sex.replace(np.nan, '', regex=True)
genders = genders.sort_values().unique()

for gender in genders:
    gender_map[gender] = counter
    counter += 1

data["gender_code"] = data.sex.map(gender_map)
mapping = {'m' : 'blue', 'f' : 'pink'}

#plt.scatter(data.age, data.age, alpha=0.2, c=data['sex'].map(mapping))
plt.hist(data.age, bins=20)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(16, 80)

plt.show()
