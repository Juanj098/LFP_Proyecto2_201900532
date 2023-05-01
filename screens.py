import tkinter as tk
from tkinter import*
import os
from fileinput import filename
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Treeview
from analisis import list_commands
from sintactico.Sintactico import E_Sintacticos
from lexico.Lexico import list_E
from analisis import analisis
from analisis import result
from analisis import command

class Home(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg ='#404754')
        self.controller = controller
        self.init_widgets()


    def init_widgets(self):
        tk.Label(
            self,
            text = 'Proyecto no.2',
            justify = tk.CENTER,
            font = ('Jetbrains mono',16),
            bg='#404754'
            ).pack(
                side=tk.TOP,
                fill=tk.BOTH,
                expand= True,
                padx=22,
                pady=11
            )
#-> Izq
        optionsFrame_Izq = tk.Frame(self)
        optionsFrame_Izq.configure(
            bg='#404754',
            # width=200
        )
        optionsFrame_Izq.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx = 10,
            pady=11
        )
        btn1 = tk.Button(
                optionsFrame_Izq,
                text='Abrir',
                font=('Jetbrains mono',10),
                width=20,
                height=2,
                command=self.openFile
            )
        btn1.grid(row=1,column=0,padx=3,pady=3)
        btn2 = tk.Button(
            optionsFrame_Izq,
            text='Guardar',
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command=self.savaChange
        )
        btn2.grid(row =2,column=0,padx=3,pady=3)
        btn3 = tk.Button(
            optionsFrame_Izq,
            text='Analizar',
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command=self.analisis 
        )
        btn3.grid(row=3,column=0,padx=3,pady=3)
        btn4 = tk.Button(
            optionsFrame_Izq,
            text='Errores',
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            # command=
        )
        btn4.grid(row=7,column=0,padx=3,pady=3)
        btn5 = tk.Button(
            optionsFrame_Izq,
            text="SALIR",
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command= self.quit
        )
        btn5.grid(row=9,column=0,padx=3,pady=3)

#-> der
        optionsFrame_Der = tk.Frame(self)

        optionsFrame_Der.configure(
            bg='#404754'
        )
        optionsFrame_Der.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx = 22,
            pady=11
        )
        self.Txt = tk.Text(
            optionsFrame_Der,
            font=('Jetbrains Mono',10),
            width=75,
            bg='#e5be77'
            )
        self.Txt.grid(row=1,column=1)

        self.txt_2 = tk.Text(
            optionsFrame_Der,
            font=('Jetbrains Mono',10),
            bg='#b6b5bd',
            width=75,
            state='disabled'
        )
        self.txt_2.grid(row=1,column=3,padx=3)

# -> functions

    def openFile(self):
        x = ''
        Tk().withdraw()
        try:
            self.filename = askopenfilename(
                title='Seleccione Archivo',
                filetypes=[('Archivos',f'*.lfp')]
                )
            with open(self.filename,encoding='UTF-8') as file:
                x = file.read()
        except:
            print('Error: No se selecciono ningun documento')
            return
        self.Insert(x)
        self.txt = x
        
    def Insert(self,txt):
        self.Txt.delete(1.0,tk.END)
        self.Txt.insert(1.0,txt)   
    
    def savaChange(self):
        try:
            mod = self.Txt.get(1.0,tk.END)
            with open(self.filename,'w+',encoding='UTF-8') as file:
                file.write(mod)
        except:
            print('Variable vacia')
            
    def analisis(self):
        list_E.clear()
        E_Sintacticos.clear()
        list_commands.clear()

        txt = self.Txt.get(0.1,tk.END)
        analisis(txt)
        command()    
        self.txt_2.configure(state="normal")
        self.txt_2.delete(1.0,tk.END)
        for com in list_commands:
            self.txt_2.insert(END,f'-> {com}\n')
        self.txt_2.configure(state="disabled")

    def Errors(self):
        pass
        # list_error.clear()
        # cadena = 'ERRORES_201900532\n'
        # cadena +='{\n'
        # txt = self.Txt.get(1.0,tk.END)
        # instruccion(txt)
        # cont = 0
        # for err in list_error:
        #     if err != None:
        #         cadena+='\t{\n'
        #         cadena+=f'\t\t"No.":{str(cont)}\n'
        #         cadena+='\t\t"Descripcion-Token":{\n'
        #         cadena+=f'\t\t\t\t"Lexema":{err.geterror()}\n'
        #         cadena+=f'\t\t\t\t"Tipo":Error\n'
        #         cadena+=f'\t\t\t\t"Columna":{err.getCol()}\n'
        #         cadena+=f'\t\t\t\t"Fila":{err.getFila()}\n'
        #         cadena+='\t\t}\n'
        #         cadena+='\t},\n'
        #         cont = cont+1
        # cadena+='}'
        # print(cadena)
        # self.txt_2.configure(state="normal")
        # self.txt_2.delete(1.0,tk.END)
        # self.txt_2.insert(1.0,cadena)
        # self.txt_2.configure(state="disabled")
        
            
class Proy(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg ='black')
        self.controller = controller