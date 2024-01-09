# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:35:02 2024

@author: sam jacob
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde 
data = pd.read_csv("C://Users//sam jacob//OneDrive//Desktop//fundamental of data science//data1-1.csv", names=['Salary'])
print(data)

# Assuming the relevant data is in the first column
salaries = data.iloc[:, 0]

# Create a Gaussian Kernel Density Estimate
kde = gaussian_kde(salaries)

# Create a range of values to evaluate KDE
salary_range = np.linspace(salaries.min(), salaries.max(), 500)

# Evaluate KDE for these values
density = kde(salary_range)

# Plot the histogram and KDE
plt.figure(figsize=(10, 6))
plt.hist(salaries, bins=30, density=True, alpha=0.5, label='Histogram of Salaries')
plt.plot(salary_range, density, label='Probability Density Function')

# Calculate the mean annual salary (W_tilde)
W_tilde = np.mean(salaries)

# Placeholder for the calculation of X
# Assuming X is some statistical measure that can be calculated from the distribution
# For example, let's calculate the median as an example for X
X = np.median(salaries)

# Add the mean and X value to the plot
plt.axvline(W_tilde, color='r', linestyle='--', label=f'Mean Salary (W_tilde): ${W_tilde:.2f}')
plt.axvline(X, color='g', linestyle='-', label=f'X (Median Salary): ${X:.2f}')

# Add labels and title
plt.xlabel('Annual Salary ($)')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Annual Salaries')
plt.legend()

# Show the plot
plt.show()