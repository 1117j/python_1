
money = 1000
rate = 0.0075

count = 1

for x in range(1,11):

    count += 1
    money = money + (money*rate)
    print(x, money)




