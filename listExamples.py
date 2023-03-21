l = [1, 2, 4, 5, 8, 9]
for i in l:
    print(i)

sum_ = 0
for value in l:
    sum_ = sum_ + value
print(sum_)

for value in [0, 1, 2, 3, 4, 5]:
    print(value * value)

myList = [1, 3, 5]
for i in range(len(myList)):
    print("index: ", i, "value: ", myList[i])

# Sometimes you may need both things (indexes and values), and you can use the "enumerate" function:
for i, value in enumerate(myList):
    print("index: ", i, "value: ", value)

n = 10
while n > 0:
    print(n)
    n = n - 1

def getSublist(l):
    l1 = l[0:3]
    l2 = l[3:]
    return [l1, l2]

#The method does not return any value but append the given object to the list
def AppendToList1(list, item):
    list.append(item)
    return list

def AppendToList2(list, sublist):
    list = list + sublist
    return list

def getAverage(list):
    avg = sum(list) / len(list)
    return avg

#The method does not return any value but removes the given object from the list
def removeList(list, sublist):
    for element in sublist:
        list.remove(element)
    return list

def getSquare(list):
    squared = [x**2 for x in list]
    return squared

def listofEvenOdds(list):
    even = [x for x in list if x%2==0]
    #odd = [y for y in list if y%2==1]
    odd =  [y for y in list if (y not in even)]
    return even,odd

def sumEvenSquaredList(list):
    #sumEvenList = sum([i**2 for i in list if i%2 ==0])
    sumEvenList = sum([x**2 for x in range(0,21,2)])
    return sumEvenList

def getSquare2(list):
    new_list = [x**2 for x in list if x%2 ==0 and x%3 !=0]
    return new_list

def findMax(list):
    max_ = list[0]
    for value in list:
        if value > max_:
            max_ = value
    return max_

def findMaxValueIndex(list):
    max_ = list[0]
    max_i =0
    for index, value in enumerate(list):
        if value> max_:
            max_ = value
            max_i = index
    return [max_i, max_ ]

def reverse(list):
    length = len(list)
    new_list = [None]*length

    for value in list:
        length = length - 1
        new_list[length] = value
    return new_list

def reverse2(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    return new_list

def isSorted(list):
    prev = list[0]
    isSorted = True
    for i in range(1,len(list)):
        if prev <= list[i]:
            prev = list[i]
        else:
            isSorted = False
            break
    return isSorted

def hasDuplicates(list):
    hasDup = False
    for i in range(len(list)):
         for j in range(i+1,len(list)):
             if list[i] == list[j]:
                hasDup = True
                break

    return hasDup

def printEvenOdd(n):
    for i in range(n,0,-1):
        if i % 2 ==0:
            print("even number:", i)
        else:
            print("odd number: ", i)