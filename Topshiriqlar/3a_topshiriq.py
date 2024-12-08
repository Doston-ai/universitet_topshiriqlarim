
def masala1(a):
    """yigindi a dan katta bolguncha hisoblaydi"""
    n = 0
    yigindi = 0
    while yigindi<=a:
        n += 1
        yigindi += 1/n
    return yigindi

a = float(input("a ni kiriting: "))
    
natija =  masala1(a)
print(f"{a} dan katta birinchi yigindi: {natija}")




