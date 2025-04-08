# 23) Ro'yxat oxiridan berilgan sondagi elementlarni olib tashlang.

class Node:
    def __init__(self,data):
        self.Data = data
        self.Next = None

class LList:
    def __init__(self):
        self.head = None

    def AddFirst(self,data):
        node = Node(data)
        node.Next = self.head()
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
    def Last(self,qiymat):
        cur = self.head
        k = 0
        while cur is not None:
            cur = cur.Next
            k+=1
        if qiymat == k:
          self.head = None

        elif qiymat>k:
            return False
        elif qiymat<0:
            return False

        g = 0
        cur = self.head
        while g<k-qiymat-1:
            cur = cur.Next
            g+=1
            if g == k-qiymat-1:
                cur.Next = None
    def Print(self):
        cur = self.head
        while cur:
            print(cur.Data, end=',')
            cur = cur.Next



l = LList()
l.Add(1)
l.Add(5)
l.Add(6)
l.Add(8)
l.Add(2)
print("Avallgi holat")
l.Print()
# l.Last(10)
print("\nKeyingi holat")
# l.Print()
natija = l.Last(5)
if natija == False:
    print('natija xato')
else:
  l.Print()
