
# FUTBOL sinfi jamoasining o„yin natijalari haqidagi <jamoa nomi>,
# <g‘alabalar soni>, <duranglar soni>, <mag‘lubiyatlar soni>, <kiritgan to‘plar
# soni> va <o‘tkazgan to‘plar soni> berilganlarni o„z ichiga oladi.
# Berilgan n uchun FUTBOL sinfi obyektlari massivi hosil qilinsin va
# to„plagan ochkolari bo„yicha jamolar jadvali chop etilsin. Bunda
# quyidagilarga e‟tibor berilsin: agar ikkita jamoaning ochkolari teng
# bo„lsa, kiritilgan va o„tkazib yuborilgan to„plar farqi qaraladi. Farqi
# katta bo„lgan jamoa uyqori qatorga o„tadi, aks holda qur‟a tashlanadi va
# shunga qarab jamoa o„rni aniqlanadi.

class Futbol:
    def __init__(self,jamoa_nomi,galabalar_soni,duranglar_soni,maglubiyatlar_soni,kiritilgan_toplar,otkazilgan_toplar):
        self.jamoa_nomi = jamoa_nomi
        self.galabalar_soni = galabalar_soni
        self.duranglar_soni = duranglar_soni
        self.maglubiyatlar_soni = maglubiyatlar_soni
        self.umumiy = galabalar_soni+duranglar_soni
        self.kiritilgan_toplar = kiritilgan_toplar
        self.otkazilgan_toplar = otkazilgan_toplar
        self.farq = kiritilgan_toplar-otkazilgan_toplar
    def __str__(self):
        return f"{self.jamoa_nomi} ->Achkosi {self.umumiy}, farqi {self.farq}"
    
jamoalar = [
    Futbol("Nasaf", 10, 3, 2, 25, 12),
    Futbol("Paxtakor", 10, 3, 2, 28, 15),
    Futbol("Bunyodkor", 9, 4, 2, 24, 13),
    Futbol("Navbahor", 10, 3, 2, 27, 17),
    Futbol("Lokomotiv", 8, 5, 2, 22, 14),
    Futbol("Qo'qon-1912", 7, 3, 5, 19, 18),
    Futbol("Andijon", 6, 4, 5, 18, 21),
    Futbol("Surxon", 28, 3, 7, 16, 22),
    Futbol("Mash'al", 4, 2, 9, 14, 25),
    Futbol("AGMK", 21, 7, 9, 13, 27),
    Futbol("Sogdiana", 2, 4, 9, 10, 24),
    Futbol("Dinamo", 6, 10, 12, 8, 30)
]

jamoalar = sorted(jamoalar, key=lambda x: (x.umumiy, x.farq), reverse=True)
for t in jamoalar:
    print(t)


from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
        