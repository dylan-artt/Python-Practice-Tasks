# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y' or "Y"

# # Calculate a series of commissions.
# while keep_going == 'y' or "Y":
#     # Get a salesperson's sales and commission rate.
#     sales = float(input('Enter the amount of sales: '))
#     comm_rate = float(input('Enter the % commission rate: '))
#
#     # Calculate the commission.
#     commission = sales * comm_rate / 100
#     if sales >= 5000:
#         commission += 50
#
#     # Display the commission.
#     print('The commission is £',
#           format(commission, '.2f'), sep='')
#
#     # See if the user wants to do another one.
#     keep_going = input('Do you want to calculate another ' + \
#                        'commission (Enter y for yes): ')
#
# # end of while loop



# print('number\tSquare')
# print('---------------')
# target = int(input("Please choose the highest number to be used"))
#
# for number in range (target,0,-1):
#     square = number**2
#     cube = number **3
#     print(number, '\t', square, '\t', cube)


# This program calculates the sum of a series
# of numbers entered by the user.

# big = int(input("Enter the amount of numbers you are entering"))  # The maximum number
#
# # Initialize an accumulator variable.
# total = 0.0
#
# # Explain what we are doing.
# print('This program calculates the sum of')
# print(big, 'numbers you will enter.')
#
# # Get the numbers and accumulate them.
# for counter in range(big):
#     number = int(input('Enter a number: '))
#     total += number
#
# # Display the total of the numbers.
# print('The total is', total)
# print("The average is", total/big)

# #process 1
# number = 0
# floppy = 0.0
# while floppy < 1000000:
#     floppy += 1.44
#     number += 1
#     print(number)

#process 2
# length = 694445 * 3.2
# print(length, "MM, which converts to", length*0.001,"M")

# this program draws a square of side 100

# #import turtle
# import turtle
#
# sides = int(input("How many sides should the shape be?"))
# # draw a line of length 100
# # then turn left thru 90 degrees
# # repeat this process 4 times to
# # draw the four sides of the square
#
# for i in range(sides):
#     angle = 360 / sides
#     turtle.forward(50)
#     turtle.left(angle)
# #end of for loop

# import turtle
# for i in range (36):
#     for i in range(4):
#         turtle.forward(50)
#         turtle.left(90)
#     turtle.left(10)

num = int(input("Please select a number: "))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False

if prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")







