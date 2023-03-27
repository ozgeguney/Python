class myRange:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a +=1
            return value
        else:
            raise StopIteration

myRange = myRange(1,4)
iterr =iter(myRange)
print(myRange.__next__())
print(myRange.__next__())
#print(myRange.__next__())
#print(myRange.__next__())
print(next(iterr))

# myRange2 = myRange(1,6)
# for value in myRange2:
#     print(value)


class myRange2:
    i =1
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        value = myRange2.i
        if value < self.n:
            if value % 2 == 0:
                myRange2.i += 2
                return value
            else:
                myRange2.i +=1
                return self.__next__()
        else:
            raise StopIteration


# a = myRange2(8)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


class MyRangeAA:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    result = []
    for i in range(0,self.n):
        if i == 0 or i == 1:
            result.append(i)
        else:
            result.append(result[i-2] + result[i-1])
    return result

# aaa = MyRangeAA(8)
# print(aaa.next())


#yield - generator

def myrangeq(a, b):
  while a < b:
    yield a
    a += 1

# a = myrangeq(2, 4) # call the generator function which returns an object
# print(a)
# print (next(a)) # iterate through items using next
# print (next(a))
#
# for value in myrangeq(1, 4):
#   print(value)

def squares(n):
  for value in range(n):
    yield value * value

sqr = squares(8)
# print(next(sqr))
# print(next(sqr))
# print(next(sqr))

def odd(n):
  for i in range(n+1):
    if i%2 ==1:
      yield i

odd = odd(13)

# for j in odd:
#     print(j)

def reverse(n):
  for i in range(n,-1,-1):
    yield i
# for i in reverse(8):
#   print(i)

def fibonacci(n):
  result = []
  for i in range(n):
    if i == 0 or i==1:
      result.append(i)
      yield i
    else:
      x = result[i-1] + result[i-2]
      result.append(x)
      yield x
# for i in fibonacci(8):
#   print(i)
