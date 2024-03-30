'''Görev 1:  Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
Görev 2:  Titanic verisetindeki kadın ve erkek yolcuların sayısını bulunuz.
Görev3:  Her birsutuna ait unique değerlerin sayısını bulunuz.
Görev4:  pclass değişkeninin unique değerlerinin sayısını bulunuz.
Görev5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
Görev6:  embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz vetekrarkontrolediniz '''
import seaborn as sns
df=sns.load_dataset("titanic")
df["sex"].value_counts()
df.nunique()
df["pclass"].unique().shape[0]
df["parch"].unique().shape[0]
df["embarked"].dtype
df["embarked"]=df["embarked"].astype("category")
df["embarked"].dtype


'''Görev7:  embarked değeri C olanların tüm bilgelerini gösteriniz.
Görev8:  embarked değeri S olmayanlarıntümbilgelerinigösteriniz.
Görev9:   Yaşı30 dan küçük ve kadın olan yolcularıntümbilgilerinigösteriniz.
Görev10:  Fare'i500'den büyük veya yaşı70 den büyükyolcularınbilgilerinigösteriniz.'''
df.loc[df["embarked"] == "C"]
df.loc[df["embarked"] != "S"]
df.loc[(df["age"]<30) & (df["sex"]=="female")]
df.loc[(df["fare"]>500) | (df["age"]>70)]

'''Görev 11:  Her birdeğişkendekiboşdeğerlerintoplamınıbulunuz.
Görev 12:  who değişkeninidataframe’dençıkarınız.
Görev13:  deck değikenindeki boş değerleri deck değişkeninençoktekraredendeğeri(mode) iledoldurunuz.
Görev14:  age değikenindekiboşdeğerleriage değişkeninmedyanıiledoldurunuz.
Görev15:  survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz'''
df.isnull().sum()
df=df.drop(["who"],axis=1)
df["deck"].fillna(df["deck"].mode()[0],inplace=True)
df["deck"].isnull().sum()
df["age"].fillna(df["age"].median(),inplace=True)
df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})

'''Görev16:  30 yaşın altında olanlar 1, 30'a eşit veüstündeolanlara0 vericekbirfonksiyonyazın. 
Yazdığınızfonksiyonukullanaraktitanikverisetindeage_flagadındabirdeğişkenoluşturunuzoluşturunuz. (apply velambda yapılarınıkullanınız)
Görev17:  Seaborn kütüphanesi içerisinden Tipsveri setini tanımlayınız.
Görev18:  Time değişkeninin kategorilerine(Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max veo rtalamasını bulunuz.
Görev19:  Günlere ve time göretotal_billdeğerlerinintoplamını, min, max veortalamasınıbulunuz.'''

df["age_flag"]=df["age"].apply(lambda x: 1 if x < 30 else 0)

df=sns.load_dataset("tips")
df.groupby("time").agg({"total_bill": ["sum","min", "max", "mean"]})
df.groupby(["day","time"]).agg({"total_bill": ["sum","min", "max", "mean"]})

'''Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'egöre toplamını, min, max ve ortalamasınıbulunuz.
Görev 21:size'i 3'ten küçük, total_bill'i10'dan büyükolansiparişlerin ortalamasınedir? (loc kullanınız)
Görev22:  total_bill_tip_sumadındayeni birdeğişkenoluşturunuz. Her birmüşterininödediğitotalbillvetip in toplamınıversin.
Görev23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni birdataframe'eatayınız'''

df.groupby((df["time"]=="dinner") & (df["sex"]=="female")).agg({"total_bill": ["sum","min", "max", "mean"],
                                                                "tip": ["sum","min", "max", "mean"]})
df.loc[(df["size"]<3)& (df["total_bill"]>10)].mean()
df["total_bill_tip"]=df[["total_bill", "tip"]].apply(lambda x: x[0]+x[1] ,axis=1)
df.sort_values(by="total_bill_tip")
new_df=df[0:30]