'''print("بيئتي جاهزة")
#استعملت vsc عشان اتعودت عليه و في عليه ااكستنشن مريحة 


# الجزء 1 
#-----------------------------------------------------------
#1
name = "Moath Marwan Amirah"
age = "27" 
hight = "1.83"
print(f"Name: {name}, Age: {age}, Height: {hight}")
#---------------------------------------------------------
#2
first_mark = float(input("enter your first mark: "))
second_mark = float(input("enter your second mark: "))
avarage = (first_mark + second_mark) /2
print(f"your avarage is {avarage:.2f}")

#---------------------------------------------------------
#3
string = "66"
number = int(string)
print(type(number))
print(f"the number is {number} and the type is {type(number)}")
#----------------------------------------------------------------

#الجزء 2
#----------

#1
x  = int(input("enter your age pleas : "))
if x < 13:
    print("you are a child")
elif x >= 13 and x < 19:
    print("you are a teenager")
else:
    print("you are an adult")

#---------------------------------------------------
#2
first_mark = float(input("enter your first mark: "))
second_mark = float(input("enter your second mark: "))
avarage = (first_mark + second_mark) /2
print(f"your avarage is {avarage:.2f}")
if avarage >= 90:
    print("your grade is A")
elif avarage >= 80 and avarage < 90:
    print("your grade is B")
elif avarage >= 70 and avarage < 80:    
    print("your grade is C")
elif avarage >= 60 and avarage < 70:
    print("your grade is D")
else:
    print("your grade is F")

#----------------------------------------
#3
numbers  = input("enter 3 numbers saparated by comma : ").split(',')
if int(numbers[0])>int(numbers[1]) and int(numbers[0])>int(numbers[2]):
    print("the largest number is ", numbers[0])
elif int(numbers[1])>int(numbers[0]) and int(numbers[1])>int(numbers[2]):
    print("the largest number is ", numbers[1])
else:
    print("the largest number is ", numbers[2])


#----------------------------------------------------------------------

#الجزء3
#---------

#1
x = int(input("enter a number pleas : "))
for i in range(1,11):
    print(f"{x} * {i} = {x*i}")'''
#------------------------------------------------------
#2
'''even_numbers = []
for i in range(1,101):
    if i %2 == 0:
        even_numbers.append(i)
print(f"the sume of even numbers is {sum(even_numbers)}")
#------------------------------------------------------------

#3
fizzbuzz_numbers = []
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz_numbers.append("FizzBuzz")
    elif i % 3 == 0:
        fizzbuzz_numbers.append("Fizz")
    elif i % 5 == 0:
        fizzbuzz_numbers.append("Buzz")
    else:
        fizzbuzz_numbers.append(i)
print(fizzbuzz_numbers)
#--------------------------------------------------------------

#4
guess_number = 7
while True:
    user_input = int(input("guess a number between 1 and 10:"))
    if user_input == guess_number:
        print("gongrats")
        break
    elif user_input < guess_number:
        print("your guess is lower try a higher number")
    else:
        print("your guess is higher try a lower number")    
#---------------------------------------------------------------

#الجزء 4
#-----------------

#1
def my_primenumber(num):
    if num < 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

num = int(input("enter a number pleas : "))
print(my_primenumber(num))

#-------------------------------------------------------------

#2
width = 0
length = 0
radius = 0
shape = input("enter the shape (rectangle or circle): ")
if shape == "rectangle":
     width = float(input(("enter the width of the rectangle: ")))
     length = float(input(("enter the length of the rectangle: ")))
elif shape == "circle":
    radius = float(input(("enter the radius of the circle: ")))
else:
    print("invalid shape")

def calculate_area(shape, width, length, radius):
    if shape == "rectangle":
        return width * length
    elif shape == "circle":
        return 3.14 * radius ** 2

print(calculate_area(shape, width, length, radius))

#--------------------------------------------------------------------------
#3
mysring = str(input("enter a string pleas :"))
def reverse_sting(mystring):
    revers_string = ""
    for i in range(len(mystring)):
        revers_string = mystring[i] + revers_string
    return revers_string

print(reverse_sting(mysring))'''
#---------------------------------------------------------------------------
#4
list1 = input("enter a list of numbers separated by comma: ").split(',')
int_list = []
for i in list1:
    int_list.append(int(i))
def avglist1(list1):
    if len(list1) == 0:
        return 0
    return sum(list1) / len(list1)

print(avglist1(int_list))
#---------------------------------------------------------------------------



#الجزء 5
#-----------------

#1
my_list = [5,6,1,7,5,2,3,4,9,8,2,1,]
my_list.sort()
print(my_list)
print(max(my_list), "," , min(my_list))
#--------------------------------------------------

#2
my_dict = {"moath" : 88, "karam": 77, "nourhan" : 90, "zaid" : 66}
print(max(my_dict , key= my_dict.get), max(my_dict.values()))

#-----------------------------------------------------

#3
list2 = [1,1,1,1,2,2,2,3,3,3,4,4,5,5,9,9,6,6,8,8]
unique = set(list2)
print(unique)


#4
# مثال على إحداثيات موقع (x, y)
# بنستخدم tuple عشان الإحداثيات ثابتة وممنوع تتغير بالخطأ

location = (31.95, 35.91)

# لو حاولنا نعدل القيمة الأولى هيك:
# location[0] = 32.00
# الكود رح يعطي Error لأن الـ tuple ما بتتعدل (Immutable)

print("Coordinates:", location)