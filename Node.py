class Node:

    def __init__(self, pos1, pos2, elder, val, radius, color, left, right):
        self.elder = elder
        self.val = val
        self.radius = radius
        self.color = color
        self.left = left
        self.right = right
        self.pos1 = pos1
        self.pos2 = pos2

    def setValue(self, val):
        self.val = val

    def getValue(self):
        return self.val

    def getPos(self):
        return self.pos1, self.pos2

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getRadius(self):
        return self.radius

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right