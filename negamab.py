import keyboard
import pygame
import sys
import random
import math
from Node import Node
import time


Start = input('Start with:\n1-Max 2-Min\n')
if Start == '1':
    player = 1
else:
    player = -1


# draws
rectangleWidth = 50
rectangleHeight = 50
circleRadius = 30
lineThickness = 8
# colors
none_explored = (192, 192, 192)
rect_color = (128, 128, 128)
winnerColor = (220, 20, 60)
explored = (65, 105, 225)
screenBG = (255, 255, 255 )
write=(220, 0, 0)
# surface
width = 1000
height = 700


def drawRect(screen, color, w, h, rectW, rectH):
    pygame.draw.rect(screen, color, pygame.Rect(w, h, rectW, rectH))


def drawCircle(screen, w, depth, listnodes):
    for node in listnodes:
        pygame.draw.circle(screen, node.getColor(), node.getPos(), node.getRadius())
        if node.getValue()!=None and node.getColor() is  none_explored:
           x, y = node.getPos()
           writeNumbers(screen, str(node.getValue()), x - 10, y - 20)


def drawLine(screen, listnodes):
    for node in listnodes:
        if node.getLeft() is not None and node.getRight() is not None:
            pygame.draw.line(screen, node.getLeft().getColor(), node.getPos(), node.getLeft().getPos(), lineThickness)
            pygame.draw.line(screen, node.getRight().getColor(), node.getPos(), node.getRight().getPos(), lineThickness)

def writeNumbers(screen, number, x, y):
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    number = my_font.render(number, False, write)
    screen.blit(number, (x, y))            

def InitTree(width, depth):
    listNodes = []
    NodeCount = 2 ** (depth - 1)
    diameter = (height // NodeCount) / 2
    radius = circleRadius
    for level in range(depth):
        totalNodes = 2 ** level
        startPoint = (width // totalNodes) / 2
        for node in range(totalNodes):
            listNodes.append(
                Node(startPoint + ((width // totalNodes) * node),
                     (height // depth) * level + (height / depth / 2),
                     None,
                     None,
                     radius,
                     none_explored,
                     None,
                     None,
                     
                     )
            )
    feuilles = []
    randomValues = []
    for i in range(len(listNodes)):
        if 2 * i + 1 < len(listNodes) and listNodes[2 * i + 1]:
            listNodes[i].setLeft(listNodes[2 * i + 1])

    for j in range(len(listNodes)):
        if 2 * j + 2 < len(listNodes) and listNodes[2 * j + 2]:
            listNodes[j].setRight(listNodes[2 * j + 2])
    
    liste=[10,5,7,11,12,8,9,8,5,12,11,12,9,8,7,10]
    k=0
    """for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            feuilles.append(node)
              
                #n = random.randint(-20, 30)
            randomValues.append(liste[k])
            node.setValue(liste[k])
            k=k+1"""
    for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            feuilles.append(node)

            for i in range(len(feuilles)):
                n = random.randint(-20, 30)
                randomValues.append(n)
                node.setValue(n)     
    for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            x, y = node.getPos()
            x -= 20
            y += 30
            feuilles.append(node)     
            pygame.draw.circle(screen, none_explored, node.getPos(), node.getRadius())
            drawRect(screen, (0, 0, 0), x, y,rectangleWidth,rectH=rectangleHeight)
            writeNumbers(screen, str(node.getValue()), x, y)            
    return listNodes

def InitTree1(width, depth):
    listNodes = []
    NodeCount = 2 ** (depth - 1)
    diameter = (height // NodeCount) / 2
    radius = circleRadius
    for level in range(depth):
        totalNodes = 2 ** level
        startPoint = (width // totalNodes) / 2
        for node in range(totalNodes):
            listNodes.append(
                Node(startPoint + ((width // totalNodes) * node),
                     (height // depth) * level + (height / depth / 2),
                     None,
                     None,
                     radius,
                     none_explored,
                     None,
                     None,

                     )
            )
    feuilles = []
    randomValues = []
    for i in range(len(listNodes)):
        if 2 * i + 1 < len(listNodes) and listNodes[2 * i + 1]:
            listNodes[i].setLeft(listNodes[2 * i + 1])

    for j in range(len(listNodes)):
        if 2 * j + 2 < len(listNodes) and listNodes[2 * j + 2]:
            listNodes[j].setRight(listNodes[2 * j + 2])

    liste = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
    k = 0
    for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            feuilles.append(node)

            # n = random.randint(-20, 30)
            randomValues.append(liste[k])
            node.setValue(liste[k])
            k = k + 1
    """for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            feuilles.append(node)
        for i in range(len(feuilles)):
                n = random.randint(-20, 30)
                randomValues.append(n)
                node.setValue(n)"""
    for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            x, y = node.getPos()
            x -= 20
            y += 30
            feuilles.append(node)
            pygame.draw.circle(screen, none_explored, node.getPos(), node.getRadius())
            drawRect(screen, (0, 0, 0), x, y, rectangleWidth, rectH=rectangleHeight)
            writeNumbers(screen, str(node.getValue()), x, y)
    return listNodes

def displayAlphaBeta(screen, value, x, y):
    pygame.font.init()
    drawRect(screen, screenBG, x, y-70, 50, 20)
    my_font = pygame.font.SysFont('Comic Sans MS', 15, bold=True)
    value = my_font.render(value, False, (0, 0, 0), screenBG)
    screen.blit(value, (x, y - 70))
    pygame.display.flip()
    pygame.display.update()

screen = pygame.display.set_mode((width, height))
def drawNodes(screen, width, depth, listnodes):
    global x, y
    drawLine(screen, listnodes)
    drawCircle(screen, width, depth, listnodes)
    feuilles = []  
    randomValues = []
    # display feuilles values (still a problem)
    
    nodeValues = []
    for node in feuilles:
        x, y = node.getPos()
        writeNumbers(screen, str(node.getValue()), x - 10, y - 20)
        nodeValues.append(node.getValue())
    #print(nodeValues) 

    pygame.display.update()


alpha = - math.inf
beta = math.inf

def NegaMaxAlphaBetaPruning(node, player, depth, alpha, beta,nodes):
    
    
    if depth == 1:
        if player == -1:
            node.val = - node.val
        
        node.setColor(explored)
        x, y = node.getPos()
        writeNumbers(screen, str(node.getValue()), x, y)
        pygame.draw.circle(screen, explored, node.getPos(), node.getRadius())
        drawNodes(screen, width, depth, nodes)
    
        displayAlphaBeta(screen, "α=" + str(alpha), x, y)
        displayAlphaBeta(screen, "β=" + str(beta), x, y + 15)
        pygame.display.flip()

    else:

        x, y = node.getPos()  
        displayAlphaBeta(screen, "α=" + str(alpha), x, y)
        displayAlphaBeta(screen, "β=" + str(beta), x, y + 15)
        
        node.setColor(explored)
        
        writeNumbers(screen, str(node.getValue()), x, y)
        pygame.draw.circle(screen, explored, node.getPos(), node.getRadius())
        drawNodes(screen, width, depth, nodes)
 


        pygame.display.update()
        listChildren = [node.left, node.right]
        bestValue = - math.inf
        bestPath = None

        for child in listChildren:
            NegaMaxAlphaBetaPruning(child, -player, depth - 1, -beta, -alpha,nodes)
            drawNodes(screen, width, depth, nodes)
            time.sleep(1)
            l=-(child.getValue())
            if l > bestValue:
                bestValue = l
                bestPath = child
            drawNodes(screen, width, depth, nodes)
            if bestValue > alpha:
                alpha = bestValue 
                x,y=node.getPos()  # a changer    
                displayAlphaBeta(screen, "α=" + str(alpha), x, y)
                displayAlphaBeta(screen, "β=" + str(beta), x, y + 15)           

            if beta <= alpha:
                break

        x,y=bestPath.getPos()    
        bestPath.setColor(winnerColor)
        pygame.draw.circle(screen,winnerColor, bestPath.getPos(), bestPath.getRadius())       
        node.val = bestValue
        node.path = bestPath
        drawNodes(screen, width, depth, nodes)
        time.sleep(2)
    #if(nodes[0].getColor()==winnerColor):
             #return 0   
    return 0             
screen.fill(screenBG)



#---------------------
pygame.init()

pygame.display.update()
depth = 5
nodes = InitTree1(width, depth)
alpha = - math.inf
beta = math.inf

while True:

    time.sleep(2)
    #screen.fill((0, 0, 0))
    x=NegaMaxAlphaBetaPruning(nodes[0],player, depth,alpha,beta, nodes)
    if x==0:
        time.sleep(2)
        pygame.quit()
        sys.exit()
    time.sleep(2)
    """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()"""

    pygame.display.flip()        