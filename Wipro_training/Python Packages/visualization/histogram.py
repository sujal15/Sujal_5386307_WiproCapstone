# Sample data
import numpy as np
from matplotlib import pyplot as plt


data = np.random.randn(100)

# Create a figure with a histogram and a density plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Histogram
ax1.hist(data, bins=10, color='skyblue', edgecolor='black')
ax1.set_title('Histogram')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')

# Density plot

#the bar-graph to appear on second
# ax2.hist(data, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.6)

data_density = np.linspace(min(data), max(data), 100)
ax2.plot(data_density, (1/(np.sqrt(2 * np.pi))) * np.exp(-0.5 * (data_density)**2), color='red')
ax2.set_title('Density Plot')
ax2.set_xlabel('Value')
ax2.set_ylabel('Density')

# Show the plots
plt.tight_layout()
plt.show()