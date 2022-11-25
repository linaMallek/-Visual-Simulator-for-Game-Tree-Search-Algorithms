import math
import time

import pygame
import defs as p
import AlgorithmesDeRecherche as a


def getInputs():
    player = input("1 for max and -1 for min: ")
    values = input("a for random values and tp for TPs values: ")
    return player, values


pygame.init()
p.setCaption("Projet TP2 RP")

alpha = - math.inf
beta = math.inf
done = False
while not done:
    p.menu(p.screen, p.width, p.height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            done = True
            key_input = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
           
            # MiniMax with player max
            if event.key == pygame.K_1:
                p.screen.fill(p.screenBG)
                p.displayMenuTexts(p.screen, "MiniMax", 120, 20)
                pygame.init()
                depth = 5
                #player, values = getInputs()
                nodes = p.InitTree(p.width, depth, "tp")
                a.miniMax(nodes[0],1, depth, nodes)
                time.sleep(3)
                break

            if event.key == pygame.K_2:
                p.screen.fill(p.screenBG)
                p.displayMenuTexts(p.screen, "MiniMax", 120, 20)
                pygame.init()
                depth = 5
                #player, values = getInputs()
                nodes = p.InitTree(p.width, depth, "tp")
                a.miniMax(nodes[0],-1, depth, nodes)
                time.sleep(3)
                break  
            
            # NegaMax with max
            if event.key == pygame.K_3:
                p.screen.fill(p.screenBG)
                p.displayMenuTexts(p.screen, "NegaMax", 120, 20)
                pygame.init()
                depth = 5
                #player, values = getInputs()
                nodes = p.InitTree(p.width, depth,"tp")
                a.NegaMax(nodes[0], 1, depth, nodes)
                time.sleep(3)
                break

            if event.key == pygame.K_4:
                p.screen.fill(p.screenBG)
                p.displayMenuTexts(p.screen, "NegaMax", 120, 20)
                pygame.init()
                depth = 5
                #player, values = getInputs()
                nodes = p.InitTree(p.width, depth,"tp")
                a.NegaMax(nodes[0], -1, depth, nodes)
                time.sleep(3)
                break
            # AlphaBetaMax
            if event.key == pygame.K_5:
                p.screen.fill(p.screenBG)
                p.displayMenuTexts(p.screen, "AlphaBetaPruning", 220, 20)
                pygame.init()
                depth = 5
                #player, values = getInputs()
                nodes = p.InitTree(p.width, depth, "tp")
                a.NegaMaxAlphaBetaPruning(nodes[0], 1 , depth, alpha, beta, nodes)
                time.sleep(3)
                break

            if event.key == pygame.K_6:
                p.screen.fill(p.screenBG)
                p.displayMenuTexts(p.screen, "AlphaBetaPruning", 220, 20)
                pygame.init()
                depth = 5
                #player, values = getInputs()
                nodes = p.InitTree(p.width, depth, "tp")
                a.NegaMaxAlphaBetaPruning(nodes[0], -1 , depth, alpha, beta, nodes)
                time.sleep(3)
                break 

    pygame.display.flip()
