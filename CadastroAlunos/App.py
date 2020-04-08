from Usuarios import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2,text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblra = Label(self.container4, text="RA:",font=self.fonte, width=10)
        self.lblra.pack(side=LEFT)
        self.txtra = Entry(self.container4)
        self.txtra["width"] = 25
        self.txtra["font"] = self.fonte
        self.txtra.pack(side=LEFT)

        self.lbldisc = Label(self.container5, text="Disciplinas:",font=self.fonte, width=10)
        self.lbldisc.pack(side=LEFT)
        self.txtdisc = Entry(self.container5)
        self.txtdisc["width"] = 25
        self.txtdisc["font"] = self.fonte
        self.txtdisc.pack(side=LEFT)

        self.lblmd = Label(self.container6, text="Médias:", font=self.fonte, width=10)
        self.lblmd.pack(side=LEFT)
        self.txtmd = Entry(self.container6)
        self.txtmd["width"] = 25
        self.txtmd["font"] = self.fonte
        self.txtmd.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=8)
        self.bntInsert["command"] = self.testeDados
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",font=self.fonte, width=8)
        self.bntAlterar["command"] = self.testeDados
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",font=self.fonte, width=8)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def testeDados(self):
        if str(self.txtmd.get()).isnumeric() and str(self.txtra.get()).isnumeric():
            return True
        else:
            self.lblmsg["text"] = 'Dados inválidos'

    def inserirUsuario(self):
        user = Usuarios()
        if self.testeDados() == True:
            user.nome = self.txtnome.get()
            user.ra = self.txtra.get()
            user.materia = self.txtdisc.get()
            user.media = self.txtmd.get()

            self.lblmsg["text"] = user.insertUser()

            self.txtidusuario.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtra.delete(0, END)
            self.txtdisc.delete(0, END)
            self.txtmd.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()
        if self.testeDados() == True:
            user.idusuario = self.txtidusuario.get()
            user.nome = self.txtnome.get()
            user.ra = self.txtra.get()
            user.materia = self.txtdisc.get()
            user.media = self.txtmd.get()

            self.lblmsg["text"] = user.updateUser()

            self.txtidusuario.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtra.delete(0, END)
            self.txtdisc.delete(0, END)
            self.txtmd.delete(0, END)


    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtra.delete(0, END)
        self.txtdisc.delete(0, END)
        self.txtmd.delete(0, END)


    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtra.delete(0, END)
        self.txtra.insert(INSERT, user.ra)

        self.txtdisc.delete(0, END)
        self.txtdisc.insert(INSERT, user.materia)

        self.txtmd.delete(0, END)
        self.txtmd.insert(INSERT, user.media)


root = Tk()
Application(root)
root.mainloop()