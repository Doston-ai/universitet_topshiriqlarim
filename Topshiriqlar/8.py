# 12. Uchburchak uchlari va shu uchburchak ichidagi biror nuqta
# koordinatasi bilan berilgan. Berilgan nuqtadan uchburchak
# tomonlarigacha bo'lan eng yaqin masofa topilsin.
#//uchburchak ichidagi biron nuqtadan tomonlarigacha bo'lgan perpendikulyarlar yig'indisi uchburchak balandligiga teng.
x = [1,2] 
y = [5,2]
z = [3,6]
d = [3,4]

uch1 =[
((y[0]-x[0])**2+(y[1]-x[1])**2)**0.5,
((d[0]-x[0])**2+(d[1]-x[1])**2)**0.5,
((y[0]-d[0])**2+(y[1]-d[1])**2)**0.5,
]   
uch2 = [
((d[0]-y[0])**2+(d[1]-y[1])**2)**0.5,
((z[0]-d[0])**2+(z[1]-d[1])**2)**0.5,
((z[0]-y[0])**2+(z[1]-y[1])**2)**0.5,    
]
uch3 = [
((d[0]-z[0])**2+(d[1]-z[1])**2)**0.5,
((x[0]-d[0])**2+(x[1]-d[1])**2)**0.5,
((x[0]-z[0])**2+(x[1]-z[1])**2)**0.5,
]
def h1():
    a=uch1[0]
    b=uch1[1]
    c=uch1[2]
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    h1 = 2*(s/a)
    return h1
print(h1())    

def h2():
    a=uch2[0]
    b=uch2[1]
    c=uch2[2]
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    h2 = 2*(s/a)
    return h2
print(h2())     

def h3():
    a=uch3[0]
    b=uch3[1]
    c=uch3[2]
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    h3 = 2*(s/a)
    return h3
print(h3()) 

# h = h1+h2+h3

h = h1()+h2()+h3()
print(h)