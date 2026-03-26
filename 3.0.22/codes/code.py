import numpy as np
import matplotlib.pyplot as plt

samples = 200000
values = np.zeros(samples)

# Simulation
for s in range(samples):
    X = np.random.normal(0, 1, 5)
    Xbar = np.mean(X)
    T = np.sum((X - Xbar)**2)
    values[s] = (T**2) * (Xbar**2)

estimated_value = np.mean(values)
theoretical_value = 24 / 5

print("Estimated =", estimated_value)
print("Theoretical =", theoretical_value)

plt.figure()

# Histogram
plt.hist(values, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# 🔥 Slight shift for visibility
offset = 0.1

# Theoretical line (red)
plt.axvline(theoretical_value, color='red', linestyle='--', linewidth=3,
            label=f'Theoretical = {theoretical_value:.2f}')

# Estimated line (blue, slightly shifted)
plt.axvline(estimated_value + offset, color='blue', linestyle='-', linewidth=2,
            label=f'Estimated ≈ {estimated_value:.2f}')

# 🔥 Add text labels near lines
plt.text(theoretical_value, 150000, "4.8", color='red', ha='center')
plt.text(estimated_value + offset, 140000, f"{estimated_value:.2f}", color='blue', ha='center')

# Better scaling
plt.xlim(0, 45)
plt.ylim(0, None)

plt.title("Distribution of T^2 * Xbar^2")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.legend()
plt.grid()

plt.show()
