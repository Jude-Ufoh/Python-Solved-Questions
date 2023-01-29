# for i in range(4):
#     print('hello')
# print('Thank you very much')


# x = eval(input('Please enter the number of lines: '))
# for i in range(x):
#     print('*'*10)
# a= eval(input('Please put the multiple: '))
# y = eval(input('Please how long are you multiplying: '))
# for i in range(y):
# #     print(a,' x ',i,'=',a*i)
# from random import randint
# for i in range(50):
#     print(randint(3,6))

#-------3.8 no 2--------------
# from random import randint
# x = randint(1,50)
# y = randint(2,5)
# z = x**y
# print(z)
# print('NB: we used x as', x, 'and y as ', y)

#-----------3.8 no 3--------------
# from random import randint
# x = randint(1,10)
# for i in range(x):
#     print('Jude')
# print(x)
#---------------3.8 no 4---------
# from random import randint
# x = randint(5,10)
# y = randint(1,4)
# z = x/y
# print(round(z,2))
#-----------3.8 No 7-----------------------
# x = eval(input('please input x: '))
# y = eval(input('please input y: '))
# z = abs(x-y)/(x+y)
# print(z)
# ---------3.8 n0 8-----------
# x = eval(input('Please enter the number of second: '))
# print('This contains ',x//60,'Minutes and',x%60,'seconds')
# ---------3.8 n09---------------------------------------
# x = eval(input('enter a hour: '))
# y = eval(input('how many hour ahead: '))
# z = x +y
# print('New Hour: ',z%12,"o'clock")

#-------Exercise 4.5--------
# x = eval(input('please enter the length in Centimeter: '))
# if x < 0:
#     print('Sorry this is an invalid entry.')
# else:
#     z= x/2.54
#     print( x,'cm', "is" ,'=',z,'inches' )
#------- Exercise 4.5 no 4____
# x = eval(input('How many credits have you taken: '))
# if x<=23:
#     print('Oh you are a freshman')
# elif x<=53:
#     print('Oh you are a Sophomore')
# elif x<=83:
#     print('Oh you are a Junior')
# else:
#     print('Oh you are a Senior')

#----------exer4.5 no8----------
# x = eval(input('Please input the year: '))
# if (x%4==0 and x%100!=0) or(x%4==0 and x%100==0 and x%400==0):
#     print(x,'is a leap year')
# else:
#     print(x, 'is a not leap year')
#---------exec4.5 no9-----------
# x = eval(input('Please enter the number: '))
# for i in range(2, x):
#     if x%i==0:
#         print(i,end =' ')
#---------Exec 4.5 no10---------
# from random import randint
# d= eval(input('Choose diffuculty Level: '))
# r = eval(input('Choose number of questions: '))
# for i in range(r):
#     x= randint(1,d)
#     y = randint(1, d)
#     opr=randint(1,3)
#     if opr ==1:
#         t= "+"
#         corr = x+y
#     elif opr ==2:
#         t= "-"
#         corr = x - y
#     else:
#         t="*"
#         corr = x*y
#     print('Question ',i+1,':', x,t,y,'=',end= " ")
#     ans =eval( input(''))
#     if ans == corr:
#         print('Right!')
#     else:
#         print('Wrong. The answer is',corr );

#----------no11 exer 4.5------
# x= eval(input('Enter Hour: '))
# y = eval(input('What period: '))
# if y==1:
#     char='am'
# elif y==2:
#     char ='pm'
# z= eval(input('How many Hours ahead: '))
# a= (x+z)//12
# b= (x+z)%12
# print('You are leaving by ',x,char)
# if(a%2!=0) and y==1:
#     print('New Hour :', b,'pm')
# elif(a%2!=0) and y==2:
#     print('New Hour :', b,'am')
# else:
#     print('New Hour :', b,char)

#-------no 12 exercise4.5 ----------
# for i in range(200):
#     if (i%5==2) and (i%6==3) and (i%7==2):
#         print(i)

#------n0
#
# x = eval(input('Enter hour: '))
# y = eval(input('enter 1 for am or 2 for pm'))
# if y == 1:
#  char='am'
#  inv_char ='pm'
# elif y==2:
#     char='pm'
#     inv_char='am'
# z= eval(input('How many hours ahead:'))
# print('the current time is ',x,char)
# a= x+z
# if a//12==0:
#     print('the current time is ',a%12,char)
# else:
#     print('the current time is ',a%12, inv_char)

#----------
# sum =0
# for i in range(6):
#     sum=sum+i
# print(sum)

#------------------------

# x = eval(input('Please enter the number: '))
# sum = 0
# for i in range(2, x):
#     if x%i==0:
#         sum=sum+i
#         print(i,end =' ')
# print()
# print('the sum of the numbers is ',sum, end=' ')

#------------------------
# from random import randint
# count =0
# d= eval(input('Choose diffuculty Level: '))
# r = eval(input('Choose number of questions: '))
#
# for i in range(r):
#     x= randint(1,d)
#     y = randint(1, d)
#     opr=randint(1,3)
#     if opr ==1:
#         t= "+"
#         corr = x+y
#     elif opr ==2:
#         t= "-"
#         corr = x - y
#     else:
#         t="*"
#         corr = x*y
#     print('Question ',i+1,':', x,t,y,'=',end= " ")
#     ans =eval( input(''))
#     if ans == corr:
#         print('Right!')
#         count = count+1
#     else:
#         print('Wrong. The answer is',corr )
# print('You got ',count, 'answers right')

#---------exec 6.11 no 1
# s= input('Please input a string: ')
# print('(a): ',len(s))
# print('(b): ',s*10)
# print('(c): ',s[0])
# print('(d): ',s[:4])
# print('(e): ',s[-3:])
# print('(f): ',s[: : -1])
# if len(s)>=7:
#     print('(g): ', s[6])
# else:
#     print('(g): The string has less than seven characters')
# print('(h): ', s[1:len(s)-1])
# print('(i): ', s.upper())
# s=s.lower()
# print('(j): ', s.replace('a','e'))
# for c in s:
#     s=s.replace(c, ' ')

# print('(k): ', s)
#----------
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#     if c.isalpha():
#         print(key[alphabet.index(c)],end='')
#     else:
#         print(c, end='')
# #
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#     if c.isalpha():
#         print(alphabet[key.index(c)],end='')
#     else:
#         print(c, end='')

#-------exer6.11  no7

# s= input('Enter the word: ')
# a= s[: : -1]
# if a ==s:
#     print('the word is a paliondrome')
# else:
#     print('it is not a paliondrome')

# s='francis'
# s.upper()
#
# l=s.upper()
# print(s)
# print(l)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#     if c.isalpha():
#         print(key[alphabet.index(c)],end='')
#     else:
#         print(c, end='')
#
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#     if c.isalpha():
#         print(alphabet[key.index(c)],end='')
#     else:
#         print(c, end='')

# s =input('Enter String')
# y= s.count(' ')
# print('the word count is ',y+1)

# s = input('input your formula: ')
# c1=0
# c2=0
# for c in s:
#     if c=='(':
#         c1=c1+1
#     elif c==')':
#         c2 =c2+1
# if c1==c2:
#     print('Your formula has the same number of parenthesis')
# else:
#     print('the perenthesis are not equal')

# s= input('enter a word: ')
# vowel_count =0
# for c in s:
#     if c in 'aeiou':
#        vowel_count=vowel_count+1
# if vowel_count==0:
#     print('the word doesn\'t contain any vowel')
# else:
#     print('there are',vowel_count,'vowels in the word')

# s= input('Enter your string: ')
# new_string = s[0]+'*'+s[2:]+'!!!'
# print(new_string)

# x = eval(input('input a number: '))
# for i in range(1,x+1):
#     print(' '*i,i)


# --------excer 6.11 no 14

# s= input('Please Enter your name: ')
# s= s.lower()
# x = s.index(' ')
# y = s[0].upper()+s[1:x]+' '+s[x+1].upper()+s[x+2: ]
# print(y)


# s= input('input the question: ')
# if s[0]=='x':
#     s='1'+s
# x = s.index('^')
# n = eval(s[x+1])
# a = eval(s[0])
# c= int(s[x+1])-1
# d= a*n
# print(d,'x^',c, sep='')

# s= input('input your string: ')
# emp_str=''
# for c in s:
#     if c in 'xy(':
#         emp_str='(s.index(c))'+emp_str
# print(emp_str)
# L=[]
# for i in range(10):
#      L.append(i)
# print(L)
# L= [0, 9, 1, 3, 7, 1, 6, 7, 8, 5]
# del L[3]
# print(L)
# L=[]
# for i in range(50):
#     L.append(i)
# print(L)
# M=[]
# for i in range(50):
#     M.append(i**2)
# print(M)
# N=[]
# s='abcdefghijklmnopqrstuvwxyz'
# for c in s:
#    N.append(c*(s.index(c)+1))
#
# print(N)
#------exer 7 no 4---------
# L= []
# for i in range(7):
#     x= eval(input('Please enter a number: '))
#     L.append(x)
# print(L)
#
#
# for item in L:
#    if item > 10:
#       L[L.index(item)]=10
#
# print(L)
#_____exer 7 no 5_______
# L= []
# for i in range(3):
#     x= input('Please enter a string: ')
#     L.append(x)
# print(L)
# M=[]
# for item in L:
#     M.append(item[1:])
#
# print(M)
#-----Exer 7 no 8----------
# L=[]
# x= int(input('Plaese enter a number: '))
# for i in range(2,x):
#     if x%i==0:
#         L.append(i)
# print(L)

# -------Exer 7 no 9-----
# from random import randint
# z= eval(input('Input the number of rolls: '))
# outcome= []
# for i in range(z):
#     r1= randint(1,6)
#     r2 = randint(1, 6)
#     outcome.append(r1+r2)
# print(outcome)
# outcome.sort()
# print(outcome)
# d =[]
# e = []
# for item in outcome:
#     if item not in e:
#         i = outcome.count(item)
#         d.append(i)
#         e.append(item)
#
# print("e =",e)
# print("d =",d)
# f=[]
# for i in d:
#     f.append(round(((i/z)*100),2))
# print(f)
# print(e[f.index(max(f))])

#_______Example
# from string import punctuation
# s = input('Enter a string: ')
# for c in punctuation:
#     s = s.replace(c, '')
# s = s.lower()
#
# L = s.split()
# print(L)
# word = input('Enter a word: ')
#
# print(word, 'appears', L.count(word), 'times.')

#-------
# L = ['a','i','t','a','c','xyz']
# M= [1,10,14,9,2,13,1,3]
# N= ['five','one','three','four','two']
# # x= len(L)
# print(x)
# y = sum(M)
# print(y)
# avg = sum(M)/len(L)
# print(avg)
# x =sorted(M, reverse=True)
# print(M)
# print(x)
#
# M.reverse()
# print(M)
#
# N.insert(3,'Six')
# print(N)
#------7.7 no 3
# L=[8,9,10]
# L[1]=17
# M =[4,5,6]
# L=L+M
# del L[0]
# L.sort()
# L=L*2
# L.insert(3,25)
# print(L)

#------7.7 no 2
# L=[1,1,2,3,5,12,18,13,9,7,4,1,3,5,12,13,9,7,16,15]
# L.sort()
#
# M=[]
#
# for item in L:
#     if item not in M:
#         M.append(item)
#
# s= '234-806-abuja call'
# L=s.split('-')
# print(L)


# print("(a)",L)
# print(M)
# # print("(b)",avg)
# print("(c) Largest:", L[19], 'and Smallest: ',L[0])
# print("(d) Second Largest: ",M[len(M)-2], 'and second Smallest: ', M[1])
# for item in L:
#     if item%2==0:
#         count=count+1
# print("(e) There are ", count, 'even numbers')

# L= []
# for i in range(1,11):
#     L.append(i)
# print(L)
#
# M=[i for i in range(1,11)]
# print(M)

# L = ['one','three','eight','two','nine','ten']
# M= []
#
# for item in L:
#     M.append(item[0])
# print(M)
# # N=[]
# # for item in L:
# #     if len(item)>3:
# #         N.append(item[0])
#
# N=[item[0] for item in L if len(item)>3]
# print(N)

#-----Exer8 question 1
# count= 0
# s= input('input your text: ')
#
# s=s.lower()
#
# L= s.split() L= ["a","boy","is","coming",'to']
# A=['a','an','the']
# for item in L:
#     if item in A:
#         count =count+1
# print()
# print(L)
# print('there are',count,'articles in the text')
# exercise 8 no 2
# L= []
# for i in range(5):
#     x= input('Please enter a number: ')
#     L.append(x)
# print(L)
# s= '+'.join(L)
# print(s)
# from random import *
# Q= ['no food for lazy man','God dey','all that giliiters is not gold','Knowledge is power',
#     'Evil that men do dey follow them']
# QoD=choice(Q)
# print(QoD)
# from random import *
# L=[i for i in range(1,49)]
# number = sample(L,6)
# print(number)
#--------Question 18 exec8-----
# from random import *
# L = [[randint(1,100) for i in range(10)] for j in range(10)]
# print(L)
# for i in range(len(L)):
#     for a in range(len(L[i])):
#         print(L[i][a], end =' ')
#     print()
# print(max(L[2]))
# print(min(L[i][5] for i in range(len(L))))

# while (1):
#     num= int(input('Please type in a number: '))
#     if num == 0:
#         print('Oh You have just ended the program')
#         break
#     elif num > 100:
#         print('Sorry the number is out of scope')
#         continue
#     else:
#         print('The square of your number is: ',num**2)
# i=1
# while i<=50:
#     print(i)
#     i=i+1

# s= input('enter a string: ')
# i=0
# print(s[i])
# print(s[i+2])
# while i<len(s):
#     if s[i] in ' ':
#         print(s[i+2])
#         i=i+1

# while (1):
#     weight =eval(input('Please enter the weight in kilogram: '))
#     if weight<0:
#         print('invalid entry,enter a number greater than 0')
#         continue
#     else:
#         print('this is equivalent to', weight/2.205,'pounds')
# L= ['12345','12548','13589','78958']
# i=0
# while i<5:
#     pword=input('please enter your password: ')
#     if pword in L:
#         print('Recharge Successful')
#         break
#     else:
#         if i==3:
#             print('you have just one chance left')
#         elif i==4:
#             print('You are blocked! Contact MTN center')
#         else:
#             print('you have ', 4-i, 'chances left')
#         i=i+1
# L=[]
# count=0
# while True:
#     score=eval(input('Please a score: '))
#     if score <0:
#         print('Bye')
#         break
#     else:
#         L.append(score)
#         if score>=90:
#             count+=1
# print('You entered',L)
# print('There are ',count, 'numbers greater or equal to 90')
# avg=sum(L)/len(L)
# print('the average of your numbers is ', avg)
# d = {'A':100, 'B':200}
# print(d['A'])
# d['A']=400
# print(d)
# d['C']=500
# print(d)

# d= {'dog' : 'has a tail and goes woof!',
#      'cat' : 'says meow',
#      'mouse' : 'chased by cats'}
# print(d['mouse'])
# points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
#          'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
#          'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
#          'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
# word = input('Please input a word: ')
# word=word.upper()
# sum=0
# for c in word:
#    sum=sum+(points[c])
# print(sum)
L1=[]
L2 =[]

while True:
    PN=input('Please put a product name: ')
    PP = eval(input('Please add the price: '))
    if PN =="done" and PP == 0:
        break
    else:
        L1.append(PN)
        L2.append(PP)
print(L1)
print(L2)
d= {c : L2[L1.index(c)] for c in L1}
print(d)
while True:
    prod=input('Which product price do you want?:')
    if prod in d:
        print('The price of', prod, 'is', d[prod])
    else:
        print('Sorry, we dont have your product')




