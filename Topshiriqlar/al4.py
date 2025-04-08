# 13) Ro‘yxatda berilgan qiymatga ega birinchi elementni takrorlang (2 marta
# ko’paytiring).


class Node:
    def __init__(self,data):
        self.Data = data
        self.Next = None

class LList:
    def __init__(self):
        self.head = None

    def AddFirst(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node

    def Add(self,data):
        node = Node(data)
        if self.head is  None:
            self.head = node
        else:
            cur = self.head
            while cur.Next:
                cur = cur.Next
            cur.Next = node
    def Print(self):
      cur = self.head
      while cur:
        print(cur.Data, end='->')
        cur = cur.Next

    def Takrorla(self,natija):
      cur = self.head
      while cur:
        if cur.Data == natija:
          cur.Data *= 2
          break
        cur = cur.Next

l = LList()
l.Add(1)
l.Add(2)
l.Add(3)
l.Add(4)
l.Add(5)
l.Add(6)

print('Birinchi holat')
l.Print()
l.Takrorla(6)

print('\nIkkinchi holat')
l.Print()
