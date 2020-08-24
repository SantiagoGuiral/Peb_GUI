import tkinter as tk
import peb_fun as pfun

data=[]
probTramo=[]
qxtmp=[]
pTramo=[]
pstring=""
qxstring=""
tramoArg=""

def restart():
    global data,probTramo,qxtmp,pTramo,pstring,qxstring,tramoArg
    data=[]
    probTramo=[]
    qxtmp=[]
    pTramo=[]
    pstring=""
    qxstring=""
    tramoArg=""
    i1.delete(0,"end")
    i2.delete(0,"end")
    i3.delete(0,"end")
    clearLabels()

def clearLabels():
    lerror=tk.Label(fl3,text="")
    lerror.place(relx=0.55,rely=0.42,relwidth=0.4,relheight=0.30)
    lqx=tk.Label(fl3,text="")
    lqx.place(relx=0.05,rely=0.42,relwidth=0.4,relheight=0.30)
    ldata=tk.Label(fl3,text="")
    ldata.place(relx=0.05,rely=0.06,relwidth=0.4,relheight=0.30)
    lresult=tk.Label(fl3,text="")
    lresult.place(relx=0.05,rely=0.84,relwidth=0.9,relheight=0.04)
    ltramo=tk.Label(fl3,text="")
    ltramo.place(relx=0.55,rely=0.06,relwidth=0.4,relheight=0.30)
    

def printqx(x):
    global qxstring
    qxstring=qxstring + f'{x:.3}\n'
    lqx=tk.Label(fl3,text=qxstring)
    lqx.place(relx=0.05,rely=0.42,relwidth=0.4,relheight=0.30)

def printError(error):
    global pstring
    pstring=pstring + f'{error:.6%}\n'
    lerror=tk.Label(fl3,text=pstring)
    lerror.place(relx=0.55,rely=0.42,relwidth=0.4,relheight=0.30)

def init_data(tr,a,b):
    data.append(int(tr))
    data.append(int(a))
    data.append(int(b))
    txt=f'Tramos: {tr}\nNumerador Q(x): {a}\nDenominador Q(x): {b}'
    ldata=tk.Label(fl3,text=txt)
    ldata.place(relx=0.05,rely=0.06,relwidth=0.4,relheight=0.30)

def tramo_data(at,vt,n):
    global tramoArg
    tramoArg=tramoArg+f'At:{at} Vt:{vt} N:{n}\n'
    ltramo=tk.Label(fl3,text=tramoArg)
    ltramo.place(relx=0.55,rely=0.06,relwidth=0.4,relheight=0.30)

def tr_info(tramo):
    At,Vt,N=[float(i) for i in tramo.split(",")]
    tramo_data(At,Vt,N)
    x=(data[1]*pfun.voltage(At,Vt))/(data[2]*pfun.sigma(N))
    qxtmp.append(x)
    probTramo.append(pfun.q(x))
    printqx(x)
    printError(pfun.q(x))
    i4.delete(0,"end")

def prob():
    probTotal=0
    for i in range(2**data[0]):
        bits=bin(i).lstrip("-0b").zfill(data[0])
        error=pfun.peb(bits,probTramo)
        pTramo.append(error)
        probTotal+=error
    probPrint=f'{probTotal:.5%}'
    lresult=tk.Label(fl3,text=probPrint)
    lresult.place(relx=0.05,rely=0.84,relwidth=0.9,relheight=0.04)


root=tk.Tk()
root.title("Probabilidad de error en una red de enlaces")
root.geometry("900x600+600+200")

title=tk.Frame(root)
title.place(rely=0.02,relwidth=0.9,relheight=0.06,relx=0.05)

label=tk.Label(title,text="Software para encontrar el valor de error de probabilidad de bit en una red de enlaces")
label.place(relx=0.05,relwidth=0.70,relheight=0.9)

brestart=tk.Button(title,text="Reiniciar",command=restart)
brestart.place(relx=0.80,relwidth=0.15,relheight=0.9)

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
l2=tk.Label(fl1,text="Numerador q(x):")
l2.place(relx=0.05,rely=0.425,relwidth=0.4,relheight=0.15)
l3=tk.Label(fl1,text="Denominador(qx):")
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

l4=tk.Label(fl3,text="Datos:")
l4.place(relx=0.05,rely=0.02,relwidth=0.4,relheight=0.03)
l4=tk.Label(fl3,text="Tramo:")
l4.place(relx=0.55,rely=0.02,relwidth=0.4,relheight=0.03)
l6=tk.Label(fl3,text="Q(x) tramo:")
l6.place(relx=0.05,rely=0.38,relwidth=0.4,relheight=0.03)
l7=tk.Label(fl3,text="Error tramo:")
l7.place(relx=0.55,rely=0.38,relwidth=0.4,relheight=0.03)
lr=tk.Label(fl3,text="La probabilidad de error total es:")
lr.place(relx=0.05,rely=0.80,relwidth=0.9,relheight=0.03)


root.mainloop()
