import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2022, 2024, 2026, 2028])
y1 = np.array([10, 100, 40, 100, 10])
y2 = np.array([100, 10, 60, 10, 100])
y3 = np.array([60,50,50,50,60])

line_style = dict(marker = ".",
        markersize = 10,
        markerfacecolor = "#49ffeb",
        markeredgecolor = "red",
        linestyle = "dotted",
        linewidth = 2.5)
plt.title("Code Manoj",
         fontsize = 20,
         family = "Times New Roman",
         fontweight = "bold",
         color = "#b936c9")
plt.xlabel("Year",
         fontsize = 15,
         family = "Times New Roman",
         fontweight = "bold",
         color = "#49e9ff")
plt.ylabel("Students",
         fontsize = 15,
         family = "Times New Roman",
         fontweight = "bold",
         color = "#49e9ff")

plt.plot(x,y1,**line_style,
                color = "#7dff58")
plt.plot(x,y2,**line_style,
                color = "#f94949")
plt.plot(x,y3,**line_style,
                color = "#7b727c")
plt.tick_params(colors = "#3d7bf3",
               axis = "both")
plt.show()


