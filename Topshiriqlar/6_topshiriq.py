#n ta elementdan tashkil topgan ro’yxat berilgan. Oddiy qo’shish (insertion sort) algoritmi orqali massivni o’sish tartibida chiqaruvchi dastur tuzilsin.
#Algoritm quyidagicha:  va  elementlar o‘sish tartibida joylashtiriladi. Ya’ni zarurat bo’lsa qiymatlari almashtiriladi.
#Keyin  elementi joylangan elementlar  orasiga shunday joylashtiriladiki, natijada  tartiblangan xolatda bo’ladi.
#Shu tartibda har bir element tartiblangan elementlar orasiga qo’shib boriladi.


arr = [4,2,0,5,3,-6,9,1,16,7]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if(arr[j-1]>arr[j]):
            arr[j]+=arr[j-1]
            arr[j-1]=arr[j]-arr[j-1]
            arr[j]-=arr[j-1]
        else:
            break
print(arr)


########DONE>>>>>>.......
#Next(Y/n):y
