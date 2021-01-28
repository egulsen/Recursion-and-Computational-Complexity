"""
Recursion and Complexity
Written by: Elifnaz Gulsen
Student Number: 20021346
"""


"""
This recursive function prints out the individual digits of the given integer
line by line
"""
def printNums(number):
    strNumber = str(number)
    #base case, if our number has length one, then return number
    if len(strNumber) < 2:
        print(strNumber)
    else:
        #print the first value of the string, then re-call our recursive
        #function with the remaining integers 
        print(strNumber[0])
        printNums(strNumber[1:])


"""
This recursive function counts the number of vowels in a string
"""
def numVowels(string):
    vowels = "aeiouAEIOU"
    #base case, string empty
    if len(string) == 0:
        return 0
    #if the first val of string is in vowels then return 1 + remaining
    #if not, return remaining, and check again until we reach base case
    if string[0] in vowels:
        return 1 + numVowels(string[1:])
    else:
        return numVowels(string[1:])


"""
This  recursive function removes the vowels from a string containing
all lower case letters
"""
def remVowels(string):
    vowels = "aeiou"
    #base case, if empty string, return ""
    if len(string) == 0:
        return ""
    #if first val in vowels, move on to check string[1:]
    elif string[0] in vowels:
        return remVowels(string[1:])
    #if first val not in vowels return it + check string[1:]
    else:
        return string[0] + remVowels(string[1:])

"""
This recursive function finds the products of the numbers from n to m
inclusively by recursively splitting the list in half each time.
"""
def multiply(n, m):
    #mid finds the middle of the numbers, and we split between the two each time
    #until we reach the base case, then multiply all of them via recursion
    mid = (n+m) // 2
    if n > m:
        return None
    if n == m:
        return m
    else:
        return multiply(n,mid) * multiply(mid+1,m)    
    
    
"""
This recursive function swaps the neighbouring elements of a list
and returns a copy, newList, without altering the original list given
We use the property that [1,2] + [3,4] = [1,2,3,4] for the recursive step
"""
def swapNeighbours(lst):
    #base case, if list is empty or has one element, then return list 
    if len(lst) < 2:
        newList = lst
        return newList
    else:
        newList = [lst[1],lst[0]] + swapNeighbours(lst[2:])
        return newList
        

"""
This function checks if two integer lists are equal recursively.
It checks until the two lists are empty, when they are both empty we
conclude that they are equal because if the first elements are not
equal, and the lengths are not equal then we return the second,and third,
until we reach two empty lists (our base case)
"""
def checkLists(int1,int2):
    #base case : if both lists empty, return True
    if len(int1) == 0 and len(int2) == 0:
        return True
    elif len(int1) != len(int2):
        return False
    elif int1[0] != int2[0]:
        return False
    else:
         return checkLists(int1[1:],int2[1:])

"""
def tester():
  printNums(54321)
  print()
  printNums(987)
  print()
  printNums(4)
  print()
  print(numVowels("mnsty"))
  print(numVowels(""))
  print(numVowels("annn"))
  print(numVowels("nnnnna"))
  print(numVowels("canoe"))
  print(remVowels("mnsty"))
  print(remVowels(""))
  print(remVowels("annn"))
  print(remVowels("nnnnna"))
  print(remVowels("canoe")) 
  print(multiply(4, 7))
  print(multiply(2, 10))
  print(multiply(8, 2))
  print(swapNeighbours([2,3,4]))
  print(swapNeighbours([1])) 
  print(swapNeighbours([4,5,6,7])) 
  print(swapNeighbours([])) 
  print(checkLists([],[]))
  print(checkLists([2,5,7],[2,5,7]))
  print(checkLists([7,8,3],[7,8,2])) 
  print(checkLists([2,2],[2,2,2])) 
  print(checkLists([1],[1])) 
  print(checkLists([],[]))


tester()
"""


