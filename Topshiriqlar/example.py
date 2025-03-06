class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None

    def __del__(self):
        print(self.Data, "deleted")


class LList:
    def __init__(self):
        self.head = None

    def AddFirst(self, data):
        node = Node(data)
        node.Next = self.head
        self.head = node

    def Add(self, data):
        node = Node(data)
        cur = self.head
        if cur is not None:
            while cur.Next is not None:
                cur = cur.Next
            cur.Next = node
        else:
            self.head = node

    def Insert(self, data, pos):
        node = Node(data)
        cur = self.head
        k = 1
        if cur is not None:
            while cur.Next is not None and k < pos:
                cur = cur.Next
                k = k + 1
            node.Next = cur.Next
            cur.Next = node
        else:
            self.head = node

    def Delete(self, pos):
        cur = self.head
        prev = None
        k = 1
        if cur is not None:
            while cur.Next is not None and k < pos:
                prev = cur
                cur = cur.Next
                k = k + 1
            if k <= 1:
                self.head = self.head.Next
            else:
                prev.Next = cur.Next

    def Print(self):
        cur = self.head
        while cur is not None:
            print(cur.Data)
            cur = cur.Next


# ✅ Sinov uchun kod
l = LList()
l.Add(1)
l.Add(2)
l.Add(3)
l.Delete(1)
l.Print()

#  Berilgan qiymatli birinchi elementni takrorlang.

# class CustomList:
#     def __init__(self, elements):
#         """ Ro'yxatni boshlash """
#         self.data = elements if elements else []

#     def repeat_first(self, times):
#         """ Berilgan qiymatli birinchi elementni 'times' marta takrorlash """
#         if self.data:  # Agar ro'yxat bo'sh bo'lmasa
#             first_element = self.data[0]  # Birinchi elementni olamiz
#             self.data = [first_element] * times + self.data[1:]  # Takrorlaymiz

#     def display(self):
#         """ Ro'yxatni ekranga chiqarish """
#         print(self.data)


# # ✅ Test qilish
# clist = CustomList([5, 10, 15, 20])
# clist.repeat_first(3)  # Birinchi elementni 3 marta takrorlash
# clist.display()  # ➝ [5, 5, 5, 10, 15, 20]




