seconds = 374
def seconds_to_hms(seconds):
    minutes = seconds//60
    hours = minutes//60
    return f"{hours:02}:{(minutes % 60):02}:{(seconds % 60):02}"
# print(seconds_to_hms(seconds))

# ----------------------->
celsius = 124
def celsius_to_fahrenheit(celsius):
    return round(celsius * 9/5 + 32 ,2)
# print(celsius_to_fahrenheit(celsius))

# ----------------------->
total = 10
people = 5
def split_evenly(total, people):
    share = total // people
    remainder = total % people
    return share, remainder
# print(split_evenly(total, people))

# ----------------------->
full_name = "mohamed farouk"
def initials(full_name):
    name = full_name.split()
    i = 0 
    initials = ""
    while i < len(name):
        initials += name[i][0]
        i += 1
    return initials
# print(initials(full_name))

# ----------------------->
word = " leVeL     "
def is_palindrome_word(word):
    now_word = word[::-1].strip().lower()
    if (now_word == word.strip().lower()):
        return True
    else:
        return False
# print(is_palindrome_word(word))

# ----------------------->
email = "mohamedmx010@gmail.com"
def mask_email(email):
    a = email.index("@")
    new_email = email[0:3]
    for i in range(3,a):
        new_email += "*"
    new_email += email[a:]
    return new_email
# print(mask_email(email))

# ----------------------->
values =[1 ,3 ,5 ,6 ,9 ,3]
def middle(values):
    if(len(values) % 2 > 0):
        return values[len(values) // 2]
    else:
        return values[len(values) // 2 - 1] ,values[len(values) // 2]
# print(middle(values))

# ----------------------->
k = 3
def rotate_left(values, k):
    new_values = values[k:] + values[:k]
    return new_values
# print(rotate_left(values, k))

# ----------------------->
n = 10
def fib_list(n):
    list = []
    i = 0
    a = 0
    b = 1
    list.append(a)
    while i < n -1:
        a, b = b, a + b
        list.append(a)
        i += 1
    return list
# print(fib_list(n))

# ----------------------->
def collatz_steps(n):
    steps = 0
    while n != 1:
        if (n % 2 == 0):
            n /= 2
            steps += 1
        else:
            n *= 3
            n += 1
            steps += 1
    return steps 
print(collatz_steps(n))
