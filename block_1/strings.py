name="Emerson"
secondName="Silva"

print("Hello, my name is {} and my second name is {}".format(name, secondName))

# conversion of data
age = int(input("Enter your age: "))
print("You are {} years old".format(age))

# I need to convert the age variable to an integer because the input function returns a string. If I don't convert it, I will get an error when I try to use the variable in the format method.