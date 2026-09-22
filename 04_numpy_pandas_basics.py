import numpy as np
import pandas as pd
import math
import seaborn as sns

titanic = sns.load_dataset('titanic')

#الجزء الاول

#------------------------------------------------------------------------
#1
my_list = np.arange(1,21)
reshped_list = my_list.reshape(4,5)
print(my_list)
print(reshped_list)

#----------------------------------------------------------------------
#2
list_1 = np.array([2,5,6,4,8])
list_2 = np.array([3,6,4,8,9])
addition = list_1 + list_2
redution = list_1 - list_2
multiplication = list_1 * list_2
print(addition , redution, multiplication)

#----------------------------------------------------------------
#3
r_list = np.random.randint(1,100, size= 50)
def calculate_variance(numbers):
    mean_num = sum(numbers) / len(numbers)
    varience = []
    for i in numbers:
        x = i - mean_num
        varience.append(x)
    squared = []
    for j in varience:
        s = j**2
        squared.append(s)
    mean_squared = sum(squared) / len(squared)
    return mean_squared    

def calculate_std(numbers):
    var = calculate_variance(numbers)
    std = math.sqrt(var)
    return std

def mean(x):
    return sum(x) / len(x)

std = np.std(r_list)
mean1 = np.mean(r_list)
max1 = np.max(r_list)
min1 = np.min(r_list)


print(calculate_std(r_list))
print(std)
print(mean1)
print(mean(r_list))

#----------------------------------------------------------

#4
my_matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120] 
])
row = my_matrix[2]
column = my_matrix[0:,1]
sub_matrix = my_matrix[1:3, 2:]
print(row)
print(column)
print(sub_matrix)

#------------------------------------------------------------
#------------------------------------------------------------

#الجزء 2 

#-----------------------
#1
my_series = pd.Series(data=[80, 84, 91, 71, 78], index=["math", "biology", "chemistry", "physics", "english"])
print(my_series.index)
print(my_series.values)
print(my_series.dtype)
#----------------------------------------------------------------

#2
marks = {"moath":{"age": 27, "mark": 91}, "nourhan":{"age":25, "mark":89}, "basel":{"age":26, "mark": 80},
          "mohamed": {"age": 28,"mark":88 }, "karam": {"age":22, "mark":79}}
frame = pd.DataFrame(marks)
print(frame)
print(titanic.head(5))
print(titanic.shape)
print(titanic.dtypes)
print(titanic.describe())
print(titanic.isnull().sum())
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#الجزء 3

#---------------

print(titanic.loc[:,'age'])
def older_than_40(x):
    forty = []
    for i in titanic['age']:
        if i >= 40:
            forty.append(i)
    return forty
print(older_than_40(titanic['age']))
print(titanic[titanic["age"]>40])
print(titanic[(titanic['sex'] == "female" )& (titanic["survived"] == 1)])
sorted1 = titanic.sort_values("age" , ascending=False)
print(sorted1.head(10))
print(titanic.loc[5:10, ["survived", "sex" , "age"]])

#---------------------------------------------------------------------
#---------------------------------------------------------------------

#الجزء 4
#-------------

print(titanic.info())

#survived: حالة النجاة (0 يعني توفي، 1 يعني نجا)
#pclass: فئة التذكرة أو الركاب (1 للدرجة الأولى 2 للثانية، 3 للثالثة)
#age: عمر الراكب بالسنوات
#sex: جنس الراكب 
#fare: سعر تذكرة الرحلة

#3   age          177 null ممكن نقدر نعبيه بالمتوسط مش متاكد
#7   embarked     2 null نعمل دروب لهدول الصفين
#11  deck         688 null  لازم ينعمل الو دروب
#12  embark_town  2 null نعمل دروب لهدول الفين

print(titanic.describe())
#في فرق كبير بين اغلى تذكرة 512 و متوسط سعر التذاكر

print(titanic["survived"].mean())
female_s = titanic[titanic['sex'] == 'female']['survived'].mean() 
male_s = titanic[titanic['sex'] == 'male']['survived'].mean() 
print(female_s, male_s)
#نسبة نجاة الاناث 74
#نسبة نجاة الذكور 18

class_1 = titanic[titanic["pclass"] == 1]["survived"].mean()
class_3 = titanic[titanic["pclass"] == 3]["survived"].mean()
print(class_1 , class_3)
#متوسط نجاة الدرجة الاولى 62
#متوسط نجاة الدرجة الثاثة 24

survived_a = titanic[titanic["survived"] == 1]["age"].mean()
died_a = titanic[titanic["survived"] == 0]["age"].mean()
print(survived_a, died_a)
#متوسط عمر الناجين 28.3
#متوسط عمر الميتين 30.6


#اللي لاجظتو انو الاناث كانت الهم الاولوية 
#و كمان لاحظت انو الناس اللي بالدرجة الاولى كانت الهم فرض اعلى بالنجاة 