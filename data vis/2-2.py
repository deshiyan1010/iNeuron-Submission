import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url,usecols=['sex','fare','age'])

pop = titanic.sex.value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(pop,autopct='%1.1f%%',labels=["Male","Female"])
ax1.axis('equal')  
plt.show()

colour = np.where(titanic.sex=='male','r',np.where(titanic.sex=='female','b','g'))

plt.scatter(titanic['age'],titanic['fare'],color=colour,label=['male','female'])
plt.xlabel('Age')
plt.ylabel('Fare')

red_patch = mpatches.Patch(color='red', label='Male')
blue_patch = mpatches.Patch(color='blue', label='Female')

plt.legend(handles=[red_patch, blue_patch])
plt.show()
