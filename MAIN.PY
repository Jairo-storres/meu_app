import tkinter as tk
from PIL import ImageTk, Image
import os
from pygame import mixer

# Inicializar o mixer
mixer.init()

# Listas de palavras, imagens e áudios
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

caminho = os.path.join(os.path.dirname(__file__), "")
indice = 0

# Função para verificar a resposta
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

# Função para ir para a próxima palavra
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
        
# Função para carregar imagem
def carregar_imagem():
    imagem_path = os.path.join(caminho, imagens[indice])
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((400, 400))
    imagem_tk = ImageTk.PhotoImage(imagem)
    painel.config(image=imagem_tk)
    painel.image = imagem_tk

# Função para tocar áudio
def tocar_audio():
    mixer.music.load(os.path.join(caminho, audios[indice]))
    mixer.music.play()

# Interface principal
root = tk.Tk()
root.title("App Educativo")
root.geometry("800x800")

# Troca de telas
def mostrar_tela_principal():
    esconder_todas()
    tela_principal.pack()

def mostrar_portugues():
    global indice
    indice = 0
    esconder_todas()
    tela_portugues.pack()
    carregar_imagem()
    entrada.config(state="normal")
    botao_verificar.config(state="normal")
    botao_audio.config(state="normal")
    entrada.delete(0, tk.END)
    resultado.config(text="")

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

# Tela principal
tela_principal = tk.Frame(root)
btn_portugues = tk.Button(tela_principal, text="Português", width=30, command=mostrar_portugues)
btn_matematica = tk.Button(tela_principal, text="Matemática", width=30, command=mostrar_matematica)
btn_historia = tk.Button(tela_principal, text="História", width=30, command=mostrar_historia)


btn_portugues.pack(pady=15)
btn_matematica.pack(pady=15)
btn_historia.pack(pady=15)

# Tela de Português
tela_portugues = tk.Frame(root)
painel = tk.Label(tela_portugues)
painel.pack(pady=10)
pontuacao = 0

def atualizar_progresso():
    label_progresso.config(text=f"Palavra {indice + 1} de {len(palavras)}")

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


label_pontuacao = tk.Label(tela_portugues, text="Pontuação: 0", font=("Arial", 14))
label_pontuacao.pack(pady=5)

label_progresso = tk.Label(tela_portugues, text="Palavra 1 de 43", font=("Arial", 14))
label_progresso.pack(pady=5)


botao_audio = tk.Button(tela_portugues, text="Ouvir Palavra", command=tocar_audio)
botao_audio.pack(pady=5)

entrada = tk.Entry(tela_portugues, font=("Arial", 20))
entrada.pack(pady=10)

botao_verificar = tk.Button(tela_portugues, text="Verificar", command=verificar)
botao_verificar.pack(pady=5)

botao_avancar = tk.Button(tela_portugues, text="Avançar", command=proximo)
botao_avancar.pack(pady=5)

btn_voltar1 = tk.Button(tela_portugues, text="Voltar", command=mostrar_tela_principal)
btn_voltar1.pack(pady=10)

resultado = tk.Label(tela_portugues, text="", font=("Arial", 16))
resultado.pack(pady=10)


# Tela de Matemática
tela_matematica = tk.Frame(root)
lbl_matematica = tk.Label(tela_matematica, text="Conteúdo de Matemática")
lbl_matematica.pack(pady=20)
btn_voltar2 = tk.Button(tela_matematica, text="Voltar", command=mostrar_tela_principal)
btn_voltar2.pack()

# Tela de História
tela_historia = tk.Frame(root)
lbl_historia = tk.Label(tela_historia, text="Conteúdo de História")
lbl_historia.pack(pady=20)
btn_voltar3 = tk.Button(tela_historia, text="Voltar", command=mostrar_tela_principal)
btn_voltar3.pack()

# Iniciar na tela principal
mostrar_tela_principal()
root.mainloop()
