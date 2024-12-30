import tkinter as tk
from tkinter import messagebox
import random

# configurações do jogo
linhas = 4
colunas = 4
card_sizew = 10
card_sizeh = 5
card_cores = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta']
max_tentativas = 27
background = '#343a40'
cor_texto = '#ffffff'
font_style = ('Arial', 12, 'bold')

# Interface

janela = tk.Tk()
janela.title('memorygame')
janela.config(bg=background)

# Grade aleatoria de cores para os cards

def create_card_grid():
    cores = card_cores * 2
    random.shuffle(cores) # misturando as cores dentro da lista
    print(cores)
    grid = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            cor = cores.pop()
            print(cor)
            linha.append(cor)
            print(linha)
        grid.append(linha)
    print(grid)
    return grid

# função para lidar com clique do jogador

def card_clique(linha, coluna):
    card = cards[linha][coluna]
    cor = card['bg']
    if cor == 'black':
        card['bg'] = grid[linha][coluna]
        card_revelado.append(card)
        print(card_revelado)
        if len(card_revelado) == 2:
            checa_cards()

# verificando se os dois cards revelados são iguais

def checa_cards():
    card1, card2 = card_revelado
    print(card1)
    print(card2)
    if card1['bg'] == card2['bg']:
        card1.after(1000, card1.destroy)
        card2.after(1000, card2.destroy)
        card_correspondente.extend([card1, card2])
        check_win()
    else:
        card1.after(1000, lambda:card1.config(bg='black'))
        card2.after(1000, lambda:card2.config(bg='black'))
    card_revelado.clear()
    atualiza_tentativas()

# verificando se o jogador ganhou o jogo

def check_win():
    if len(card_correspondente) == linhas * colunas:
        messagebox.showinfo('Você venceu', 'Parabéns!')
        janela.quit()

# atualizando as tentativas e verificando se jogador excedeu as tentativas

def atualiza_tentativas():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas, max_tentativas))
    if numero_tentativas >= max_tentativas:
        messagebox.showinfo('Você perdeu!', 'Fim de jogo')
        janela.quit()

# Criando grade de cards
grid = create_card_grid()
cards = []
card_revelado = []
card_correspondente = []
numero_tentativas = 0

for linha in range(linhas):
    linha_cards = []
    for coluna in range(colunas):
        card = tk.Button(janela, width=card_sizew, height=card_sizeh, bg='black', relief=tk.RAISED, bd=3, command=lambda r=linha, c=coluna: card_clique(r, c)) # criando o card
        card.grid(row=linha, column=coluna, padx=5, pady=5)
        linha_cards.append(card)
    cards.append(linha_cards)

print(f'cards: {cards}')

# botao
button_style = {'activatebackground': '#f8f9fa', 'font': font_style, 'fg': cor_texto}
janela.option_add('*Button', button_style)

# label para tentativas

label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(numero_tentativas, max_tentativas), fg=cor_texto, bg=background, font=font_style)
label_tentativas.grid(row=linhas, columnspan= colunas, padx=10, pady=10)


janela.mainloop()