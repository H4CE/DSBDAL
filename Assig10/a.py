import seaborn as sns
import matplotlib.pyplot as plt

# Create some example data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 8, 9]

# Create the histplot
sns.histplot(data)

# Adjust the x-axis ticks
plt.xticks(range(min(data), max(data)+1))

# Show the plot
plt.show()
