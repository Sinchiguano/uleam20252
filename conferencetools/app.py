import matplotlib.pyplot as plt

# Example data
tools = ['ChatGPT', 'Grammarly', 'Copilot', 'Elicit', 'Khanmigo']
usage = [80, 65, 50, 30, 25]  # number of students using each tool

# Create bar chart
plt.bar(tools, usage)

# Add labels and title
plt.xlabel('AI Tools Used in Education')
plt.ylabel('Number of Students')
plt.title('AI Usage Among Students in 2025')

# Show the plot
plt.show()
