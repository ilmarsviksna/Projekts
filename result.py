month = input("Kuru menesi parbaudit?")
with open("data.csv","r") as f:
    next(f)
    next(f)
    paradnieki=[[]]
    for line in f:
        row=line.rstrip().split(",")
        if (row[int(month)] != "7"):
            temp = []
            temp.append(row[0])
            parads = 0
            for x in range(1, int(month)):
                 parads = parads + int(row[x])
            parads = 7 * int(month) - parads
            temp.append(parads)
            paradnieki.append(temp)
if bool(paradnieki):
    print("Nav paradnieku")
else:
    print(paradnieki)
