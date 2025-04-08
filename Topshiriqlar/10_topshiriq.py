# Kutubxona = [<kitob registratsiya nomeri>, <muallif>, <kitob nomi>, <nashr yili>, <nashriyot>]*n. Berilgan butun n uchun elementlari Kutubxona massivi hosil qilinsin va quyidagi amallar bajarilsin:
# a) mualliflar familiyalari alfavit bo‘yicha tartiblangan ko‘rinishdagi kitoblar ro‘yxati chop etilsin;
# b) ko‘rsatilgan nashriyot tomonidan chiqarilgan kitoblar ro‘yxati chop etilsin;
# d) registratsiya nomeri ko‘rsatilgan kitob massivdan o‘chirilsin.


Kutubxona = [
    (101, "Tolstoy L.", "War and Peace", 1869, "Penguin"),
    (102, "Dostoevsky F.", "Crime and Punishment", 1866, "Oxford"),
    (103, "Hemingway E.", "The Old Man and the Sea", 1952, "Scribner"),
    (104, "Orwell G.", "1984", 1949, "Penguin"),
    (105, "Rowling J.K.", "Harry Potter", 1997, "Bloomsbury")
]

# a)
print('Tartiblangan mualiflar\n')
for book in sorted(Kutubxona, key=lambda x:x[1]):
  print(book)

# b)
nashriyot = input("Nashriyot nomini kiriting: ")
nomi = []
for book in Kutubxona:
  if book[4] == nashriyot:
    nomi.append(book)

if nomi:
  for kitob in nomi:
    print(kitob)
else:
  print('Bu nashriyotdan kitob topilmadi')

# c)
nomeri = int(input('kitob nomerini kiriting: ')).strip()
deleted = []
for book in Kutubxona:
  if book[0] != nomeri:
    deleted.append(book)


for a in deleted:
  print([a])
