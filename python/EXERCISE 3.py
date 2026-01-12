#-PRACTİCE-1

# Task

# Kullanıcıdan age al ve:

# Age < 18 → "You are under 18"

# Age ≥ 18 → "You are an adult"

# 📌 Rules

# input() kullan

# int() ile type casting yap

# if / else kullan

# 📤 Output example
# Enter your age: 17
# You are under 18

#-PRACTİCE-1 ANSWER

# age = int(input("Please Enter Your Age: "))
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are under 18")

#PRACTİCE-2

# Task

# Kullanıcıdan score (0–100 arası) al ve:

# 90–100 → "Grade: A"

# 80–89 → "Grade: B"

# 70–79 → "Grade: C"

# 60–69 → "Grade: D"

# 0–59 → "Grade: F"

# 📌 Rules

# input() kullan

# int() ile type casting

# if / elif / else kullan

#-PRACTİCE-2 ANSWER
# score = int(input("Enter Your Exam Score: "))
# if score > 100:
#     print("Undefined Exam Score.")
# elif score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# elif score >= 0:
#     print("Grade: F")
# else:
#     print("Undefined Exam Score.")


#-PRACTİCE-3
# Task

# Kullanıcıdan:

# age

# has_license (yes / no)

# al ve:

# Age ≥ 18 ve license = yes
# → "You can drive"

# Aksi halde
# → "You cannot drive"

# 📌 Rules

# input() kullan

# int() ile age al

# and kullan

# has_license string olacak


#-PRACTİCE-3 ANSWER

# age = int(input("What's your age?: "))
# yes = "yes"
# no = "no"
# has_license = str(input("Have Driving License?(yes/no): "))
# if age >= 18 and yes in has_license:
#     print ("You can drive")
    
    
# elif age <=0:
#     print ("Undefined Answer")
# else:
#     print("You cannot drive")