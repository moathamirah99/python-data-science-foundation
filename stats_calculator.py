import math 

def calculate_count(numbers):
    return len(numbers)

def calculate_sum(numbers):
    total = 0
    for i in numbers:
       total = total + i
    return total

def calculate_mean(numbers):
    x = calculate_sum(numbers)
    return x / len(numbers)

def calculate_median(y):
    sorted_y = sorted(y)
    n = len(sorted_y)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_y[mid-1] + sorted_y[mid]) / 2
    return sorted_y[mid]

def calculate_mode(numbers):
    most = {}
    for i in numbers:
        if i not in most:
           most[i] = 1
        else:
            most[i] = most[i] + 1
    max_count = max(most.values())
    max_list = []
    for i in most:
        if most[i] == max_count:
            max_list.append(i)
    return max_list

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

def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum , maximum

def calculate_range(numbers):
     minimum = min(numbers)
     maximum = max(numbers)
     return maximum - minimum

def get_numbers_from_user():
    while True:
     s = input("pleas enter your numbers splited by couma ")
     if s == "":
        print("Error: Input cannot be empty!")
        continue
     splited_s = s.split(",")
     final_list = []
     try: 
      for i in splited_s:
         final_list.append(float(i.strip()))
      return final_list
     
     except ValueError:
            print("Error: Alphabetical input is not allowed. Please enter numbers only.")

def display_statistics(numbers):
    count = calculate_count(numbers)
    summation = calculate_sum(numbers)
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mod = calculate_mode(numbers)
    variance = calculate_variance(numbers)
    std = calculate_std(numbers)
    minimum, maximum = find_min_max(numbers)
    ranges = calculate_range(numbers)
    
    print("\n=== نتائج التحليل الإحصائي ===")
    print(f"عدد القيم: {count}")
    print(f"المجموع: {summation}")
    print(f"المتوسط: {mean}")
    print(f"الوسيط: {median}")
    print(f"المنوال: {mod}")
    print(f"التباين: {variance}")
    print(f"الانحراف المعياري: {std}")
    print(f"أصغر قيمة: {minimum}")
    print(f"أكبر قيمة: {maximum}")
    print(f"المدى: {ranges}")
    print("==============================\n")
last_analysis = []
while True:
    print("1- veiw last anlalysis")
    print("2- analize new numbers list")
    print("3- exite")
    
    choice = input("")
    if choice == "3" or choice =="exite":
        break
    elif choice == "2" or choice =="analize new numbers list":
        current_number = get_numbers_from_user()
        display_statistics(current_number)
        last_analysis = current_number
    elif choice == "1" or choice == "veiw last anlalysis":
        if len(last_analysis) == 0:
          print ("there is no previos analysis")
        else:
            display_statistics(last_analysis)




