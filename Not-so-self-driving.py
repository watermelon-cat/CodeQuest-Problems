test = int(input())
for i in range(test):
    car = []
    car = input()
    collen = car.find(":")
    speed = float(car[0 : collen])
    obs = float(car[collen+1:])
    
    if (obs - speed) <= 0:
        print("SWERVE")
    elif (speed * 5) > obs:
        print("BRAKE")
    else:
        print("SAFE")
