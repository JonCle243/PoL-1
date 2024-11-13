import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
data = pd.read_csv("mRNA.csv")

# Extract time and mRNA concentration data from the CSV file
t = data['time'].values  # time values
y = data['mRNA'].values  # mRNA concentration values

# Define the fitting function f(t) = a(1 - e^(-bt))
def fit_func(t, a, b):
    return a * (1 - np.exp(-b * t))

# Use curve_fit to determine the parameters a and b
popt, pcov = curve_fit(fit_func, t, y)

# Extract the optimal parameters a and b
a_opt, b_opt = popt
print("Optimal parameters a and b:", a_opt, b_opt)


# Plot the original data points
plt.scatter(t, y, label='Data', color='red')

# Generate fitted curve using the optimal parameters
t_fit = np.linspace(min(t), max(t), 100)  # create a range of time points for the fit
y_fit = fit_func(t_fit, a_opt, b_opt)  # generate the corresponding mRNA values

# Plot the fitted curve
plt.plot(t_fit, y_fit, label='Fitted Curve', color='blue')

# Add labels and legend
plt.xlabel('Time (t)')
plt.ylabel('mRNA Concentration')
plt.legend()
plt.show()