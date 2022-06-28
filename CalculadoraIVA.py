import tkinter
from tkinter import *
from tkinter import ttk,font
class Ventana(object):
    __ventana=None
    __precio=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title('Calculadora IVA')
        self.__ventana.configure(background='lightblue')
        fuente=font.Font(weight='normal')
        opts = { 'ipadx': 10, 'ipady': 10, 'sticky':'nswe' }
        self.__precio=DoubleVar()
        self.__precio.set('')
        self.iva=DoubleVar()
        self.labelA=ttk.Label(self.__ventana,background='lightblue',text='Precio sin IVA:',font=fuente,padding=(5,5))
        self.textA=ttk.Entry(self.__ventana,textvariable=self.__precio,width=30)
        ttk.Radiobutton(text='IVA 21%',value=0.21,variable=self.iva).grid(column=0,row=3)
        ttk.Radiobutton(text='IVA 10,5%',value=0.105,variable=self.iva).grid(column=1,row=3)
        self.labelB=ttk.Label(self.__ventana,background='lightblue',text='IVA:',font=fuente,padding=(5,5))
        self.labelC=ttk.Label(self.__ventana,background='lightblue',text='Precio con IVA:',font=fuente,padding=(5,5))
        self.boton1=ttk.Button(self.__ventana,text='Calcular',command=self.calcular)
        self.boton2=ttk.Button(self.__ventana,text='Salir',command=self.destroy)

        self.labelA.grid(column=0,row=2)
        self.textA.grid(column=1,row=2)
        self.labelB.grid(column=0,row=4)
        self.labelC.grid(column=0,row=5)
        self.boton1.grid(column=0,row=6)
        self.boton2.grid(column=1,row=6)


    def calcular(self):
        iva=self.__precio.get()*self.iva.get()
        self.labelD=ttk.Label(self.__ventana,background='lightblue',text='{:.2f}'.format(iva))
        self.labelD.grid(column=1,row=4)
        precioconiva=self.__precio.get()+iva
        self.labelE=ttk.Label(self.__ventana,background='lightblue',text='{:.2f}'.format(precioconiva))
        self.labelE.grid(column=1,row=5)

    def destroy(self):
        self.__ventana.destroy()

    def ejecutar(self):
        self.__ventana.mainloop()
if __name__=='__main__':
    ventana=Ventana()
    ventana.ejecutar()
