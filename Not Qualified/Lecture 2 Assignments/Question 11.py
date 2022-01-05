# Male and Female percentages
male = float(input("Enter the number of male students within the class: "))
female = float(input("Enter the number of females students within the class: "))
total = male + female
mp = (male/total)*100
fp = (female/total)*100
print(mp, "percent of the students are male")
print(fp, "percent of the students are female")
