
"""for x in range(0,100):
    if (x%3|x%5==0):
        print("The number {0} is fizzbuzz".format(x))
    elif(x%3==0):
        print("The number {0} is fizz".format(x))
    elif(x%5==0):
        print("The number {0} is buzz".format(x))"""
for x in range(0,100):
    print("fizz"*(x%3<1)+"buzz"*(x%5<1) or x)

