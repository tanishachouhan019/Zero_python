#print("Hello python")
#var = 23


#comments#3 types of naming
#empolye0ne = 1 #camel case
#Employe0ne = 2 #pascal case
#employe_one = 3 #snake case

#data types

#1numbers - int float complaax
#2strings - str#
#3- boolean

#a= 12
#print(type(a))

#b = 0.9
#print(type(b))

#c=5/7
#print(type(c))

#a = 12j
#print(type(a))

#str
#name = "abc#$23340" 
#print(type(name))

#boolean
#a = True
#print(type(a))

#age = input("what is your age - ")
#print("how are you")

#practice que---------------

#ask for numbers
#num = input("please proived a number - ")
#print(num)
#type convestion
#1. int()
#2. float()
#3. str()
#4. bool()

#a = "12"
#a = int(a)
#print(a)

#a ="HELLO"
#print(a[3])

#if you have a string and inside that string you have integer then you can use the int() function
#and if you have a string and inside and you have decimal or fraction value then should be use float() functions

#a = 12
#a = float(a)

#print(a)

#bool()

#0,false.0.0,"",{},[],{}

a = 7
b = 0.0
c = ""
d = {}
e = []
f = False 

#print(bool(a))
#print(bool(b))
#print(bool(c))
#print(bool(d))
#print(bool(e))
#print(bool(f))

#name = input("please tell your name")
#age = int(input("now tell your age"))
#print(f"your name is {name} and your {age}")

#operaters

#arithematic oprators (+,_,/,*,//,**,%)
#assignment operators
#comparison operators
#logic operators

#print(a + b)
#print(a - b)
#print(a * b)
#a = 12.5
#b = 8
#print(a + b )
#a = 20
#b = 5
#print(a / b)
#print(a // b)
#print(a * 8 * b)
#print(a % b)

#BODMAS - brakets of division multipication addition substraction
#print((10 + 20) * 2)#

#p = float(input("tell your principle amount:"))
#r = float(input("tell your rate of intrest:"))
#t = float(input("tell your time in years:"))
#simple interest
#si =( p * r * t) / 100
#print(f"your simple insterest will be {si}")
# compound interest
#ci = (p * (1 + (r / 100))** t)
#print(f"your compound interesrt will be{ci - p}")

#comparision oprators
#( < , > , <= , >= , != , == )
#THIS OPERTAORS COMPARES TWO THINGSS AND THEY WILL ALWAYS PRODUCE REAULTS IN BOOLEN
#print(12 == 12)
#print(12< 12.1)

##logical operaators - (and , or , not)#

#print(12 == 13, 56 == 56)
##print(12 == 12 and 56 == 56 and 44 == 44 and 12< 3 )
##all the oprations must be true if a single opration is false result is also going to be false
#print(12 > 34 or 13 == 45 or 56 == 78 or 12 == 12)
#all are false then false,if one going to be true then must be true 
#if any one of the opration is true the whiole result will be true
#print(not 12 == 12)
##converts true to false , flase to true

#control flow - if else , loops , functions
#if 
#age = int(input("entre your age! - "))
#if True:

#    print("my if statment is true")

#if age >= 18:
#    print("you can vote")

#if age < 18:
#    print("you cannot vote")

#if else
#if age >= 18:
#    print("you can vote")
#else:
#    print("you cannot vote")


#elif
#a)10 b)20 c)30 d)40
#ans = input("select one option")
#if ans == "a":
#    print("a is wrong answer")
#elif ans == "b":
#    print("b is weong answer")
#elif ans == "c":
#    print("c is wrong answer")
#if ans == "d":
#    print("d is correct answer")



#problem sloving
#a = int(input("entre a number"))
#b = int(input("entre another number"))
#if a > b:
#    print("a is greater then b")
#elif b > a:
 #   print("b is greater than a")
#else:
#    print("both are equal")

#--------------#
# gen = input("plase tell your gender as char(M or F)")
# if gen == "M" or gen == "m"
#     print("good moring sir")
# elif gen == "F" or gen == "f":
#      print("good moring mam")
#
# else:
#     print("unknown gender"#


#------------------
#a = int(input("entre a even number"))
#if a % 2 == 0:
#    print("number is even")
#else:
#    print("your number is odd")
# #-----------------------

#name = input("please tell your name ")
#age = int(input("please tell your age"))

#if age >=18:
#    print(f"Hello {name} you are a valid voter")
#else:
#    print(f"Hello {name} you are not a valid voter you can vote after {18 - age} years")

#num = int(input("entre a number"))
#if num >= 10 and num <= 50:
#    print("your number is bw 10 and 50")
#else:
#    print("your number is out of range")

#m = int(input("entre your score"))
#e = int(input("entre your score"))
#if m >= 40 and e >= 40:
#    print("you passed")
#elif m >= 80 and e >= 80:
#    print("you passed")
#else:
#    print("you failed")

#short
#if (m >= 40 and e >= 40) or (m >= 80 or e >= 80):

#chr = input("please tell your character :- ")
#if chr == "a" or chr == "e" or chr == "i" or chr == "o" or chr =="u":
#    print("its a vowel")
#else:
#    print("consonent")

#short - if che in "AEIOUaeiou":
#in - it is used in loops

#year = int(input("please tell your year :-"))
#if year % 100 == 0 and year % 400 == 0:
#    print("your year is a leap year")
#elif year % 100 != 0 and year % 4 == 0:
#    print("your year is a leap year")
#else:
#    print("its a normal year")

#num = int(input("entre a number"))
#if num % 3 == 0 and num % 5 == 0:
#    print("number is special")
#elif num % 7 == 0 and num % 10 != 0:
#    print("its a special number")
#else:
#    print("not a special number")

#strings---
#a = "hello"
#print(a[3])
#print(a[4] , a[-1])

#s ="hello how are you"
#print(s[6:9])
#print(s[14:])

#print(ord("A"))
#print(ord("a"))

#string slicing [ start, stop, steps]
#str = "SHERYIANS"
#print(str[0:4:1])
#print(str[0:4:2])
#print(str[0:4:3])
#print(str[::])

#unicode
#print(ord("A"))

#c = input("give me a character")
#value = ord(c)
#if value >=65 and value <= 90:
#    print("its is an alphabets")
#elif value >= 97 and value <= 122:
#    print("its an alphabet")
#else:
#    print("its not an alphabet")

#loops
#for i in range(1,11,1):
#    print(i)

#for i in range(50,151):
#    print(i)

#for i in range(20,31):
#    print(i)

#for i in range(-12,11):
#    print(i)

#for i in range(10,-11,-1):
#    print(i)



#for i in range(5,51,5):
#    print(i)

#n = int(input("entre a number"))

#for a in range(n, a*10+1, n):
#    print(i)

#for i in range(100):
#    print("hello world")

#n = int(input("tell your stop point"))

#for i in range(1 , n+1):
#    print(i)

#indentation:

#n = int(input("entre a number -"))
#for i in range(n,0,-1):
#    print(i)

#n = int(input("entre a number"))
#for i in range(1,11):
#    print(f"{n} * {i} = {n * i}")


#n = int(input("entre a number"))
#a = 0
#for i in range(1,n+1):
#    a = a + i
#    print(a)

#n = int(input("which number factorial you want "))
#fact = 1
#for i in range(1,n+1):
#    fact = fact* i
#    print(fact)
    

# n = int(input("please tell your number"))
#sum = 0
#for i in range(1,n+1):
#    sum = n + i
#    print(sum)


#n = int(input("entre a number"))
#a = 1
#for i in range(2,n + 1, 2):
#    
#    print(a)

#n = int(input("entre a number"))
#a = 1
#for i in range(0,10,1):
#    print(a)

#n = int(input("give me a number"))
#for i in range(1,n +1):
#    if i % 2 == 0:
#        print(f"{i} is even")
#    else:
#        print(f"{i} is odd")

#n = int(input("entre a no"))
#even_sum = 0
#odd_sum = 0
#for i in range(1, n+1):
#    if i % 2 == 0:
#       even_sum = even_sum + i
#    else:
#        odd_sum = odd_sum + i

#        print(f"even sum is {even_sum}and odd sum is {odd_sum}")


#factor
#n = int(input("which no. factor you want"))
#for i in range(1, n+ 1):
#    if n % i == 0:
#        print(i)
#---------------------------
#n = int(input("entre a number"))
#for i in range(1,n +1,-1):
#print(i)

#n = int(input("entre a number"))
#for i in range(1, n+1):
#    if n % i == 0:
#        print(i)

"""n = int(input("entre a number"))
sum = 0
for i in range(1,n):
    if n %i == 0:
        print(i)
        sum = sum + i
if sum == n:
      print(f"your number {n} is perfect")
else:
     print(f"{n} not a perfect number")"""




'''n = int(input("entre a  number"))
count= 0

for i in range(1, n+1):
    if n % i == 0:
        count = count + 1
        print(i)
if count == 2:
    print("my number is prime ")
else:
    print("composite number")'''

#break,else,continue

'''n = int(input("entre a  number"))
for i in range( 2, (n //2)+1):
    if n%i == 0:
        print("your no. is not prime")
        break

else:
    print("your no. is prime")'''

    
'''n = int(input("please tell your number : ")) # 5


sum = 0
for i in range(1,n+1):
    sum = sum + i


print(sum)'''


'''n = int(input("which number factorial you want :- "))

fact = 1

for i in range(1,n+1):
    fact = fact * i

print(fact)'''

'''for i in range(1,21):
    if i == 5:
        break

    print(i)

for i in range(1,21):
    if i == 5:
        continue

    print(i)

n = int(input("tell me a no."))

for i in range(2,n//2+1):
    if n % i == 0:
        print("your number is composite")
        break
else:
    print("your number is prime")'''

'''a = 10

while a > 0:
    print(a)
    a = a - 1'''

'''a = 123637389

while a > 0:
    print(a % 10)
    a = a // 10'''

#sum of all digits
'''n = int(input("tell me a number"))
sum = 0
while n != 0:
    sum = sum + (n % 10)
    n = n // 10

print(sum)'''

# que reverse a number
'''n = int(input("entre a number"))
rev = 0
while n !=0:
    rev = rev * 10 + (n%10)
    n = n // 10

print(rev)

n = int(input("entre a number"))
copy = n
rev = 0
while n != 0:
    rev = rev * 10 + n%10
    n = n // 10

if rev == copy:
    print("palindrome")
else:
    print("not palindrome")'''


#powersession

#take a digit input from user and reverse it using for loop
'''n = (input("entre your digit"))
print(n[::-1])

n = int(input("entre your digit"))
sum = ""
for i in str(n)[::-1]:

    sum = sum + i
    print(sum)'''

'''for i in range(1,6,1):
    print('hello world')

print("hellp world\'5")

#fibonacci series upto N terms
n = int(input("entre your series no."))
a = 0
b = 1
for i in range(n):
    print(a)
    a , b = b , a + b

# print the lagrest digit in a number
n = 4289
largest = 0
for i in str(n):
    a = int(i)
    if a > largest:
        largest = a
print(largest)'''

#guessing game(user guess a no. untill corect)
'''import random

praveshika = random.randint(1,50)
for i in range(5):
    tanisha = int(input("entre your number"))

    if tanisha == praveshika:
        print('you won')
        break

    if tanisha < praveshika:
        print("too small go higher")

    if tanisha > praveshika:
        print("too high values go for lower")

else:
    print(f"didi haar gaye, number hai{praveshika}")'''

#check weather a number pallindrome or not
'''num = 121
if str(num) == str(num)[::-1]:
    print(f'number {num} is pallindrome')
else:
    print(f'number {num} is not pallindrome')'''

# keep taking input until user enters 0, then print sum
sum = 0
while True:
    n = int(input("entre a number"))

    if n == 0:
        break
    sum += n 
print(sum)

# reverse anumber using while loop
n = 8934
rev = 0
while n !=0:
    rev = rev * 10 + (n%10)
    n = n // 10

print(rev)

#count number

#armstrong number
n = 153
copy = n
length = len(str(n))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit**length
    n = n // 10
if copy == sum :
    print("amrstrong no.")
else:
    print("not an amrstrong no.")
