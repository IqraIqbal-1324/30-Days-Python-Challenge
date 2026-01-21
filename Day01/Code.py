
print(5)
age=23
print(age)
print("age")

Agent="AHMED ALI"
print(Agent[1:4])
print(type(Agent))
int(input ("Enter your age:\n"))
print(2+5)
print(Agent.lower())
print(Agent.count("A"))
print(len(Agent))
print(Agent[5: ])
Ahmed=[1,"Ahmed","Ali",22,44.5,"Fail"]
print(Ahmed[1])

Tuple=(0,1,3,"Ahmed")
print(Tuple[3])

DICT={
    "Name":"Ahmed",
    "ROLLNO.":21,
    "Class":"BS",
    "Subjects":{
        "PHY":23,
        "BIO":25
    }
}
print(DICT.items())
print(DICT.keys())
print(DICT["Subjects"].keys())
print(DICT["Subjects"]["PHY"])

set1={1,3,3.3,1}
set2={1,5,6.3,1}
print(set1)
print(set2.pop())
print(set1.union(set2))
print(set1.intersection(set2))
age=int(input("age:"))
if(int(input("age:"))>18):
    print("Can Drive")
else:
    print("Cannot")

while int(input("Age:"))>18:
    print("Can Drive")

Ahmed=[1,55,"Late"]
for x in Ahmed:
  print(x)
 
def Driving(age):
  if(age>18):
      return "You can drive"
  else:
      return "You cannot drive"
      
print(Driving(54))
List=["Ahmed","Ayesha","Ali","Ayesha","Sara"]
Set={"Ahmed","Ayesha","Ali","Ayesha","Sara"}
print(List)
print(Set)
for x in Set:
    if x.startswith("A"):
      print(x)


#recursion
#Write a recursive function to calculate the power of a number (x^n).

def power(x,n):
  if(n==0):
    return 1
  return power(x,n-1)*x
  
print(power(2,3))

# Write a recursive function to count how many times a specific element appears in a list.

def CountFUN(list,target,index=0):
    if(index==len(list)):
      return 0 
    if list[index]==target:
      count=1 
    else: 
      count=0
    return count+CountFUN(list,target,index+1)

numbers=[1,2,3,2,4,1,5,6]
print(CountFUN(numbers,2))


# Write a recursive function to check if a string is a palindrome.

def palindrome(s):
   if len(s)==0:
     return True
   if len(s)==1:
     return True
   if s[0]!=s[-1]:
     return False
   return palindrome(s[1:-1])
  
print(palindrome("racecar"))    # True

#primeno
def primenum(n):
    if n<2:
      return False  
    else:
     for i in range(2,int((n**0.5)+1)):
      if n % i ==0:
        return False
        
    return True
    
print(primenum(4))   
#Vowels Count
def vowel_count(s):
    count = 0
    for x in s.lower():
        if x in ("a", "e", "i", "o", "u"):
            count += 1
    return count

print(vowel_count("Ahmed"))

# Maximum number in 3 numbers
def max_of_three(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

print(max_of_three(1, 2, 3))

#sum of numbers in a list
def list_sum(S):
    total = 0
    for x in S:
        total += x
    return total

print(list_sum([1, 3, 4, 6, 8]))


#palindrome or not
def palindrome_check(lst):
    return lst == lst[::-1]

print(palindrome_check([1, 2, 5, 2, 1]))

#recusive for factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))

#consonant count
def consonant_count(s):
    count = 0
    for x in s.lower():
        if x.isalpha() and x not in ("a", "e", "i", "o", "u"):
            count += 1
    return count

print(consonant_count("abshrid"))
#minimu of three count
def min_of_three(x, y, z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

print(min_of_three(1, 2, 3))
#multiply all numer of list and print product
def multiply(S):
    product = 1
    for x in S:
        product *= x
    return product

print(multiply([2, 3, 4, 5]))

#palindrome check 
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))







