#الجزء الاول 1 
#------------------
import math
v1 = [3,4]
v2 = [1,2]

# الجمع 
def vector_add(v1, v2):
    v = [(v1[0]+ v2[0]) , (v1[1]+v2[1])]
    return v
print(vector_add(v1,v2))

#الطرح 
def subtract(v1,v2):
    v = [(v1[0] - v2[0]) , (v1[1] - v2[1])]
    return v
print(subtract(v1,v2))

# الضرب 
def muliply(v1,v2):
    v = (v1[0] * v2[0]) + (v1[1] * v2[1])
    return v
print(muliply(v1,v2))

#طول المتجه 
def magnitude(v):
    return  math.sqrt(v[0]**2 + v[1]**2)
    
print(magnitude(v1))
print(magnitude(v2))
#-----------------------------------------------------------
#-----------------------------------------------------------
#الجزء 2

m1 = [[1, 2], 
      [3, 4]]

m2 = [[5, 6], 
      [7, 8]]

#الجمع 
def matrix_add(m1,m2):
    result = []
    for i in range(len(m1)):
        curent_row = []
        for j in range(len(m1[0])):
            value = m1[i][j] + m2[i][j]
            curent_row.append(value)
        result.append(curent_row)
    return(result)
print(matrix_add(m1,m2))

#الضرب 
def matrix_multiply(m1,m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] = result[i][j] + (m1[i][k] * m2[k][j])
    return result
print(matrix_multiply(m1,m2))      


#القلب
def transpose(m):
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result
print(transpose(m1))
print(transpose(m2))    
    
#----------------------------------------------------
#----------------------------------------------------
#الجزء 3
#1
def mean(x):
    return sum(x) / len(x)
#2
def median(y):
    sorted_y = sorted(y)
    x = len(sorted_y) // 2
    if sorted_y % 2 == 0 : 
        return x - 1
    else:
        return x

#3
mylist = [85, 90, 78, 92, 88, 76, 95]
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
print (calculate_variance(mylist))

#4
def calculate_std(numbers):
    var = calculate_variance(numbers)
    std = math.sqrt(var)
    return std

print (calculate_std(mylist))

#------------------------------------------------------
#------------------------------------------------------

#الجزء 4

#1
studing_period = [1, 2, 3, 4, 5, 6]
marks = [50, 55, 65, 70, 80, 85]

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
print(calculate_correlation(studing_period, marks))


#-----------------------------------------------------------
#-----------------------------------------------------------

#الجزء 5

#1
red_balls = 5 
blue_balls = 3
def redball(x,y):
    all = x+y
    probx = x / all
    return probx
print(redball(red_balls, blue_balls))



#2
probs1 = 0.5
probs2 = 0.5
def probs_photo(x,y):
    probs = x * y
    return probs
print(probs_photo(probs1, probs2))

#3
total = 60
succes = 54
def succes_student(x,y):
    probs  = y / x
    return probs
print(succes_student(total, succes))