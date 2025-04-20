import tkinter as tk
from PIL import ImageTk, Image
import os
from pygame import mixer

mixer.init()

palavras = [
    "bola", "casa", "medo", "meia", "sapato", "teia", "elefante", "sapo", "mala", "pato",
    "lupa", "luva", "lata", "gato", "rato", "vaca", "lobo", "urso", "peixe", "foca",
    "anta", "corvo", "livro", "papel", "nuvem", "fogo", "moto", "barco", "cavalo",
    "girafa", "tartaruga", "esquilo", "telefone", "panela", "janela", "relogio",
    "pipoca", "sorvete", "estrela", "ovo", "suco", "macaco", "borboleta"
]

imagens = [
    "imagens/bola.jpg", "imagens/casa.jpg", "imagens/medo.jpg", "imagens/meia.jpg", "imagens/sapato.jpg",
    "imagens/teia.png", "imagens/elefante.jpg", "imagens/sapo.jpg", "imagens/mala.jpg", "imagens/pato.jpg",
    "imagens/lupa.jpg", "imagens/luva.jpg", "imagens/lata.jpg", "imagens/gato.jpg", "imagens/rato.jpg",
    "imagens/vaca.jpg", "imagens/lobo.jpg", "imagens/urso.jpg", "imagens/peixe.jpg", "imagens/foca.png",
    "imagens/anta.jpg", "imagens/corvo.png", "imagens/livro.png", "imagens/papel.jpg", "imagens/nuvem.jpg",
    "imagens/fogo.png", "imagens/moto.jpg", "imagens/barco.jpg", "imagens/cavalo.jpg", "imagens/girafa.jpg",
    "imagens/tartaruga.jpg", "imagens/esquilo.jpg", "imagens/telefone.jpg", "imagens/panela.jpg", "imagens/janela.jpg",
    "imagens/relogio.jpg", "imagens/pipoca.png", "imagens/sorvete.jpg", "imagens/estrela.jpg", "imagens/ovo.jpg",
    "imagens/suco.jpg", "imagens/macaco.jpg", "imagens/borboleta.jpg"
]

audios = [
    "audios/bola.mp3", "audios/casa.mp3", "audios/medo.mp3", "audios/meia.mp3", "audios/sapato.mp3",
    "audios/teia.mp3", "audios/elefante.mp3", "audios/sapo.mp3", "audios/mala.mp3", "audios/pato.mp3",
    "audios/lupa.mp3", "audios/luva.mp3", "audios/lata.mp3", "audios/gato.mp3", "audios/rato.mp3",
    "audios/vaca.mp3", "audios/lobo.mp3", "audios/urso.mp3", "audios/peixe.mp3", "audios/foca.mp3",
    "audios/anta.mp3", "audios/corvo.mp3", "audios/livro.mp3", "audios/papel.mp3", "audios/nuvem.mp3",
    "audios/fogo.mp3", "audios/moto.mp3", "audios/barco.mp3", "audios/cavalo.mp3", "audios/girafa.mp3",
    "audios/tartaruga.mp3", "audios/esquilo.mp3", "audios/telefone.mp3", "audios/panela.mp3", "audios/janela.mp3",
    "audios/relógio.mp3", "audios/pipoca.mp3", "audios/sorvete.mp3", "audios/estrela.mp3", "audios/ovo.mp3",
    "audios/suco.mp3", "audios/macaco.mp3", "audios/borboleta.mp3"
]

caminho = os.path.dirname(__file__)
indice = 0

def verificar():
    resposta = entrada.get().lower()
    if resposta == palavras[indice]:
        resultado.config(text="Acertou!", fg="green")
        proximo()
    else:
        resultado.config(text="Tente novamente.", fg="red")

def proximo():
    global indice
    indice += 1
    if indice < len(palavras):
        carregar_imagem()
        entrada.delete(0, tk.END)
        resultado.config(text="")
    else:
        resultado.config(text="Parabéns! Você completou o jogo.", fg="blue")
        entrada.config(state="disabled")
        botao_verificar.config(state="disabled")
        botao_audio.config(state="disabled")

def carregar_imagem():
    imagem_path = os.path.join(caminho, imagens[indice])
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((300, 300))
    imagem_tk = ImageTk.PhotoImage(imagem)
    painel.config(image=imagem_tk)
    painel.image = imagem_tk

def tocar_audio():
    mixer.music.load(os.path.join(caminho, audios[indice]))
    mixer.music.play()

def mostrar_tela(tela):
    for frame in [tela_principal, tela_portugues, tela_matematica, tela_historia]:
        frame.pack_forget()
    tela.pack(fill="both", expand=True)
    if tela == tela_portugues:
        global indice
        indice = 0
        carregar_imagem()
        entrada.config(state="normal")
        botao_verificar.config(state="normal")
        botao_audio.config(state="normal")
        entrada.delete(0, tk.END)
        resultado.config(text="")

# === Interface ===
root = tk.Tk()
root.title("App Educativo")
root.geometry("800x800")  # Define a resolução mínima
root.minsize(800, 800)  # Definir o tamanho mínimo da janela
root.state("normal")  # Permitir redimensionamento

# Cor do fundo das telas (verde mais claro)
COR_FUNDO = "#f1fdf3"  # Fundo mais claro
# Cor dos botões (verde mais claro)
COR_BOTAO = "#b2e1a1"  # Verde mais claro
# Cor do texto dos botões (verde escuro)
COR_TEXTO = "#2a8c2f"  # Verde escuro

# === Tela Principal ===
tela_principal = tk.Frame(root, bg=COR_FUNDO)
tela_principal.pack(fill="both", expand=True)

fundo_img = Image.open("C:/Users/Kids/Desktop/meu_app/fundo.png")
fundo_img = fundo_img.resize((500, 500))
fundo_tk = ImageTk.PhotoImage(fundo_img)
fundo_label = tk.Label(tela_principal, image=fundo_tk, bd=0, bg=COR_FUNDO)  # Fundo transparente
fundo_label.place(relx=0.5, rely=0.5, anchor="center")

layout = tk.Frame(tela_principal, bg=COR_FUNDO)
layout.place(relx=0.5, rely=0.8, anchor="center")

btn_portugues = tk.Button(layout, text="Português", width=20, height=2, bg=COR_BOTAO, fg=COR_TEXTO, command=lambda: mostrar_tela(tela_portugues))
btn_matematica = tk.Button(layout, text="Matemática", width=20, height=2, bg=COR_BOTAO, fg=COR_TEXTO, command=lambda: mostrar_tela(tela_matematica))
btn_historia = tk.Button(layout, text="História", width=20, height=2, bg=COR_BOTAO, fg=COR_TEXTO, command=lambda: mostrar_tela(tela_historia))

btn_portugues.pack(side="left", padx=10)
btn_matematica.pack(side="left", padx=10)
btn_historia.pack(side="left", padx=10)

# === Tela Português ===
tela_portugues = tk.Frame(root, bg=COR_FUNDO)
painel = tk.Label(tela_portugues, bg=COR_FUNDO)  # Altere o fundo aqui também
painel.pack(pady=10)

entrada = tk.Entry(tela_portugues, font=("Arial", 20))
entrada.pack(pady=10)

botao_verificar = tk.Button(tela_portugues, text="Verificar", width=20, height=2, command=verificar, bg=COR_BOTAO, fg=COR_TEXTO)
botao_verificar.pack(pady=5)

botao_audio = tk.Button(tela_portugues, text="Ouvir Palavra", width=20, height=2, command=tocar_audio, bg=COR_BOTAO, fg=COR_TEXTO)
botao_audio.pack(pady=5)

btn_voltar1 = tk.Button(tela_portugues, text="Voltar", width=20, height=2, command=lambda: mostrar_tela(tela_principal), bg=COR_BOTAO, fg=COR_TEXTO)
btn_voltar1.pack(pady=10)

resultado = tk.Label(tela_portugues, text="", font=("Arial", 16))
resultado.pack(pady=10)

# === Tela Matemática ===
tela_matematica = tk.Frame(root, bg=COR_FUNDO)
tk.Label(tela_matematica, text="Conteúdo de Matemática", bg=COR_FUNDO).pack(pady=20)
tk.Button(tela_matematica, text="Voltar", width=20, height=2, command=lambda: mostrar_tela(tela_principal), bg=COR_BOTAO, fg=COR_TEXTO).pack()

# === Tela História ===
tela_historia = tk.Frame(root, bg=COR_FUNDO)
tk.Label(tela_historia, text="Conteúdo de História", bg=COR_FUNDO).pack(pady=20)
tk.Button(tela_historia, text="Voltar", width=20, height=2, command=lambda: mostrar_tela(tela_principal), bg=COR_BOTAO, fg=COR_TEXTO).pack()

# === Iniciar App ===
mostrar_tela(tela_principal)
root.mainloop()
