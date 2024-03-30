import pandas as pd
import numpy as np
import seaborn as sns  #high level
import matplotlib.pyplot as plt          #low level
import seaborn

#kategorik değişken: sütun grafik. countplot bar
# sayısal değişken: hist, boxplot

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')
plt.show()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()


x=np.array([1,8])
y=np.array([0,150])
plt.plot(x,y)


# Seaborn ile gorsellestirme (daha az caba)
df=sns.load_dataset("tips")
df.head()
df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df)
# df["sex"].value_counts().plot(kind='bar')
sns.boxplot(x=df["total_bill"])
plt.show()
