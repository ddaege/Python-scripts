temperature = int(input("What is the temperature?\n"))

if temperature  > 80:
     print("It's too hot!")
elif temperature < 60:
     print("It's too cold!")
if temperature > 80 or temperature < 60:
     print("stay inside!")
else:
     print("Enjoy the outdoors!")
