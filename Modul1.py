# Aşağdaki şekilde string dönüştüren fonk yaz.
# before: "hi my name is jhon and i am learining python"
#after : "Hi mY Name iS John aNd i aM LeArNiNg pYtHoN"
#tek indeksteki harfleri küçük çift indek büyük harf

def alternating(string):
    new_string = string
    for i in range(len(new_string)):
        if i % 2 == 0:
            new_string += new_string[i].upper()
        else:
            new_string += new_string[i].lower()
    print(new_string)
alternating ("rayhana")

def alternating_enumerate(string):
    new_string=string
    for index, char in enumerate(string):
        if index % 2 == 0:
            new_string += new_string[index].upper()
        else:
            new_string += new_string[index].lower()
    print(new_strin g)
alternating_enumerate("rayhana ben")

# divide_students fonk yaz.
# çift indexte yer alan öğrencileri A listesine alın. Tek indexteki öğrencileri B listesine atın
#bu iki liste tek bir liste olarak return olsun
students = ["Ahmet", "Mehmet", "Selma", "Kübra"]
def divide_student(students):
    groups= [[],[]]
    for index, student in enumerate(students):
        if index % 2==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)

divide_student(students)

## List comprehensions   Tüüm işlemleri tek bir satıra indirgemek.
salaries=[1230,2600,8900,7400,3000]
[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary <7000]  #sadece if kullanılacaksa forun sağında olur
[salary * 2 if salary < 7000 else salary*0 for salary in salaries ]  #if else birlikte kullanılıyorsa forun solunda olur


students = ["Ahmet", "Mehmet", "Selma", "Kübra"]
students_no=["Mehmet", "Kübra"]
[ student.lower() if student in students_no else student.upper() for student in students]

# dict comprehension
dictionary= {'a':1,
             'b':2,
             'c':3,
             'd':4}
dictionary.keys()
dictionary.values()
dictionary.items()

{k.upper(): v**2 for (k,v) in dictionary.items()}


## Mülakat sorusu: Amaç: çift sayıların karesi alınarak sözlüğe eklemmeli
numbers=range(10)
new_dict={}
for n in numbers:
    if n % 2 ==0:
        new_dict[n]=n**2


{n:n**2 for n in numbers if n % 2==0 }

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
# ListComprehension yapısı kullanarak car_crashesverisindeki numeric değişkenlerin isimlerini büyükharfe çeviriniz ve başına NUM ekleyiniz.
["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O"]

# ListComprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna"FLAG" yazınız.
[for col in df.columns if col ]