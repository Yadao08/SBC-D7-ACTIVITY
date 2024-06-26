# num = input("Bet: ")
# while num != "27":
#     print("You lose")
#     num = input("Bet: ")
# else:
#     print("You won")

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))

# print(num1 + num2)
#FUNCTIONS
'''
def add():
    return 1 + 1     # return use  to hold
# print(add())

def sub():
    print (1 - 1)

num = add()
num2 = sub() # print 0 kay wa nay value nabilin kay na print na daan

print(num)
print(num2)''' #returns none since wala nay value

#FUNCTION PARAMETERS
'''def add(x):
    print(x + 1)
add(1)

def add(x):
    print(x + 1)
i = 142
add(i)

def triangle(b1,b2,g1):
    print(f"{b1} likes {g1}")
    print(f"{b2} likes {g1}")

triangle( g1 ="Marj",b2 = "Bertox", b1 = "Don")'''
#ARGUMENTS
def names(*args):
    for arg in args:
        print(arg)
names ("carlo", "Just", "hansel", "Christina","shamon","Ace")

# def names(name):
#     for n in name:
#         print(n)
# names("tox", "don")

def names(**kwargs): #kwargs applicable for dictionary
    for key, value in kwargs: # 2 iterator which is si key and value
        print(f"{key} -> {value}")
names (Paloma = "Airon", Bubbles = "Daniel")