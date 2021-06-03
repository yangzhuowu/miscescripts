# Python Program to Check if a Number is a Prime Number
  def checkPrimeNumber(num):
    k = 0
    for i in range(2, num//2+1):
        print(i)
        if num % i == 0:
            k = k + 1
        else:
            pass
        
    if k == 0:
        print('Number is Prime')
    else:
        print('Number is Non-Prime')
        
# Python Program to Check if a Number is an Armstrong Number    
   def checkArmstrongNumber(num):
    ls = list(map(int, str(num)))
    n = len(ls)
    newlist = list(map(lambda x: x**n, ls))

    if sum(newlist) == num:
        print('Number is Armstrong Number')
    else:
        print('Number is Non-Armstrong Number')

# Python Program to Check if a Number is a Perfect Number  
  def checkPerfectNumber(num):
    sumnum = 0
    for i in range(1, num):
        if num % i == 0:
            sumnum = sumnum + i
        else:
            pass
    if sumnum == num:
        print('Number is Perfect Number')
    else:
        print('Number is Non-Perfect Number')
 
 # Python Program to Check if a Number is a Strong Number
 import math
  def checkStrongNumber(num):
    sumnum = 0
    ls = list(map(int, str(num)))
    for i in ls:
        sumnum = sumnum + math.factorial(i)
    if sumnum == num:
        print('Number is Strong Number')
    else:
        print('Number is Non-Strong Number')
   
 # Python Program to Check if a String is a Palindrome or Not
 def checkPalindrome(word):
    if str(word.lower()) == str(word.lower())[::-1]:
        print("The string is a Palindrome")
    else:
        print("The string is Not a Palindrome")