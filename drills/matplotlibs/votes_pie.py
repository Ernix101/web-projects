import matplotlib.pyplot as plt
import numpy as np

# This is gonna show how many people voted for their favorite leader in the 2027. (Ruto, Gachagua, Matiang'i, Maraga)

candidates = np.array(["Ruto", "Gachagua", "Matiang'i", "Maraga"])
votes_casted = np.array([3000000, 4000000, 6000000, 5000000])

colors = ["Yellow", "Red", "Blue", "Brown"]


plt.pie(votes_casted, labels=candidates,
                                  autopct='%1.1f%%',
                                  colors=colors,
                                  shadow=True,
                                  explode=[0.1,0,0,0],
                                  startangle=90)

plt.title("Votes in Presidential election (2027)", fontsize="15",
                                                   family="Sans Serif")

plt.show()

