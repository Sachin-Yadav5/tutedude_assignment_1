# Creating a Personalized Greeting


#Taking first and last name from the user
first_name = input('Enter your first name: ').strip().title()
last_name = input('Enter your last name: ').strip().title()

# Handling capatilization 

# Adding both the names with the space 
full_name = first_name + " "+ last_name

print(f"Hello, {full_name}! Welcome to the python program.")
