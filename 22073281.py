# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:24:15 2024

@author: sam jacob
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis


data = pd.read_csv("data1.csv", names=['Salary'])

# Plot the histogram
plt.hist(data['Salary'], bins=30, density=True, label='PDF',alpha=0.7, color='#1f77b4', edgecolor='black')

# Fit a normal distribution to the data
mu, std = norm.fit(data['Salary'])
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
 

# Plot the PDF as a black line
plt.plot(x, p, 'k', linewidth=2, label='Normal distribution fit')

# Calculate and print the mean annual salary (W)
mean_salary = np.mean(data['Salary'])
plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Mean Salary ($W$): {mean_salary:.2f}')

# Calculate the value 'X', which is the 67th percentile of the salary data, and plot a vertical line at this value.
X = np.percentile(data['Salary'], 67)  # 100% - 33% = 67%
plt.axvline(X, color='purple', linestyle='dashed', linewidth=2, label=f'X: {X:.2f}')

# Add labels, title, and legend
plt.xlabel('Annual Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Distribution of Annual Salaries')
#set x-axis and y-axis limit start from 0
plt.xlim(0,xmax)
plt.ylim(0,plt.ylim()[1])

plt.legend()

# Show the plot
plt.show()

# Calculate skewness and kurtosis
salary_skewness = skew(data['Salary'])
salary_kurtosis = kurtosis(data['Salary'])

# Print skewness and kurtosis
print(f"Skewness of the salary distribution: {salary_skewness}")
print(f"Kurtosis of the salary distribution: {salary_kurtosis}")