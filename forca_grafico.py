import random
import tkinter as tk
from tkinter import messagebox

class JogoForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        
        self.palavra_secreta = self.carrega_palavra_secreta()
        self.letras_acertadas = self.inicializa_letras_acertadas(self.palavra_secreta)
        self.erros = 0

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.label_letras_acertadas = tk.Label(master, text=" ".join(self.letras_acertadas))
        self.label_letras_acertadas.pack()

        self.entry_chute = tk.Entry(master)
        self.entry_chute.pack()

        self.botao_chutar = tk.Button(master, text="Chutar", command=self.chutar)
        self.botao_chutar.pack()

        self.desenha_forca()

    def carrega_palavra_secreta(self):
        arquivo = open("palavras.txt", "r")
        palavras = [linha.strip().upper() for linha in arquivo]
        arquivo.close()
        return random.choice(palavras)

    def inicializa_letras_acertadas(self, palavra):
        return ["_" for letra in palavra]

    def atualiza_interface(self):
        self.label_letras_acertadas["text"] = " ".join(self.letras_acertadas)

    def desenha_forca(self):
        self.canvas.delete("all")

        if self.erros >= 1:
            self.canvas.create_line(50, 250, 200, 250)  # Base
        if self.erros >= 2:
            self.canvas.create_line(125, 250, 125, 50)  # Poste vertical
        if self.erros >= 3:
            self.canvas.create_line(125, 50, 200, 50)  # Barra horizontal superior
        if self.erros >= 4:
            self.canvas.create_oval(175, 50, 225, 100)  # Cabeça
        if self.erros >= 5:
            self.canvas.create_line(200, 100, 200, 175)  # Corpo
        if self.erros >= 6:
            self.canvas.create_line(200, 125, 150, 75)  # Braço esquerdo
        if self.erros >= 7:
            self.canvas.create_line(200, 125, 250, 75)  # Braço direito
        if self.erros >= 8:
            self.canvas.create_line(200, 175, 150, 225)  # Perna esquerda
        if self.erros == 9:
            self.canvas.create_line(200, 175, 250, 225)  # Perna direita

        self.canvas.pack()


    def chutar(self):
        chute = self.entry_chute.get().strip().upper()

        if chute in self.palavra_secreta:
            self.marca_chute_correto(chute)
        else:
            self.erros += 1

        if self.erros == 9 or "_" not in self.letras_acertadas:
            self.finaliza_jogo()

        self.desenha_forca()
        self.atualiza_interface()

        self.entry_chute.delete(0, tk.END)


    def marca_chute_correto(self, chute):
        for i, letra in enumerate(self.palavra_secreta):
            if chute == letra:
                self.letras_acertadas[i] = letra

    def finaliza_jogo(self):
        if "_" not in self.letras_acertadas:
            messagebox.showinfo("Fim do Jogo", "Parabéns, você ganhou!")
        else:
            messagebox.showinfo("Fim do Jogo", f"Puxa, você foi enforcado! A palavra era {self.palavra_secreta}")
        self.master.destroy()

def main():
    root = tk.Tk()
    jogo_forca = JogoForca(root)
    root.mainloop()

if __name__ == "__main__":
    main()
