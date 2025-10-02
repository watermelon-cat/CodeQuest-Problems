case = int(input())
YinYang = " "
Element = ["Wood", "Fire", "Earth", "Metal", "Water"]
Animal = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
for i in range(case):
    year = int(input())
    if year % 2 == 0:
        YinYang = "Yang"
    else:
        YinYang = "Yin"

    yearEle = year
    yearEle = yearEle - 4
    yearEle = yearEle % 10
    yearEle = yearEle // 2


    year = year - 4
    year = year % 12

    print(YinYang, Element[yearEle], Animal[year])

