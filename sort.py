def bubble(unsorted):
    print("Unsorted list equals:\n",unsorted)
    for num in range(len(unsorted)-1):
        for place in range(len(unsorted)-1):
            if(unsorted[place] > unsorted[place+1]):
               holder = unsorted[place + 1]
               unsorted[place + 1] = unsorted[place]
               unsorted[place] = holder
        #print(unsorted)
    print("Sorted list with bubble sort equals:\n",unsorted)
    return (unsorted)
bubble([89, 23, 33, 45, 10, 12, 45, 45, 45])
bubble([67, 45, 2, 13, 1, 998])

def radix(unsorted):
    print("Unsorted list equals:\n",unsorted)
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
            #print (cycle)
            divisor = 10 ** (cycle-1)
            #print (unsorted[num])
            if(int((unsorted[num]%modnum)/(divisor)) == 0):
                zero.append(unsorted[num])
                #print ("append zero")
            elif(int((unsorted[num]%modnum)/(divisor)) == 1):
                one.append(unsorted[num])
                #print ("append one")
            elif(int((unsorted[num]%modnum)/(divisor)) == 2):
                two.append(unsorted[num])
                #print ("append two")
            elif(int((unsorted[num]%modnum)/(divisor)) == 3):
                three.append(unsorted[num])
                #print ("append three")
            elif(int((unsorted[num]%modnum)/(divisor)) == 4):
                four.append(unsorted[num])
                #print ("append four")
            elif(int((unsorted[num]%modnum)/(divisor)) == 5):
                five.append(unsorted[num])
                #print ("append five")
            elif(int((unsorted[num]%modnum)/(divisor)) == 6):
                six.append(unsorted[num])
                #print ("append six")
            elif(int((unsorted[num]%modnum)/(divisor)) == 7):
                seven.append(unsorted[num])
                #print ("append seven")
            elif(int((unsorted[num]%modnum)/(divisor)) == 8):
                eight.append(unsorted[num])
                #print ("append eight")
            elif(int((unsorted[num]%modnum)/(divisor)) == 9):
                nine.append(unsorted[num])
                #print ("append nine")
            else:
                print("error: ", unsorted[num])
        emptyArray = []
        if (len(zero) == len(unsorted)):
            repeat = False
        if (len(zero)!= 0):
            for x in zero:
                emptyArray.append(x)#1
                #zero.remove(x)
                #print(x," removed")
            #print (zero)
        if (len(one)!= 0):
            for x in one:
                emptyArray.append(x)#2
                #one.remove(x)
            #print (one)
        if (len(two)!= 0):
            for x in two:
                emptyArray.append(x)#3
                #two.remove(x)
                #print(x," removed")
            #print (two)
        if (len(three)!= 0):
            for x in three:
                emptyArray.append(x)#4
                #three.remove(x)
                #print(x," removed")
            #print (three)
        if (len(four)!= 0):
            for x in four:
                emptyArray.append(x)#5
                #four.remove(x)
                #print(x," removed")
            #print(four)
        if (len(five)!= 0):
            for x in five:
                emptyArray.append(x)#6
                #five.remove(x)
                #print(x," removed")
            #print(five)
        if (len(six)!= 0):
            for x in six:
                emptyArray.append(x)#7
                #six.remove(x)
                #print(x," removed")
            #print(six)
        if (len(seven)!= 0):
            for x in seven:
                emptyArray.append(x)#8
                #seven.remove(x)
                #print(x," removed")
            #print(seven)
        if (len(eight)!= 0):
            for x in eight:
                emptyArray.append(x)#9
                #eight.remove(x)
                #print(x," removed")
            #print(eight)
        if (len(nine)!= 0):
            for x in nine:
                emptyArray.append(x)#10
                #nine.remove[x]
                #print(x," removed")
            #print (nine)
        zero.clear()
        one.clear()
        two.clear()
        three.clear()
        four.clear()
        five.clear()
        six.clear()
        seven.clear()
        eight.clear()
        nine.clear()
        unsorted = emptyArray        
        cycle += 1
        #print(unsorted)
    print("Sorted list with radix sort equals:\n",unsorted)
radix([67, 45, 2, 13, 1, 998])
radix([89, 23, 33, 45, 10, 12, 45, 45, 45])


