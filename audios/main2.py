import tkinter as tk

# Funções para trocar de tela
def mostrar_tela_principal():
    esconder_todas()
    tela_principal.pack()

def mostrar_portugues():
    esconder_todas()
    tela_portugues.pack()

def mostrar_matematica():
    esconder_todas()
    tela_matematica.pack()

def mostrar_historia():
    esconder_todas()
    tela_historia.pack()

def esconder_todas():
    tela_principal.pack_forget()
    tela_portugues.pack_forget()
    tela_matematica.pack_forget()
    tela_historia.pack_forget()

# Criação da janela principal
root = tk.Tk()
root.title("App Educativo")
root.geometry("300x300")

# Tela principal
tela_principal = tk.Frame(root)
btn_portugues = tk.Button(tela_principal, text="Português", command=mostrar_portugues)
btn_matematica = tk.Button(tela_principal, text="Matemática", command=mostrar_matematica)
btn_historia = tk.Button(tela_principal, text="História", command=mostrar_historia)

btn_portugues.pack(pady=10)
btn_matematica.pack(pady=10)
btn_historia.pack(pady=10)

# Tela de Português
tela_portugues = tk.Frame(root)
lbl_portugues = tk.Label(tela_portugues, text="Conteúdo de Português")

btn_voltar1 = tk.Button(tela_portugues, text="Voltar", command=mostrar_tela_principal)
lbl_portugues.pack(pady=20)
btn_voltar1.pack()

# Tela de Matemática
tela_matematica = tk.Frame(root)
lbl_matematica = tk.Label(tela_matematica, text="Conteúdo de Matemática")
btn_voltar2 = tk.Button(tela_matematica, text="Voltar", command=mostrar_tela_principal)
lbl_matematica.pack(pady=20)
btn_voltar2.pack()

# Tela de História
tela_historia = tk.Frame(root)
lbl_historia = tk.Label(tela_historia, text="Conteúdo de História")
btn_voltar3 = tk.Button(tela_historia, text="Voltar", command=mostrar_tela_principal)
lbl_historia.pack(pady=20)
btn_voltar3.pack()

# Mostrar a tela principal ao iniciar
mostrar_tela_principal()

root.mainloop()
