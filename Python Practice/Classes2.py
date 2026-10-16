from operator import index

# from Week9Prac import House
#
#
# def main():
#     found = False
#     enterHouse = True
#     houseList = []
#     while enterHouse == True:
#         address = input("Enter Address: ")
#         floors = input("Enter Floors: ")
#         rooms = input("Enter Rooms: ")
#         heating = input("Enter Heating Type: ")
#         houseList.append(House(address, floors, rooms, heating))
#         house1 = House(address, floors, rooms, heating)
#         print(house1)
#         print(House.noOfHouses())
#         choice = input("Would you like to enter a house (y), search (s), or exit (e)? ")
#         if choice == 'y':
#             enterHouse = True
#         elif choice == 's':
#             enterHouse = False
#
#             addresssearch = input("Enter Address to Search: ")
#             for item in range(len(houseList)):
#                 if addresssearch == address:
#                     found = True
#                     foundindex = item
#                 else:
#                     found = False
#
#
#             if found == True:
#                 print("Found!")
#                 print(houseList[foundindex])
#             else:
#                 print("Sorry, house not found")
#
#         else:
#             enterHouse = False
#             print("Exited Program")
#
# main()



from Week9Prac import BankAccount

def main():
    adding = True
    accountsList = []
    while adding == True:
        name = input("Account Holder: ")
        accNo = input("Account Number: ")
        openBal = float(input("Opening Balance: "))
        overLimit = float(input("Overdraft Limit: "))
        account1 = BankAccount(name, accNo, openBal, overLimit)
        accountsList.append(BankAccount(name, accNo, openBal, overLimit))

        choice = input("w for withdraw | d for deposit: ")
        for acc in accountsList:
            if choice == 'w':
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)
                print("Your final balance is", acc.openBal)
            elif choice == 'd':
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
                print("Your final balance is", acc.openBal)
        cont = input("Would you like to continue? (y or n): ")
        if cont == "y":
            adding = True
        else:
            adding = False

main()