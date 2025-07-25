saxeli = "Misoon"
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  
print("Data type of full_name:", type(full_name).__name__) 

age = 20
print(f"You are {age} years old") 
print("Data type of age:", type(age).__name__) 


temperature = 20.3
print(f"The temperature is {temperature} degrees") 
print("Data type of temperature:", type(temperature).__name__)  


is_hot = temperature > 30
print(is_hot)  
print("Data type of is_hot:", type(is_hot).__name__)  

print("\nExplanation of Data Types:")
print("- int (Integer): Whole numbers without decimals. Example: 5, -10, 0")
print("- float (Floating-Point): Numbers with decimals. Example: 3.14, -0.001, 20.3")
print("- str (String): Sequence of characters (text). Example: 'Hello', 'John Doe', '123'")
print("- bool (Boolean): Logical values, either True or False. Example: True, False")