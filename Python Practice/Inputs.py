## This program gets a numeric test score from the
## user and displays the corresponding letter grade.
##
## Variables to represent the grade thresholds
##A_score = 90
##B_score = 80
##C_score = 70
##D_score = 60
##
## Get a test score from the user.
##score1 = float(input('Enter your score for coursework 1: '))
##score2 = float(input('Enter your score for coursework 2: '))
##score3 = float(input('Enter your score for coursework 3: '))
##final = (score1 + score2 + score3) / 3
##print("Final score: ", final)
## 
## Determine the grade.
##if final >= A_score:
##    print(f'Your grade is A.')
##elif final >= B_score:
##    print(f'Your grade is B.')
##elif final >= C_score:
##    print(f'Your grade is C.')
##elif final >= D_score:
##    print(f'Your grade is D.')
##else:
##    print(f'Your grade is F.')
## End of if-elif structure
##

##price = 0.10
##postage = 2
##amount = float(input("How many nails would you like to buy?"))
##
##if amount < 51:
##    finalprice = ((amount * price) + postage)
##    print(f"The final price is {finalprice:.2f}")
##elif amount >= 51 and amount <= 100:
##    finalprice = ((amount * price) * 0.9) + postage
##    print(f"The final price includes a 10% discount so the total is {finalprice:.2f}")
##elif amount >= 101 and amount <= 200:
##    finalprice = ((amount * price) * 0.8) + postage 
##    print(f"The final price includes a 20% discount so the total is {finalprice:.2f}")
##elif amount >= 201:
##    finalprice = ((amount * price) * 0.75) + postage 
##    print(f"The final price includes a 25% discount so the total is {finalprice:.2f}")



### This program determines whether a bank customer
### qualifies for a loan. A customer is eligible for
### a loan if s/he satisifes at least one of the following:
### 1)earns at least £30,000/year
### 2)has been in full time emplyment for at least 2 years
##
##min_salary = 30000.0  # The minimum annual salary
##min_years = 2         # The minimum years on the job
##
### Get the customer's annual salary.
##salary = float(input('Enter your annual salary: '))
##
### Get the number of years on the current job.
##years_on_job = int(input('Enter the number of ' +
##                         'years employed: ')
##
### Determine whether the customer qualifies.
##if salary >= min_salary and years_on_job >= min_years:
##    print('You qualify for the loan.')
##else:
##    print('You do not qualify for this loan.')
##    
###end of if-else structure




## this program draws a square of side 100
##
##import turtle
##import turtle
##
## draw a line of length 100
## then turn left thru 90 degrees
## repeat this process 4 times to
## draw the four sides of the square
##
##
##
##side_length = 100  
##turtle.pensize(5)  
##turtle.speed(3)
##turtle.pencolor("blue")  
##
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(100)
##turtle.left(90)

##year = int(input("Enter year "))
##
##if ((year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)):
##    print ("This is a leap year")
##else:
##    print("This isnt a leap year")















