from tkinter import *
from Pack import usuarios

class Login(Frame):
    def __init__(self, parent):
        super().__init__()
        self['bg'] = 'Blue'
        self['width'] = 200
        self['height'] = 100

        self.user = Label(self, text='Usuário', font='Times 10')
        self.user.place(x=75,y=10)
        self.text_user = Spinbox(self, values=("--- ---",'Root', 'Cliente'), wrap=True, justify='center')
        self.text_user.place(x=35,y=30)
        self.cmd_login = Button(self, text='Login', command=self.login)
        self.cmd_login.place(x=80, y=50)

    def login(self):
        esc = self.text_user.get()
        if esc != '--- ---' and usuarios.Users(esc):
            login = Label(self, text=f'Você Entrou Como {esc}')
            login.place(x=30, y=70)
        elif esc != '--- ---' and not usuarios.Users(esc):
            self.cmd_login.place(x=5000, y=5000)
            self.user.place(x=5000, y=5000)      


def centralizar(master, coord):
    largura = int(coord[0])
    altura = int(coord[1])
    largura_screen = master.winfo_screenwidth()
    altura_screen = master.winfo_screenheight()

    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    return f'{posx:.0f}+{posy:.0f}'


banco = Tk()
banco.title("PyBank")
banco.geometry("200x100+"+centralizar(banco, [200, 100]))
banco.resizable(False, False)

login = Login(banco).place(x=1,y=1)

banco.mainloop()
