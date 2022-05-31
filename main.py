import matplotlib.pyplot as plt
fig,axes = plt.subplots(nrows=2,ncols=2)
x = [i for i in range  (0,11)]
y=x
y1=[i**2 for i in x]
y2=[i**3 for i in x]
y3=[i**4 for i in x]
axes[0,0].plot(x,y ,label = 'y=x')
axes[0,1].plot(x,y1, label ='y1=x^2')
axes[1,0].plot(x,y2 ,label ='y2=x^3')
axes[1,1].plot(x,y3 ,label ='y3=x^4')
plt.legend()
plt.show()
