def stingToInt(num):
    return int(num)


maxNumber = 0

while (True):
    number = raw_input("please input number : ")
    try:
        maxNumber = stingToInt(number)
        break
    except Exception as e:
        print("please INPUT a NUMBER")
        continue

farmerKey = [0, 0, 0]

while (True):
    try:
        passwordOfFarmer = raw_input("please set up the password of farmer : ")
        passwordArray = passwordOfFarmer.split(",")
        if len(passwordArray) != 3:
            raise Exception("please type THREE number SEPERATELY")
        for i in range(0, len(passwordArray)):
            farmerKey[i] = stingToInt(passwordArray[i])
            if farmerKey[i]>maxNumber:
                raise Exception("You can't write a number that's bigger than your lock's digit")
        break
    except Exception as e:
        print(e)
        continue

makerKey = [0, 0, 0]

while (True):
    try:
        passwordOfMaker = raw_input("please set up the password of maker : ")
        passwordArray = passwordOfMaker.split(",")
        if len(passwordArray) != 3:
            raise Exception("please type THREE number SEPERATELY")
        for i in range(0, len(passwordArray)):
            makerKey[i] = stingToInt(passwordArray[i])
            if makerKey[i]>maxNumber:
                raise Exception("You can't write a number that's bigger than your lock's digit")
        break
    except Exception as e:
        print(e)
        continue

print(maxNumber)
print(farmerKey)
print(makerKey)

matchCount = 0
for i in range(1, maxNumber+1):
    for j in range(1, maxNumber+1):
        for k in range(1, maxNumber+1):
            count = 0
            x1 = farmerKey[0]
            x2 = farmerKey[1]
            x3 = farmerKey[2]
            if abs(i - x1) <= 2 or abs(i - x1) >= maxNumber-2:
                count = count + 1
            if abs(j - x2) <= 2 or abs(j - x2) >= maxNumber-2:
                count = count + 1
            if abs(k - x3) <= 2 or abs(k - x3) >= maxNumber-2:
                count = count + 1
            y1 = makerKey[0]
            y2 = makerKey[1]
            y3 = makerKey[2]
            makerCount = 0
            if abs(i - y1) <= 2 or abs(i - y1) >= maxNumber-2:
                makerCount = makerCount + 1
            if abs(j - y2) <= 2 or abs(j - y2) >= maxNumber-2:
                makerCount = makerCount + 1
            if abs(k - y3) <= 2 or abs(k - y3) >= maxNumber-2:
                makerCount = makerCount + 1
            if makerCount >= 3 or count >= 3:
                print(i,j,k)
                matchCount = matchCount + 1
print(matchCount)