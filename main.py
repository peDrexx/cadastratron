# Projeto tão simples que funciona só com um arquivo, mas ainda sim vai ser súper útil pra mim
# Não vai funcionar só em um arquivo não, mudei de ideia.

# Preparando as funções do xl_handle
import xl_handle as xlH

# Função de exportar os dados
def xl_export_cadastrados():
    # Função que é chamada quando o botão de Salvar é apertado
    def Trigger_export():
        xlH.xl_export(listbox, input_nome_do_arquivo.get())
        janela_export.destroy()

    # Janela para escolher o nome do arquivo exportado
    janela_export = tk.Toplevel(janela)
    janela_export.title("Salvar Contatos")
    janela_export.focus_set()

    lbl_nome_do_arquivo = tk.Label(janela_export, text="Escolha o nome do arquivo (incluir .xlsx)")
    lbl_nome_do_arquivo.grid(row=3, column=1)

    input_nome_do_arquivo = tk.Entry(janela_export)
    input_nome_do_arquivo.grid(row=4, column=1)

    btn_enviar = tk.Button(janela_export, text="Salvar", command=Trigger_export)
    btn_enviar.grid(row=5, column=1)

# Função para importar planilhas
def xl_import_cadastrados():
    arquivo_planilha = filedialog.askopenfilename(filetypes=[("Planilhas", "*.xlsx")])

    xlH.xl_import(dados_cadastrados, arquivo_planilha)
    print(dados_cadastrados)
    listar_cadastrados()

import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
lista_dados = []
dados_cadastrados = []

# Função executada ao clicar no botao de enviar
def enviar():
    # Catando os dados do formulario
    RazaoSocial = input_razaoSocial.get()
    BairroMunicipio = input_bairroMunicipio.get()
    Telefone = input_telefone.get()
    Email = input_email.get()
    Representante = input_representante.get()

    # Adicionando os dados ao Array de dados
    dados = [RazaoSocial, Telefone, Email, BairroMunicipio, Representante]
    # Integrando ao array de cadastrados
    dados_cadastrados.append(dados)

    # Limpando os dados da tela de cadastro
    input_razaoSocial.delete(0, tk.END)
    input_bairroMunicipio.delete(0, tk.END)
    input_telefone.delete(0, tk.END)
    input_email.delete(0, tk.END)
    input_representante.delete(0, tk.END)

    print('Dados cadastrados.')
    print(dados_cadastrados)
    texto_enviado.config(text="Dados cadastrados.")
    aba1.after(2000, resetarMSG)

    listar_cadastrados()

def resetarMSG():
    texto_enviado.config(text="")

# Criando a janela
janela = tk.Tk()

# Definindo o nome da janela e suas respectivas abas (Cadastro e Registro)
janela.title("Cadastratron")
notebook = ttk.Notebook(janela)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)

# Definindo onde vai ficar e o nome de cada aba
notebook.grid(row=0, column=0, padx=10, pady=10, columnspan=15)
notebook.add(aba1, text="Cadastro")
notebook.add(aba2, text="Registrados")

janela.columnconfigure(0, weight=1)
notebook.columnconfigure(0, weight=1)

# Criando e posicionando os campos que devem ser preenchidos e os nomes deles.
# (ABA 1)
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

# Botão de enviar
btn = tk.Button(aba1, text="Enviar", command=enviar)
btn.grid(row=4, column=2, padx=20, pady=20, sticky='nswe', columnspan=4)

texto_enviado = tk.Label(aba1, text="")
texto_enviado.grid(row=4, column=6, padx=20, pady=20, sticky='nswe', columnspan=1)

# (ABA 2)
# Lista de cadastrados
aba2.columnconfigure(0, weight=1)
def listar_cadastrados():

    listbox.delete(0, tk.END)
    for i in dados_cadastrados:
            listbox.insert(tk.END, " | ".join(i))

# Função de salvar os dados num arquivo txt
def salvar():
    dados = listbox.get(0, tk.END) # Catando os dados da lista
    with open('cache.txt', 'w') as arquivo:
        for item in dados:
            arquivo.write(item + '\n')

def limpar():
    listbox.delete(0, tk.END)
def restaurar():
    try:
        with open('cache.txt', 'r') as arquivo:
            for linha in arquivo:
                item = linha.strip()
                listbox.insert(tk.END, item)

    except FileNotFoundError:
        pass

lbl_cadastrados = tk.Label(aba2, text="Registros")
lbl_cadastrados.grid(row=1, column=0, padx=20, pady=20, sticky='nswe', columnspan=1)

btn_salvar = tk.Button(aba2, text="💾", command=salvar)
btn_salvar.grid(row=1, column=2, padx=20, pady=20, sticky='nswe', columnspan=1)

btn_limpar = tk.Button(aba2, text="❌", command=limpar)
btn_limpar.grid(row=1, column=3, padx=20, pady=20, sticky='nswe', columnspan=1)

btn_restaurar = tk.Button(aba2, text="🔁", command=restaurar)
btn_restaurar.grid(row=1, column=4, padx=20, pady=20, sticky='nswe', columnspan=1)

listbox = tk.Listbox(aba2)
listbox.grid(row=2, column=0, padx=20, pady=20, sticky='nswe')

# Atualizando a largura da listbox
def redimensionar_listbox(event):
    largura_notebook = notebook.winfo_width()
    largura_listbox = int(largura_notebook * 0.2)
    listbox.config(width=largura_listbox)

# Redimensionando tamanho da tela de cadastro (Remover, talvez...)
def redimensionar_cadastro(event):
    largura_notebook = notebook.winfo_width()
    largura_cadastro = int(largura_notebook * 0.2)

aba1.bind("<Configure>", redimensionar_cadastro)
aba2.bind("<Configure>", redimensionar_listbox)

btn_export = tk.Button(aba2, text="⬆️", command=xl_export_cadastrados)
btn_export.grid(row=3, column=2, padx=20, pady=20, columnspan=1)

btn_import = tk.Button(aba2, text="⬇️", command=xl_import_cadastrados)
btn_import.grid(row=3, column=3, padx=20, pady=20, columnspan=1)

janela.mainloop()

# O que falta:
# -- Importar e exportar arquivos de planilhas
# -- Quick save e limpar a listbox
# -- Encontrar um cliente para vender meus serviços de criação de sites :)