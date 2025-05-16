# -*- coding: utf-8 -*-
"""
Created on Fri May 16 13:24:00 2025

@author: luisl
"""

from graphics import *

def media(valores):
    return sum(valores) / len(valores)

def main():
    # Criar janela gráfica
    largura = 600
    altura = 400
    win = GraphWin("Regressão Linear", largura, altura)
    win.setCoords(0, 0, largura, altura)  # coordenadas de usuário

    # Desenhar botão "Concluído"
    fim_ret = Rectangle(Point(10, 10), Point(80, 40))
    fim_ret.setFill("green")
    fim_ret.draw(win)
    fim_text = Text(Point(45, 25), "Concluído")
    fim_text.draw(win)
    
    fim_ret = Rectangle(Point(520, 10), Point(590, 40))
    fim_ret.setFill("red")
    fim_ret.draw(win)
    fim_text = Text(Point(555, 25), "fechar")
    fim_text.draw(win)

    pontos = []
    soma_x = soma_y = soma_x2 = soma_xy = 0

    while True:
        click = win.getMouse()
        x, y = click.getX(), click.getY()
        
        if 10 <= x <= 80 and 10 <= y <= 40:
            break
        
        if 520 <= x <= 590 and 10 <= y <= 40:
            print("ffff")
            win.close()
    
        circ = Circle(Point(x, y), 3)
        circ.setFill("blue")
        circ.draw(win)

        pontos.append((x, y))
        soma_x += x
        soma_y += y
        soma_x2 += x * x
        soma_xy += x * y

    n = len(pontos)
    if n < 2:
        print("Número insuficiente de pontos.")
        win.close()
        return

   
    x_media = soma_x / n
    y_media = soma_y / n

    numerador = soma_xy - n * x_media * y_media
    denominador = soma_x2 - n * x_media ** 2
    m = numerador / denominador

    
    x0 = 0
    y0 = y_media + m * (x0 - x_media)

    x1 = largura
    y1 = y_media + m * (x1 - x_media)


    linha = Line(Point(x0, y0), Point(x1, y1))
    linha.setOutline("red")
    linha.draw(win)
    
    click = win.getMouse()
    x, y = click.getX(), click.getY()
    
    if 520 <= x <= 590 and 10 <= y <= 40:
        print("ffff")
        win.close()
 
if __name__ == "__main__":
    main()
