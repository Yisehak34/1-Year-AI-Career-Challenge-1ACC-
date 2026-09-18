# initializing the age  
age = 18  
  
# if statement: checking if the given age is greater than or equal to 18  
if age >= 18:  
  # printing a message  
  print("You are eligible to vote.")  # This executes because the condition is True  

  # asking age from the user  
age = int(input("Enter your age: "))  
  
# multiple if blocks  
if age < 18: # checking if age is less than 18  
    # printing a message  
    print("You are not eligible to vote")  
  
if age >= 18: # checking if age is greater than or equal to 18  
    # printing a message  
    print("You are eligible to vote.")  
  
if age >= 21: # checking if age is greater than or equal to 21  
    # printing a message  
    print("You are allowed to consume alcohol in some countries.")  
  
if age >= 60: # checking if age is greater than or equal to 60  
    # printing a message  
    print("You are eligible for senior citizen benefits.")  
  
if age >= 80: # checking if age is greater than or equal to 80  
    # printing a message  
    print("You are a very senior citizen. Take extra care of your health.")

    # asking age from the user  
age = int(input("Enter your age: "))  
  
# if-else statement: checking whether the user is eligible to vote or not  
if age >= 18:  
  # if block  
  print("You are eligible to vote.")  
else:  
  # else block  
  print("You are not eligible to vote.") 

   # given list  
cars = ["Tata", "Honda", "Mahindra", "Suzuki", "BMW"]  
# using for loop to iterate each element from the list  
for brands in cars:  
  print(brands) # printing elements 

  row = int(input("Enter number of rows: "))  
  
for i in range(1, row + 1):  
    # Print spaces  
    for j in range(row - i): #nested loop used  
        print("  ", end="")  
      
    # Print stars  
    for stars in range(2 * i - 1):  
        print("* ", end="")  
      
    print()  

    # Loop through numbers from 1 to 10  
for num in range(1, 11):  
    if num % 2 == 0:  
        continue  # Skip the rest of the loop for even numbers  
    print(num)  