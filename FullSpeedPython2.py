import listExamples

[l1,l2] = listExamples.getSublist([1,2,3,4,5])
print(l1, l2)

list = listExamples.AppendToList1([1, 2, 3, 4, 5], 90)
print(list)

n2 = listExamples.AppendToList2([1, 2, 3, 4, 5], [90])
print(n2)

avgList = listExamples.getAverage([1,2,3,4,5,6])
print(avgList)

print(listExamples.removeList([1,2,3,4,5,6], [2,4,6]))

new_array = [i**3 for i in [1,2,3,4]]
print(new_array)

print([x for x in range(1,10,3)])
print([x**2 for x in range(1,10,3) if x%2 ==0])

print(listExamples.getSquare(range(1,11)))

[even,odd] = listExamples.listofEvenOdds(range(21))
print([even,odd])

print(listExamples.sumEvenSquaredList(range(21)))

print(listExamples.getSquare2(range(21)))

print(listExamples.findMax([-1, -2, 3, 4, 8, 0]))

print(listExamples.findMaxValueIndex([11,14,18,19]))

print(listExamples.reverse2([10, 20, 30, 40, 50, 60]))

print(listExamples.isSorted([1,1,2,8,4]))

print(listExamples.hasDuplicates([1,11,8]))

listExamples.printEvenOdd(10)
