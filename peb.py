import tkinter as tk
import peb_fun as pfun

data=[]
probTramo=[]
qxtmp=[]
pTramo=[]

def init_data(tr,a,b):
    data.append(int(tr))
    data.append(int(a))
    data.append(int(b))
    l=tk.Label(fl3,text="Datos iniciales:")
    l.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.04)
    txt=f'Tramos: {tr}\nNumerador Q(x): {a}\nDenominador Q(x): {b}'
    data_label=tk.Label(fl3,text=txt)
    data_label.place(relx=0.05,rely=0.08,relwidth=0.9,relheight=0.10)

def tr_info(tramo):
    At,Vt,N=[float(i) for i in tramo.split(",")]
    x=(data[1]*pfun.voltage(At,Vt))/(data[2]*pfun.sigma(N))
    print(x)
    qxtmp.append(x)
    probTramo.append(pfun.q(x))
    i4.delete(0,"end")

def prob():
    probTotal=0
    for i in range(2**data[0]):
        bits=bin(i).lstrip("-0b").zfill(data[0])
        error=pfun.peb(bits,probTramo)
        pTramo.append(error)
        probTotal+=error
    probPrint=f'{probTotal:.5%}'
    lr=tk.Label(fl3,text="La probabilidad de error es:")
    lr.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.04)
    lresult=tk.Label(fl3,text=probPrint)
    lresult.place(relx=0.05,rely=0.22,relwidth=0.9,relheight=0.04)


root=tk.Tk()
root.title("Probabilidad de error en una red de enlaces")
root.geometry("800x600+600+200")

label=tk.Label(root,text="Software para encontrar el valor de error de probabilidad de bit en una red de enlaces")
label.place(relwidth=0.9,relheight=0.1,relx=0.05)

frame=tk.Frame(root)
frame.place(rely=0.1,relwidth=0.9,relheight=0.9,relx=0.05)


fl1=tk.LabelFrame(frame,text="Ingresa los valores")
fl1.place(relwidth=0.48,relheight=0.45)
fl2=tk.LabelFrame(frame,text="Guarda los valores de los tramos")
fl2.place(rely=0.5,relwidth=0.48,relheight=0.45)
fl3=tk.LabelFrame(frame,text="Resultados")
fl3.place(relx=0.5,relwidth=0.48,relheight=0.95)

l1=tk.Label(fl1,text="Ingrese el numero de tramos:")
l1.place(relx=0.05,rely=0.025,relwidth=0.9,relheight=0.15)
i1=tk.Entry(fl1)
i1.place(relx=0.05,rely=0.225,relwidth=0.9,relheight=0.15)
l2=tk.Label(fl1,text="Ingrese a:")
l2.place(relx=0.05,rely=0.425,relwidth=0.4,relheight=0.15)
l3=tk.Label(fl1,text="Ingrese b:")
l3.place(relx=0.55,rely=0.425,relwidth=0.4,relheight=0.15)
i2=tk.Entry(fl1)
i2.place(relx=0.05,rely=0.625,relwidth=0.4,relheight=0.15)
i3=tk.Entry(fl1)
i3.place(relx=0.55,rely=0.625,relwidth=0.4,relheight=0.15)
b1=tk.Button(fl1,text="Ingresar datos iniciales",command=lambda:init_data(i1.get(),i2.get(),i3.get()))
b1.place(relx=0.05,rely=0.825,relwidth=0.9,relheight=0.15)

l4=tk.Label(fl2,text="Ingrese At,V,N (separado por comas)")
l4.place(relx=0.05,rely=0.15,relwidth=0.9,relheight=0.15)
i4=tk.Entry(fl2)
i4.place(relx=0.05,rely=0.4,relwidth=0.9,relheight=0.15)
b2=tk.Button(fl2,text="Ingresar",command=lambda:tr_info(i4.get()))
b2.place(relx=0.05,rely=0.65,relwidth=0.4,relheight=0.15)
b3=tk.Button(fl2,text="Calcular",command=prob)
b3.place(relx=0.55,rely=0.65,relwidth=0.4,relheight=0.15)


root.mainloop()
