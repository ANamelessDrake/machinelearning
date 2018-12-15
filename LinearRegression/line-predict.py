#!/usr/bin/python3

import sys, os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

debug = False

if debug:
    print("Number of CL arguments:", len(sys.argv))
    print("CL Arguments:", sys.argv)

if len(sys.argv) == 1:
    print("You must specify a CSV file\n")
    sys.exit(1)
elif len(sys.argv) >= 3:
    print("Only specify one CSV file\n")
    sys.exit(1)
elif len(sys.argv) == 2:
    csv_file = sys.argv[1]

    exists = os.path.isfile(csv_file)

    if debug:
        print("CSV File:",csv_file)
        print("File exists:", exists)

    if exists:
        df = pd.read_csv(csv_file)
    else:
        print("File does not exist:", csv_file)
        sys.exit(1)


y_values = df.iloc[:, 0].tolist()
x_values = np.array(df.iloc[:, 1].tolist())

if debug:
    print(df.head())
    print(y_values)
    print(x_values)

x_values = x_values.reshape(-1, 1)

line_fitter = LinearRegression()
line_fitter.fit(x_values, y_values)
line_predict = line_fitter.predict(x_values)

plt.plot(x_values, y_values, "o")
plt.plot(x_values, line_predict)
plt.show()
plt.savefig('output.png')
