password = input("Please enter new Password:  ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit(): #if i is a digit then this is not executed
        digit = True


result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase
print(result)
print(all(result))

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")

