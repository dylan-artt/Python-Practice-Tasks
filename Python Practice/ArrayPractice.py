#TASK 1
# rainfall = []
# total = 0.0
# highest = 0
# lowest = 1000
#
# for i in range(12):
#     rain = int(input(f"Please enter rainfall (mm) for month {i+1}: "))
#     rainfall.append(rain)
#
# for r in range(len(rainfall)):
#     total += rainfall[r]
#     if rainfall[r] < lowest:
#         lowest = rainfall[r]
#         lowestindex = r+1
#     if rainfall[r] > highest:
#         highest = rainfall[r]
#         highestindex = r+1
#
#
# print(f"Average rainfall: {total/12}")
# print(f"The month with the highest rainfall was: {highestindex} = {highest}")
# print(f"The month with the lowest rainfall was: {lowestindex} = {lowest}")


#TASK 2
# word1 = input("Enter 1st word: ").lower()
# word2 = input("Enter 2nd word: ").lower()
# wordvalue1 = 0
# wordvalue2 = 0
# word1report = []
# word2report = []
# for char in word1:
#     word1report.append(char)
# for char in word2:
#     word2report.append(char)
#
# alphabet_dict = {i: chr(96 + i) for i in range(1, 27)}
#
# for char in word1:
#     for aNum, letter in alphabet_dict.items():
#         for item in letter:
#             if char == item:
#                 wordvalue1 += aNum
#
# for char in word2:
#     for aNum, letter in alphabet_dict.items():
#         for item in letter:
#             if char == item:
#                 wordvalue2 += aNum
#
# if wordvalue1 == wordvalue2:
#     print("These are anagrams")
# else:
#     print("These are not anagrams")
#
# print(f"Word 1 was made up of letters: {word1report}")
# print(f"Word 2 was made up of letters: {word2report}")


#TASK 3
# def searchfile(searchnum):
#     found = False
#     with open('charge_accounts.txt', 'r') as file:
#         accountlist = [line.strip() for line in file]
#
#     for i in range(len(accountlist)):
#         if searchnum == accountlist[i]:
#             found = True
#
#     if found == True:
#         print(f"{searchnum} was found in the list")
#     else:
#         print(f"{searchnum} was not found in the list")
#     file.close()
#
# def main():
#     searchnum = input("Search account number: ")
#     searchfile(searchnum)
#
# main()

#TASK 4
morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.'
}

word = input("Enter a word to convert to morse code: ").upper()
print (f"{word} translated to morse code:")
for char in word:
    print(f"{char}: {morse_code_dict[char]}   ")







