
# 16) Berilgan qiymatli birinchi elementni takrorlang.

class Node:
    def __init__(self,d):
        self.Data = d
        self.Next = None
    
    
    def __del__(self):
        print(self.Data, 'Deleted')
    
class LList:
    def __init__(self):
        self.head = None
    
    def AddFirst(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node

    def Add(self,data):
        node = Node(data)
        cur = self.head
        if cur is not None:
            while cur is not None:
                cur = cur.Next
            cur.Next = Node
        else:
            self.head = node



    def double(self,data):
        node = Node(data)
        cur = self.head
        cur.Next = cur
        cur.Next.Next = node




    def Print(self):
        cur = self.head
        while cur is not None:
            print(cur.Data)
            cur = cur.Data

l = LList()
l.Add(1)
l.Add(2)
l.Add(3)
l.double(1)
l.Print()



        
# *******************************************************************************
# def faktorial(N):
#     i = 1
#     fak = 1
#     while i!=N+1:
#         fak = fak*i
#         i+=1
#     return fak
# print(faktorial(5))
# ***********************************LINEAR SEARCH****************************************
# n = int('input(n ni qiymatini kiriting\n>>>')) # Qiymat

# def my_list(n):
#     myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
#     for i in myList:
#         if n == i:
#             a = myList.index(i)
#             print(a)
                
# print(my_list(n))


# **********************************BINARY SEARCH*******************************************************

# n = int(input('n ni qiymatini kiriting\n>>>')) # Qiymat
# myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
