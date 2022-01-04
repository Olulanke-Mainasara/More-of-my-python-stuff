'''
#Code 1
print("Code1")
str = "Azubuike Ezenwoke"
for ch in str:
    print(ch)
print(len(ch))
print("\n")

#Code 2
print("Code 2")
str = "Azubuike Ezenwoke"
count = 0
for ch in str:
    if ch == "u":
        count += 1
print("The number of U's in the name is ", count)
print(len(str))
print("\n")


#Code 3
print("Code 3")
doc = "A parallel computer is a multiple-processor computer system supporting parallel programming."
print(len(doc))
count = 0
Letter = input("Enter the character you want to count: ")
for letter in doc:
    if letter == Letter:
        count += 1
print("The number of times the character appears in the above text is ", count)
print("\n")

#Code 4
print("Code 4")
doc = "A parallel computer is a multiple-processor computer system supporting parallel programming."
print(len(doc))
count1 = 0
count2 = 0
count3 = 0
Letter1 = input("Enter the character you want to count: ")
Letter2 = input("Enter the character you want to count: ")
Letter3 = input("Enter the character you want to count: ")

for letter in doc:
    if letter == Letter1:
        count1 += 1
    elif letter == Letter2:
        count2 += 1
    elif letter == Letter3:
        count3 += 1
print("These are the counts: ")
print("The number of times",Letter1, "appers in the above text is ", count1)
print("The number of times",Letter2, "appears in the above text is ", count2)
print("The number of times",Letter3, "appears in the above text is ", count3)
print("\n")

#Code 5
print("Code 5")
First = input("Enter your First name: ")
Surname = input("Enter your surname: ")
First += " " + Surname
print("Your full name is ",First)
print("\n")

#Code 6
print("Code 6")
Text = input("Enter the text you want to use: ")
print(Text[0:3])

#Code 7
print("Code 7")
first = input("Enter your first name: ")
last = input("Enter your last name: ")
matricno = input("Enter your Matric.no: ")
print(first[0:3] + last[-3:len(last)] + matricno[0:3])
print("\n")

#Code 8
print("Code 8")
word1 = input("Enter the main word: ")
word2 = input("Enter the letter combination you are looking for you are looking for: ")
for word2 in word1:
    print(True)
print(word1 in word2)
'''

#Code 9
print("Code 9")
word = input("Enter a word: ")
if word.isalnum:
    print("Yes")
else:
    print("Nope")










