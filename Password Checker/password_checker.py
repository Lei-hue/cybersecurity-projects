import string

password_info = {
    "has_uppercase": False,
    "has_lowercase": False,
    "has_number": False,
    "has_special": False,
    }

print ("script is running...")

password = input("Enter your password: ")
print ("You entered: ", password)

if len(password) >= 13:
    password_info["is_long_enough"] = True
else:
    password_info["is_long_enough"] = False
    


for char in password:
    if char.isupper():
        password_info["has_uppercase"] = True
    if char.islower():
        password_info["has_lowercase"] = True
    if char.isdigit():
        password_info["has_number"] = True
    if char in string.punctuation:
        password_info["has_special"] = True

true_count = 0
for keys in password_info:
    if password_info[keys] == True:
        true_count +=1
    
if true_count <= 1:
    print ("Password Strength | Very Weak")
elif true_count == 2:
    print ("Password Strength | Weak")
elif true_count == 3:
    print ("Password Strength | Medium")
else:
    print ("Password Strength | Strong")
