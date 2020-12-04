from tkinter import *


def centralizar(master, coord):
    largura = int(coord[0])
    altura = int(coord[1])
    largura_screen = master.winfo_screenwidth()
    altura_screen = master.winfo_screenheight()

    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    return f'{posx:.0f}+{posy:.0f}'


def login():
    login = Label(banco, text=f'Você Entrou Como {text_user.get()}')
    login.place(relx=0.2, rely=0.7)


banco = Tk()
banco.title("PyBank")
banco.geometry("200x100+"+centralizar(banco, [200, 50]))
banco.resizable(False, False)

user = Label(banco, text='Usuário', font='Times 10')
user.place(relx=0, rely=0.3, anchor='w')
text_user = Spinbox(banco, values=("--- ---",'Root', 'Cliente'), wrap=True, justify='center')
text_user.place(relx=0.3, rely=0.3, anchor='w')
cmd_login = Button(banco, text='Login', command=login)
cmd_login.place(relx=0.4, rely=0.5)


banco.mainloop()
