ways = 0
for a in range(3):
    for b in range(int(1+(200-a*100)/50)):
        for c in range(int(1+(200-a*100-b*50)/20)):
            for d in range(int(1+(200-a*100-b*50-c*20)/10)):
                for e in range(int(1+(200-a*100-b*50-c*20-d*10)/5)):
                    for f in range(int(1+(200-a*100-b*50-c*20-d*10-e*5)/2)):
                            ways += 1
ways += 1
print("There are %s different ways to make 2 pounds with coins"%ways)
