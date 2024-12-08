
def masala(a):
    """yigindini qanoatlantiruvchi eng kichik n ni topish"""
    n = 0
    yigindi = 0
    while yigindi<a:
        n+=1
        yigindi +=1/n
    return n
a = float(input("Ixtiyoriy son kiriting\n>>>"))
natija = masala(a)
print(f"Eng kichik n: {natija}")

