#队列的实现
class Queue:
   def __init__(self):
      self.items = []

   def isEmpty(self):      
      return self.items == []

   def enqueue(self, item):
      self.items.insert(0,item)

   def dequeue(self):
      return self.items.pop()
   def size(self):
      return len(self.items)
# q=Queue()
# print(q.items)
# q.enqueue(4)
# print(q.items)
# q.enqueue('dog')
# print(q.items)
# q.enqueue(True)
# print(q.items)
# q.dequeue()
# print(q.items)
# print(q.isEmpty())
