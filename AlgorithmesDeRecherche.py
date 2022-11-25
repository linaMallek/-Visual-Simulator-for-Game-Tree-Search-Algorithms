import math
import time
import defs as p
import pygame


def miniMax(node, player, depth, nodes):
    if depth == 1:
        node.setColor(p.explored)
        x, y = node.getPos()
        p.writeNumbers(p.screen, str(node.getValue()), x, y)
        pygame.display.update()
        pygame.draw.circle(p.screen, p.explored, node.getPos(), node.getRadius())
        pygame.display.update()
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()

        if player == -1:
            p.displayMenuTexts(p.screen, "Min", p.width * 0.60, 45)
        else:
            p.displayMenuTexts(p.screen, "Max", p.width * 0.60, 45)

    else:
        # mark as explored
        node.setColor(p.explored)
        pygame.draw.circle(p.screen, p.explored, node.getPos(), node.getRadius())
        pygame.display.update()

        listChildren = [node.left, node.right]
        if player == +1:
            bestValue = - math.inf
            bestPath = None
            for child in listChildren:
                miniMax(child, -player, depth - 1, nodes)
                if child.getValue() > bestValue:
                    bestValue = child.getValue()
                    bestPath = child

            bestPath.setColor(p.winnerColor)
            pygame.draw.circle(p.screen, p.winnerColor, bestPath.getPos(), bestPath.getRadius())
            pygame.display.update()
            p.drawNodes(p.screen, p.width, depth, nodes)
            pygame.display.update()
        else:
            bestValue = math.inf
            bestPath = None
            for child in listChildren:
                time.sleep(0.5)
                miniMax(child, -player, depth - 1, nodes)
                if child.getValue() < bestValue:
                    bestValue = child.getValue()
                    bestPath = child
                time.sleep(0.5)
            time.sleep(0.5)
            bestPath.setColor(p.winnerColor)
            pygame.draw.circle(p.screen, p.winnerColor, bestPath.getPos(), bestPath.getRadius())
            pygame.display.update()

        node.val = bestValue
        node.path = bestPath
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()


def NegaMax(node, player, depth, nodes):
    if depth == 1:
        if player == -1:
            p.displayMenuTexts(p.screen, "Min", p.width*0.60, 45)
            node.val = -(node.getValue())
            p.drawNodes(p.screen, p.width, depth, nodes)
            pygame.display.update()
        else:
            p.displayMenuTexts(p.screen, "Max", p.width*0.60, 45)
        # Display the current node’s value and mark it as explored
        node.setColor(p.explored)
        x, y = node.getPos()
        p.writeNumbers(p.screen, str(node.getValue()), x, y)
        pygame.draw.circle(p.screen, p.explored, node.getPos(), node.getRadius())
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()

    else:
        # Mark the current node as explored
        node.setColor(p.explored)
        pygame.draw.circle(p.screen, p.explored, node.getPos(), node.getRadius())
        pygame.display.update()
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()

        listChildren = [node.left, node.right]
        bestValue = - math.inf
        bestPath = None
        for child in listChildren:
            time.sleep(0.5)
            NegaMax(child, -player, depth - 1, nodes)
            p.drawNodes(p.screen, p.width, depth, nodes)
            pygame.display.update()
            x = -(child.getValue())
            if x > bestValue:
                bestValue = x
                bestPath = child
            time.sleep(0.5)
        time.sleep(0.5)

        node.val = bestValue
        node.path = bestPath
        bestPath.setColor(p.winnerColor)
        pygame.draw.circle(p.screen, p.winnerColor, bestPath.getPos(), bestPath.getRadius())
        pygame.display.update()
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()


def NegaMaxAlphaBetaPruning(node, player, depth, alpha, beta, nodes):
    if depth == 1:
        if player == -1:
            node.val = - node.val
            p.displayMenuTexts(p.screen, "Min", p.width * 0.60, 45)
        else:
            p.displayMenuTexts(p.screen, "Max", p.width * 0.60, 45)

        node.setColor(p.explored)
        x, y = node.getPos()
        p.writeNumbers(p.screen, str(node.getValue()), x, y)
        pygame.display.update()
        pygame.draw.circle(p.screen, p.explored, node.getPos(), node.getRadius())
        pygame.display.update()
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()

        p.displayAlphaBeta(p.screen, "α=" + str(alpha), x, y)
        p.displayAlphaBeta(p.screen, "β=" + str(beta), x, y + 20)
        pygame.display.update()
    else:

        x, y = node.getPos()
        p.displayAlphaBeta(p.screen, "α=" + str(alpha), x, y)
        p.displayAlphaBeta(p.screen, "β=" + str(beta), x, y + 20)
        pygame.display.update()
        node.setColor(p.explored)
        p.writeNumbers(p.screen, str(node.getValue()), x, y)
        pygame.display.update()
        pygame.draw.circle(p.screen, p.explored, node.getPos(), node.getRadius())
        pygame.display.update()
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()
        listChildren = [node.left, node.right]
        bestValue = - math.inf
        bestPath = None

        for child in listChildren:
            time.sleep(1)
            NegaMaxAlphaBetaPruning(child, -player, depth - 1, -beta, -alpha, nodes)
            p.drawNodes(p.screen, p.width, depth, nodes)
            pygame.display.update()
            l = -(child.getValue())
            if l > bestValue:
                bestValue = l
                bestPath = child
            p.drawNodes(p.screen, p.width, depth, nodes)
            pygame.display.update()
            if bestValue > alpha:
                alpha = bestValue
                x, y = node.getPos()  # a changer
                p.displayAlphaBeta(p.screen, "α=" + str(alpha), x, y)
                p.displayAlphaBeta(p.screen, "β=" + str(beta), x, y + 20)
                pygame.display.update()
            if beta <= alpha:
                break
            time.sleep(0.5)
        time.sleep(0.5)

        x, y = bestPath.getPos()
        bestPath.setColor(p.winnerColor)
        pygame.draw.circle(p.screen, p.winnerColor, bestPath.getPos(), bestPath.getRadius())
        pygame.display.update()
        node.val = bestValue
        node.path = bestPath
        p.drawNodes(p.screen, p.width, depth, nodes)
        pygame.display.update()
