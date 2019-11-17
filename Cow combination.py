
adj1s = sorted(["large", "small"])
adj2s = sorted(["white", "brown", "spotted"])
adj3s = sorted(["noisy", "silent"])


class Cow:
    def __init__(self, param1, param2, param3):
        if param1 not in adj1s:
            raise Exception('The first adjective must be in {items}'.format(items=adj1s))
        self.adj1 = param1
        if param2 not in adj2s:
            raise Exception('The second adjective must be in {items}'.format(items=adj2s))
        self.adj2 = param2
        if param3 not in adj3s:
            raise Exception('The third adjective must be in {items}'.format(items=adj3s))
        self.adj3 = param3

    #def __str__(self):
      #  return "{adj1}, {adj2}, {adj3}".format(adj1=self.adj1, adj2=self.adj2, adj3=self.adj3)

    def __eq__(self, other):
        return self.adj1 == other.adj1 and self.adj2 == other.adj2 and self.adj3 == other.adj3


allCows = []

for adj1 in adj1s:
    for adj2 in adj2s:
        for adj3 in adj3s:
            allCows.append(Cow(adj1, adj2, adj3))

excludeCows = []

while True:
    adjstr = raw_input("what kind of cow do farmer John don't have(press 'return' to finish) : ")
    if adjstr == "":
        break

    try:
        adjs = adjstr.split(",")

        if len(adjs) < 3:
            raise Exception("They need to be 3 adjectives")

        excludeCows.append(Cow(adjs[0], adjs[1], adjs[2]))

    except Exception as e:
        print e.message
        continue

cows = filter(lambda x: x not in excludeCows, allCows)

print cows;

while True:
    indexstr = raw_input("Do you want to know which cow's adjectives(press 'return' to finish ):")
    if indexstr == "":
        break
    try:
        index = int(indexstr)
        print"NO.{index} cow's adjectives are {cow}".format(index=index, cow=cows[index-1])
    except Exception as e:
        print e.message
