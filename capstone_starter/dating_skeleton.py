#!/usr/bin/python3

#Can we determine gender based on the words used in essay answers
#Can we determine income based off of words used in essay answers
#Can we determine education based off of words used in essay answers

import re, time, os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

def data_therapy(dataFrame):
    temp_holder = []
    dataFrame = dataFrame.replace(['<br />', '</b>', '\n', '[,.!"/():?_]'],' ', regex=True)
    for i in range(len(dataFrame)):
        temp_holder.append(re.sub(' +', ' ', dataFrame[i].strip().lower()))

    return temp_holder

debug = False
os.system('clear')

version = 1.0

start_time = int(time.time())
localtime = time.localtime(time.time())
localdatetime = time.asctime(time.localtime(time.time()))

data = pd.read_csv('profiles.csv') ## Create DataFrame

#print (data.columns.values.tolist())
#data.info(memory_usage='deep')

#plt.hist(data.age, bins=20)
#plt.xlabel("Age")
#plt.ylabel("Frequency")
#plt.xlim(16, 80)
#plt.show()

counter = CountVectorizer()

data_holder = []

essay_0 = data.essay0.replace(np.nan, '', regex=True)
essay_0 = data_therapy(essay_0)

essay_1 = data.essay1.replace(np.nan, '', regex=True)
essay_1 = data_therapy(essay_1)

essay_2 = data.essay2.replace(np.nan, '', regex=True)
essay_2 = data_therapy(essay_2)

essay_3 = data.essay3.replace(np.nan, '', regex=True)
essay_3 = data_therapy(essay_3)

essay_4 = data.essay4.replace(np.nan, '', regex=True)
essay_4 = data_therapy(essay_4)

essay_5 = data.essay5.replace(np.nan, '', regex=True)
essay_5 = data_therapy(essay_5)

essay_6 = data.essay6.replace(np.nan, '', regex=True)
essay_6 = data_therapy(essay_6)

essay_7 = data.essay7.replace(np.nan, '', regex=True)
essay_7 = data_therapy(essay_7)

essay_8 = data.essay8.replace(np.nan, '', regex=True)
essay_8 = data_therapy(essay_8)

essay_9 = data.essay9.replace(np.nan, '', regex=True)
essay_9 = data_therapy(essay_9)

educations = data.education.replace(np.nan, '', regex=True)
educations = educations.sort_values().unique()

counter = 0
education_map = {}

for education in educations:
    education_map[education] = counter
    counter += 1

data["education_code"] = data.education.map(education_map)

genders = data.sex.replace(np.nan, '', regex=True)
genders = genders.sort_values().unique()

counter = 0
gender_map = {}

for gender in genders:
    gender_map[gender] = counter
    counter += 1

data["gender_code"] = data.sex.map(gender_map)


print(essay_1[96])




end_time = int(time.time())

actual_time = end_time - start_time
total_time = end_time - start_time

if total_time >= 60:
    total_time = float(total_time)
    total_time = total_time / 60
    if total_time >= 60:
        total_time = total_time / 60
        total_time = "%0.2f" % (total_time)
        total_time = total_time+" Hours"
    else:
        total_time = "%0.2f" % (total_time)
        total_time = total_time+" Minutes"

else:
    total_time = str(total_time)
    total_time = total_time+"  Seconds"

actual_time = str(actual_time)
print ("INFO: Script Execution Time :",actual_time+"  Seconds")
print ("INFO: Human Readable Format :",total_time)
