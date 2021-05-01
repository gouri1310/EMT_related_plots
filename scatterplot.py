import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
fname=("C:/Users/rajaram/Desktop/CSBDump/EMT Scores.xlsx")
t=pd.read_excel(fname,engine="openpyxl")
gs=t["76_GS"].tolist()
ks=t["KS"].tolist()
x=np.array(gs)
y=np.array(ks)
m,b=np.polyfit(x,y,1)
plt.plot(x,m*x+b)
a=stats.pearsonr(x,y)
r=round(a[0],3)
p_value=round(a[1],3)
con="Pearson's correlation coefficient ="+str(r)+" "+"P-value="+str(p_value)
plt.scatter(gs,ks,c="black",alpha=1.0)
plt.xlabel("EMT Score by 76_GS Method")
plt.ylabel("EMT Score by KS Method")
plt.title(con)
plt.savefig("Scatterplot_KSvs76GS.png")
quit()
