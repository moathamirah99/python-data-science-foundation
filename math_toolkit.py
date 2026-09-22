students = ["Ahmad", "Sara", "Khaled", "Mona", "Ali", "Laila", "Omar", "Nour", "Sami", "Huda"]
study_hours = [2, 5, 3, 7, 4, 6, 1, 8, 3, 5]
grades = [55, 75, 60, 90, 65, 85, 45, 95, 58, 80]
import math

# الجزء 1: المتجهات
def vector_add(v1, v2):
    v = [(v1[0]+ v2[0]) , (v1[1]+v2[1])]
    return v

def subtract(v1,v2):
    v = [(v1[0] - v2[0]) , (v1[1] - v2[1])]
    return v

def muliply(v1,v2):
    v = (v1[0] * v2[0]) + (v1[1] * v2[1])
    return v

def magnitude(v):
    return  math.sqrt(v[0]**2 + v[1]**2)

# الجزء 2: المصفوفات
def matrix_add(m1,m2):
    result = []
    for i in range(len(m1)):
        curent_row = []
        for j in range(len(m1[0])):
            value = m1[i][j] + m2[i][j]
            curent_row.append(value)
        result.append(curent_row)
    return(result)

def matrix_multiply(m1,m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] = result[i][j] + (m1[i][k] * m2[k][j])
    return result

def transpose(m):
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result

# الجزء 3: الإحصاء
def mean(x):
    return sum(x) / len(x)

def median(y):
    sorted_y = sorted(y)
    n = len(sorted_y)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_y[mid-1] + sorted_y[mid]) / 2
    return sorted_y[mid]

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

# الجزء 4: الارتباط
def calculate_correlation(x, y):
    mean_stud = sum(x) / len(x)
    mean_marks = sum(y) / len(y)
    sud_dist = []
    marks_stud = []
    for i in x:
       s =  i - mean_stud
       sud_dist.append(s)
    for j in y:
        a = j - mean_marks
        marks_stud.append(a)
    cor_list = []
    for k in range(len(x)):
        w = marks_stud[k] * sud_dist[k]
        cor_list.append(w)
    cor_mean = sum(cor_list) / len(cor_list)
    stdx = calculate_std(x)
    stdy = calculate_std(y)
    result = cor_mean / (stdx * stdy)
    return result

# الجزء 5: الاحتمالات
def redball(x,y):
    all = x+y
    probx = x / all
    return probx

def probs_photo(x,y):
    probs = x * y
    return probs

def succes_student(x,y):
    probs  = y / x
    return probs



print(mean(grades))
print( calculate_std(grades))
print(calculate_correlation(study_hours, grades))

total_students = 10
passed_students = 7
print(succes_student(total_students, passed_students))




#متوسط العلامات طلع 71 تقريباً، والانحراف المعياري 16يعني إنو مستويات الطلاب متباعدة ومتفاوتة ومش متقاربة من بعضها

#معامل الارتباط المطلوبة بين ساعات الدراسة والعلامة طلعت 0.99(الطلاب اللي درسوا ساعات أكتر جابوا علامات أعلى).

#احتمال اختيار طالب ناجح بشكل عشوائي من هاي العينة هو 70%