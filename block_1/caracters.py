nome="Robert"

# concat like js
print("My name is" + nome)

# in Python it's possible multiply strings like this:
msg="Hello, " * 3
print(msg)
# output = "Hello, Hello, Hello, "

# String functions
print(nome.upper())
# output = "ROBERT"

print(nome.lower())
# output = "robert"

print(nome.capitalize())
# output = "Robert"

print(nome.strip())
# output = "Robert"

print(nome.replace("R", "P"))
# output = "Pobert"

print(nome.split("b"))
# output = ['Ro', 'ert']