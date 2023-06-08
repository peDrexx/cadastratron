# já joguei pro github!

import tkinter as tk
from tkinter import ttk

def enviar():
    print('Dados integrados a planilha!')

janela = tk.Tk()

janela.title("Cadastratron")
notebook = ttk.Notebook(janela)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)

notebook.grid(row=0, column=0, padx=10, pady=10)
notebook.add(aba1, text="Cadastro")
notebook.add(aba2, text="Registrados")

lbl_razaoSocial = tk.Label(aba1, text="Razão Social *")
lbl_razaoSocial.grid(row=1, column=0, padx=20, pady=20, sticky='nswe', columnspan=4)

input_razaoSocial = tk.Entry(aba1)
input_razaoSocial.grid(row=1, column=5, padx=20, pady=20, sticky='nswe', columnspan=1)

lbl_telefone = tk.Label(aba1, text="Telefone *")
lbl_telefone.grid(row=2, column=0, padx=20, pady=20, sticky='nswe', columnspan=1)

input_telefone = tk.Entry(aba1)
input_telefone.grid(row=2, column=5, padx=20, pady=20, sticky='nswe', columnspan=1)

lbl_email = tk.Label(aba1, text="Email *")
lbl_email.grid(row=3, column=0, padx=10, pady=20, sticky='nswe')

input_email = tk.Entry(aba1)
input_email.grid(row=3, column=5, padx=20, pady=20, sticky='nswe', columnspan=2)

lbl_bairroMunicipio = tk.Label(aba1, text="Bairro, Município")
lbl_bairroMunicipio.grid(row=1, column=6, padx=20, pady=20, sticky='nswe', columnspan=1)

input_bairroMunicipio = tk.Entry(aba1)
input_bairroMunicipio.grid(row=1, column=7, padx=20, pady=20, sticky='nswe', columnspan=5)

lbl_representante = tk.Label(aba1, text="Representante")
lbl_representante.grid(row=2, column=6, padx=20, pady=20, sticky='nswe', columnspan=1)

input_representante = tk.Entry(aba1)
input_representante.grid(row=2, column=7, padx=20, pady=20, sticky='nswe', columnspan=4)

btn = tk.Button(aba1, text="Enviar", command=enviar)
btn.grid(row=4, column=2, padx=20, pady=20, sticky='nswe', columnspan=4)

janela.mainloop()
