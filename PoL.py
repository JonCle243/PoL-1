import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
alpha = 2  # Production rate (adjustable)
tau = 5    # Lifetime of mRNA (adjustable)

# Define the differential equation dy/dt = α - y/τ
def dydt(t, y):
    return alpha - y / tau

# Time range for the solution (from t=0 to t=20)
t_span = (0, 20)
# Time points where we want the solution evaluated
t_eval = np.linspace(0, 20, 200)

# Initial condition 1: y(0) = 0
y0_1 = 0
sol1 = solve_ivp(dydt, t_span, [y0_1], t_eval=t_eval)

# Initial condition 2: y(0) = 2 * α * τ
y0_2 = 2 * alpha * tau
sol2 = solve_ivp(dydt, t_span, [y0_2], t_eval=t_eval)

# Steady-state value
steady_state = alpha * tau

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the first solution (y(0) = 0)
plt.plot(sol1.t, sol1.y[0], label=r"$y(0) = 0$", color='blue')

# Plot the second solution (y(0) = 2ατ)
plt.plot(sol2.t, sol2.y[0], label=r"$y(0) = 2\alpha\tau$", color='green')

# Plot the steady-state line
plt.axhline(y=steady_state, color='red', linestyle='--', label=r"Steady-state $y = \alpha \tau$")

# Labels and title
plt.xlabel("Time (t)")
plt.ylabel("Number of mRNA molecules (y)")
plt.title("mRNA Production and Degradation")
plt.legend()
plt.grid()
plt.show()