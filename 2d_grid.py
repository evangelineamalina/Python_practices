import matplotlib.pyplot as plt

# Define the table data
table = [
    {"x-coordinate": 0, "Character": "█", "y-coordinate": 0},
    {"x-coordinate": 0, "Character": "█", "y-coordinate": 1},
    {"x-coordinate": 0, "Character": "█", "y-coordinate": 2},
    {"x-coordinate": 1, "Character": "▀", "y-coordinate": 1},
    {"x-coordinate": 1, "Character": "▀", "y-coordinate": 2},
    {"x-coordinate": 2, "Character": "▀", "y-coordinate": 1},
    {"x-coordinate": 2, "Character": "▀", "y-coordinate": 2},
    {"x-coordinate": 3, "Character": "▀", "y-coordinate": 2}
]

# Extract x and y coordinates
x_coords = [row['x-coordinate'] for row in table]
y_coords = [row['y-coordinate'] for row in table]
chars = [row['Character'] for row in table]

# Create a plot
plt.scatter(x_coords, y_coords)

# Place characters at their respective coordinates
for (x, y), char in zip(zip(x_coords, y_coords), chars):
    plt.text(x, y, char, ha='center', va='center')

# Display the plot
plt.show()
