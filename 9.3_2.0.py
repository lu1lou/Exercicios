from graphics import *

def main():
    infile = input('imagem inicial: ')
    outfile = input('nome da imagem cinzento: ')

    img = Image(Point(0,0), infile)
    width, height = img.getWidth(), img.getHeight()
    win = GraphWin("Grayscale Converter", width, height + 60)
    win.setBackground("blue")
    
    img.move(width/2, height/2)
    img.draw(win)
    
    
    com_btn = Rectangle(Point(width/2-50-40, height+30-15),
                       Point(width/2-50+40, height+30+15))
    com_btn.setFill('lightgray')
    com_btn.draw(win)
    Text(Point(width/2-50, height+30), "Começar").draw(win)
    
    
    fec_btn = Rectangle(Point(width/2+50-40, height+30-15),
                        Point(width/2+50+40, height+30+15))
    fec_btn.setFill('lightgray')
    fec_btn.draw(win)
    Text(Point(width/2+50, height+30), "Sair").draw(win)
    
    while True:
        click = win.getMouse()
        
        
        com_p1, com_p2 = com_btn.getP1(), com_btn.getP2()
        if (com_p1.getX() <= click.getX() <= com_p2.getX() and 
            com_p1.getY() <= click.getY() <= com_p2.getY()):
            
            for y in range(height):
                for x in range(width):
                    r, g, b = img.getPixel(x, y)
                    new_r = 255 - r
                    new_g = 255 - g
                    new_b = 255 - b
                    img.setPixel(x, y, color_rgb(new_r, new_g, new_b))
                win.update()  
            img.save(outfile)
            
    
        fec_p1, fec_p2 = fec_btn.getP1(), fec_btn.getP2()
        if (fec_p1.getX() <= click.getX() <= fec_p2.getX() and 
            fec_p1.getY() <= click.getY() <= fec_p2.getY()):
            win.close()
            break

main()