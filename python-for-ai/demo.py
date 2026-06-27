print("This is an written statement")

first_name = 'Pranav'
last_name = 'Rane'

full_name = first_name + " " + last_name  

print(full_name)

long_dash = "_" * 30

print(long_dash)

len(long_dash)

age = 15

can_vote = age >= 18

is_18 = print(age==18)


print(can_vote)

score = 20

score += 10


name = input("Enter your name -")
name2 = "James" 
Welcome = "Hello " + name +"!.Nice to meet you"
Welcome2 = f"Hello {name2}!,Yorushkaishimas"
print(Welcome)
print(Welcome2)

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

temperature = input("Enter the temperature -")
temperature = int(temperature)

if temperature <= 20:
    print("Its cold outside!")

elif temperature <= 30:
    print("Its nice weather!")

else:
    print("Its Hot outside!")





