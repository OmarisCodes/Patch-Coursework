from graphics import *
def main():
    
    
    colour1 = colourCheck()
    colour2 = colourCheck()
    colour3 = colourCheck()


    patchworkNumber = input("Enter a number from 5, 7 and 9: ")
    if patchworkNumber == "5":
        patchwork5(colour1,colour2,colour3)
    elif patchworkNumber == "7":
        patchwork7(colour1,colour2,colour3)
    elif patchworkNumber == "9":
        patchwork9(colour1,colour2,colour3)
    else:
        print("Enter a valid number provided")

    
def colourCheck():
    coloursAvailable = ["red", "green", "blue", "yellow", "white", "black", "orange", "purple", "pink", "cyan", "magenta"]
    while True:
        colour =  input("Enter a colour: ")
        if colour in coloursAvailable: 
            return colour
        else:
            print(f"{colour} is not availbe. Please Choose a valid colour such as:")
            print(coloursAvailable)
def patchwork9(colour1,colour2,colour3):
    windowWidth = 900
    windowHeight = 900
    win = GraphWin("",windowWidth,windowHeight)
    for row in range(0,10):
        for column in range(0,10):
            position = [row*100,column*100]

            if (row ==0 and column == 0) or (row ==1 and column == 1) or (row ==2 and column == 2) or (row ==3 and column == 3) or(row ==4 and column == 4) or(row ==5 and column == 5) or (row ==6 and column == 6) or (row ==7 and column == 7) or (row ==8 and column == 8):
                mainColour = colour2
                diagramFinal(windowWidth,windowHeight,win,mainColour,position)
            elif (row ==0 and column == 1) or (row ==0 and column == 2) or (row ==0 and column == 3) or (row ==0 and column == 4) or (row ==0 and column == 5) or (row ==0 and column == 6) or (row ==0 and column == 7) or (row ==0 and column == 8) or(row ==1 and column == 8) or (row ==2 and column == 8) or (row ==3 and column == 8) or (row ==4 and column == 8) or (row ==5 and column == 8) or(row ==6 and column == 8) or (row ==7 and column == 8):
                mainColour = colour3
                diagramFinal(windowWidth,windowHeight,win,mainColour,position)
            elif (row ==2 and column == 1) or (row ==3 and column == 1) or (row ==4 and column == 1) or(row ==5 and column == 1) or(row ==6 and column == 1) or(row ==6 and column == 2) or(row ==6 and column == 3) or(row ==6 and column == 4) or(row ==6 and column == 5) or (row ==3 and column == 2) or (row ==4 and column == 2) or (row ==5 and column == 2) or (row ==4 and column == 3) or (row ==5 and column == 3) or (row ==5 and column == 4) or(row ==7 and column == 1) or(row ==7 and column == 2)or(row ==7 and column == 3)or(row ==7 and column == 4)or(row ==7 and column == 5)or(row ==7 and column == 6):
                mainColour = colour1
                diagramPenultimate(win,position,mainColour)
            elif (row ==1 and column == 2) or (row ==1 and column == 3) or (row ==1 and column == 4) or (row ==1 and column == 5) or (row ==1 and column == 6) or (row ==1 and column == 7) or (row ==2 and column == 3) or (row ==2 and column == 4) or (row ==2 and column == 5) or (row ==2 and column == 6) or (row ==2 and column == 7) or (row ==3 and column == 4) or (row ==3 and column == 5) or (row ==3 and column == 6) or (row ==3 and column == 7) or (row ==4 and column == 5) or (row ==4 and column == 6) or (row ==4 and column == 7) or (row ==5 and column == 6) or (row ==5 and column == 7) or (row ==6 and column == 7) :
                mainColour = colour3
                colorRectangle(win,position,mainColour)
            elif (row ==1 and column == 0) or (row ==2 and column == 0) or (row ==3 and column == 0) or (row ==4 and column == 0) or (row ==5 and column == 0) or (row ==6 and column == 0) or (row ==7 and column == 0) or (row ==8 and column == 0) or (row ==8 and column == 1) or (row ==8 and column == 2) or (row ==8 and column == 3) or (row ==8 and column == 4) or (row ==8 and column == 5) or (row ==8 and column == 6) or (row ==8 and column == 7):
                mainColour = colour1
                colorRectangle(win,position,mainColour)
            

def patchwork7(colour1,colour2,colour3):
    windowWidth = 700
    windowHeight = 700
    win = GraphWin("",windowWidth,windowHeight)
    for row in range(0,10):
        for column in range(0,10):
            position = [row*100,column*100]

            if (row ==0 and column == 0) or (row ==1 and column == 1) or (row ==2 and column == 2) or (row ==3 and column == 3) or(row ==4 and column == 4) or(row ==5 and column == 5) or(row ==6 and column == 6):
                mainColour = colour2
                diagramFinal(windowWidth,windowHeight,win,mainColour,position)
            elif (row ==0 and column == 1) or (row ==0 and column == 2) or (row ==0 and column == 3) or (row ==0 and column == 4) or (row ==0 and column == 5) or (row ==0 and column == 6) or(row ==1 and column == 6) or (row ==2 and column == 6) or (row ==3 and column == 6) or (row ==4 and column == 6) or (row ==5 and column == 6):
                mainColour = colour3
                diagramFinal(windowWidth,windowHeight,win,mainColour,position)
            elif (row ==2 and column == 1) or (row ==3 and column == 1) or (row ==4 and column == 1) or(row ==5 and column == 1) or (row ==3 and column == 2) or (row ==4 and column == 2) or (row ==5 and column == 2) or (row ==4 and column == 3) or (row ==5 and column == 3) or (row ==5 and column == 4):
                mainColour = colour1
                diagramPenultimate(win,position,mainColour)
            elif (row ==1 and column == 2) or (row ==1 and column == 3) or (row ==1 and column == 4) or (row ==1 and column == 5) or (row ==2 and column == 3) or (row ==2 and column == 4)or (row ==2 and column == 5) or (row ==3 and column == 4) or (row ==3 and column == 5) or (row ==4 and column == 5):
                mainColour = colour3
                colorRectangle(win,position,mainColour)
            elif (row ==1 and column == 0) or (row ==2 and column == 0) or (row ==3 and column == 0) or (row ==4 and column == 0) or (row ==5 and column == 0) or (row ==6 and column == 0) or (row ==6 and column == 1) or (row ==6 and column == 2) or (row ==6 and column == 3) or (row ==6 and column == 4) or (row ==6 and column == 5):
                mainColour = colour1
                colorRectangle(win,position,mainColour)
            
def patchwork5(colour1,colour2,colour3):
    windowWidth = 500
    windowHeight = 500
    win = GraphWin("",windowWidth,windowHeight)
    for row in range(5):
        for column in range(5):
            position = [row*100,column*100]

            if (row ==0 and column == 0) or (row ==1 and column == 1) or (row ==2 and column == 2) or (row ==3 and column == 3) or(row ==4 and column == 4):
                mainColour = colour2
                diagramFinal(windowWidth,windowHeight,win,mainColour,position)
            elif (row ==0 and column == 1) or (row ==0 and column == 2) or (row ==0 and column == 3) or (row ==0 and column == 4) or(row ==1 and column == 4) or (row ==2 and column == 4) or (row ==3 and column == 4):
                mainColour = colour3
                diagramFinal(windowWidth,windowHeight,win,mainColour,position)
            elif (row ==2 and column == 1) or (row ==3 and column == 1) or (row ==3 and column == 2):
                mainColour = colour1
                diagramPenultimate(win,position,mainColour)
            elif (row ==1 and column == 2) or (row ==1 and column == 3) or (row ==2 and column == 3):
                mainColour = colour3
                colorRectangle(win,position,mainColour)
            elif (row ==1 and column == 0) or (row ==2 and column == 0) or (row ==3 and column == 0) or (row ==4 and column == 0) or (row ==4 and column == 1) or (row ==4 and column == 2) or (row ==4 and column == 3):
                mainColour = colour1
                colorRectangle(win,position,mainColour)
            
def diagramPenultimate(win,position,mainColour):

    
    starty = 100
    startx = 0
    endx = 100
    endy = 0
    list = [mainColour, "white",mainColour, "white",mainColour, "white",mainColour, "white",mainColour, "white"]
    for row in range(10):
        tl = Point((startx+position[1]),(starty+position[0]))
        br = Point((endx+position[1]),(endy+position[0]))
        rectangle = Rectangle(tl,br)
        rectangle.setFill(list[row])
        rectangle.draw(win)
        endx = endx - 10
        endy = endy + 10
def colorRectangle(win,position,mainColour):
    
        starty = 100
        startx = 0
        endx = 100
        endy = 0
        tl = Point((startx+position[1]),(starty+position[0]))
        br = Point((endx+position[1]),(endy+position[0]))
        rectangle = Rectangle(tl,br)
        rectangle.setFill(mainColour)
        rectangle.draw(win)

def diagramFinal(windowWidth,windowHeight,win,mainColour,position):
    for row in range(0,10):
        for column in range(0,5):
            if row %2 == 0:
                drawRectangle(win,windowWidth,windowHeight,column,row,25,mainColour,position)
            else:
                if column % 2 == 1:
                    colour = "white"
                else:
                    colour = mainColour
                    drawRectangle(win,windowWidth,windowHeight,column,row,20,colour,position)
                    
def drawRectangle(win,windowWidth,windowHeight,column,row,size,colour,position):
    tl = Point((column*size)+position[1],(row*10)+position[0])
    br = Point(((column+1)*size)+position[1],((row+1)*10)+position[0])
    rectangle = Rectangle(tl,br)
    rectangle.setFill(colour)
    rectangle.setOutline("black")
    rectangle.draw(win)

main()