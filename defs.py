import math

import pygame
import random
from Node import Node

# drawsMesurements
rectangleWidth = 50
rectangleHeight = 50
circleRadius = 30
lineThickness = 8

# colors
none_explored = (192, 192, 192)
rect_color = (128, 128, 128)
winnerColor = (220, 20, 60)
explored = (65, 105, 225)
screenBG = (255, 255, 255)

# surface
width = 1400
height = 700
screen = pygame.display.set_mode((width, height))
screen.fill(screenBG)

bg = pygame.image.load('CanvaDesign.png')


def setCaption(caption):
    pygame.display.set_caption(caption)


def drawRect(screen, color, w, h, rectW, rectH):
    pygame.draw.rect(screen, color, pygame.Rect(w, h, rectW, rectH))


def drawCircle(screen, w, depth, listnodes):
    for node in listnodes:
        pygame.draw.circle(screen, node.getColor(), node.getPos(), node.getRadius())
        if node.getValue() is not None and node.getColor() is not none_explored:
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
    number = my_font.render(number, False, (255, 255, 255))
    screen.blit(number, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def displayMenuTexts(screen, text, x, y):
    pygame.font.init()
    largeText = pygame.font.SysFont('Comic Sans MS', 40, bold=True)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


def displayAlphaBeta(screen, value, x, y):
    pygame.font.init()
    drawRect(screen, screenBG, x, y - 70, 50, 20)
    my_font = pygame.font.SysFont('Comic Sans MS', 15, bold=True)
    value = my_font.render(value, False, (0, 0, 0), screenBG)
    screen.blit(value, (x, y - 70))
    pygame.display.flip()
    pygame.display.update()


# initialisation de l'arbre :
def InitTree(width, depth, type):
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
                     None
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

    # initialisation des valeurs:
    liste = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
    k = 0
    for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            feuilles.append(node)

            if type == 'a':
                for i in range(len(feuilles)):
                    n = random.randint(-20, 30)
                    # randomValues.append(n)
                    node.setValue(n)
            else:
                node.setValue(liste[k])
                k = k + 1

    for node in listNodes:
        if node.getLeft() is None and node.getRight() is None:
            x, y = node.getPos()
            x -= 20
            y += 30
            feuilles.append(node)
            pygame.draw.circle(screen, none_explored, node.getPos(), node.getRadius())
            drawRect(screen, (0, 0, 0), x, y, rectangleWidth, rectangleHeight)
            writeNumbers(screen, str(node.getValue()), x, y)
    return listNodes


def drawNodes(screen, width, depth, listnodes):
    global x, y
    drawLine(screen, listnodes)
    drawCircle(screen, width, depth, listnodes)
    feuilles = []
    randomValues = []
    # display feuilles values
    nodeValues = []
    for node in feuilles:
        x, y = node.getPos()
        writeNumbers(screen, str(node.getValue()), x - 10, y - 20)
        nodeValues.append(node.getValue())

    pygame.display.update()


def blitImage(screen, image, x, y):
    screen.blit(image, (x, y))


def menu(screen, width, height):
    blitImage(screen, bg, 0, 0)
