import pafy
from tkinter import *
from tkinter import filedialog
from DowYou import Download


class Application:

    def __init__(self, master=None):

        self.fonte = ("Helvetica", "24","bold")
        self.container1 = Frame(master)
        self.container1["pady"] =20  
        self.container1.pack()
        
        self.container2 = Frame(master,background="white")
        self.container2.pack()
        self.container2["pady"] = 50

        self.container3 = Frame(master,background="white")
        self.container3.pack()

        self.titulo = Label(self.container1,text="Downloads YouTube",foreground="#4A4238",background="white")
        self.titulo.pack()
        self.titulo["font"] = self.fonte

        self.botao1 = Button(self.container2,text="Lista De Links",foreground="#79C99E",background="#4D5359",font=("Helvetica",14),command=self.modalInformativo)
        self.botao1.pack(side=LEFT)
        
        
        self.branco = Label(self.container2,text="   ",background="white")
        self.branco.pack(side=LEFT)

        self.botao2 = Button(self.container2,text="Lista De Nomes",foreground="#79C99E",background="#4D5359",font=("Helvetica",14))
        self.botao2.pack(side=LEFT)

        self.status =  Label(self.container3,background="white", foreground="#97DB4F",font=("Helvetica",14))
        self.status["text"] = ""
        self.status.pack()
        
        self.dowYou = Download()       
    
    def modalInformativo(self):

        self.janelaEscolhaLista = Toplevel(root)
        self.janelaEscolhaLista.geometry("550x200")
        self.janelaEscolhaLista["pady"]=10
        labelRegrasLista = Label(self.janelaEscolhaLista, text = "A lista deve estar no formato TXT e cada link deve ser separado por ponto e virgula ';'",font=("Helvetica",10,"bold"),foreground="red")
        buttonEscolherLista = Button(self.janelaEscolhaLista, text = "Selecionar Lista",command=self.selecionaListaDeLinks)
        buttonEscolherLista["pady"] = 20

        labelRegrasLista.pack()
        buttonEscolherLista.pack()
    
    def selecionaListaDeLinks(self):
        self.path = filedialog.askopenfilename()
        self.dowYou.organizaLista(self.path)
        self.baixar()
        self.janelaEscolhaLista.destroy()
        
        
    def baixar(self):
        self.dowYou.download()
        
            
root = Tk()
root.geometry("500x300")
root.title("Downloads YouTube")
root.configure(background="white")
Application(root)


root.mainloop()
