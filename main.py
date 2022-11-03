# jelszogenerator
'''
import fuggveny
print(fuggveny.jelszogenerator(18, True, True))

from objektum import *

p = objektum.Jelszoobjektum()
p.jelszohossz = 15
print(p.jelszogeneralas_alap())
'''
from tkinter import *
import fuggveny

def jelszokiiras():
    jelszocimke.pack()

ablak = Tk()
ablak.title('Jelszógenerálás')
cimke = Label(ablak, text='A jelszó', fg='red')
gomb = Button(ablak, text='Ok', command=ablak.destroy)
jelszocimke = Label(ablak, text=fuggveny.jelszogenerator(10, True, True))
jelszogomb = Button(ablak, text='jelszógenerálás', command=jelszokiiras())

gomb.pack()
cimke.pack()
jelszogomb.pack()
mainloop()