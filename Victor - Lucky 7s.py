import random
dice1 = random.randint(1, 6)
print(dice1)

dice2 = random.randint(1, 6)
print(dice2)

total = dice1 + dice2
print(total)

money = 15

if total == 7:
    print("You win!!!!! YAY!!!!!")
    money += 4
else:
    money -= 1