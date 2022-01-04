# Stock Transaction program
print("Joe brought 2000 shares at a rate of $40")
shares1 = 2000*40
commission1 = shares1*0.03
print("Joe brought his shares for", shares1)
print("and at a commission of 3% to the stockbroker he paid", commission1)
print("Two weeks later Joe sold his 2000 shares at a rate of $42.75")
shares2 = 2000*42.75
commission2 = shares2*0.03
print("Joe received", shares2, "after selling")
print("and paid his stockbroker 3% of these sales")
print("Joe paid his stockbroker", commission2)
amount_left = shares1 - commission1
amount_left2 = shares2 - commission2
print("After paying the stock broker when buying the shares. Joe was left with", amount_left)
print("After selling the shares and paying the stock broker, Joe had", amount_left2, "left")
profit = amount_left2-amount_left
print("Joe made a profit of", profit, "dollars")
