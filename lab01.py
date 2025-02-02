# -*- coding: utf-8 -*-
"""Lab01

**Instructions to Follow (Failing to follow these will result mark deductions).**
1. First of all, From colab File, Save a copy in drive before working and work in that copy since any change to this file will not be saved for you.
2. You can not use any built-in function except len()

3. You can not use any other python collections except array (e.g: tuple, dictionaries etc.).

4. We will initialize a new array using numpy library. We have to mention the fixed size during initialization. There might be 4 approaches.

 i. arr = np.array([None] * 10) #Initializing an array length 10 with values None.

 ii. arr = np.array([0] * 10) #Initializing an array length 10 with values zero.

 iii. arr = np.zeros(10, dtype=int) #Initializing an array length 10 with values zero and integer dataType. By default, dtype is float.

 iv. arr = np.array([10, 20, 30, 40]) #Initializing an array length 4 with the values.
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""You will see the status Accepted after completion if your code is correct.

If your function is wrong you will see wrong [correction percentage]

Do not change the driver code statements. You can only change the input values to test your code.
"""

#Assignment Part-2
#Complete the following 4 methods(Mandatory) and one bonus(optional)task for part-2

#Task 01: Merge Lineup
def mergeLineup(pokemon_1, pokemon_2):

  result = np.array([0]*len(pokemon_1))
  n=len(pokemon_2)-1

  for i in range(len(result)):
   if pokemon_1[i] is None:
      pokemon_1[i]=0
   if pokemon_2[n] is None:
     pokemon_2[n]=0
   result[i]+=pokemon_1[i]+pokemon_2[n]
   n-=1
  return result

print("///  Task 01: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None] )
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [12, 3, 28, -8, 5]
unittest.output_test(returned_value, np.array([12, 3, 28, -8, 5]))
pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [4,17,6,27,2]
unittest.output_test(returned_value, np.array([4,17,6,27,2]))

# Task 02: Discard Cards

def discardCards(cards, t):

  new_cards=np.array([0]*len(cards))
  count=0
  intl=0

  for i in range(len(cards)):
    if cards[i]==t:
      count+=1
      if count % 2!=0:
        pass
      else:
        new_cards[intl]=cards[i]
        intl+=1
    else:
      new_cards[intl]=cards[i]
      intl+=1
  return new_cards

print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]
unittest.output_test(returned_value, np.array([1,3,7,5,2,2,0,0,0]))

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]
unittest.output_test(returned_value, np.array([5,0,0,0,0]))

# Task 03: DUBER Fare Splitting
def findGroups(money, fare):
  # TO DO
  # Print outputs inside the method

  x=np.array([0]*len(money))
  group_count=0
  n = len(money)

  for i in range(len(money)):
    if money[i]==fare:
      group_count+=1
      x[i]=money[i]
      print(f"Group { group_count} : {money[i]}")
      money[i]=0
    for j in range(len(money)):
      if money[i]+money[j]==fare and x[i]==0 and x[j]==0:
        group_count+=1
        x[i]==money[i]
        x[j]==money[j]
        print(f"Group { group_count} : {money[i]}, {money[j]}")
        money[i]=0
        money[j]=0
  for k in money:
    if k!=0:
      print("Ungrouped:", end="")
      break
  for k in range(len(money)):
    if money[k]!=0:
      print(money[k], end=" ")


print("///  Task 03: DUBER Fare Splitting  ///")
money = np.array( [120, 100, 150, 50, 30])
fare = 150
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 120, 30
# Group 2 : 100, 50
# Group 3 : 150


money = np.array( [60, 150, 60, 30, 120, 30])
fare = 180
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 60, 120
# Group 2 : 30, 150
# Ungrouped : 30 60

import numpy as np
def analyzeHobbies(* participants): #(* arguments) is used for variable number of parameters

    total = 0
    idx = 0
    unq_count = 0

    for p in participants:
      total += len(p)

    hobbies = np.zeros(total, dtype=object)
    for p in participants:
        for hobby in p:
            hobbies[idx] = hobby
            idx += 1

    unq_hobbies = np.zeros(total, dtype=object)
    for i in range(total):
        for j in range(unq_count):
            if hobbies[i] == unq_hobbies[j]:
                break
        else:
            unq_hobbies[unq_count] = hobbies[i]
            unq_count += 1

    hobby_count = np.zeros(unq_count, dtype=int)
    for hobby in hobbies:
        for k in range(unq_count):
            if hobby == unq_hobbies[k]:
                hobby_count[k] += 1
                break

    print("Unique Activities in the Town:")
    print("[", end="")
    for i in range(unq_count):
        print(f"'{unq_hobbies[i]}'", end=", "
              if i < unq_count - 1
              else "]\n")

    print("Statistics:")
    for i in range(unq_count):
        print(f"{hobby_count[i]} participant(s) like(s) {unq_hobbies[i]}.")


print("///  Task 04: Get Those Hobbies  ///")
participant_1 = np.array( ["Hiking", "Reading", "Photography", "Cooking"])
participant_2 = np.array( ["Reading", "Hiking", "Painting"])
participant_3 = np.array( ["Hiking", "Cooking", "Photography"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2, participant_3) #This should print

#Unique Activities in the Town:
#['Photography', 'Painting', 'Cooking', 'Reading', 'Hiking']

#Statistics:
#2 participant(s) like(s) Photography.
#1 participant(s) like(s) Painting.
#2 participant(s) like(s) Cooking.
#2 participant(s) like(s) Reading.
#3 participant(s) like(s) Hiking.



participant_1 = np.array( ["Gardening", "Traveling"])
participant_2 = np.array( ["Singing", "Gardening", "Painting"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2) #This should print

#Unique Activities in the Town:
#[Gardening, Traveling, Singing, Painting]

#Statistics:
#2 participant(s) like(s) Gardening.
#1 participant(s) like(s) Traveling.
#1 participant(s) like(s) Singing.
#1 participant(s) like(s) Painting.

# Bonus Ungraded Task: Look and Say
def look_and_say(arr):
  #TO DO

#:)

print("///  Bonus Task: Look and Say  ///")
arr = np.array([1,3,1,1,2,2,2,1])
returned_value = look_and_say(arr)
print(f'Bonus Task: {returned_value}') # This should print [1,1,1,3,2,1,3,2,1,1]
#Hint: The size of the new array will never be more than 100.
#[You need not worry about the extra zeroes at the end of your resulting array]

"""For Assignment Part-1, you can create new code cells in the below and write your codes there. Also you should write driver codes to test your code for part-1."""

#Assignment Part-1
#Write 3 methods and driver codes for this part.

#task1
import numpy as np

arr=np.array([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])

def mean(arr):
  sum=0
  for i in arr:
    sum+=i
  mn=sum/len(arr)
  return mn
print(f"The mean of the numbers is : {mean(arr)}")

def sd(arr):
  new_x=mean(arr)
  s=0
  for i in arr:
    s+=(i-new_x)**2
  sd=(s/(len(arr)-1))**(1/2)
  return sd
print(f"The standard deviation is: {sd(arr)}")

def newarray(arr):
    mn = mean(arr)
    std = sd(arr)
    a = 1.5 * std
    count=0
    for i  in arr:
      if i>=(mn+a) or i<=(mn-a):
        count+=1
    new= np.array([0]*count)
    intl=0
    for i  in arr:
      if i>=(mn+a) or i<=(mn-a):
        new[intl]=i
        intl+=1
    return new

print("New array:", newarray(arr))
