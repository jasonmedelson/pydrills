name = "Jason"  # step 2
age = 21 #step 1
height = 69.5 # step 3
print("Hello, my name is {}, I am {} years old and {} inches tall.".format(name,age,height)) #step 4
num = raw_input("please enter an integer: ")
num = int(num)
plus = num + 5 # step 5
minus = num - 5 # step 5
mult = num * 5 # step 5
div = num / 5 # step 5
mod = num % 5 # step 5
print("Your number has been altered by 5, add:{}, subtract:{}, muliply:{}, divide:{}, modulo:{}".format(plus,minus,mult,div,mod))
def strReturn(): # step 12
    f_name = ["Obi Wan","Anakin","Luke","Mace","Han","Yoda", "Darth"]
    l_name = ("Kenobi","Skywalker", "Solo", "Windu", "Urso", "Ren")
    print "Hello this is the Jedi Name Generator"
    seed = raw_input("Enter any amount of random characters: ")
    seed = len(seed)
    print "possible first name choices: \n"
    i = 0
    for each in f_name: #step 9&10
        print each
        print "\n"
        i += 1 # step 5 done
    print "possible last name choices: \n"
    for people in l_name: #step 11
        print people
        print "\n"
    print "Generating jedi name now".upper()
    f_seed = seed%len(f_name)
    j = 0
    count = seed
    while j < count: #step 8
        seed += j
        j += 1
    l_seed = seed%len(l_name)
    if f_name == "Anakin" and l_name == "Skywalker": # step 6&7
        print "You are the most powerful Jedi"
    elif f_name == "Obi Wan" or f_name == "Mace": # step 6&7 
        print "You are a very strong Jedi"
    elif f_name == "Darth" and not l_name == "Skywalker": # step 6
        print "The dark side is strong with this one"
    else: # step 7
        print "You are the first Jedi of your kind"
    print("\nYour Jedi name is: \n{} {}".format(f_name[f_seed],l_name[l_seed]))
    
strReturn() #step 13 
