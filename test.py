import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Step 1: Load Excel data into a DataFrame
file_path = 'tuisong.xlsx'
df = pd.read_excel(file_path)

# Step 2: Count the number of pushes per squadron
squadron_counts = df['推送支队'].value_counts()

# Step 3: Set font properties for matplotlib
rcParams['font.family'] = 'SimHei'  # 设置全局字体为黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# Step 4: Create Pie Chart
plt.figure(figsize=(12, 10))  # 调整图表大小以适应所有标签
plt.title('推送支队占比')

# Plot the pie chart with all squadrons
wedges, texts, autotexts = plt.pie(squadron_counts, labels=squadron_counts.index,
                                   autopct='%1.1f%%', startangle=140,
                                   pctdistance=0.85, labeldistance=1.1)  # 调整标签和百分比的位置

# Customize the texts and autotexts
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(8)

plt.axis('equal')  # 确保饼状图为圆形

# Draw circle for better visual
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

# Display the plot
plt.show()