# import math
#
# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __str__(self):
#         return f"Radius: {self.radius}"
#
#     def area(self):
#         return f"Area = {self.radius * (math.pi ** 2)}"
#
#     def circumference(self):
#         return f"Circumference = {(self.radius * 2) * math.pi}"
#
# circle1 = Circle(4)
# print(circle1)
# print(circle1.area())
# print(circle1.circumference())


# class House:
#     count = 0
#
#     def __init__(self, address, floors, rooms, heating):
#         self.address = address
#         self.floors = floors
#         self.rooms = rooms
#         self.heating = heating
#         House.count += 1
#
#     def __str__(self):
#         return (f"Address: {self.address} \n" \
#                 f"Floors: {self.floors} \n" \
#                 f"Rooms: {self.rooms} \n" \
#                 f"Type of heating: {self.heating}")
#
#     @classmethod
#     def noOfHouses(cls):
#         return f"The number of houses is {House.count}"


class BankAccount:
    def __init__(self, name, accNo, openBal, overLimit):
        self.name = name
        self.accNo = accNo
        self.openBal = openBal
        self.overLimit = overLimit

    def __str__(self):
        return (f"Name: {self.name} \n" \
         f"accNo: {self.accNo} \n" \
         f"Open Balance: {self.openBal} \n" \
         f"Over Limit: {self.overLimit} \n")

    def deposit(self, amount):
        self.openBal += amount
        return f"Balance is now {self.openBal}"

    def withdraw(self, amount):
        if ((self.openBal - amount) < self.overLimit):
            print("Overdraft exceeded. Transaction not completed")
            return f"Balance is now {self.openBal}"
        else:
            self.openBal -= amount
            return f"Balance is now {self.openBal}"


