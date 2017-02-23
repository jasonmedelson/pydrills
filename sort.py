def bubble(unsorted):
    print("Unsorted list equals:\n",unsorted)
    for num in range(len(unsorted)-1):
        for place in range(len(unsorted)-1):
            if(unsorted[place] > unsorted[place+1]):
               holder = unsorted[place + 1]
               unsorted[place + 1] = unsorted[place]
               unsorted[place] = holder
        #print(unsorted)
    print("Sorted list equals:\n",unsorted)
    return (unsorted)
bubble([89, 23, 33, 45, 10, 12, 45, 45, 45])
bubble([67, 45, 2, 13, 1, 998])

def radix(unsorted):
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    repeat = True
    cycle = 1
    while repeat:
        for num in range(len(unsorted)):
            modnum = 10 ** cycle
            print (modnum)
            divisor = 10 ** (cycle-1)
            print(divisor)
            print (unsorted[num])
            print (unsorted[num]%modnum)
            print ((unsorted[num]%modnum)/(divisor))
            if(((unsorted[num]%modnum)/(divisor)) == 0):
                zero.append(unsorted[num])
                print ("append zero")
            elif(((unsorted[num]%modnum)/(divisor)) == 1):
                one.append(unsorted[num])
                print ("append one")
            elif(((unsorted[num]%modnum)/(divisor)) == 2):
                two.append(unsorted[num])
                print ("append two")
            elif((unsorted[num]%modnum)/(divisor) == 3):
                three.append(unsorted[num])
                print ("append three")
            elif((unsorted[num]%modnum)/(divisor) == 4):
                four.append(unsorted[num])
                print ("append four")
            elif((unsorted[num]%modnum)/(divisor) == 5):
                five.append(unsorted[num])
                print ("append five")
            elif((unsorted[num]%modnum)/(divisor) == 6):
                six.append(unsorted[num])
                print ("append six")
            elif((unsorted[num]%modnum)/(divisor) == 7):
                seven.append(unsorted[num])
                print ("append seven")
            elif((unsorted[num]%modnum)/(divisor) == 8):
                eight.append(unsorted[num])
                print ("append eight")
            elif((unsorted[num]%modnum)/(divisor) == 9):
                nine.append(unsorted[num])
                print ("append nine")
            else:
                print("error: ", unsorted[num])
        emptyArray = []
        if len(zero) == len(unsorted):
            repeat = False
        for x in zero:
            emptyArray.append(x)#1
            #zero.remove(x)
            print(x," removed")
        print (zero)
        for x in one:
            emptyArray.append(x)#2
            one.remove(x)
            #print(x," removed")
        print (one)
        for x in two:
            emptyArray.append(x)#3
            #two.remove(x)
            print(x," removed")
        print (two)
        for x in three:
            emptyArray.append(x)#4
            #three.remove(x)
            print(x," removed")
        print (three)
        for x in four:
            emptyArray.append(x)#5
            #four.remove(x)
            print(x," removed")
        print(four)
        for x in five:
            emptyArray.append(x)#6
            #five.remove(x)
            print(x," removed")
        print(five)
        for x in six:
            emptyArray.append(x)#7
            #six.remove(x)
            print(x," removed")
        print(six)
        for x in seven:
            emptyArray.append(x)#8
            #seven.remove(x)
            print(x," removed")
        print(seven)
        for x in eight:
            emptyArray.append(x)#9
            #eight.remove(x)
            print(x," removed")
        print(eight)
        for x in nine:
            emptyArray.append[x]#10
            #nine.remove[x]
            print(x," removed")
        print (nine)
        print (emptyArray)
        unsorted = emptyArray        
        cycle += 1
        print(unsorted)
radix([67, 45, 2, 13, 1, 998,34,55,100,101,22,15,1142,1104,2,3])
