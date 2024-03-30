import pandas as pd
import numpy as np
import seaborn as sns
pd.set_option('display.max_columns',None) #bütün sütunları göster
df=sns.load_dataset("titanic")
df.head()
df.shape
df.info()
df.columns
df.describe()
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()

## SEÇİM İŞLEMLERİ
df.index
df[0:13]
df.drop(0,axis=0).head()

df["age"].head()
df.age.head()

#df.index= df["age"]
#df["age"]=df.index

"age" in df
df["age"].head()
type(df["age"].head())  #dataframe değil pandas serisine dönüştü
df[["age"]].head()   ## dataframe
type(df[["age"]].head())

# loc -> label based selection  iloc-> integer based selection
df.loc[:, df.columns.str.contains("a")].head()   ## df.loc[:, ~df.columns.str.contains("a")].head() değildirrrr
df.iloc[0:3]   # e kadar seçer yani 3 dahil değil
df.iloc[0,0]

df.loc[0:3]   ## mutlak seçim. girilen aralığın hepsini gözterir

df.iloc[0:3,0:3]  #index girmek lazım
df.loc[0:3, "age"]  #label girilebilir

## Koşullu seçim
df[df["age"]>50].head()
df[df["age"]>50]["age"].count()

#yasi 50den büyük olanların sınıfını göster
df[df["age"]>50]["class"].count()
df.loc[df["age"]>50,["age","class"]].head()
#yasi 50den büyük olan erkekler  iki koşullu durumlarda koşullar () içine yazılır
df.loc[(df["age"]>50) & (df["sex"]== "male"),["age","class"]].head()
df.loc[(df["age"] > 50) & (df["sex"] == "male")
             & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
             ["age", "sex", "embark_town"]]


## aggregation & grouping
df["age"].mean()
df.groupby("sex")["age"].mean()
df.groupby("sex").agg({"age" : "mean"})
df.groupby("sex").agg({"age" : ["mean","sum"]})
df.groupby("sex").agg({"age" : ["mean","sum"],
                       "embark_town": "count"})

df.groupby("sex").agg({"age" : ["mean","sum"],
                       "survived": "mean"})

df.groupby(["sex","embark_town","class"]).agg({"age" : ["mean","sum"],
                       "survived": "mean"})

##Pviot table
df.pivot_table("survived","sex","embarked")  ## values ortalama olarak alınır
df.pivot_table("survived","sex","embarked", aggfunc="std")  #standart sapma olarak özelleştirdik
df.pivot_table("survived","sex",["embarked","class"])

df["new_age"]=pd.cut(df["age"],[0,10,18,25,40,90])

pd.set_option('display.width',500)  ##Tüm çıktıyı yanyana göster
df.pivot_table("survived","sex",["new_age","class"])


##Apply & Landa
## Apply -> fonksiyonu bütün listeye uygulama
## Landa -> Kullan at fonksiyon

df["age2"]=df["age"]*2
df["age3"]=df["age"]*5

df[["age","age2","age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()



## Join işlemleri
m=np.random.randint(1,30,size=(5,3))
df1= pd.DataFrame(m, columns=["var1","var2","var3"])
df2 =df1+99

pd.concat([df1,df2],ignore_index=True)