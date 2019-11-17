def stringToInt(num):
    return int(num)


how_many_cows = 0


while True:
    number = raw_input("please determine how many cows are there : ")
    try:
        how_many_cows = stringToInt(number)
        break
    except Exception as e:
        print("please input a NUMBER")
        continue

cowBestTemp = [[0, 0]] * how_many_cows

for i in range(0, how_many_cows):
    while True:
        try:
            tempPrint = "please determine the No.%s cow's comfortable temperature : " % (i + 1)
            temp = raw_input(tempPrint)
            temprange = temp.split("-")
            if len(temprange) != 2:
                raise Exception("please type TWO number SEPERATELY using '-', ex:1-100")
            intrange = map(stringToInt, temprange)
            if intrange[0] > intrange[1]:
                raise Exception("the first number(lowest temperature afford) must be smaller than "
                                "the second number(highest temperature afford)")
            if intrange[0] < 0:
                raise Exception("the lowest temperature must be equal or larger than 0")
            if intrange[1] > 1000000000:
                raise Exception("the highest temperature must be equal or smaller than 0")
            cowBestTemp[i] = intrange
            break
        except Exception as e:
            print(e)
            continue

too_cold_milk_amount = 0
too_hot_milk_amount = 0
comfortable_milk_amount = 0

while True:

    try:
        too_cold_milk_amount = stringToInt(raw_input("please input the amount of milk the cows will produce when "
                                                     "it's too cold : "))
        comfortable_milk_amount = stringToInt(raw_input("please input the amount of milk the cows will produce when "
                                                        "it's just right : "))
        too_hot_milk_amount = stringToInt(raw_input("please input the amount of milk the cows will produce when "
                                                    "it's too hot : "))


        if too_hot_milk_amount >= comfortable_milk_amount or too_cold_milk_amount >= comfortable_milk_amount:
            raise Exception("the cow will produce the most milk when the temperature is just right for him")
        break
    except Exception as e:
        print(e.message)
        continue

result = [[0, 0]] * 101

produce_milk_amount = 0
for i in range(0, 101):
    produce_milk_amount = 0
    for j in cowBestTemp:
        rangeMin = j[0]
        rangeMax = j[1]
        if i < rangeMin:
            produce_milk_amount += too_cold_milk_amount
        if i > rangeMax:
            produce_milk_amount += too_hot_milk_amount
        if rangeMin <= i <= rangeMax:
            produce_milk_amount += comfortable_milk_amount
    result[i] = [i, produce_milk_amount]


def amount(array):
    return array[1]
def temperature(num):
    return lambda a: a[1] == num


max_milk_amount = max(map(amount, result))

#print("temperature when you can get the most milk produced : %s" %(filter(temperature(max_milk_amount)),result))

resultstr = "most milk possibly produced: %s" % max_milk_amount

print(resultstr)

for i in result:
    if i[1] == max_milk_amount:
        print("%s celsius degree" %i[0])


# tempRange = raw_input("").split(",")
# print(cowBestTemp)
