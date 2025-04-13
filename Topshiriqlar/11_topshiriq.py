# 6-masala
# Berilgan gapdagi so„zlar bir-biridan ',' yoki „ „ (probel) belgisi bilan ajratilgan
# va gap nuqta bilan tugaydi. Quyidagi shartlarni bajaruvchi so„zlar chop qilinsin:
# a) birinchi harfi yana uchragan;
# b) eng uzun;
# d) harflari takrorlanmaydigan.

satr = "Salom, sizga qanday yordam beraolaman: Telefon yoki komputer."
lower = satr.lower()

word = lower.replace(',',"")
word = word.replace(':',"")
word = word.replace('.',"")
sozlar = word.split()

# 1)
# for soz in sozlar:
#     birinchi_h = soz[0]
#     k = 0
#     for h in sozlar:
#         if h.startswith(birinchi_h):
#             k+=1
#     if k>1:
#         print(soz)
# 2)
# eng_uzun = max(sozlar, key=len)
# print(f"Eng uzun so'z bu '{eng_uzun}' so'zi")
# 3)
for soz in sozlar:
    takror = False
    for harf in soz:
        if soz.count(harf)>1:
            takror =True
            break
    if takror:
        print(soz)
    
# 19-masala
# Harf yoki pastki chiziq (_) bilan boshlanishi kerak.
# Keyingi belgilar harf, raqam, yoki pastki chiziq (_) bo‘lishi mumkin.
# Python'ning ajratilgan (reserved) so‘zlari identifikator bo‘la olmaydi (masalan, if, for, class va h.k.).

def indefikator(satr):
  if not satr:
    return False
  if not (satr[0].isalpha() or satr[0]=='_'):
    return False
  for a in satr[1:]:
    if not (a.isalnum() or a=='_'):
      return False
  return True
print(indefikator('my-name'))


