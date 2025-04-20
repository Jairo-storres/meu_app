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
   "imagens/bola.png", "imagens/casa.png", "imagens/medo.png", "imagens/meia.png", "imagens/sapato.png",
   "imagens/teia.png", "imagens/elefante.png", "imagens/sapo.png", "imagens/mala.png", "imagens/pato.png",
   "imagens/lupa.png", "imagens/luva.png", "imagens/lata.png", "imagens/gato.png", "imagens/rato.png",
   "imagens/vaca.png", "imagens/lobo.png", "imagens/urso.png", "imagens/peixe.png", "imagens/foca.png",
   "imagens/anta.png", "imagens/corvo.png", "imagens/livro.png", "imagens/papel.png", "imagens/nuvem.png",
   "imagens/fogo.png", "imagens/moto.png", "imagens/barco.png", "imagens/cavalo.png", "imagens/girafa.png",
   "imagens/tartaruga.png", "imagens/esquilo.png", "imagens/telefone.png", "imagens/panela.png", "imagens/janela.png",
   "imagens/relogio.png", "imagens/pipoca.png", "imagens/sorvete.png", "imagens/estrela.png", "imagens/ovo.png",
   "imagens/suco.png", "imagens/macaco.png", "imagens/borboleta.png"
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
pontuacao = 0

# Cores e visuais (da branch Nmayelle)
COR_FUNDO = "#f1fdf3"
COR_BOTAO = "#b2e1a1"
COR_TEXTO = "#2a8c2f"

# === Funções ===
def verificar():
    global pontuacao
    resposta = entrada.get().lower()
    if resposta == palavras[indice]:
        resultado.config(text="Acertou!", fg="green")
        pontuacao += 1
        label_pontuacao.config(text=f"Pontuação: {pontuacao}")
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
        atualizar_progresso()
    else:
        resultado.config(text="Parabéns! Você completou o jogo.", fg="blue")
        entrada.config(state="disabled")
        botao_verificar.config(state="disabled")
        botao_audio.config(state="disabled")

def carregar_imagem():
    imagem_path = os.path.join(caminho, imagens[indice])
    imagem = Image.open(imagem_path).resize((400, 400))
    imagem_tk = ImageTk.PhotoImage(imagem)
    painel.config(image=imagem_tk)
    painel.image = imagem_tk

def tocar_audio():
    mixer.music.load(os.path.join(caminho, audios[indice]))
    mixer.music.play()

def atualizar_progresso():
    label_progresso.config(text=f"Palavra {indice + 1} de {len(palavras)}")

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
        atualizar_progresso()

# === Interface ===
root = tk.Tk()
root.title("App Educativo")
root.geometry("800x800")
root.minsize(800, 800)
root.state("normal")

# === Tela Principal ===
tela_principal = tk.Frame(root, bg=COR_FUNDO)
tela_principal.pack(fill="both", expand=True)

# Fundo visual
fundo_img = Image.open("C:/Users/Kids/Desktop/meu_app/fundo.png").resize((500, 500))
fundo_tk = ImageTk.PhotoImage(fundo_img)
fundo_label = tk.Label(tela_principal, image=fundo_tk, bd=0, bg=COR_FUNDO)
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
painel = tk.Label(tela_portugues, bg=COR_FUNDO)
painel.pack(pady=10)

label_pontuacao = tk.Label(tela_portugues, text="Pontuação: 0", font=("Arial", 14), bg=COR_FUNDO, fg=COR_TEXTO)
label_pontuacao.pack(pady=5)

label_progresso = tk.Label(tela_portugues, text="Palavra 1 de 43", font=("Arial", 14), bg=COR_FUNDO, fg=COR_TEXTO)
label_progresso.pack(pady=5)

botao_audio = tk.Button(tela_portugues, text="Ouvir Palavra", width=20, height=2, command=tocar_audio, bg=COR_BOTAO, fg=COR_TEXTO)
botao_audio.pack(pady=5)

entrada = tk.Entry(tela_portugues, font=("Arial", 20), width=25)  # Aumentando o width
entrada.pack(pady=30)


# Criando o frame para alinhar os botões na horizontal
frame_botoes = tk.Frame(tela_portugues)
frame_botoes.pack(pady=10)

botao_verificar = tk.Button(frame_botoes, text="Verificar", width=15, height=2, command=verificar, bg=COR_BOTAO, fg=COR_TEXTO)
botao_verificar.pack(side="left", padx=5)

botao_avancar = tk.Button(frame_botoes, text="Avançar", width=15, height=2, command=proximo, bg=COR_BOTAO, fg=COR_TEXTO)
botao_avancar.pack(side="left", padx=5)

btn_voltar1 = tk.Button(frame_botoes, text="Voltar", width=15, height=2, command=lambda: mostrar_tela(tela_principal), bg=COR_BOTAO, fg=COR_TEXTO)
btn_voltar1.pack(side="left", padx=5)


resultado = tk.Label(tela_portugues, text="", font=("Arial", 16), bg=COR_FUNDO)
resultado.pack(pady=10)

# === Tela Matemática ===
tela_matematica = tk.Frame(root, bg=COR_FUNDO)
tk.Label(tela_matematica, text="Conteúdo de Matemática", bg=COR_FUNDO).pack(pady=20)
tk.Button(tela_matematica, text="Voltar", width=20, height=2, command=lambda: mostrar_tela(tela_principal), bg=COR_BOTAO, fg=COR_TEXTO).pack()

# === Tela História ===
tela_historia = tk.Frame(root, bg=COR_FUNDO)
tk.Label(tela_historia, text="Conteúdo de História", bg=COR_FUNDO).pack(pady=20)
tk.Button(tela_historia, text="Voltar", width=20, height=2, command=lambda: mostrar_tela(tela_principal), bg=COR_BOTAO, fg=COR_TEXTO).pack()

# Iniciar app
root.mainloop()
