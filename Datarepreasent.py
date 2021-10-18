#Draw a scatterplot
import matplotlib.pyplot as plt
import random 
'''randomnumber=random.randint(1,10)
print(randomnumber)'''



x=[]
y=[]
for i in range(5):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))
plt.scatter(x, y,color='blue')
plt.show()
