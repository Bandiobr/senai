import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("350x200")

def login():
    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "Lucas" and  senha == "123":
        messagebox("Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

lbl_login = ttk.Label(
    janela,
    text="Login:"
)
lbl_login.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)
edt_login = ttk.Entry(
    janela,
    width=25
)
edt_login.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
)
#senha
lbl_senha = ttk.Label(
    janela,
    text="Senha:"
)
lbl_senha.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
)
edt_senha = ttk.Entry(
    janela,
    width=25,
    show="*"
)
edt_senha.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
)
janela.mainloop()
