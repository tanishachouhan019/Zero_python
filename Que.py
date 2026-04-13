#input & output-----------------------------
#ask the user to entre their name and print : Welcome [name]!18
#name = input("entre your name ")
#print(f"welcome {name}")

#ask the user to entre their agr and print : you are [agr]years old
#age = input("entre their age")
#print(f"You are {age} years old")

#ask the user to entre their city and print : I live in [city]
#city = input("enter their city")
#print(f"I live in {city}")

#colour = input("enter their favourite colour")
#print(f"My favourite colour is {colour}")

#firstname = input("entre firstname")
#lastname = input("enter lastname")
#print(f"full name: {firstname} {lastname}")

#firstname/lastname = input("entre firstname/lastname")


#number = input("entre their phone number")
#print(f"My number is{number} ")

#school = input("entre their schooL,name")
#print(f"I study at {school}")

#food = input("entre their favourite food")
#print(f"I love eating {food} ")

#country =input("entre their county")
#print(f"I am from {country} ")

#name2 =input("entre their pet name")
#print(f"My pet's name is {name2}")

#subject = input("entre their favourite sunject")
#print(f"My favourite subject is {subject}")

#name3 = input("entre thire frirnd's name")
#print(f"My bestfeirnds name is {name3}")

#hobby = input("entre their hobby")
#print(f"I enjoy {hobby} in my free time")

#email = input("entre thir email")
#print(f"Your email is {email}")

#moive = input("entre their favourite moive")
#print(f"My favourite moive is {moive}")

#ARITHMATIC OPERATORS--------------------
#a = float(input("entre a number here: "))
#b = float(input("entre another number here: "))
#sum = a + b
#print(sum)

#c = float(input("entre a number "))
#d = float(input("entre another number here "))
#print("Differnce =", c - d)

#e = float(input("entre a number here "))
#f = float(input("entre another number here "))
#print("product = ", e * f)

#g = float(input("entre a number here"))
#h = float(input("entre a number"))
#print("Divison =", g / h)

#i = float(input("entre a number here"))
#j = float(input("entre another number here"))
#print("Remainder =",i % j)

#k = float(input("entre base"))
#l = float(input("entre exponent"))
#print("Result =", k ** l)

#m = float(input("entre a number here"))
#n = float(input("entre another number here"))
#print("Floor division =", m // n)

#o = float(input("entre a numbere here"))
#print("Square =", o ** 2)

#p = float(input("entre a number here"))
#print("Cube =", p ** 3)

#s = float(input("entre first number"))
#t = float(input("entre sencond number"))
#print("sum =", s + t)
#print("diffrence =", s - t)
#print("product =", s * t)
#print("division =", s / t)

#-----------------

#a = float(input("entre a number"))
#if a > 0 :
#    print("positive")
#else:
#    print("negative")

#num = float(input('entre a number'))
#if num < 0 :
#    print("negative")
#else:
#    print("postive")

#b = float(input("entre a number"))
#if b > 10:
#    print("print gater than 10")

#c = float(input("entre a number"))
#if c == 0:
#    print("zero")

#d = float(input("entre a number"))
#e = float(input("entre a another number"))
#if d > e :
#    print(f"{d} is grater")
#else:
#    print(f"{e} is smaller")

#age = int(input("entre your age"))
#if age >+ 18:
#    print("eligible")
#else:
#    print("not eligible")

#num = int(input("entre a number"))
#if num / 5:
#    print("divisible" )
#else:
#    print("not divisible")

#num = int(input("entre a number"))
#if num % 2 == 0 and num % 3 == 0:
#    print("divisble by 2 or 3")
#else:
#    print("not divisble")

#marks = int(input("entre marks"))
#if marks >= 40:
#    print("pass")
#else:
#    print("fail")

#num = int(input("entre a number "))
#if 1 <= num <= 100:
#    print("in range")
#else:
#    print("out of range")

#temp = float(input("entre temp"))
#if temp >30:
#    print("hot")
#else:
#    print("cool")

#num = int(input("entre a number"))
#if num % 10 == 0:
#    print("mutiple of 10")
#else:
#    print("not mutiple of 10")

#num = int(input("entre a number"))
#if num > 0:
#    print("positive")
#elif num < 0:
#    print("negative")
#else:
#    print("zero")

#slicing strings------------------------
#a = "hello"
#print(a[0])

#b = "world"
#print(b[4])

#c = "python"
#print(c[1])

#d = "coding"
#print(d[0:3])

#e = "python"
#print(e[0:5:2])

#f = "coding"
#print(f[2:])

#g = "computer"
#print(g[0:5])

#h = "program"
#print(h[4:])

#i = "python"
#print(i[1:5])

#j ="hello"
#print(j[::-1])

#loops---------------
#1.for loop
#for i in range(1,6):
#    print(i)

#for i in range(1,11):
#    print(i)

#for i in range(1,11):
#    if i % 2 == 0:
#        print(i)

#for i in range(1,11,2):
#    print(i)

#for i in range(10,0,-1):
#    print(i)

#n = int(input("entre a number"))
#for i in range(1,11):
#    print(f"{n} * {i} = {n * i}")

#-----------------------
#n = int(input("entre a number"))
#for i in range (1 , n + 1):
#    print(i, end="")

#num = int(input("entre a number"))
#total_sum = sum(range(1, num + 1))
#print(f"sum = {total_sum}")

#n = int(input("which number factoral you want"))
#fact = 1
#for i in range(1,n+1):
#    fact = fact * i
#    print(fact)

#n = int(input("please tell me a number"))
#for i in range(1,n+1):
#    if i % 2 == 0:
#        print(i)



#num = int(input("entre a number"))
#for i in range(1,n+1):
#    if i % 2 != 0:
#        print(i)

#n = int(input("please tell a number"))
#for i in range(5, n+1,5):
#    print(i)
    

#n = int(input("please tell me a number"))
#evensum = 0
#for i in range(2,n+1,2):
#     evensum = evensum + i
#     print("sum =", evensum)

#n = int(input("which no you want sq"))
#product = 1
#for i in range(1,n+1):
#        product = n * i
#        print("product =",product)

#n = int(input("which number you want to product"))
#product = 1
#for i in range(1, n +1):


'''n = int(input("tell your number :- "))
evensum = 0 
oddsum = 0 
for i in range(1,n+1):
    if i % 2 == 0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i

print(f"even sum is {evensum} and odd sum is {oddsum}")


#taking an input 
n = int(input("which number factors you want :- "))

#accessing all the numbers below n 
for i in range(1,n+1):
    if n % i == 0:
        print(i)'''
#--------------------------------------
'''a = "121"
b = ""
for i in range(len(a)-1,-1,-1):
     b = b + a[i]

print(b)
if b == a:
     print("pallimdrome")
else:
     print("not pallindrome")'''

n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is prime")

'''n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)'''

'''n = int(input("entre a number"))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i , end="")'''