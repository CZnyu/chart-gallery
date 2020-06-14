import matplotlib.pyplot as plt
import numpy as np
# three_charts.py
# CHART 1 (PIE)
pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]
print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data
# CHART 2 (LINE)
line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]
print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data
# CHART 3 (HORIZONTAL BAR)
bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]
print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data
# Generate a Pie Chart for data
labels = [x["company"] for x in pie_data]
values = [y["market_share"] for y in pie_data]
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, autopct='%1.0f%%', startangle=90)
ax1.axis('equal')
plt.show()
# Generate Line Plot for data
x = [a["date"] for a in line_data]
y = [b["stock_price_usd"] for b in line_data]
fig, ax = plt.subplots()
ax.plot(x, y) 
ax.set(xlabel="Date", ylabel = "Stock Price (USD)", title = "Stocke Price vs. Date")
ax.grid()
plt.show()
# Generate Bar Chart for data
genre = [x["genre"] for x in bar_data]
y_pos = np.arange(len(genre))
views = [y["viewers"] for y in bar_data]
plt.barh(y_pos, views, align='center')
plt.yticks(y_pos, genre)
plt.xlabel('Views')
plt.title('Views by Genre')
plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
plt.show()