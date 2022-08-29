def f_to_c(f):
    c = (f - 32) * 5/9
    return c
c = int(input("What is the temperature in fahrenheit?\n"))
print(c, "degrees F is equal to: ", f_to_c(c), "degrees C") 
