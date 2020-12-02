import tkinter


def centralizar(master, coord):
    largura = int(coord[0])
    altura = int(coord[1])
    largura_screen = master.winfo_screenwidth()
    altura_screen = master.winfo_screenheight()

    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    return f'{posx:.0f}+{posy:.0f}'


banco = tkinter.Tk()
banco['bg'] = 'black'
banco.title("PyBank")
banco.geometry("200x100+"+centralizar(banco, [200,50]))
banco.resizable(False, False)

user = tkinter.Label(banco, text='Usuário', bg = 'black', fg='green', font = 'Times 10')
escolha_user = tkinter.Spinbox(banco, values=('Root', 'Cliente'), wrap=True, bg='black', fg='green', font = 'Times 10')
login = tkinter.Button(banco, text='Login', command = lambda: print(f"Entrando como {escolha_user.get()}..."), bg = 'black', fg='green', font = 'Times 10')

tkinter.Label(banco, text='          ', bg = 'black').grid(row=0, column=0)
user.grid(row=0, column=1, sticky='nswe')
escolha_user.grid(row=1, column=1, sticky='nswe')
login.grid(row=2, column=1, sticky='nswe')

banco.mainloop()