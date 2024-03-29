# 双端队列的实现
class Deque:
   def __init__(self):
      self.items = []

   def isEmpty(self):      
      return self.items == []

   def addFront(self,item):
      self.items.append(item)

   def addRear(self, item):
      self.items.insert(0,item)

   def removeFront(self):
      return self.items.pop()
   
   def removeRear(self):
      return self.items.pop(0)

   def size(self):
      return len(self.items)
# d=Deque()
# print(d.isEmpty())
# d.addRear(4)
# print(d.items)
# d.addRear('dog')
# print(d.items)
# d.addFront('cat')
# print(d.items)
# d.addFront(True)
# print(d.items)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.items)
# print(d.removeRear())
# print(d.items)
# print(d.removeFront())
# print(d.items)
