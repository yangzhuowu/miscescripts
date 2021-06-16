"""
subject: Some Python Code Collections
"""
#179. Largest Number - using built-in comparator function
#1st method
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        
        def findLargeNumber(a, b):
            conc1 = a + b
            conc2 = b + a
            
            if int(conc1) > int(conc2):
                return -1
            elif int(conc1) < int(conc2):
                return 1
            else:
                return 0
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        ans = ''.join(sorted(nums, cmp=findLargeNumber))
        
        return '0' if ans[0] == '0' else ans

#2nd methods 
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(nums).lstrip('0') or '0'

#922. Sort Array By Parity II
#1st method
   class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        
        for i in nums:
            if i % 2 == 1:
                odd_list.append(i)
            else:
                even_list.append(i)
        
        res = [None]*(len(odd_list) + len(even_list))
        res[::2] = even_list
        res[1::2] = odd_list
        
        return res 

#2nd methods - using pointer
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        
        len_list = len(nums)
        
        while i < len_list and j < len_list:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums

#976. Largest Perimeter Triangle
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)[::-1]
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
        
#1122. Relative Sort Array
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hm = {v: k  for k, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: hm.get(i, 1000 + i))
    
 #1356. Sort Integers by The Number of 1 Bits - Bit Manipulation
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda i: [bin(i).count('1'), i])
 
#Python Program to Check if a Number is a Prime Number
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
        
#Python Program to Check if a Number is an Armstrong Number    
   def checkArmstrongNumber(num):
    ls = list(map(int, str(num)))
    n = len(ls)
    newlist = list(map(lambda x: x**n, ls))

    if sum(newlist) == num:
        print('Number is Armstrong Number')
    else:
        print('Number is Non-Armstrong Number')

#Python Program to Check if a Number is a Perfect Number  
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
 
 #Python Program to Check if a Number is a Strong Number
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
   
 #Python Program to Check if a String is a Palindrome or Not
 def checkPalindrome(word):
    if str(word.lower()) == str(word.lower())[::-1]:
        print("The string is a Palindrome")
    else:
        print("The string is Not a Palindrome")
