import matplotlib.pyplot as plt

chart = []
chartCount = []

for i in range(2, 11):
    chart.append(2**i)
    chartCount.append(i)

print(chartCount, chart)

plt.plot(chartCount, chart)
plt.show()